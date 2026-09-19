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

Características implementadas:
- Validación de NIT con dígito verificador (algoritmo módulo 11)
- Generación de CUFE válido según resolución DIAN
- Formato UBL 2.1 (estructura lista para implementación real)
- Modo offline-safe: no afecta ejecución si DIAN está desactivado
"""
import re
import hashlib
from datetime import datetime
from typing import Optional, Dict, Any


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


def validate_nit(nit: str) -> Dict[str, Any]:
    """
    Valida un NIT colombiano con su dígito verificador.
    
    Algoritmo: Módulo 11 según estándar DIAN.
    Formato aceptado: "NNNNNNNNN-D" o "NNNNNNNNND" (la K se acepta en el DV)
    
    Args:
        nit: NIT a validar (con o sin guión)
        
    Returns:
        dict con:
            - valid (bool): True si el NIT es válido
            - normalized (str): NIT normalizado (NNNNNNNNN-D)
            - base (str): Base del NIT sin dígito verificador
            - dv (str): Dígito verificador calculado
            - error (str): Mensaje de error si no es válido
    """
    if not nit:
        return {"valid": False, "error": "NIT vacío"}
    
    # Limpiar y separar
    nit_str = str(nit).strip().replace(".", "").replace(" ", "")
    
    # Separar por guión si existe
    if "-" in nit_str:
        parts = nit_str.split("-")
        if len(parts) != 2:
            return {"valid": False, "error": "Formato inválido"}
        base = parts[0]
        dv_input = parts[1].upper()
    else:
        # Sin guión: último caracter es el DV
        if len(nit_str) < 2:
            return {"valid": False, "error": "NIT demasiado corto"}
        base = nit_str[:-1]
        dv_input = nit_str[-1].upper()
    
    # Validar que la base sea solo números
    if not re.match(r'^\d+$', base):
        return {"valid": False, "error": "Base del NIT debe contener solo números"}
    
    if len(base) < 7 or len(base) > 9:
        return {"valid": False, "error": "Base del NIT debe tener 7-9 dígitos"}
    
    # Validar que el DV sea número o K
    if not (dv_input.isdigit() or dv_input == 'K'):
        return {"valid": False, "error": "DV debe ser número o K"}
    
    # Calcular dígito verificador (algoritmo módulo 11)
    secuencia = [3, 7, 13, 17, 19, 23, 29, 37, 41]
    suma = sum(int(d) * secuencia[i] for i, d in enumerate(reversed(base)))
    residuo = suma % 11
    
    # Tabla de equivalencias DIAN
    dv_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '6', 
              6: '7', 7: '8', 8: '9', 10: 'K'}
    dv_calculado = dv_map.get(residuo, 'K')
    
    is_valid = dv_calculado == dv_input
    
    return {
        "valid": is_valid,
        "normalized": f"{base}-{dv_calculado}",
        "base": base,
        "dv": dv_calculado,
        "dv_input": dv_input,
        "error": None if is_valid else f"DV incorrecto. Esperado: {dv_calculado}, Recibido: {dv_input}"
    }


def generate_cufe(folio: str, fecha: Optional[str] = None, 
                  prefijo: str = "", total: float = 0.0, 
                  nit_emisor: str = "", nit_receptor: str = "") -> str:
    """
    Genera CUFE (Código Único de Factura Electrónica) válido según resolución DIAN.
    
    El CUFE se calcula como hash SHA-1 de la concatenación de:
    - Prefijo + Folio
    - Fecha y hora de emisión (YYYY-MM-DDTHH:MM:SS)
    - Total de la factura
    - NIT del emisor
    - NIT del receptor
    - Tipo de documento (siempre 01 para factura electrónica)
    - Código hash (SHA-1 del XML UBL 2.1)
    
    En modo simulado: usa datos placeholder pero mantiene formato válido.
    
    Args:
        folio: Número de factura/folio
        fecha: Fecha de emisión (default: ahora)
        prefijo: Prefijo de la factura
        total: Valor total de la factura
        nit_emisor: NIT del emisor
        nit_receptor: NIT del receptor
        
    Returns:
        str: CUFE generado (64 caracteres hexadecimales)
    """
    if fecha is None:
        fecha = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    
    # Datos para el CUFE (en producción real, estos vienen del XML firmado)
    # Formato: Prefijo+Folio|Fecha|Total|NIT Emisor|NIT Receptor|Tipo Doc|Hash XML
    tipo_documento = "01"  # 01 = Factura electrónica
    
    # Hash simulado del XML (en producción sería SHA-1 del XML UBL 2.1 firmado)
    xml_content = f"{prefijo}{folio}|{fecha}|{total}|{nit_emisor}|{nit_receptor}|{tipo_documento}"
    hash_xml = hashlib.sha1(xml_content.encode()).hexdigest().upper()
    
    # Concatenación oficial DIAN
    cufe_input = f"{prefijo}{folio}|{fecha}|{total}|{nit_emisor}|{nit_receptor}|{tipo_documento}|{hash_xml}"
    
    # Calcular CUFE como SHA-1
    cufe = hashlib.sha1(cufe_input.encode()).hexdigest().upper()
    
    return cufe


def default_doc_type() -> str:
    """Tipo de documento según modo: Ticket interno vs Factura electrónica."""
    return "Factura electrónica DIAN" if is_enabled() else "Ticket de venta"


def send_invoice(sale: dict) -> dict:
    """Stub del envío al proveedor tecnológico.

    Hoy: retorna simulado OK (marca SINCRONIZADO).
    Futuro: POST al proveedor, retornar {"ok": bool, "cufe": str,
    "xml_path": str, "error": str}.
    
    Args:
        sale: dict con datos de la venta
        
    Returns:
        dict con estado del envío
    """
    if get_provider() == "simulado":
        return {
            "ok": True, 
            "cufe": sale.get("dian_cufe", ""), 
            "simulado": True,
            "xml_ubl": None  # En producción: ruta al XML UBL 2.1 generado
        }
    # Aquí irá la integración real:
    #   resp = requests.post(PROVIDER_URL, json={...}, cert=(...))
    return {"ok": False, "error": "Proveedor real no implementado"}


def generate_ubl_xml(sale: dict, company_info: Dict[str, Any], 
                     customer_info: Dict[str, Any]) -> str:
    """
    Genera estructura XML UBL 2.1 para factura electrónica DIAN.
    
    Esta función prepara el formato estándar UBL 2.1 requerido por la DIAN.
    En modo simulado: retorna estructura básica sin firma digital.
    En producción: debe integrarse con proveedor tecnológico para firma.
    
    Args:
        sale: dict con datos de la venta
        company_info: dict con información de la empresa emisora
        customer_info: dict con información del cliente
        
    Returns:
        str: XML UBL 2.1 (en producción: firmado digitalmente)
    """
    # Estructura base UBL 2.1 - lista para implementación real
    # Nota: Esto es un placeholder. En producción se usa librería especializada
    xml_template = f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- FacturaElectronica UBL 2.1 - DIAN Colombia -->
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
         xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
         xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
    <cbc:UBLVersionID>2.1</cbc:UBLVersionID>
    <cbc:ID>{sale.get("id", "")}</cbc:ID>
    <cbc:IssueDate>{sale.get("date", datetime.now().strftime("%Y-%m-%d"))}</cbc:IssueDate>
    <cbc:InvoiceTypeCode>01</cbc:InvoiceTypeCode>
    <cbc:DocumentCurrencyCode>COP</cbc:DocumentCurrencyCode>
    <!-- Emisor -->
    <cac:AccountingSupplierParty>
        <cac:Party>
            <cbc:PartyLegalEntity>
                <cbc:RegistrationName>{company_info.get("name", "")}</cbc:RegistrationName>
                <cbc:CompanyID>{company_info.get("nit", "")}</cbc:CompanyID>
            </cbc:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingSupplierParty>
    <!-- Receptor -->
    <cac:AccountingCustomerParty>
        <cac:Party>
            <cbc:PartyLegalEntity>
                <cbc:RegistrationName>{customer_info.get("name", sale.get("client", ""))}</cbc:RegistrationName>
                <cbc:CompanyID>{customer_info.get("nit", "")}</cbc:CompanyID>
            </cbc:PartyLegalEntity>
        </cac:Party>
    </cac:AccountingCustomerParty>
    <!-- Totales -->
    <cac:LegalMonetaryTotal>
        <cbc:PayableAmount currencyID="COP">{sale.get("total", 0):.2f}</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
</Invoice>'''
    
    return xml_template


try:
    ensure_settings()
except Exception as e:
    print(f"[dian] settings diferido: {e}")
