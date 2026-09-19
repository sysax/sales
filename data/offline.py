"""
Offline REAL §6 — outbox persistente en SQLite + monitor + sync idempotente.

Antes (simulado): cola en /tmp/*.json (volátil, se pierde al reiniciar),
sync_queue() solo hacía repo.log, socket bloqueante en hilo UI,
POS leía mock_data en memoria.

Ahora (real):
- Outbox en SQLite (tabla `outbox`): sobrevive reinicios, transaccional.
- Ventas siempre locales primero (offline-first): repo.create_sale() nunca
  requiere internet. La cola solo guarda el trabajo pendiente remoto
  (DIAN CUFE, futuro backend): sale + dian, con idempotency_key=folio.
- sync_queue() idempotente: verifica folio existe, marca
  sales.dian_status=SINCRONIZADO, reintentos con backoff, failed tras 5.
- Monitor background (daemon thread): detecta cambios online/offline y
  dispara callback en hilo UI (Clock) + auto-sync al reconectar.
- Tickets persistentes en data/tickets/ (no solo /tmp).
- Migra una vez la cola legacy /tmp/sistema_ventas_offline.json al outbox.

Sin servidor remoto, "sync DIAN" = marcar SINCRONIZADO + audit log.
Cuando exista API real, reemplazar _remote_sync() sin tocar pantallas.
"""
import os
import json
import time
import threading
from datetime import datetime, timedelta

# ── Rutas ──
QUEUE_PATH = "/tmp/sistema_ventas_offline.json"  # legacy, solo migración
TICKETS_DIR = "/tmp/sistema_ventas_tickets"      # legacy, fallback
os.makedirs(TICKETS_DIR, exist_ok=True)

_DATA_DIR = os.path.dirname(os.path.abspath(__file__))
TICKETS_PERSIST_DIR = os.path.join(_DATA_DIR, "tickets")
os.makedirs(TICKETS_PERSIST_DIR, exist_ok=True)

MAX_ATTEMPTS = 5

# ── Monitor ──
_monitor_thread = None
_monitor_stop = threading.Event()
_monitor_last_state = None


def _get_conn():
    # import lazy para evitar ciclo data.db <-> data.offline
    from data import db as sqlite
    return sqlite.get_conn()


def ensure_outbox():
    """Crea tabla outbox si no existe. Idempotente."""
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS outbox (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_ts TEXT,
        op_type TEXT,
        idempotency_key TEXT UNIQUE,
        payload_json TEXT,
        status TEXT DEFAULT 'pending',
        attempts INTEGER DEFAULT 0,
        last_error TEXT,
        synced_ts TEXT
    )""")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_outbox_status ON outbox(status)")
    conn.commit()
    conn.close()
    _migrate_legacy_queue()


def _migrate_legacy_queue():
    """Migra /tmp json legacy al outbox una sola vez."""
    if not os.path.exists(QUEUE_PATH):
        return
    try:
        with open(QUEUE_PATH, "r", encoding="utf-8") as f:
            items = json.load(f)
    except Exception:
        return
    if not items:
        try:
            os.remove(QUEUE_PATH)
        except Exception:
            pass
        return
    try:
        conn = _get_conn()
        cur = conn.cursor()
        for it in items:
            t = it.get("type", "sale")
            d = it.get("data", {})
            key = f"legacy-{t}-{d.get('folio', '')}-{it.get('ts', '')}"
            try:
                cur.execute(
                    "INSERT OR IGNORE INTO outbox (created_ts, op_type, idempotency_key, payload_json, status) VALUES (?,?,?,?, 'pending')",
                    (it.get("ts", datetime.now().isoformat(timespec="seconds")), t, key, json.dumps(d, ensure_ascii=False)),
                )
            except Exception:
                continue
        conn.commit()
        conn.close()
    except Exception:
        return
    try:
        os.remove(QUEUE_PATH)
    except Exception:
        pass


# ── Conectividad ──
def is_offline_forced() -> bool:
    try:
        from data import mock_data as db
        return bool(getattr(db, "IS_OFFLINE", False))
    except Exception:
        return False


def set_offline_forced(value: bool):
    """Flag manual para pruebas / switch UI. True=offline."""
    try:
        from data import mock_data as db
        db.IS_OFFLINE = bool(value)
    except Exception:
        pass


def is_online(timeout=1.5) -> bool:
    """Chequeo rápido no bloqueante (timeout corto). Flag manual manda."""
    if is_offline_forced():
        return False
    try:
        import socket
        s = socket.create_connection(("8.8.8.8", 53), timeout=timeout)
        s.close()
        return True
    except Exception:
        return False


check_online = is_online  # alias


def start_monitor(on_change=None, interval=10):
    """Hilo daemon que vigila conectividad y llama on_change(online).

    on_change se invoca vía Clock.schedule_once si Kivy está disponible
    (thread-safe UI), si no directo. Auto-sync NO lo hace el monitor
    (lo hace la pantalla), solo notifica. Retorna True si inició.
    """
    global _monitor_thread, _monitor_last_state
    if _monitor_thread and _monitor_thread.is_alive():
        return True
    _monitor_stop.clear()
    try:
        _monitor_last_state = is_online(timeout=1.0)
    except Exception:
        _monitor_last_state = False

    def _loop():
        global _monitor_last_state
        while not _monitor_stop.wait(interval):
            try:
                cur = is_online(timeout=1.5)
            except Exception:
                cur = False
            if cur != _monitor_last_state:
                _monitor_last_state = cur
                if on_change:
                    try:
                        from kivy.clock import Clock
                        Clock.schedule_once(lambda dt, v=cur: on_change(v), 0)
                    except Exception:
                        try:
                            on_change(cur)
                        except Exception:
                            pass

    _monitor_thread = threading.Thread(target=_loop, daemon=True, name="offline-monitor")
    _monitor_thread.start()
    return True


def stop_monitor():
    _monitor_stop.set()


# ── Outbox ops ──
def queue_operation(op_type, data, idempotency_key=None):
    """Encola op. Idempotente por idempotency_key (INSERT OR IGNORE).
    Retorna pendientes count."""
    ensure_outbox()
    if idempotency_key is None:
        folio = (data or {}).get("folio", "")
        idempotency_key = f"{op_type}-{folio}" if folio else f"{op_type}-{datetime.now().isoformat(timespec='seconds')}-{os.getpid()}"
    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT OR IGNORE INTO outbox (created_ts, op_type, idempotency_key, payload_json, status) VALUES (?,?,?,?, 'pending')",
            (datetime.now().isoformat(timespec="seconds"), op_type, idempotency_key, json.dumps(data or {}, ensure_ascii=False)),
        )
        conn.commit()
    finally:
        conn.close()
    return pending_count()


def get_queue(status="pending"):
    """Compat: lista dicts {ts,type,data,key,attempts}. status=None=todas."""
    ensure_outbox()
    conn = _get_conn()
    cur = conn.cursor()
    try:
        if status:
            cur.execute("SELECT created_ts, op_type, idempotency_key, payload_json, attempts FROM outbox WHERE status=? ORDER BY id", (status,))
        else:
            cur.execute("SELECT created_ts, op_type, idempotency_key, payload_json, attempts FROM outbox ORDER BY id")
        out = []
        for ts, t, key, payload, attempts in cur.fetchall():
            try:
                d = json.loads(payload or "{}")
            except Exception:
                d = {}
            out.append({"ts": ts, "type": t, "data": d, "key": key, "attempts": attempts})
        return out
    finally:
        conn.close()


def pending_count() -> int:
    ensure_outbox()
    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) FROM outbox WHERE status='pending'")
        return cur.fetchone()[0] or 0
    finally:
        conn.close()


def clear_queue():
    """Compat: borra pendientes (legacy llama esto). También limpia /tmp legacy."""
    ensure_outbox()
    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM outbox WHERE status='pending'")
        conn.commit()
    finally:
        conn.close()
    try:
        if os.path.exists(QUEUE_PATH):
            os.remove(QUEUE_PATH)
    except Exception:
        pass


def _remote_sync(op_type, data, repo):
    """Punto único para futuro backend/DIAN real.

    Hoy: todo ya está aplicado localmente (offline-first), así que el sync
    solo reconcilia estado DIAN de forma idempotente. Si folio no existe
    localmente (DB reseteada), lanza ValueError -> reintento/fallido.
    """
    folio = (data or {}).get("folio", "")
    user = (data or {}).get("user", "sistema")
    if op_type in ("sale", "dian"):
        if not folio:
            raise ValueError("sync sin folio")
        sale = repo.find_sale(folio)
        if not sale:
            raise ValueError(f"folio {folio} no existe local (DB reseteada?)")
        if sale.get("dian_status") != "SINCRONIZADO":
            conn = _get_conn()
            cur = conn.cursor()
            try:
                cur.execute("UPDATE sales SET dian_status='SINCRONIZADO' WHERE id=?", (folio,))
                conn.commit()
            finally:
                conn.close()
        repo.log(user, "sync_sale" if op_type == "sale" else "sync_dian",
                 f"{folio} CUFE {(data or {}).get('cufe', sale.get('dian_cufe', ''))} reconciliado")
        return True
    # futuros: payment_cxc, payment_cxp, inventory, purchase — ya aplicados
    # local; solo audit para trazabilidad.
    repo.log(user, f"sync_{op_type}", json.dumps(data or {}, ensure_ascii=False)[:200])
    return True


def sync_queue(repo):
    """Sincroniza pendientes. Retorna (synced, failed+pending_restantes).

    - Si offline: (0, pendientes).
    - Idempotente: re-ejecutar no duplica (folio existe -> solo marca).
    - failed tras MAX_ATTEMPTS, el resto queda pending para reintento.
    - Purga synced >7 días (mantiene tabla acotada).
    """
    ensure_outbox()
    pending = pending_count()
    if pending == 0:
        return 0, 0
    if not is_online():
        return 0, pending
    conn = _get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, op_type, idempotency_key, payload_json, attempts FROM outbox WHERE status='pending' ORDER BY id")
        rows = cur.fetchall()
    finally:
        conn.close()
    synced = 0
    for oid, op_type, key, payload, attempts in rows:
        try:
            data = json.loads(payload or "{}")
        except Exception:
            data = {}
        try:
            _remote_sync(op_type, data, repo)
            conn2 = _get_conn()
            c2 = conn2.cursor()
            try:
                c2.execute("UPDATE outbox SET status='synced', synced_ts=?, attempts=?, last_error=NULL WHERE id=?",
                           (datetime.now().isoformat(timespec="seconds"), (attempts or 0) + 1, oid))
                conn2.commit()
            finally:
                conn2.close()
            synced += 1
        except Exception as e:
            err = str(e)[:300]
            nattempts = (attempts or 0) + 1
            status = "failed" if nattempts >= MAX_ATTEMPTS else "pending"
            conn2 = _get_conn()
            c2 = conn2.cursor()
            try:
                c2.execute("UPDATE outbox SET attempts=?, last_error=?, status=? WHERE id=?", (nattempts, err, status, oid))
                conn2.commit()
            finally:
                conn2.close()
    # purga synced antiguos
    try:
        conn3 = _get_conn()
        c3 = conn3.cursor()
        c3.execute("DELETE FROM outbox WHERE status='synced' AND synced_ts < ?", ((datetime.now() - timedelta(days=7)).isoformat(timespec="seconds"),))
        conn3.commit()
        conn3.close()
    except Exception:
        pass
    remaining = pending_count()
    # failed cuentan como no-sincronizados para el caller
    try:
        conn4 = _get_conn()
        c4 = conn4.cursor()
        c4.execute("SELECT COUNT(*) FROM outbox WHERE status='failed'")
        failed = c4.fetchone()[0] or 0
        conn4.close()
    except Exception:
        failed = 0
    return synced, remaining + failed


# ── Tickets persistentes ──
def save_ticket_text(folio, text):
    """Guarda ticket en data/tickets/ (persistente) + copia /tmp legacy.
    Retorna path persistente o None."""
    fname = f"ticket_{folio}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    persist = os.path.join(TICKETS_PERSIST_DIR, fname)
    try:
        with open(persist, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception:
        return None
    try:
        with open(os.path.join(TICKETS_DIR, fname), "w", encoding="utf-8") as f:
            f.write(text)
    except Exception:
        pass
    return persist


def list_tickets():
    try:
        files = sorted(os.listdir(TICKETS_PERSIST_DIR))
        if files:
            return files
    except Exception:
        pass
    try:
        return sorted(os.listdir(TICKETS_DIR))
    except Exception:
        return []


# asegurar tabla al importar (no falla si DB bloqueada brevemente)
try:
    ensure_outbox()
except Exception as e:
    print(f"[offline] ensure_outbox diferido: {e}")
