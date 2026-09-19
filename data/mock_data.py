"""
Fuente única de verdad — Colombia (COP, NIT, IVA 19% DIAN)
Genérico para cualquier comercio: abarrotes, electrónica, ropa, etc.
En el futuro se reemplaza por SQLite vía data/repository.py sin tocar pantallas.
Moneda: COP $ — IVA Colombia 19% — Documentos DIAN — NIT
"""

from datetime import datetime, timedelta
import random
from collections import Counter, defaultdict


# ═══════════════════════════════════════════════════
#  USUARIOS (credenciales de acceso)
# ═══════════════════════════════════════════════════
USERS = [
    {"username": "admin", "password": "admin123", "role": "Administrador"},
    {"username": "vendedor", "password": "venta123", "role": "Vendedor"},
    {"username": "cajero", "password": "caja123", "role": "Cajero"},
    {"username": "almacen", "password": "alma123", "role": "Almacén"},
    {"username": "contador", "password": "conta123", "role": "Contador"},
]

# Roles válidos (fases.md §1)
ROLES = ["Administrador", "Vendedor", "Cajero", "Almacén", "Contador"]


# ═══════════════════════════════════════════════════
#  PRODUCTOS — Colombia §2 genérico (abarrotes/electrónica/ropa…)
#  COP $, IVA 19% DIAN, categorías genéricas: Abarrotes, Electronica, Hogar
# ═══════════════════════════════════════════════════
PRODUCTS = [
    {"id": 1, "sku": "P001", "barcode": "7701234560011", "name": "Laptop HP 15", "description": "Laptop 15.6 i5 8GB/512GB", "cat": "Electronica", "subcat": "Computadores", "brand": "HP", "supplier": "Distribuidora XYZ", "price": 1850000.00, "price_buy": 1450000.00, "price_wholesale": 1650000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 12, "stock_min": 5, "stock_max": 30, "location": "A1-E2", "status": "activo"},
    {"id": 2, "sku": "P002", "barcode": "7701234560028", "name": "Mouse Logitech", "description": "Mouse inalámbrico M185", "cat": "Accesorios", "subcat": "Periféricos", "brand": "Logitech", "supplier": "TecnoMayorista", "price": 45000.00, "price_buy": 28000.00, "price_wholesale": 38000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 45, "stock_min": 15, "stock_max": 100, "location": "A2-E1", "status": "activo"},
    {"id": 3, "sku": "P003", "barcode": "7701234560035", "name": "Teclado Mecánico", "description": "Teclado mecánico RGB", "cat": "Accesorios", "subcat": "Periféricos", "brand": "Logitech", "supplier": "TecnoMayorista", "price": 145000.00, "price_buy": 95000.00, "price_wholesale": 120000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 20, "stock_min": 10, "stock_max": 50, "location": "A2-E2", "status": "activo"},
    {"id": 4, "sku": "P004", "barcode": "7701234560042", "name": "Monitor 24''", "description": "Monitor FullHD 75Hz", "cat": "Electronica", "subcat": "Monitores", "brand": "HP", "supplier": "Distribuidora XYZ", "price": 550000.00, "price_buy": 420000.00, "price_wholesale": 480000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 8, "stock_min": 5, "stock_max": 20, "location": "B1-E1", "status": "activo"},
    {"id": 5, "sku": "P005", "barcode": "7701234560059", "name": "Audífonos Sony", "description": "Audífonos BT WH-1000", "cat": "Audio", "subcat": "Audífonos", "brand": "Sony", "supplier": "AudioPro SA", "price": 320000.00, "price_buy": 220000.00, "price_wholesale": 280000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 15, "stock_min": 8, "stock_max": 40, "location": "B2-E1", "status": "activo"},
    {"id": 6, "sku": "P006", "barcode": "7701234560066", "name": "Webcam HD", "description": "Webcam 1080p con micrófono", "cat": "Accesorios", "subcat": "Video", "brand": "Logitech", "supplier": "TecnoMayorista", "price": 115000.00, "price_buy": 75000.00, "price_wholesale": 95000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 30, "stock_min": 10, "stock_max": 60, "location": "A3-E1", "status": "activo"},
    {"id": 7, "sku": "P007", "barcode": "7701234560073", "name": "Impresora Epson", "description": "Impresora tanque tinta", "cat": "Oficina", "subcat": "Impresoras", "brand": "Epson", "supplier": "OfiSurte", "price": 380000.00, "price_buy": 290000.00, "price_wholesale": 340000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 5, "stock_min": 3, "stock_max": 15, "location": "C1-E1", "status": "activo"},
    {"id": 8, "sku": "P008", "barcode": "7701234560080", "name": "Disco SSD 1TB", "description": "SSD NVMe 1TB", "cat": "Almacenamiento", "subcat": "Discos", "brand": "Kingston", "supplier": "TecnoMayorista", "price": 220000.00, "price_buy": 150000.00, "price_wholesale": 185000.00, "tax": "IVA 19%", "unit": "unidad", "stock": 25, "stock_min": 10, "stock_max": 50, "location": "A1-E3", "status": "activo"},
    {"id": 9, "sku": "AB01", "barcode": "7701234560097", "name": "Arroz 5kg Diana", "description": "Arroz blanco 5kg", "cat": "Abarrotes", "subcat": "Granos", "brand": "Diana", "supplier": "Abastos Colombia", "price": 23500.00, "price_buy": 18000.00, "price_wholesale": 20500.00, "tax": "IVA 5% / Exento", "unit": "unidad", "stock": 60, "stock_min": 20, "stock_max": 120, "location": "C2-E1", "status": "activo"},
    {"id": 10, "sku": "AB02", "barcode": "7701234560103", "name": "Aceite Gourmet 1L", "description": "Aceite vegetal 1L", "cat": "Abarrotes", "subcat": "Aceites", "brand": "Gourmet", "supplier": "Abastos Colombia", "price": 8500.00, "price_buy": 6200.00, "price_wholesale": 7500.00, "tax": "IVA 19%", "unit": "unidad", "stock": 80, "stock_min": 30, "stock_max": 150, "location": "C2-E2", "status": "activo"},
]


# ═══════════════════════════════════════════════════
#  CLIENTES — Colombia NIT / DIAN — genérico cualquier comercio
#  NIT, razón social, régimen tributario DIAN, COP
# ═══════════════════════════════════════════════════
CLIENTS = [
    {"id": 1, "name": "Juan Pérez", "nit": "900123456-7", "nit_dv": "7", "razon": "Juan Pérez", "regimen": "No responsable IVA", "responsabilidad": "No responsable", "email": "juan@mail.com", "phone": "3101234567", "address": "Cra 15 # 85-20", "city": "Bogotá", "credit": 0.0, "credit_limit": 5000000.0, "discount": 5, "balance": 0.0, "price_list": "detal", "status": "activo", "rfc": "900123456-7"},
    {"id": 2, "name": "María López", "nit": "900234567-8", "nit_dv": "8", "razon": "Distribuciones López SAS", "regimen": "Responsable IVA", "responsabilidad": "Responsable IVA", "email": "maria@lopez.com", "phone": "3205678901", "address": "Calle 5 # 20-30", "city": "Medellín", "credit": 500000.0, "credit_limit": 8000000.0, "discount": 10, "balance": 500000.0, "price_list": "mayorista", "status": "activo", "rfc": "900234567-8"},
    {"id": 3, "name": "Carlos Ruiz", "nit": "900345678-9", "nit_dv": "9", "razon": "Carlos Ruiz", "regimen": "No responsable IVA", "responsabilidad": "No responsable", "email": "carlos@mail.com", "phone": "3159012345", "address": "Av El Dorado 68-70", "city": "Bogotá", "credit": 1200000.0, "credit_limit": 6000000.0, "discount": 0, "balance": 1200000.0, "price_list": "detal", "status": "activo", "rfc": "900345678-9"},
    {"id": 4, "name": "Ana Martínez", "nit": "900456789-0", "nit_dv": "0", "razon": "Tienda La Economía", "regimen": "Responsable IVA", "responsabilidad": "Responsable IVA", "email": "ana@economia.com", "phone": "3183456789", "address": "Calle 30 # 45-10", "city": "Cali", "credit": 0.0, "credit_limit": 3000000.0, "discount": 0, "balance": 0.0, "price_list": "detal", "status": "activo", "rfc": "900456789-0"},
    {"id": 5, "name": "Luis García", "nit": "900567890-1", "nit_dv": "1", "razon": "García Abarrotes", "regimen": "Régimen Simple", "responsabilidad": "Régimen Simple", "email": "luis@abarrotes.com", "phone": "3167890123", "address": "Carrera 10 # 12-15", "city": "Barranquilla", "credit": 0.0, "credit_limit": 4000000.0, "discount": 0, "balance": 0.0, "price_list": "mayorista", "status": "activo", "rfc": "900567890-1"},
]


# ═══════════════════════════════════════════════════
#  PROVEEDORES Colombia NIT — abarrotes/electrónica genérico
# ═══════════════════════════════════════════════════
SUPPLIERS = [
    {"id": 1, "name": "Distribuidora XYZ SAS", "nit": "800123456-9", "rfc": "800123456-9", "contact": "Roberto Díaz", "phone": "6011001234", "email": "roberto@xyz.com.co", "city": "Bogotá", "address": "Calle 80 # 90-10", "catalog": "Electrónica, Computadores", "lead_time": "3 días", "payment_terms": "30 días", "balance": 4500000.0},
    {"id": 2, "name": "TecnoMayorista SAS", "nit": "800234567-0", "rfc": "800234567-0", "contact": "Laura Gómez", "phone": "6042002345", "email": "laura@tecno.com.co", "city": "Medellín", "address": "Av Industriales 20-30", "catalog": "Accesorios, Almacenamiento", "lead_time": "2 días", "payment_terms": "15 días", "balance": 0.0},
    {"id": 3, "name": "AudioPro Colombia", "nit": "800345678-1", "rfc": "800345678-1", "contact": "Miguel Torres", "phone": "6023003456", "email": "miguel@audiopro.com.co", "city": "Cali", "address": "Calle 5 # 40-20", "catalog": "Audio, Video", "lead_time": "5 días", "payment_terms": "Contado", "balance": 2100000.0},
    {"id": 4, "name": "OfiSurte SAS", "nit": "800456789-2", "rfc": "800456789-2", "contact": "Patricia Ruiz", "phone": "6054004567", "email": "paty@ofisurte.com.co", "city": "Barranquilla", "address": "Cra 45 # 30-15", "catalog": "Oficina, Papelería", "lead_time": "4 días", "payment_terms": "30 días", "balance": 0.0},
    {"id": 5, "name": "Abastos Colombia SAS", "nit": "800567890-3", "rfc": "800567890-3", "contact": "Jorge Hernández", "phone": "6015005678", "email": "jorge@abastos.com.co", "city": "Bogotá", "address": "Corabastos Bodega 25", "catalog": "Abarrotes, Granos, Aceites", "lead_time": "1 día", "payment_terms": "Contado", "balance": 0.0},
]


# ═══════════════════════════════════════════════════
#  VENTAS (historial) — §6 §7 + CxC §8, estados 6, doc types
# ═══════════════════════════════════════════════════
# doc_type: Cotización/Pedido/Remisión/Factura/Nota crédito/Nota cargo
# status flujo: Cotización → Pedido → Facturada → Pagada → Entregada → Cerrada/Cancelada
# payments: dict efectivo/tarjeta/transferencia/credito, cambio, promo, impuesto
SALES = [
    {"id": "V001", "date": "2026-08-25", "client": "Juan Pérez", "vendedor": "vendedor", "total": 1850000.00, "subtotal": 1600000.00, "tax": 250000.00, "discount": 0, "promo": None, "status": "Pagada", "doc_type": "Factura electrónica DIAN", "payment": "Tarjeta", "payments": {"tarjeta":1850000.0}, "paid":1850000.0, "balance":0.0, "due":"2026-08-25", "estado": "Pagada", "dian_cufe": "CUFE-V001-DIAN"},
    {"id": "V002", "date": "2026-08-26", "client": "María López", "vendedor": "admin", "total": 450000.00, "subtotal": 400000.00, "tax": 50000.00, "discount": 0, "promo": None, "status": "Pagada", "doc_type": "Factura electrónica DIAN", "payment": "Efectivo", "payments": {"efectivo":450000.0}, "paid":450000.0, "balance":0.0, "due":"2026-08-26", "estado": "Entregada"},
    {"id": "V003", "date": "2026-08-27", "client": "Carlos Ruiz", "vendedor": "vendedor", "total": 280000.00, "subtotal": 250000.00, "tax": 30000.00, "discount": 0, "promo": None, "status": "Pendiente", "doc_type": "Factura electrónica DIAN", "payment": "Credito", "payments": {"credito":280000.0}, "paid":80000.0, "balance":200000.0, "due":"2026-09-10", "estado": "Facturada"},
    {"id": "V004", "date": "2026-08-28", "client": "Ana Martínez", "vendedor": "cajero", "total": 120000.00, "subtotal": 120000.00, "tax": 0, "discount": 0, "promo": None, "status": "Pagada", "doc_type": "Remisión", "payment": "Transferencia", "payments": {"transferencia":120000.0}, "paid":120000.0, "balance":0.0, "due":"2026-08-28", "estado": "Pagada"},
    {"id": "V005", "date": "2026-08-29", "client": "Luis García", "vendedor": "vendedor", "total": 950000.00, "subtotal": 950000.00, "tax": 0, "discount": 0, "promo": None, "status": "Cancelada", "doc_type": "Factura electrónica DIAN", "payment": "Efectivo", "payments": {}, "paid":0.0, "balance":0.0, "due":"2026-08-29", "estado": "Cancelada"},
    {"id": "V006", "date": "2026-08-30", "client": "Juan Pérez", "vendedor": "admin", "total": 320000.00, "subtotal": 280000.00, "tax": 40000.00, "discount": 0, "promo": None, "status": "Pagada", "doc_type": "Factura electrónica DIAN", "payment": "Efectivo", "payments": {"efectivo":320000.0}, "paid":320000.0, "balance":0.0, "due":"2026-08-30", "estado": "Pagada"},
    {"id": "COT001", "date": "2026-09-01", "client": "María López", "vendedor": "vendedor", "total": 750000.00, "subtotal": 750000.00, "tax": 0, "discount": 0, "promo": None, "status": "Cotización", "doc_type": "Cotización", "payment": "", "payments": {}, "paid":0.0, "balance":750000.0, "due":"2026-09-15", "estado": "Cotización"},
    {"id": "PED001", "date": "2026-09-02", "client": "Luis García", "vendedor": "admin", "total": 540000.00, "subtotal": 500000.00, "tax": 40000.00, "discount": 0, "promo": None, "status": "Pedido", "doc_type": "Pedido", "payment": "", "payments": {}, "paid":0.0, "balance":540000.0, "due":"2026-09-12", "estado": "Pedido"},
]

# Contador de folios (usado por POSScreen._confirm_sale)
SALE_COUNTER = 7
QUOTE_COUNTER = 2
ORDER_COUNTER = 2
CREDIT_NOTE_COUNTER = 1

# Se usa para reportes: detalle de líneas vendidas por producto (COP)
SALE_ITEMS = [
    {"sale_id": "V001", "product_id": 1, "qty": 1, "subtotal": 1850000.00},
    {"sale_id": "V001", "product_id": 4, "qty": 1, "subtotal": 550000.00},
    {"sale_id": "V002", "product_id": 4, "qty": 1, "subtotal": 450000.00},
    {"sale_id": "V003", "product_id": 5, "qty": 1, "subtotal": 280000.00},
    {"sale_id": "V004", "product_id": 3, "qty": 1, "subtotal": 145000.00},
    {"sale_id": "V005", "product_id": 6, "qty": 10, "subtotal": 950000.00},
    {"sale_id": "V006", "product_id": 7, "qty": 1, "subtotal": 380000.00},
]


# ═══════════════════════════════════════════════════
#  COMPRAS / ÓRDENES DE COMPRA (§11) — flujo §11 con items y contador
# ═══════════════════════════════════════════════════
PURCHASE_COUNTER = 6  # OC001-005 ya existen, siguiente OC006
PURCHASES = [
    {"id": "OC001", "date": "2026-08-20", "supplier": "Distribuidora XYZ SAS", "total": 4500000.00, "status": "Recibida", "items": [{"sku": "P001", "qty": 2, "price_buy": 1450000.00}, {"sku": "P004", "qty": 4, "price_buy": 420000.00}], "notes": "Electrónica Bogotá"},
    {"id": "OC002", "date": "2026-08-22", "supplier": "TecnoMayorista SAS", "total": 1200000.00, "status": "Pendiente", "items": [{"sku": "P002", "qty": 20, "price_buy": 28000.00}, {"sku": "P003", "qty": 10, "price_buy": 95000.00}], "notes": "Periféricos Medellín"},
    {"id": "OC003", "date": "2026-08-24", "supplier": "AudioPro Colombia", "total": 840000.00, "status": "Recibida", "items": [{"sku": "P005", "qty": 3, "price_buy": 220000.00}, {"sku": "P006", "qty": 4, "price_buy": 75000.00}], "notes": "Audio Cali"},
    {"id": "OC004", "date": "2026-08-27", "supplier": "OfiSurte SAS", "total": 640000.00, "status": "En tránsito", "items": [{"sku": "P007", "qty": 2, "price_buy": 290000.00}, {"sku": "P008", "qty": 1, "price_buy": 150000.00}], "notes": "Oficina Barranquilla"},
    {"id": "OC005", "date": "2026-08-28", "supplier": "Abastos Colombia SAS", "total": 850000.00, "status": "Pendiente", "items": [{"sku": "AB01", "qty": 20, "price_buy": 18000.00}, {"sku": "AB02", "qty": 30, "price_buy": 6200.00}], "notes": "Abarrotes Corabastos"},
]

# Movimientos de inventario §5 — Entradas/Salidas/Transferencias/Ajustes
INVENTORY_MOVEMENTS = [
    {"id": 1, "ts": "2026-08-20 10:00", "sku": "P001", "product": "Laptop HP 15", "type": "Entrada", "qty": 2, "before": 10, "after": 12, "reason": "Compra OC001", "user": "admin"},
    {"id": 2, "ts": "2026-08-25 14:30", "sku": "P001", "product": "Laptop HP 15", "type": "Salida", "qty": -1, "before": 12, "after": 11, "reason": "Venta V001", "user": "vendedor"},
]


# ═══════════════════════════════════════════════════
#  CxP / CxC — se derivan de PURCHASES/SALES pero se exponen para pantallas
# ═══════════════════════════════════════════════════
PAYABLES = [
    {"id": "OC002", "supplier": "TecnoMayorista SAS", "due": "2026-09-05", "amount": 1200000.00, "paid": 400000.00, "balance": 800000.00, "status": "Pendiente", "discount_early": 2},
    {"id": "OC004", "supplier": "OfiSurte SAS", "due": "2026-09-10", "amount": 640000.00, "paid": 0.0, "balance": 640000.00, "status": "Pendiente", "discount_early": 0},
    {"id": "OC005", "supplier": "Abastos Colombia SAS", "due": "2026-09-12", "amount": 850000.00, "paid": 0.0, "balance": 850000.00, "status": "Pendiente", "discount_early": 0},
]

# Abonos CxC/CxP
PAYMENTS_CXC = [
    {"id": 1, "sale_id": "V003", "date": "2026-08-28", "amount": 800.0, "method": "Efectivo", "user": "cajero"},
]
PAYMENTS_CXP = [
    {"id": 1, "payable_id": "OC002", "date": "2026-08-23", "amount": 4000.0, "method": "Transferencia", "user": "contador"},
]

# Promociones Colombia COP — genérico abarrotes/electrónica
PROMOS = [
    {"id": 1, "name": "2x1 Audífonos", "type": "2x1", "value": 0, "condition": "P005", "code": "2X1AUD", "active": True, "desc": "Lleva 2 paga 1 — SKU P005 — aplica abarrotes/electrónica"},
    {"id": 2, "name": "10% en Electrónica", "type": "porcentaje", "value": 10, "condition": "Electronica", "code": "ELEC10", "active": True, "desc": "10% descuento categoría Electrónica"},
    {"id": 3, "name": "$50.000 OFF", "type": "monto_fijo", "value": 50000, "condition": "min 500000", "code": "50KOFF", "active": True, "desc": "$50k COP compra > $500k"},
    {"id": 4, "name": "3x2 Accesorios", "type": "3x2", "value": 0, "condition": "Accesorios", "code": "3X2ACC", "active": False, "desc": "3x2 categoría Accesorios"},
    {"id": 5, "name": "5% Volumen >10", "type": "volumen", "value": 5, "condition": "qty>=10", "code": "VOL5", "active": True, "desc": "5% si lleva 10+ unidades — aplica abarrotes"},
    {"id": 6, "name": "10% Abarrotes", "type": "porcentaje", "value": 10, "condition": "Abarrotes", "code": "ABAR10", "active": True, "desc": "10% en Abarrotes — ideal barrio"},
]

# Offline §6 — flag manual + queue (ver data/offline.py)
IS_OFFLINE = False
OFFLINE_QUEUE = []  # compat in-memoria, real en /tmp/sistema_ventas_offline.json
PENDING_DIAN = []

# Caja — apertura/cierre §6
CAJA = {"open": False, "opening_amount": 0.0, "opening_ts": None, "opening_user": None, "sales_today": [], "expected": 0.0}


# ═══════════════════════════════════════════════════
#  BITÁCORA (memoria; luego SQLite)
# ═══════════════════════════════════════════════════
AUDIT_LOG = []  # lista de {"ts","user","action","detail"}


# ═══════════════════════════════════════════════════
#  FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════

def get_stats():
    """Calcula estadisticas del dashboard."""
    total_sales = sum(s["total"] for s in SALES if s["status"] == "Pagada")
    pending = sum(1 for s in SALES if s["status"] == "Pendiente")
    low_stock = sum(1 for p in PRODUCTS if p["stock"] < p.get("stock_min", 10))
    return {
        "total_sales": f"${total_sales:,.2f}",
        "total_products": len(PRODUCTS),
        "total_clients": len(CLIENTS),
        "pending_orders": pending,
        "low_stock_alerts": low_stock,
    }

def get_inventory_value():
    """Inventario valorizado §5 — costo y venta."""
    cost = sum(p.get("price_buy", p["price"]*0.7) * p["stock"] for p in PRODUCTS)
    sale = sum(p["price"] * p["stock"] for p in PRODUCTS)
    units = sum(p["stock"] for p in PRODUCTS)
    return {"cost_value": cost, "sale_value": sale, "units": units, "cost_fmt": f"${cost:,.2f}", "sale_fmt": f"${sale:,.2f}"}

def get_inventory_alerts():
    low = [p for p in PRODUCTS if p["stock"] < p.get("stock_min", 5)]
    excess = [p for p in PRODUCTS if p["stock"] > p.get("stock_max", 9999)]
    out = [p for p in PRODUCTS if p["stock"] == 0]
    return {"low": low, "excess": excess, "out": out}


# ── Búsqueda / lookup usados por POSScreen y CRUD ──

def find_product(product_id: int):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)

def find_product_by_sku(sku: str):
    return next((p for p in PRODUCTS if p["sku"].lower() == sku.strip().lower()), None)

def find_product_by_barcode(barcode: str):
    return next((p for p in PRODUCTS if p.get("barcode","") == barcode.strip()), None)

def find_client(name: str):
    return next((c for c in CLIENTS if c["name"].lower() == name.strip().lower()), None)

def find_client_by_id(cid: int):
    return next((c for c in CLIENTS if c["id"] == cid), None)

def find_supplier(sid: int):
    return next((s for s in SUPPLIERS if s["id"] == sid), None)

def find_supplier_by_name(name: str):
    return next((s for s in SUPPLIERS if s["name"].lower() == name.strip().lower()), None)


def search_products(query: str):
    q = (query or "").strip().lower()
    if not q:
        return list(PRODUCTS)
    return [p for p in PRODUCTS if q in p["name"].lower() or q in p["sku"].lower() or q in p["cat"].lower() or q in p.get("barcode","").lower()]
def search_clients(query: str):
    q = (query or "").strip().lower()
    if not q:
        return list(CLIENTS)
    return [c for c in CLIENTS if q in c["name"].lower() or q in c.get("nit","").lower() or q in c.get("rfc","").lower() or q in c.get("phone","").lower() or q in c["email"].lower()]


def search_suppliers(query: str):
    q = (query or "").strip().lower()
    if not q:
        return list(SUPPLIERS)
    return [s for s in SUPPLIERS if q in s["name"].lower() or q in s.get("nit","").lower() or q in s.get("rfc","").lower() or q in s.get("contact","").lower()]


# ── Helpers para reports.py ──

def get_top_products(n: int = 5):
    """Top N productos por unidades vendidas (desde SALE_ITEMS)."""
    cnt = Counter()
    for it in SALE_ITEMS:
        # solo ventas no canceladas
        sale = next((s for s in SALES if s["id"] == it["sale_id"]), None)
        if sale and sale["status"] != "Cancelada":
            cnt[it["product_id"]] += it["qty"]
    # productos sin ventas aparecen con 0 para no romper gráficos
    for p in PRODUCTS:
        cnt.setdefault(p["id"], 0)
    top = cnt.most_common(n)
    out = []
    for pid, sold in top:
        prod = find_product(pid)
        if prod:
            out.append({"id": pid, "name": prod["name"], "sold": sold})
    return out


def get_sales_by_period(days: int = 7):
    """Ventas totales por día últimos `days` días. Devuelve [{"day","total"}]."""
    today = datetime.now().date()
    # agrupar por fecha
    by_date = defaultdict(float)
    for s in SALES:
        if s["status"] == "Cancelada":
            continue
        try:
            d = datetime.strptime(s["date"], "%Y-%m-%d").date()
        except Exception:
            continue
        by_date[d.isoformat()] += s["total"]
    out = []
    for i in range(days - 1, -1, -1):
        d = today - timedelta(days=i)
        key = d.isoformat()
        label = d.strftime("%m/%d")
        out.append({"day": label, "date": key, "total": by_date.get(key, 0.0)})
    return out


def get_category_sales():
    """Stock total por categoría (para gráfico Stock por Categoría)."""
    by_cat = defaultdict(int)
    for p in PRODUCTS:
        by_cat[p["cat"]] += p["stock"]
    return [{"name": k, "stock": v, "value": v} for k, v in sorted(by_cat.items())]


def get_sales_summary():
    """Conteo de ventas por estado."""
    cnt = Counter(s["status"] for s in SALES)
    # asegurar claves esperadas
    for st in ("Pagada", "Pendiente", "Cancelada"):
        cnt.setdefault(st, 0)
    return dict(cnt)

def get_least_sold(n=5):
    """Productos menos vendidos (excluye canceladas)."""
    cnt = Counter()
    for it in SALE_ITEMS:
        sale = next((s for s in SALES if s["id"] == it["sale_id"]), None)
        if sale and sale["status"] != "Cancelada":
            cnt[it["product_id"]] += it["qty"]
    for p in PRODUCTS:
        cnt.setdefault(p["id"], 0)
    least = sorted(cnt.items(), key=lambda x: x[1])
    out = []
    for pid, sold in least[:n]:
        prod = find_product(pid)
        if prod:
            out.append({"id": pid, "name": prod["name"], "sold": sold})
    return out

def get_top_clients(n=5):
    cnt = Counter()
    sums = defaultdict(float)
    for s in SALES:
        if s["status"] == "Pagada":
            cnt[s["client"]] += 1
            sums[s["client"]] += s["total"]
    top = cnt.most_common(n)
    return [{"client": c, "orders": o, "total": sums[c]} for c, o in top]

def get_top_sellers(n=5):
    cnt = Counter()
    sums = defaultdict(float)
    for s in SALES:
        if s["status"] == "Pagada":
            v = s.get("vendedor", "vendedor")
            cnt[v] += 1
            sums[v] += s["total"]
    top = cnt.most_common(n)
    return [{"seller": v, "sales": c, "total": sums[v]} for v, c in top]

def get_margin_per_product():
    """Margen ganancia por producto: (precio - costo) * vendidos, margen %"""
    cnt = Counter()
    for it in SALE_ITEMS:
        sale = next((s for s in SALES if s["id"] == it["sale_id"]), None)
        if sale and sale["status"] == "Pagada":
            cnt[it["product_id"]] += it["qty"]
    out = []
    for p in PRODUCTS:
        sold = cnt.get(p["id"], 0)
        price = p["price"]
        cost = p.get("price_buy", price*0.7)
        margin_unit = price - cost
        margin_total = margin_unit * sold
        margin_pct = (margin_unit/price*100) if price else 0
        out.append({"sku": p["sku"], "name": p["name"], "sold": sold, "price": price, "cost": cost, "margin_unit": margin_unit, "margin_total": margin_total, "margin_pct": margin_pct})
    out.sort(key=lambda x: x["margin_total"], reverse=True)
    return out

def get_ticket_promedio():
    pagadas = [s for s in SALES if s["status"] == "Pagada"]
    if not pagadas:
        return 0.0
    return sum(s["total"] for s in pagadas) / len(pagadas)

def get_ventas_por_periodo(rango="dia"):
    """Ventas día/semana/mes/año — retorna total y count"""
    today = datetime.now().date()
    def in_range(s, days):
        try:
            d = datetime.strptime(s["date"], "%Y-%m-%d").date()
        except Exception:
            return False
        return (today - d).days < days and s["status"] != "Cancelada"
    mapping = {"dia":1, "semana":7, "mes":30, "año":365}
    days = mapping.get(rango, 1)
    filt = [s for s in SALES if in_range(s, days)]
    return {"total": sum(s["total"] for s in filt), "count": len(filt), "rango": rango}

def get_estado_resultados():
    ingresos = sum(s["total"] for s in SALES if s["status"] == "Pagada")
    # costo = suma price_buy * qty vendidos
    costo = 0
    for it in SALE_ITEMS:
        sale = next((s for s in SALES if s["id"] == it["sale_id"]), None)
        if sale and sale["status"] == "Pagada":
            prod = find_product(it["product_id"])
            if prod:
                costo += prod.get("price_buy", prod["price"]*0.7) * it["qty"]
    impuestos = sum(s.get("tax",0) for s in SALES if s["status"] == "Pagada")
    bruto = ingresos - costo
    neto = bruto - impuestos*0.1  # simula otros gastos 10% impuestos
    return {"ingresos": ingresos, "costo": costo, "bruto": bruto, "impuestos": impuestos, "neto": neto}

def get_flujo_efectivo():
    entradas = sum(s.get("paid",0) for s in SALES if s["status"] in ("Pagada","Entregada","Facturada"))
    # salidas = CxP pagado
    salidas = sum(p.get("paid",0) for p in PAYABLES) + sum(p.get("amount",0)-p.get("balance",0) for p in PAYABLES if p.get("balance") is not None)
    # simplificado: salidas = sum PAYABLES paid
    salidas = sum(p.get("paid",0) for p in PAYABLES)
    return {"entradas": entradas, "salidas": salidas, "neto": entradas - salidas}

def get_impuestos_generados():
    iva = sum(s.get("tax",0) for s in SALES if s["status"] == "Pagada")
    # IVA costo no, solo ventas
    return {"iva_19": iva, "total": iva}

def get_kpis():
    # Rotación inventario = costo ventas / promedio inventario valorizado
    estado = get_estado_resultados()
    costo = estado["costo"] or 1
    inv_val = get_inventory_value()["cost_value"] or 1
    rotacion = costo / inv_val
    dias_inv = 365 / rotacion if rotacion else 0
    # Tasa conversión = Pagada / (Cotización+Pedido+Pagada)
    total_docs = len([s for s in SALES if s["status"] in ("Pagada","Cotización","Pedido")]) or 1
    pagadas = len([s for s in SALES if s["status"]=="Pagada"]) or 0
    conversion = pagadas/total_docs*100
    bruto_pct = (estado["bruto"]/estado["ingresos"]*100) if estado["ingresos"] else 0
    neto_pct = (estado["neto"]/estado["ingresos"]*100) if estado["ingresos"] else 0
    # Punto equilibrio = costos fijos / margen bruto % (asume 5.000.000 COP fijos mes)
    costos_fijos = 5000000.0
    margen_bruto = bruto_pct/100 or 0.01
    equilibrio = costos_fijos / margen_bruto
    return {"rotacion": rotacion, "dias_inventario": dias_inv, "conversion": conversion, "margen_bruto_pct": bruto_pct, "margen_neto_pct": neto_pct, "punto_equilibrio": equilibrio, "costos_fijos": costos_fijos}


def log_action(user: str, action: str, detail: str = ""):
    AUDIT_LOG.append({
        "ts": datetime.now().isoformat(timespec="seconds"),
        "user": user or "sistema",
        "action": action,
        "detail": detail,
    })
