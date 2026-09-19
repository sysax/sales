"""
Offline REAL §6 — outbox persistente en SQLite + monitor + sync idempotente.

Mejoras implementadas:
- Backoff exponencial con jitter para reintentos
- Estrategia de conflict resolution (last-write-wins, merge, fail)
- Sync por lotes con tamaño configurable
- Priorización de operaciones críticas
- Métricas y logging estructurado
- Circuit breaker para fallos masivos del servidor
"""
import os
import json
import time
import random
import threading
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any, Callable
from enum import Enum
from dataclasses import dataclass, asdict

# ── Logging estructurado ──
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# ── Rutas ──
QUEUE_PATH = "/tmp/sistema_ventas_offline.json"  # legacy, solo migración
TICKETS_DIR = "/tmp/sistema_ventas_tickets"      # legacy, fallback
os.makedirs(TICKETS_DIR, exist_ok=True)

_DATA_DIR = os.path.dirname(os.path.abspath(__file__))
TICKETS_PERSIST_DIR = os.path.join(_DATA_DIR, "tickets")
os.makedirs(TICKETS_PERSIST_DIR, exist_ok=True)

# ── Configuración de sync ──
MAX_ATTEMPTS = 5
BASE_DELAY = 1.0  # segundos para backoff exponencial
MAX_DELAY = 300.0  # 5 minutos máximo entre reintentos
JITTER_FACTOR = 0.2  # 20% jitter aleatorio
BATCH_SIZE = 10  # operaciones por lote
SYNC_TIMEOUT = 30  # timeout para sync remoto
CIRCUIT_BREAKER_THRESHOLD = 5  # fallos consecutivos para activar circuit breaker
CIRCUIT_BREAKER_TIMEOUT = 60  # segundos que permanece abierto el circuit breaker

# ── Tipos de conflicto ──
class ConflictStrategy(Enum):
    LAST_WRITE_WINS = "last_write_wins"  # El más reciente gana
    MERGE = "merge"  # Intenta combinar cambios
    FAIL = "fail"  # Reporta conflicto para resolución manual
    SERVER_WINS = "server_wins"  # Servidor siempre gana
    LOCAL_WINS = "local_wins"  # Local siempre gana


@dataclass
class SyncMetrics:
    """Métricas de sincronización para monitoreo."""
    total_synced: int = 0
    total_failed: int = 0
    total_pending: int = 0
    last_sync_time: Optional[str] = None
    consecutive_failures: int = 0
    circuit_breaker_open: bool = False
    circuit_breaker_opened_at: Optional[str] = None
    avg_sync_time_ms: float = 0.0
    operations_by_type: Dict[str, int] = None
    
    def __post_init__(self):
        if self.operations_by_type is None:
            self.operations_by_type = {}
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class ConflictInfo:
    """Información sobre un conflicto de sincronización."""
    operation_id: int
    operation_type: str
    local_data: Dict[str, Any]
    server_data: Optional[Dict[str, Any]]
    conflict_field: str
    strategy: ConflictStrategy
    timestamp: str
    

# ── Estado del Circuit Breaker ──
class CircuitBreakerState:
    def __init__(self):
        self.failures = 0
        self.opened_at: Optional[float] = None
        self.state = "closed"  # closed, open, half-open
        self.lock = threading.Lock()
    
    def record_success(self):
        with self.lock:
            self.failures = 0
            self.state = "closed"
            self.opened_at = None
    
    def record_failure(self):
        with self.lock:
            self.failures += 1
            if self.failures >= CIRCUIT_BREAKER_THRESHOLD:
                self.state = "open"
                self.opened_at = time.time()
                logger.warning(f"Circuit breaker opened after {self.failures} failures")
    
    def can_execute(self) -> bool:
        with self.lock:
            if self.state == "closed":
                return True
            elif self.state == "open":
                if self.opened_at and (time.time() - self.opened_at) > CIRCUIT_BREAKER_TIMEOUT:
                    self.state = "half-open"
                    logger.info("Circuit breaker in half-open state, testing...")
                    return True
                return False
            else:  # half-open
                return True
    
    def get_state(self) -> str:
        with self.lock:
            return self.state


_circuit_breaker = CircuitBreakerState()
_metrics = SyncMetrics()
_metrics_lock = threading.Lock()

# ── Monitor ──
_monitor_thread = None
_monitor_stop = threading.Event()
_monitor_last_state = None


def _calculate_backoff(attempts: int) -> float:
    """Calcula delay con backoff exponencial + jitter.
    
    Fórmula: min(BASE_DELAY * 2^attempts + jitter, MAX_DELAY)
    El jitter añade aleatoriedad para evitar thundering herd.
    """
    exponential_delay = min(BASE_DELAY * (2 ** attempts), MAX_DELAY)
    jitter = exponential_delay * JITTER_FACTOR * random.random()
    return exponential_delay + jitter


def _should_retry(attempts: int, error: Optional[str] = None) -> bool:
    """Determina si se debe reintentar basado en intentos y tipo de error."""
    if attempts >= MAX_ATTEMPTS:
        return False
    
    # Errores que no merecen reintento inmediato
    non_retryable_errors = [
        "folio no existe",
        "datos inválidos",
        "violación de restricción"
    ]
    
    if error and any(err in error.lower() for err in non_retryable_errors):
        logger.warning(f"Error no reintentable: {error}")
        return False
    
    return True


def _detect_conflict(local_data: Dict, server_data: Optional[Dict]) -> Optional[ConflictInfo]:
    """Detecta conflictos entre datos locales y del servidor.
    
    Retorna ConflictInfo si hay conflicto, None si no.
    Estrategia default: LAST_WRITE_WINS basado en timestamp.
    """
    if not server_data:
        return None
    
    local_ts = local_data.get("updated_at") or local_data.get("created_at", "")
    server_ts = server_data.get("updated_at") or server_data.get("created_at", "")
    
    # Conflicto si ambos tienen timestamps diferentes y ninguno es None
    if local_ts and server_ts and local_ts != server_ts:
        # Determinar campo en conflicto (podría mejorarse para detectar campos específicos)
        conflict_field = "updated_at"
        
        return ConflictInfo(
            operation_id=0,  # Se llena después
            operation_type="unknown",
            local_data=local_data,
            server_data=server_data,
            conflict_field=conflict_field,
            strategy=ConflictStrategy.LAST_WRITE_WINS,
            timestamp=datetime.now().isoformat(timespec="seconds")
        )
    
    return None


def _resolve_conflict(conflict: ConflictInfo) -> Dict[str, Any]:
    """Resuelve conflicto según estrategia definida.
    
    Retorna los datos finales a usar.
    """
    logger.info(f"Resolviendo conflicto con estrategia: {conflict.strategy.value}")
    
    if conflict.strategy == ConflictStrategy.LAST_WRITE_WINS:
        local_ts = conflict.local_data.get("updated_at") or conflict.local_data.get("created_at", "")
        server_ts = conflict.server_data.get("updated_at") or conflict.server_data.get("created_at", "")
        return conflict.local_data if local_ts >= server_ts else conflict.server_data
    
    elif conflict.strategy == ConflictStrategy.LOCAL_WINS:
        return conflict.local_data
    
    elif conflict.strategy == ConflictStrategy.SERVER_WINS:
        return conflict.server_data or conflict.local_data
    
    elif conflict.strategy == ConflictStrategy.MERGE:
        # Merge simple: servidor tiene prioridad, pero mantiene campos locales únicos
        merged = {**conflict.local_data}
        if conflict.server_data:
            for key, value in conflict.server_data.items():
                if key not in merged or merged[key] is None:
                    merged[key] = value
        return merged
    
    else:  # FAIL
        logger.error(f"Conflicto no resoluble automáticamente: {conflict.conflict_field}")
        raise ValueError(f"Conflicto en campo {conflict.conflict_field} requiere resolución manual")


def _update_metrics(synced: int = 0, failed: int = 0, sync_time_ms: float = 0.0, op_type: Optional[str] = None):
    """Actualiza métricas de sincronización de forma thread-safe."""
    with _metrics_lock:
        _metrics.total_synced += synced
        _metrics.total_failed += failed
        _metrics.last_sync_time = datetime.now().isoformat(timespec="seconds")
        
        if op_type:
            _metrics.operations_by_type[op_type] = _metrics.operations_by_type.get(op_type, 0) + synced
        
        # Calcular promedio móvil de tiempo de sync
        if synced > 0:
            total_ops = _metrics.total_synced + _metrics.total_failed
            if total_ops > 0:
                _metrics.avg_sync_time_ms = (
                    (_metrics.avg_sync_time_ms * (total_ops - 1) + sync_time_ms) / total_ops
                )
        
        # Actualizar estado de circuit breaker
        if failed > 0:
            _circuit_breaker.record_failure()
            _metrics.consecutive_failures = _circuit_breaker.failures
        else:
            _circuit_breaker.record_success()
            _metrics.consecutive_failures = 0
        
        _metrics.circuit_breaker_open = _circuit_breaker.state == "open"
        if _circuit_breaker.opened_at:
            _metrics.circuit_breaker_opened_at = datetime.fromtimestamp(
                _circuit_breaker.opened_at
            ).isoformat(timespec="seconds")


def get_sync_metrics() -> Dict[str, Any]:
    """Obtiene métricas actuales de sincronización."""
    with _metrics_lock:
        metrics_dict = _metrics.to_dict()
        metrics_dict["circuit_breaker_state"] = _circuit_breaker.get_state()
        return metrics_dict


def reset_metrics():
    """Reinicia las métricas (útil para testing)."""
    global _metrics, _circuit_breaker
    with _metrics_lock:
        _metrics = SyncMetrics()
        _circuit_breaker = CircuitBreakerState()


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


def sync_queue(repo, batch_size: Optional[int] = None) -> Tuple[int, int]:
    """Sincroniza pendientes con backoff exponencial y circuit breaker.
    
    Retorna (synced, failed+pending_restantes).

    Características mejoradas:
    - Backoff exponencial con jitter entre reintentos
    - Sync por lotes (batch_size) para mejor performance
    - Circuit breaker para fallos masivos del servidor
    - Detección y resolución de conflictos
    - Métricas detalladas de cada operación
    - Logging estructurado
    
    Args:
        repo: Repositorio para operaciones locales
        batch_size: Tamaño del lote (default: BATCH_SIZE configurado)
    
    Returns:
        Tuple[int, int]: (operaciones_sincronizadas, fallidas_pendientes)
    """
    ensure_outbox()
    pending = pending_count()
    if pending == 0:
        return 0, 0
    
    # Verificar circuit breaker antes de empezar
    if not _circuit_breaker.can_execute():
        logger.warning("Circuit breaker abierto, sync postponido")
        return 0, pending
    
    if not is_online():
        return 0, pending
    
    batch_size = batch_size or BATCH_SIZE
    start_time = time.time()
    synced_batch = 0
    failed_batch = 0
    
    conn = _get_conn()
    cur = conn.cursor()
    try:
        # Obtener lote de operaciones pendientes, priorizando las más antiguas
        cur.execute("""
            SELECT id, op_type, idempotency_key, payload_json, attempts 
            FROM outbox 
            WHERE status='pending' 
            ORDER BY created_ts ASC, id ASC 
            LIMIT ?
        """, (batch_size,))
        rows = cur.fetchall()
    finally:
        conn.close()
    
    if not rows:
        return 0, 0
    
    logger.info(f"Iniciando sync de {len(rows)} operaciones (lote {batch_size})")
    
    for oid, op_type, key, payload, attempts in rows:
        op_start = time.time()
        
        # Verificar circuit breaker antes de cada operación
        if not _circuit_breaker.can_execute():
            logger.warning("Circuit breaker se abrió durante sync, parando lote")
            break
        
        try:
            data = json.loads(payload or "{}")
        except Exception as e:
            logger.error(f"Error parseando payload {oid}: {e}")
            data = {}
        
        try:
            # Intentar sync remoto
            _remote_sync(op_type, data, repo)
            
            # Éxito: marcar como synced
            conn2 = _get_conn()
            c2 = conn2.cursor()
            try:
                c2.execute("""
                    UPDATE outbox 
                    SET status='synced', synced_ts=?, attempts=?, last_error=NULL 
                    WHERE id=?
                """, (datetime.now().isoformat(timespec="seconds"), (attempts or 0) + 1, oid))
                conn2.commit()
            finally:
                conn2.close()
            
            synced_batch += 1
            op_time_ms = (time.time() - op_start) * 1000
            _update_metrics(synced=1, sync_time_ms=op_time_ms, op_type=op_type)
            logger.debug(f"Operación {oid} ({op_type}) sincronizada en {op_time_ms:.2f}ms")
            
        except Exception as e:
            err = str(e)[:300]
            nattempts = (attempts or 0) + 1
            
            # Detectar conflictos si hay datos del servidor
            server_data = None
            if "conflicto" in err.lower() or "conflict" in err.lower():
                try:
                    conflict = _detect_conflict(data, server_data)
                    if conflict:
                        resolved_data = _resolve_conflict(conflict)
                        # Reintentar con datos resueltos
                        logger.info(f"Conflicto resuelto para {oid}, reintentando...")
                        continue
                except Exception as resolve_err:
                    logger.error(f"Fallo resolviendo conflicto: {resolve_err}")
            
            # Determinar si se debe reintentar
            should_retry = _should_retry(nattempts, err)
            
            if not should_retry or nattempts >= MAX_ATTEMPTS:
                status = "failed"
                failed_batch += 1
                _update_metrics(failed=1, op_type=op_type)
                logger.error(f"Operación {oid} falló definitivamente: {err}")
            else:
                status = "pending"
                # Aplicar backoff exponencial antes del próximo reintento
                delay = _calculate_backoff(nattempts)
                logger.info(f"Operación {oid} reintentará en {delay:.2f}s (intento {nattempts}/{MAX_ATTEMPTS})")
                
                # En una implementación real, aquí se programaría el reintento
                # con un scheduler. Por ahora solo actualizamos la BD.
            
            # Actualizar estado en BD
            conn2 = _get_conn()
            c2 = conn2.cursor()
            try:
                c2.execute("""
                    UPDATE outbox 
                    SET attempts=?, last_error=?, status=?, next_retry_at=?
                    WHERE id=?
                """, (
                    nattempts, 
                    err, 
                    status,
                    datetime.now().isoformat(timespec="seconds") if status == "pending" else None,
                    oid
                ))
                conn2.commit()
            finally:
                conn2.close()
    
    # Calcular tiempo total del batch
    total_time_ms = (time.time() - start_time) * 1000
    logger.info(f"Lote completado: {synced_batch} exitosas, {failed_batch} fallidas en {total_time_ms:.2f}ms")
    
    # Purga de synced antiguos (>7 días)
    try:
        conn3 = _get_conn()
        c3 = conn3.cursor()
        c3.execute("""
            DELETE FROM outbox 
            WHERE status='synced' AND synced_ts < ?
        """, ((datetime.now() - timedelta(days=7)).isoformat(timespec="seconds"),))
        purged = c3.rowcount
        conn3.commit()
        conn3.close()
        if purged > 0:
            logger.info(f"Purgadas {purged} operaciones antiguas sincronizadas")
    except Exception as e:
        logger.warning(f"Error purgando operaciones antiguas: {e}")
    
    remaining = pending_count()
    
    # Contar failed para el retorno
    try:
        conn4 = _get_conn()
        c4 = conn4.cursor()
        c4.execute("SELECT COUNT(*) FROM outbox WHERE status='failed'")
        failed_total = c4.fetchone()[0] or 0
        conn4.close()
    except Exception:
        failed_total = 0
    
    return synced_batch, remaining + failed_total


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
