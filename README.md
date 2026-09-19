# Sistema de Ventas — KivyMD (Colombia, COP)

Aplicación de escritorio para punto de venta y gestión comercial: catálogo,
inventario, POS con pagos mixtos, compras, CxC/CxP, reportes con KPIs,
usuarios con 2FA y modo offline real con sincronización.

## Módulos (12 + base)

| # | Módulo | Pantalla |
|---|--------|----------|
| 1 | Usuarios y Roles (PBKDF2, lockout, bitácora, 2FA TOTP) | `screens/users.py` |
| 2 | Catálogo (ABM, CSV/Excel, barcodes, lotes, kits) | `screens/products.py` |
| 3 | Clientes CRM (NIT, crédito, descuentos) | `screens/clients.py` |
| 4 | Proveedores | `screens/suppliers.py` |
| 5 | Inventario (entradas/salidas/transferencias, valorizado, alertas) | `screens/inventory.py` |
| 6 | POS (pagos mixtos, promos, ticket, cajón, corte, offline) | `screens/pos.py` |
| 7 | Ventas y Facturación (6 tipos de doc, 6 estados, DIAN opcional) | `screens/sales.py` |
| 8 | Cuentas por Cobrar (abonos, mora, recordatorios) | `screens/receivables.py` |
| 9 | Cuentas por Pagar (programación, pronto pago) | `screens/payables.py` |
| 10 | Reportes (operativos, financieros, KPIs, CSV/PDF) | `screens/reports.py` |
| 11 | Compras (OC → recepción → CxP automática) | `screens/purchases.py` |
| 12 | Promociones y Descuentos | `screens/promos.py` |

Extras: Dashboard estilo GesNet (12 tarjetas + comparativa), login con
recuperación de contraseña, `DIAN OFF` por defecto (documentos internos;
activable para futura facturación electrónica real en `data/dian.py`).

## Requisitos

- Python 3.12
- Kivy 2.3.1 · KivyMD 2.0
- `openpyxl` (import Excel) · `reportlab` (export PDF) · `pillow`

```bash
python -m venv venv && source venv/bin/activate
pip install kivy==2.3.1 kivymd==2.0.0 openpyxl reportlab pillow
```

## Ejecución

```bash
cd sistema_ventas
python main.py
```

La base SQLite (`data/sistema_ventas.db`) se crea y se siembra sola al
iniciar; no se versiona (ver `.gitignore`).

## Usuarios de prueba

| Usuario | Clave | Rol |
|---------|-------|-----|
| admin | admin123 | Administrador |
| vendedor | venta123 | Vendedor |
| cajero | caja123 | Cajero |
| almacen | alma123 | Almacén |
| contador | conta123 | Contador |

## Estructura

```
sistema_ventas/
├── main.py               # App, tema pastel, navegación por roles
├── screens/              # 14 pantallas (login, dashboard, 12 módulos)
├── components/           # sidebar, topbar, printer, theme (UI central)
├── data/
│   ├── db.py             # SQLite + migraciones + seed
│   ├── repository.py     # Acceso a datos (las pantallas no tocan file directo)
│   ├── offline.py        # Outbox persistente + monitor + sync idempotente
│   ├── dian.py           # Facturación electrónica (OFF; punto de integración)
│   ├── totp.py           # 2FA TOTP sin dependencias
│   └── mock_data.py      # Seed inicial + flags
└── fases.md              # Especificación de los 12 módulos
```

## Notas

- Moneda COP, IVA 19%, NIT — genérico (abarrotes/electrónica/ropa).
- Offline-first: las ventas siempre se guardan local; la cola `outbox`
  sincroniza DIAN/backend al reconectar (idempotente, sobrevive reinicios).
- Sin hardware de impresión, los tickets se guardan como `.txt`.
