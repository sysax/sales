"""Facturación electrónica DIAN — punto único de integración.

Estado actual: MODO SIMULADO (default OFF).
- Con DIAN desactivado la app opera normal: tickets/remisiones internas,
  CUFE se guarda como referencia técnica pero la UI no lo muestra.
- Con DIAN activado la UI muestra CUFE + estado sync (aún simulado).

A futuro (facturación real): implementar aquí sin tocar pantallas:
1. `send_invoice()` → llamar al proveedor tecnológico certificado
   (firma digital, XML UBL 2.1, envío DIAN, recepción acuse).
2. Guardar respuesta oficial (CUFE real, QR, XML) en sales.
3. `set_enabled(True)` cuando el proveedor esté configurado.

Nada fuera de este módulo debe hardcodear lógica DIAN.
"""
from datetime import datetime


def _get_conn():
    from data import db as sqlite
    return sqlite.get_conn()


def ensure_settings():
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY, value TEXT
    )""")
    cur.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('dian_enabled', '0')")
    cur.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('dian_provider', 'simulado')")
    conn.commit()
    conn.close()


def is_enabled() -> bool:
    try:
        ensure_settings()
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute("SELECT value FROM settings WHERE key='dian_enabled'")
        r = cur.fetchone()
        conn.close()
        return (r[0] if r else "0") == "1"
    except Exception:
        return False


def set_enabled(value: bool, user="sistema"):
    ensure_settings()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('dian_enabled', ?)", ("1" if value else "0",))
    conn.commit()
    conn.close()
    try:
        from data.repository import repo
        repo.log(user, "dian_config", f"enabled={bool(value)}")
    except Exception:
        pass


def get_provider() -> str:
    try:
        ensure_settings()
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute("SELECT value FROM settings WHERE key='dian_provider'")
        r = cur.fetchone()
        conn.close()
        return r[0] if r else "simulado"
    except Exception:
        return "simulado"


def generate_cufe(folio: str) -> str:
    """CUFE simulado. A futuro: cálculo oficial (hash + firma)."""
    return f"CUFE-{folio}-DIAN-{datetime.now().strftime('%Y%m%d')}-COLOMBIA"


def default_doc_type() -> str:
    """Tipo de documento según modo: Ticket interno vs Factura electrónica."""
    return "Factura electrónica DIAN" if is_enabled() else "Ticket de venta"


def send_invoice(sale: dict) -> dict:
    """Stub del envío al proveedor tecnológico.

    Hoy: retorna simulado OK (marca SINCRONIZADO).
    Futuro: POST al proveedor, retornar {"ok": bool, "cufe": str,
    "xml_path": str, "error": str}.
    """
    if get_provider() == "simulado":
        return {"ok": True, "cufe": sale.get("dian_cufe", ""), "simulado": True}
    # Aquí irá la integración real:
    #   resp = requests.post(PROVIDER_URL, json={...}, cert=(...))
    return {"ok": False, "error": "Proveedor real no implementado"}


try:
    ensure_settings()
except Exception as e:
    print(f"[dian] settings diferido: {e}")
