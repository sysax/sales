"""
SQLite — Colombia COP — reemplaza mock_data en memoria
Genérico abarrotes/electrónica — IVA 19% DIAN — NIT
Se inicializa desde mock_data si DB no existe
"""
import os, json, sqlite3, hashlib, secrets, binascii
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "sistema_ventas.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def _hash_password(pwd: str) -> str:
    """PBKDF2-HMAC-SHA256 con salt 16 bytes, retorna salt$hash hex"""
    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac('sha256', pwd.encode(), salt, 100_000)
    return binascii.hexlify(salt).decode() + "$" + binascii.hexlify(dk).decode()

def _verify_password(stored: str, provided: str) -> bool:
    try:
        salt_hex, hash_hex = stored.split("$")
        salt = binascii.unhexlify(salt_hex.encode())
        dk = hashlib.pbkdf2_hmac('sha256', provided.encode(), salt, 100_000)
        return binascii.hexlify(dk).decode() == hash_hex
    except Exception:
        # fallback plaintext (migración)
        return stored == provided

def _migrate_users(conn):
    cur = conn.cursor()
    # añadir columnas si faltan (para DB existente)
    cols = [r[1] for r in cur.execute("PRAGMA table_info(users)").fetchall()]
    for col, typ, default in [
        ("active", "INTEGER", "1"),
        ("failed_attempts", "INTEGER", "0"),
        ("locked_until", "TEXT", "NULL"),
        ("created_at", "TEXT", "NULL"),
        ("last_login", "TEXT", "NULL"),
        ("totp_secret", "TEXT", "NULL"),
        ("totp_enabled", "INTEGER", "0"),
        ("recovery_json", "TEXT", "'[]'"),
    ]:
        if col not in cols:
            cur.execute(f"ALTER TABLE users ADD COLUMN {col} {typ} DEFAULT {default}")
    # hashear passwords en texto plano
    cur.execute("SELECT username, password FROM users")
    for username, pwd in cur.fetchall():
        if pwd and "$" not in pwd:  # texto plano
            cur.execute("UPDATE users SET password=? WHERE username=?", (_hash_password(pwd), username))
    conn.commit()

def _migrate_products(conn):
    cur = conn.cursor()
    cols = [r[1] for r in cur.execute("PRAGMA table_info(products)").fetchall()]
    for col, typ, default in [
        ("image", "TEXT", "NULL"),
        ("lote", "TEXT", "NULL"),
        ("vencimiento", "TEXT", "NULL"),
        ("is_kit", "INTEGER", "0"),
        ("kit_json", "TEXT", "'[]'"),
    ]:
        if col not in cols:
            cur.execute(f"ALTER TABLE products ADD COLUMN {col} {typ} DEFAULT {default}")
    conn.commit()

def init_db(seed=True):
    conn = get_conn()
    cur = conn.cursor()
    # Users — Colombia roles, con seguridad
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY, password TEXT, role TEXT,
        active INTEGER DEFAULT 1, failed_attempts INTEGER DEFAULT 0,
        locked_until TEXT, created_at TEXT, last_login TEXT
    )""")
    # Products — Colombia genérico + imagen/lote/vencimiento/kit
    cur.execute("""CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku TEXT UNIQUE, barcode TEXT, name TEXT, description TEXT, cat TEXT, subcat TEXT,
        brand TEXT, supplier TEXT, price REAL, price_buy REAL, price_wholesale REAL,
        tax TEXT, unit TEXT, stock INTEGER, stock_min INTEGER, stock_max INTEGER,
        location TEXT, status TEXT, image TEXT, lote TEXT, vencimiento TEXT, is_kit INTEGER DEFAULT 0, kit_json TEXT DEFAULT '[]'
    )""")
    # Clients
    cur.execute("""CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE, nit TEXT, rfc TEXT, nit_dv TEXT, razon TEXT, regimen TEXT,
        responsabilidad TEXT, email TEXT, phone TEXT, address TEXT, city TEXT,
        credit REAL, credit_limit REAL, discount INTEGER, balance REAL, price_list TEXT, status TEXT
    )""")
    # Suppliers
    cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE, nit TEXT, rfc TEXT, contact TEXT, phone TEXT, email TEXT,
        city TEXT, address TEXT, catalog TEXT, lead_time TEXT, payment_terms TEXT, balance REAL
    )""")
    # Sales
    cur.execute("""CREATE TABLE IF NOT EXISTS sales (
        id TEXT PRIMARY KEY, date TEXT, client TEXT, vendedor TEXT, total REAL, subtotal REAL,
        tax REAL, discount REAL, promo TEXT, status TEXT, doc_type TEXT, payment TEXT,
        payments_json TEXT, paid REAL, balance REAL, due TEXT, estado TEXT, dian_cufe TEXT, dian_status TEXT
    )""")
    # Sale items
    cur.execute("""CREATE TABLE IF NOT EXISTS sale_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_id TEXT, product_id INTEGER, qty INTEGER, subtotal REAL
    )""")
    # Purchases
    cur.execute("""CREATE TABLE IF NOT EXISTS purchases (
        id TEXT PRIMARY KEY, date TEXT, supplier TEXT, total REAL, status TEXT, items_json TEXT, notes TEXT
    )""")
    # Inventory movements
    cur.execute("""CREATE TABLE IF NOT EXISTS inventory_movements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts TEXT, sku TEXT, product TEXT, type TEXT, qty INTEGER, before_qty INTEGER, after_qty INTEGER, reason TEXT, user TEXT
    )""")
    # Payables
    cur.execute("""CREATE TABLE IF NOT EXISTS payables (
        id TEXT PRIMARY KEY, supplier TEXT, due TEXT, amount REAL, paid REAL, balance REAL, discount_early REAL, status TEXT
    )""")
    # Payments CXC/CXP
    cur.execute("""CREATE TABLE IF NOT EXISTS payments_cxc (
        id INTEGER PRIMARY KEY AUTOINCREMENT, sale_id TEXT, date TEXT, amount REAL, method TEXT, user TEXT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS payments_cxp (
        id INTEGER PRIMARY KEY AUTOINCREMENT, payable_id TEXT, date TEXT, amount REAL, method TEXT, user TEXT
    )""")
    # Promos
    cur.execute("""CREATE TABLE IF NOT EXISTS promos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT, value REAL, condition TEXT, code TEXT UNIQUE, active INTEGER, desc TEXT
    )""")
    # Audit
    cur.execute("""CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, user TEXT, action TEXT, detail TEXT
    )""")
    # Caja single row
    cur.execute("""CREATE TABLE IF NOT EXISTS caja (
        id INTEGER PRIMARY KEY CHECK (id=1), open INTEGER, opening_amount REAL, opening_ts TEXT, opening_user TEXT, sales_today_json TEXT, expected REAL
    )""")
    cur.execute("INSERT OR IGNORE INTO caja (id, open, opening_amount, sales_today_json, expected) VALUES (1, 0, 0, '[]', 0)")
    # Counters
    cur.execute("""CREATE TABLE IF NOT EXISTS counters (
        name TEXT PRIMARY KEY, value INTEGER
    )""")
    # Outbox offline REAL — cola persistente sync DIAN/backend
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
    # Índices para mejorar performance de consultas frecuentes
    # Se crean después de las migraciones para asegurar que las columnas existen
    conn.commit()  # Commit inicial antes de índices
    _migrate_users(conn)
    _migrate_products(conn)
    
    # Crear índices (las migraciones aseguran que las columnas existen)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_outbox_status ON outbox(status)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_products_sku ON products(sku)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_products_barcode ON products(barcode)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_products_category ON products(cat)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_sales_date ON sales(date)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_sales_client ON sales(client)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_clients_nit ON clients(nit)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_inventory_movements_ts ON inventory_movements(ts)")
    if seed:
        _seed_if_empty(conn)
    conn.close()

def _seed_if_empty(conn):
    cur = conn.cursor()
    # check if already seeded
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] > 0:
        return
    from data import mock_data as md
    # Users — hash
    for u in md.USERS:
        cur.execute("INSERT INTO users (username, password, role, active, failed_attempts, created_at) VALUES (?,?,?,?,?,?)",
            (u["username"], _hash_password(u["password"]), u["role"], 1, 0, datetime.now().isoformat(timespec="seconds")))
    # Products — con imagen/lote/vencimiento/kit
    for p in md.PRODUCTS:
        # lote y vencimiento: abarrotes con vencimiento 6 meses, otros null
        lote = p.get("lote", f"L{p['sku']}-202501") if p["cat"] == "Abarrotes" else p.get("lote")
        venc = p.get("vencimiento")
        if not venc and p["cat"] == "Abarrotes":
            venc = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")
        cur.execute("""INSERT INTO products (id, sku, barcode, name, description, cat, subcat, brand, supplier, price, price_buy, price_wholesale, tax, unit, stock, stock_min, stock_max, location, status, image, lote, vencimiento, is_kit, kit_json)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (p["id"], p["sku"], p["barcode"], p["name"], p["description"], p["cat"], p["subcat"], p["brand"], p["supplier"], p["price"], p["price_buy"], p["price_wholesale"], p["tax"], p["unit"], p["stock"], p["stock_min"], p["stock_max"], p["location"], p["status"], p.get("image"), lote, venc, 1 if p.get("is_kit") else 0, json.dumps(p.get("kit_json", []))))
    # Clients
    for c in md.CLIENTS:
        cur.execute("""INSERT INTO clients (id, name, nit, rfc, nit_dv, razon, regimen, responsabilidad, email, phone, address, city, credit, credit_limit, discount, balance, price_list, status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (c["id"], c["name"], c.get("nit",c.get("rfc","")), c.get("rfc",""), c.get("nit_dv",""), c["razon"], c["regimen"], c.get("responsabilidad",c["regimen"]), c["email"], c["phone"], c["address"], c["city"], c["credit"], c["credit_limit"], c["discount"], c["balance"], c["price_list"], c["status"]))
    # Suppliers
    for s in md.SUPPLIERS:
        cur.execute("""INSERT INTO suppliers (id, name, nit, rfc, contact, phone, email, city, address, catalog, lead_time, payment_terms, balance)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (s["id"], s["name"], s.get("nit",s.get("rfc","")), s.get("rfc",""), s["contact"], s["phone"], s["email"], s["city"], s["address"], s["catalog"], s["lead_time"], s["payment_terms"], s["balance"]))
    # Sales
    for s in md.SALES:
        cur.execute("""INSERT INTO sales (id, date, client, vendedor, total, subtotal, tax, discount, promo, status, doc_type, payment, payments_json, paid, balance, due, estado, dian_cufe, dian_status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (s["id"], s["date"], s["client"], s.get("vendedor","vendedor"), s["total"], s.get("subtotal",s["total"]), s.get("tax",0), s.get("discount",0), s.get("promo"), s["status"], s.get("doc_type","Factura electrónica DIAN"), s.get("payment",""), json.dumps(s.get("payments",{})), s.get("paid",0), s.get("balance",0), s.get("due",s["date"]), s.get("estado",s["status"]), s.get("dian_cufe",f"CUFE-{s['id']}-DIAN"), s.get("dian_status","SINCRONIZADO")))
    # Sale items
    for it in md.SALE_ITEMS:
        cur.execute("INSERT INTO sale_items (sale_id, product_id, qty, subtotal) VALUES (?,?,?,?)", (it["sale_id"], it["product_id"], it["qty"], it["subtotal"]))
    # Purchases
    for p in md.PURCHASES:
        cur.execute("INSERT INTO purchases (id, date, supplier, total, status, items_json, notes) VALUES (?,?,?,?,?,?,?)",
            (p["id"], p["date"], p["supplier"], p["total"], p["status"], json.dumps(p.get("items",[])), p.get("notes","")))
    # Movements
    for m in md.INVENTORY_MOVEMENTS:
        cur.execute("INSERT INTO inventory_movements (id, ts, sku, product, type, qty, before_qty, after_qty, reason, user) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (m["id"], m["ts"], m["sku"], m["product"], m["type"], m["qty"], m["before"], m["after"], m["reason"], m["user"]))
    # Payables
    for p in md.PAYABLES:
        cur.execute("INSERT INTO payables (id, supplier, due, amount, paid, balance, discount_early, status) VALUES (?,?,?,?,?,?,?,?)",
            (p["id"], p["supplier"], p["due"], p["amount"], p.get("paid",0), p.get("balance",p["amount"]), p.get("discount_early",0), p["status"]))
    for pc in md.PAYMENTS_CXC:
        cur.execute("INSERT INTO payments_cxc (id, sale_id, date, amount, method, user) VALUES (?,?,?,?,?,?)", (pc["id"], pc["sale_id"], pc["date"], pc["amount"], pc["method"], pc["user"]))
    for pp in md.PAYMENTS_CXP:
        cur.execute("INSERT INTO payments_cxp (id, payable_id, date, amount, method, user) VALUES (?,?,?,?,?,?)", (pp["id"], pp["payable_id"], pp["date"], pp["amount"], pp["method"], pp["user"]))
    for pr in md.PROMOS:
        cur.execute("INSERT INTO promos (id, name, type, value, condition, code, active, desc) VALUES (?,?,?,?,?,?,?,?)",
            (pr["id"], pr["name"], pr["type"], pr["value"], pr["condition"], pr["code"], 1 if pr["active"] else 0, pr["desc"]))
    # Audit empty
    # Counters
    cur.execute("INSERT OR REPLACE INTO counters VALUES ('SALE_COUNTER', ?)", (md.SALE_COUNTER,))
    cur.execute("INSERT OR REPLACE INTO counters VALUES ('QUOTE_COUNTER', ?)", (md.QUOTE_COUNTER,))
    cur.execute("INSERT OR REPLACE INTO counters VALUES ('ORDER_COUNTER', ?)", (md.ORDER_COUNTER,))
    cur.execute("INSERT OR REPLACE INTO counters VALUES ('CREDIT_NOTE_COUNTER', ?)", (md.CREDIT_NOTE_COUNTER,))
    cur.execute("INSERT OR REPLACE INTO counters VALUES ('PURCHASE_COUNTER', ?)", (md.PURCHASE_COUNTER,))
    # Seed caja already done
    conn.commit()

def get_counter(name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT value FROM counters WHERE name=?", (name,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0

def set_counter(name, value):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO counters VALUES (?,?)", (name, value))
    conn.commit()
    conn.close()

def next_counter(name, prefix, width=3):
    val = get_counter(name)
    folio = f"{prefix}{val:0{width}d}"
    set_counter(name, val+1)
    return folio

# init on import
try:
    init_db()
except Exception as e:
    print(f"[DB] init error: {e}")
