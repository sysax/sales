"""
Capa de acceso — Colombia COP — SQLite (data/db.py) — antes mock_data
Pantallas no tocan mock_data directo; todo vía repo (offline queue en /tmp)
"""
import json, sqlite3
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from data import db as sqlite
from data import mock_data as mock  # solo IS_OFFLINE, ROLES

ROLE_PERMISSIONS = {
    "Administrador": {"*"},
    "Vendedor": {"dashboard", "products", "pos", "sales", "clients", "inventory"},
    "Cajero": {"dashboard", "pos", "sales"},
    "Almacén": {"dashboard", "products", "inventory", "purchases", "suppliers"},
    "Contador": {"dashboard", "sales", "receivables", "payables", "reports", "purchases"},
}

def _row_to_dict(row):
    if row is None:
        return None
    d = dict(row)
    # decode json fields
    if "payments_json" in d and d["payments_json"]:
        try:
            d["payments"] = json.loads(d["payments_json"])
        except Exception:
            d["payments"] = {}
    if "items_json" in d and d["items_json"]:
        try:
            d["items"] = json.loads(d["items_json"])
        except Exception:
            d["items"] = []
    if "sales_today_json" in d and d["sales_today_json"]:
        try:
            d["sales_today"] = json.loads(d["sales_today_json"])
        except Exception:
            d["sales_today"] = []
    # active boolean
    if "active" in d:
        d["active"] = bool(d["active"])
    return d

class Repository:
    # Users — autenticación segura PBKDF2 + lockout + active
    def list_users(self):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT username, role, active, failed_attempts, locked_until, created_at, last_login, totp_enabled FROM users ORDER BY username")
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
        for r in rows:
            r["totp_enabled"] = bool(r.get("totp_enabled", 0))
        return rows
    def find_user(self, username, password):
        """Auth segura: verifica hash, controla active/bloqueo 3 intentos → 5 min lockout, actualiza last_login"""
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cur.fetchone()
        if not row:
            conn.close(); return None
        user = _row_to_dict(row)
        if not user.get("active", 1):
            conn.close(); return None
        locked = user.get("locked_until")
        if locked:
            try:
                locked_dt = datetime.fromisoformat(locked)
                if datetime.now() < locked_dt:
                    conn.close(); return None
                else:
                    cur.execute("UPDATE users SET failed_attempts=0, locked_until=NULL WHERE username=?", (username,))
                    conn.commit()
            except Exception:
                pass
        from data.db import _verify_password
        stored = row["password"]
        if _verify_password(stored, password):
            cur.execute("UPDATE users SET failed_attempts=0, locked_until=NULL, last_login=? WHERE username=?", (datetime.now().isoformat(timespec="seconds"), username))
            conn.commit()
            conn.close()
            # retornar sin password hash
            user["password"] = "***"
            return user
        else:
            attempts = (user.get("failed_attempts") or 0) + 1
            locked_until = None
            if attempts >= 3:
                locked_until = (datetime.now() + timedelta(minutes=5)).isoformat(timespec="seconds")
            cur.execute("UPDATE users SET failed_attempts=?, locked_until=? WHERE username=?", (attempts, locked_until, username))
            conn.commit()
            conn.close()
            return None
    def find_user_by_name(self, username):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT username, role, active, failed_attempts, locked_until, created_at, last_login, totp_enabled FROM users WHERE username=?", (username,))
        r = cur.fetchone()
        if r:
            d = dict(r)
            d["active"] = bool(d["active"])
            d["totp_enabled"] = bool(d.get("totp_enabled", 0))
            conn.close(); return d
        conn.close(); return None
    def find_user_raw(self, username):
        """Devuelve fila completa para admin (con hash)"""
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        r = _row_to_dict(cur.fetchone()); conn.close(); return r
    def add_user(self, username, password, role):
        if self.find_user_by_name(username):
            raise ValueError("Usuario ya existe")
        if role not in mock.ROLES:
            raise ValueError(f"Rol inválido: {role}")
        if len(password) < 4:
            raise ValueError("Contraseña mínimo 4 caracteres")
        from data.db import _hash_password
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password, role, active, failed_attempts, created_at) VALUES (?,?,?,?,?,?)",
            (username, _hash_password(password), role, 1, 0, datetime.now().isoformat(timespec="seconds")))
        conn.commit(); conn.close()
        self.log(username, "alta_usuario", f"rol={role}")
    def update_user(self, username, password=None, role=None):
        u = self.find_user_by_name(username)
        if not u:
            raise ValueError("Usuario no encontrado")
        conn = sqlite.get_conn(); cur = conn.cursor()
        if password:
            if len(password) < 4:
                conn.close(); raise ValueError("Contraseña mínimo 4")
            from data.db import _hash_password
            cur.execute("UPDATE users SET password=? WHERE username=?", (_hash_password(password), username))
        if role:
            if role not in mock.ROLES:
                conn.close(); raise ValueError(f"Rol inválido: {role}")
            cur.execute("UPDATE users SET role=? WHERE username=?", (role, username))
        conn.commit(); conn.close()
    def set_user_active(self, username, active: bool):
        if username == "admin" and not active:
            raise ValueError("No se puede bloquear admin")
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("UPDATE users SET active=?, failed_attempts=0, locked_until=NULL WHERE username=?", (1 if active else 0, username))
        if cur.rowcount == 0:
            conn.close(); raise ValueError("Usuario no encontrado")
        conn.commit(); conn.close()
        self.log("sistema", "usuario_bloqueo" if not active else "usuario_desbloqueo", username)
    def reset_password(self, username, new_password):
        if len(new_password) < 4:
            raise ValueError("Contraseña mínimo 4")
        from data.db import _hash_password
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("UPDATE users SET password=?, failed_attempts=0, locked_until=NULL WHERE username=?", (_hash_password(new_password), username))
        if cur.rowcount == 0:
            conn.close(); raise ValueError("Usuario no encontrado")
        conn.commit(); conn.close()
        self.log("sistema", "reset_password", username)
    def delete_user(self, username):
        if username == "admin":
            raise ValueError("No se puede eliminar admin")
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE username=?", (username,))
        if cur.rowcount == 0:
            conn.close(); raise ValueError("Usuario no encontrado")
        conn.commit(); conn.close()
    # ── 2FA TOTP + códigos recuperación ──
    def is_2fa_enabled(self, username) -> bool:
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT totp_enabled FROM users WHERE username=?", (username,))
        r = cur.fetchone(); conn.close()
        return bool(r and r[0])
    def enable_2fa(self, username):
        """Genera secreto y lo guarda pendiente (enabled=0). Retorna secreto."""
        from data import totp as t
        u = self.find_user_by_name(username)
        if not u: raise ValueError("Usuario no encontrado")
        secret = t.generate_secret()
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("UPDATE users SET totp_secret=?, totp_enabled=0 WHERE username=?", (secret, username))
        conn.commit(); conn.close()
        self.log("sistema", "2fa_secret", username)
        return secret
    def confirm_2fa(self, username, code):
        """Verifica código contra secreto pendiente y activa. Retorna recovery codes plano (una vez)."""
        from data import totp as t
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT totp_secret FROM users WHERE username=?", (username,))
        r = cur.fetchone()
        if not r or not r[0]:
            conn.close(); raise ValueError("Sin secreto 2FA — genere primero")
        if not t.verify(r[0], code):
            conn.close(); raise ValueError("Código 2FA inválido")
        codes = t.generate_recovery_codes(8)
        hashed = json.dumps([t.hash_code(c) for c in codes])
        cur.execute("UPDATE users SET totp_enabled=1, recovery_json=? WHERE username=?", (hashed, username))
        conn.commit(); conn.close()
        self.log(username, "2fa_activado", "")
        return codes
    def verify_2fa(self, username, code):
        """Acepta TOTP o código recuperación (un solo uso, lo consume)."""
        from data import totp as t
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT totp_secret, recovery_json FROM users WHERE username=?", (username,))
        r = cur.fetchone()
        if not r:
            conn.close(); return False
        secret, rec_json = r[0], r[1]
        if secret and t.verify(secret, code):
            conn.close(); return True
        # recovery code (consume)
        try:
            hashed = json.loads(rec_json or "[]")
        except Exception:
            hashed = []
        h = t.hash_code(code)
        if h in hashed:
            hashed.remove(h)
            cur.execute("UPDATE users SET recovery_json=? WHERE username=?", (json.dumps(hashed), username))
            conn.commit(); conn.close()
            self.log(username, "2fa_recovery_usado", f"quedan {len(hashed)}")
            return True
        conn.close(); return False
    def disable_2fa(self, username):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("UPDATE users SET totp_secret=NULL, totp_enabled=0, recovery_json='[]' WHERE username=?", (username,))
        if cur.rowcount == 0:
            conn.close(); raise ValueError("Usuario no encontrado")
        conn.commit(); conn.close()
        self.log("sistema", "2fa_desactivado", username)
    def regenerate_recovery_codes(self, username):
        from data import totp as t
        if not self.is_2fa_enabled(username):
            raise ValueError("2FA no activo para este usuario")
        codes = t.generate_recovery_codes(8)
        hashed = json.dumps([t.hash_code(c) for c in codes])
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("UPDATE users SET recovery_json=? WHERE username=?", (hashed, username))
        conn.commit(); conn.close()
        self.log(username, "2fa_recovery_regenerado", "")
        return codes
    def recovery_codes_left(self, username) -> int:
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT recovery_json FROM users WHERE username=?", (username,))
        r = cur.fetchone(); conn.close()
        try:
            return len(json.loads((r[0] if r else "[]") or "[]"))
        except Exception:
            return 0
    # ── Recuperación contraseña (tokens un solo uso, 30 min) ──
    def request_recovery(self, username):
        """Genera token de recuperación. Sin servidor correo: se muestra en UI y bitácora."""
        import secrets as _s
        u = self.find_user_by_name(username)
        if not u: raise ValueError("Usuario no existe")
        token = _s.token_hex(3).upper()  # 6 hex chars
        now = datetime.now()
        exp = (now + timedelta(minutes=30)).isoformat(timespec="seconds")
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO recovery_tokens (token, username, created_ts, expires_ts, used) VALUES (?,?,?,?,0)",
                    (token, username, now.isoformat(timespec="seconds"), exp))
        conn.commit(); conn.close()
        self.log(username, "recovery_solicitado", f"expira {exp}")
        return token, exp
    def redeem_recovery(self, username, token, new_password):
        if len(new_password) < 4:
            raise ValueError("Contraseña mínimo 4")
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT username, expires_ts, used FROM recovery_tokens WHERE token=?", (token.strip().upper(),))
        r = cur.fetchone()
        if not r:
            conn.close(); raise ValueError("Token inválido")
        if (r[0] or "").lower() != username.strip().lower():
            conn.close(); raise ValueError("Token no corresponde a este usuario")
        if r[2]:
            conn.close(); raise ValueError("Token ya usado")
        cur.execute("SELECT expires_ts FROM recovery_tokens WHERE token=?", (token.strip().upper(),))
        try:
            exp = datetime.fromisoformat(cur.fetchone()[0])
        except Exception:
            conn.close(); raise ValueError("Token expirado")
        if datetime.now() > exp:
            conn.close(); raise ValueError("Token expirado (30 min)")
        from data.db import _hash_password
        cur.execute("UPDATE users SET password=?, failed_attempts=0, locked_until=NULL WHERE username=?",
                    (_hash_password(new_password), username))
        cur.execute("UPDATE recovery_tokens SET used=1 WHERE token=?", (token.strip().upper(),))
        conn.commit(); conn.close()
        self.log(username, "recovery_completado", "")
        return True
    def can_access(self, role, screen_name):
        perms = ROLE_PERMISSIONS.get(role, set())
        return "*" in perms or screen_name in perms

    # Products
    def list_products(self):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products ORDER BY id")
        rows = [_row_to_dict(r) for r in cur.fetchall()]
        conn.close(); return rows
    def find_product(self, pid):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=?", (pid,))
        r = _row_to_dict(cur.fetchone()); conn.close(); return r
    def find_product_by_sku(self, sku):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE lower(sku)=lower(?)", (sku.strip(),))
        r = _row_to_dict(cur.fetchone()); conn.close(); return r
    def find_product_by_barcode(self, barcode):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE barcode=?", (barcode.strip(),))
        r = _row_to_dict(cur.fetchone()); conn.close(); return r
    def search_products(self, q):
        q = (q or "").strip().lower()
        if not q:
            return self.list_products()
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE lower(name) LIKE ? OR lower(sku) LIKE ? OR lower(cat) LIKE ? OR barcode LIKE ?", (f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%"))
        rows = [_row_to_dict(r) for r in cur.fetchall()]
        conn.close(); return rows
    def add_product(self, data):
        sku = data.get("sku","").strip()
        if not sku: raise ValueError("SKU requerido")
        if self.find_product_by_sku(sku): raise ValueError(f"SKU {sku} ya existe")
        name = data.get("name","").strip()
        if len(name) < 2: raise ValueError("Nombre mínimo 2 caracteres")
        try:
            price = float(data.get("price",0)); stock = int(data.get("stock",0))
        except Exception:
            raise ValueError("Precio/stock numérico")
        if price <=0 or stock<0: raise ValueError("Precio >0 y stock >=0")
        # numéricos opcionales toleran "" (vienen de Excel/CSV)
        try:
            price_buy = float(data.get("price_buy") or price * 0.7)
            price_ws = float(data.get("price_wholesale") or price * 0.9)
        except Exception:
            raise ValueError("price_buy/price_wholesale numérico")
        # imagen, lote, vencimiento, kit
        image = data.get("image")
        lote = data.get("lote")
        venc = data.get("vencimiento")
        # si es abarrotes y no tiene vencimiento, sugerir 180 días
        if not venc and data.get("cat","") == "Abarrotes":
            from datetime import datetime, timedelta
            venc = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")
        is_kit = 1 if data.get("is_kit") else 0
        kit_json = data.get("kit_json", "[]")
        if isinstance(kit_json, list):
            import json as _json
            kit_json = _json.dumps(kit_json)
        # kit validación: si es kit, debe tener componentes y stock es virtual
        if is_kit:
            try:
                comps = json.loads(kit_json) if isinstance(kit_json, str) else kit_json
                if not comps:
                    raise ValueError("Kit debe tener componentes")
                for c in comps:
                    if not self.find_product_by_sku(c.get("sku","")):
                        raise ValueError(f"Componente {c.get('sku')} no existe")
            except ValueError:
                raise
            except Exception:
                raise ValueError("kit_json inválido")
        barcode = data.get("barcode", f"770{abs(hash(sku))%10000000000:010d}")
        # asegurar EAN 13: si no es 13 dígitos, generar
        if not barcode or len(barcode) < 8:
            barcode = f"770{abs(hash(sku))%10000000000:010d}"
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("""INSERT INTO products (sku, barcode, name, description, cat, subcat, brand, supplier, price, price_buy, price_wholesale, tax, unit, stock, stock_min, stock_max, location, status, image, lote, vencimiento, is_kit, kit_json)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (sku, barcode, name, data.get("description",""), data.get("cat","General"), data.get("subcat",""), data.get("brand",""), data.get("supplier",""), price, price_buy, price_ws, data.get("tax","IVA 19%"), data.get("unit","unidad"), stock, int(data.get("stock_min",5)), int(data.get("stock_max", stock+50)), data.get("location",""), data.get("status","activo"), image, lote, venc, is_kit, kit_json))
        conn.commit()
        cur.execute("SELECT * FROM products WHERE sku=?", (sku,))
        r = _row_to_dict(cur.fetchone()); conn.close(); return r
    def update_product(self, sku, updates):
        p = self.find_product_by_sku(sku)
        if not p: raise ValueError(f"Producto SKU {sku} no encontrado")
        conn = sqlite.get_conn(); cur = conn.cursor()
        for k in ("name","cat","price","stock","stock_min","stock_max","status","price_buy","brand","location","image","lote","vencimiento","is_kit","kit_json","barcode"):
            if k in updates and updates[k]!="":
                if k in ("price","price_buy","price_wholesale"):
                    try:
                        v=float(updates[k])
                        if v<=0: raise ValueError
                    except Exception:
                        conn.close(); raise ValueError(f"{k} debe ser número >0")
                    cur.execute(f"UPDATE products SET {k}=? WHERE sku=?", (v, sku))
                elif k in ("stock","stock_min","stock_max","is_kit"):
                    try:
                        v=int(updates[k])
                        if k!="is_kit" and v<0: raise ValueError
                    except Exception:
                        conn.close(); raise ValueError(f"{k} debe ser entero >=0")
                    cur.execute(f"UPDATE products SET {k}=? WHERE sku=?", (v, sku))
                else:
                    v=updates[k].strip() if isinstance(updates[k], str) else updates[k]
                    # kit_json puede ser lista
                    if k=="kit_json" and isinstance(v, list):
                        import json as _json
                        v=_json.dumps(v)
                    cur.execute(f"UPDATE products SET {k}=? WHERE sku=?", (v, sku))
        conn.commit()
        r = self.find_product_by_sku(sku); conn.close(); return r
    def delete_product(self, sku):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE sku=?", (sku,))
        if cur.rowcount==0:
            conn.close(); raise ValueError(f"SKU {sku} no encontrado")
        conn.commit(); conn.close()
    # Barcode generar/imprimir + lotes + kits
    def generate_barcode(self, sku):
        """Genera barcode EAN13 imagen en /tmp/barcodes/{sku}.png — COP Colombia, usa PIL fallback"""
        p = self.find_product_by_sku(sku)
        if not p: raise ValueError(f"SKU {sku} no encontrado")
        barcode = p.get("barcode") or f"770{abs(hash(sku))%10000000000:010d}"
        # asegurar
        if len(barcode) < 12:
            barcode = barcode.ljust(12, "0")
        barcode = barcode[:13]
        import os
        out_dir = "/tmp/barcodes"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{sku}.png")
        # intentar python-barcode
        try:
            import barcode as bc
            from barcode.writer import ImageWriter
            from barcode import get_barcode_class
            ean = get_barcode_class('ean13')
            writer = ImageWriter()
            obj = ean(barcode[:12], writer=writer)
            # ean calcula dígito control; usar 12 dígitos base
            filename = obj.save(os.path.join(out_dir, sku))
            # obj.save añade .png si no existe, pero ya lo hace
            if os.path.exists(filename):
                # actualizar producto barcode si cambió
                conn = sqlite.get_conn(); cur = conn.cursor()
                cur.execute("UPDATE products SET barcode=? WHERE sku=?", (barcode, sku))
                conn.commit(); conn.close()
                return filename
        except Exception:
            pass
        # fallback PIL texto
        try:
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (400, 100), color='white')
            d = ImageDraw.Draw(img)
            try:
                font = ImageFont.load_default()
            except Exception:
                font = None
            d.text((10,10), f"SKU: {sku}", fill='black', font=font)
            d.text((10,35), f"BARCODE: {barcode}", fill='black', font=font)
            d.rectangle([10,60,390,90], outline='black')
            # barras simuladas
            for i, ch in enumerate(barcode):
                w = 2 if int(ch) %2==0 else 4
                d.rectangle([10+i*20, 62, 10+i*20+w, 88], fill='black')
            img.save(out_path, 'PNG')
            # actualizar barcode
            conn = sqlite.get_conn(); cur = conn.cursor()
            cur.execute("UPDATE products SET barcode=? WHERE sku=?", (barcode, sku))
            conn.commit(); conn.close()
            return out_path
        except Exception as e:
            # fallback txt
            txt_path = os.path.join(out_dir, f"{sku}.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(f"SKU {sku}\nBARCODE {barcode}\n")
            return txt_path
    def print_barcode(self, sku):
        path = self.generate_barcode(sku)
        # intentar lp
        try:
            import subprocess
            subprocess.run(["lp", path], timeout=2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return path, True
        except Exception:
            return path, False
    def get_products_by_vencimiento(self, days=30):
        """Productos por caducar en X días — solo abarrotes con vencimiento"""
        from datetime import datetime, timedelta
        limit = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE vencimiento IS NOT NULL AND vencimiento != '' AND date(vencimiento) <= date(?) AND date(vencimiento) >= date('now')", (limit,))
        rows = [_row_to_dict(r) for r in cur.fetchall()]
        conn.close(); return rows
    def get_kits(self):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE is_kit=1")
        rows = [_row_to_dict(r) for r in cur.fetchall()]
        conn.close(); return rows
    def create_kit(self, sku, name, components, price=None, user="sistema"):
        """Crea kit: components = [{"sku": "AB01", "qty":2}, ...]"""
        if self.find_product_by_sku(sku):
            raise ValueError(f"SKU {sku} ya existe")
        if not components or not isinstance(components, list):
            raise ValueError("Componentes lista requerida")
        total_cost = 0
        for c in components:
            prod = self.find_product_by_sku(c.get("sku",""))
            if not prod:
                raise ValueError(f"Componente {c.get('sku')} no existe")
            if c.get("qty",0) <=0:
                raise ValueError("Qty >0")
            total_cost += prod.get("price_buy", prod["price"]*0.7) * c["qty"]
        # precio venta kit: si no se da, suma precio venta componentes con 5% descuento
        if price is None:
            total_sale = sum(self.find_product_by_sku(c["sku"])["price"] * c["qty"] for c in components)
            price = total_sale * 0.95
        import json as _json
        kit_json = _json.dumps(components)
        # stock kit = mínimo de componentes floor(stock/qty)
        min_stock = min(self.find_product_by_sku(c["sku"])["stock"] // c["qty"] for c in components)
        data = {"sku": sku, "name": name, "cat": "Kits", "description": f"Kit {len(components)} productos", "price": price, "stock": min_stock, "is_kit": 1, "kit_json": kit_json, "barcode": f"770{abs(hash(sku))%10000000000:010d}", "price_buy": total_cost}
        prod = self.add_product(data)
        self.log(user, "kit_creado", f"{sku} {components}")
        return prod
    def get_kit_components(self, sku):
        p = self.find_product_by_sku(sku)
        if not p or not p.get("is_kit"):
            raise ValueError(f"Kit {sku} no encontrado")
        import json as _json
        try:
            return _json.loads(p.get("kit_json") or "[]")
        except Exception:
            return []

    # Clients
    def list_clients(self):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM clients ORDER BY id")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def find_client(self, name):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE lower(name)=lower(?)", (name.strip(),))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_client_by_id(self, cid):
        conn = sqlite.get_conn(); cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE id=?", (cid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def search_clients(self, q):
        q=(q or "").strip().lower()
        if not q: return self.list_clients()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM clients WHERE lower(name) LIKE ? OR lower(nit) LIKE ? OR lower(rfc) LIKE ? OR lower(phone) LIKE ? OR lower(email) LIKE ?", (f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%"))
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def add_client(self, data):
        name=data.get("name","").strip()
        if len(name)<2: raise ValueError("Nombre mínimo 2 caracteres")
        if self.find_client(name): raise ValueError("Cliente ya existe")
        nit=data.get("nit", data.get("rfc","")).strip()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("""INSERT INTO clients (name, nit, rfc, nit_dv, razon, regimen, responsabilidad, email, phone, address, city, credit, credit_limit, discount, balance, price_list, status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (name, nit, nit, nit.split("-")[-1] if "-" in nit else "", data.get("razon",name), data.get("regimen","No responsable IVA"), data.get("responsabilidad", data.get("regimen","No responsable IVA")), data.get("email",""), data.get("phone",""), data.get("address",""), data.get("city",""), float(data.get("credit",0)), float(data.get("credit_limit",5000000)), int(data.get("discount",0)), float(data.get("balance",0)), data.get("price_list","detal"), data.get("status","activo")))
        conn.commit()
        cur.execute("SELECT * FROM clients WHERE name=?", (name,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def update_client(self, cid, updates):
        c=self.find_client_by_id(cid)
        if not c: raise ValueError(f"Cliente ID {cid} no encontrado")
        conn=sqlite.get_conn(); cur=conn.cursor()
        for k in ("name","nit","rfc","email","phone","city","address","credit_limit","discount","status","price_list","regimen","responsabilidad"):
            if k in updates and updates[k]!="":
                if k=="credit_limit":
                    try: v=float(updates[k])
                    except: conn.close(); raise ValueError("Límite crédito numérico")
                    cur.execute("UPDATE clients SET credit_limit=? WHERE id=?", (v,cid))
                elif k=="discount":
                    try: v=int(updates[k]); assert 0<=v<=100
                    except: conn.close(); raise ValueError("Descuento 0-100")
                    cur.execute("UPDATE clients SET discount=? WHERE id=?", (v,cid))
                else:
                    v=updates[k].strip() if isinstance(updates[k], str) else updates[k]
                    col = "nit" if k=="nit" else k
                    cur.execute(f"UPDATE clients SET {col}=? WHERE id=?", (v,cid))
                    if k=="nit":
                        cur.execute("UPDATE clients SET rfc=? WHERE id=?", (v,cid))
        conn.commit()
        r=self.find_client_by_id(cid); conn.close(); return r
    def delete_client(self, cid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("DELETE FROM clients WHERE id=?", (cid,))
        if cur.rowcount==0: conn.close(); raise ValueError(f"Cliente ID {cid} no encontrado")
        conn.commit(); conn.close()

    # Suppliers
    def list_suppliers(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers ORDER BY id")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def find_supplier(self, sid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE id=?", (sid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_supplier_by_name(self, name):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE lower(name)=lower(?)", (name.strip(),))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def search_suppliers(self, q):
        q=(q or "").strip().lower()
        if not q: return self.list_suppliers()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE lower(name) LIKE ? OR lower(nit) LIKE ? OR lower(rfc) LIKE ? OR lower(contact) LIKE ?", (f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%"))
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def add_supplier(self, data):
        name=data.get("name","").strip()
        if len(name)<2: raise ValueError("Empresa mínimo 2 caracteres")
        if self.find_supplier_by_name(name): raise ValueError("Proveedor ya existe")
        nit=data.get("nit", data.get("rfc","")).strip()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("""INSERT INTO suppliers (name, nit, rfc, contact, phone, email, city, address, catalog, lead_time, payment_terms, balance)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (name, nit, nit, data.get("contact",""), data.get("phone",""), data.get("email",""), data.get("city",""), data.get("address",""), data.get("catalog",""), data.get("lead_time",""), data.get("payment_terms",""), float(data.get("balance",0))))
        conn.commit()
        cur.execute("SELECT * FROM suppliers WHERE name=?", (name,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def update_supplier(self, sid, updates):
        s=self.find_supplier(sid)
        if not s: raise ValueError(f"Proveedor ID {sid} no encontrado")
        conn=sqlite.get_conn(); cur=conn.cursor()
        for k in ("name","nit","rfc","contact","phone","email","city","catalog","lead_time","payment_terms"):
            if k in updates and updates[k]!="":
                v=updates[k].strip() if isinstance(updates[k], str) else updates[k]
                col=k
                cur.execute(f"UPDATE suppliers SET {col}=? WHERE id=?", (v,sid))
                if k=="nit":
                    cur.execute("UPDATE suppliers SET rfc=? WHERE id=?", (v,sid))
        conn.commit(); r=self.find_supplier(sid); conn.close(); return r
    def delete_supplier(self, sid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("DELETE FROM suppliers WHERE id=?", (sid,))
        if cur.rowcount==0: conn.close(); raise ValueError(f"Proveedor ID {sid} no encontrado")
        conn.commit(); conn.close()

    # Sales etc
    def list_sales(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM sales ORDER BY date DESC, id DESC")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def list_purchases(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM purchases ORDER BY date DESC")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def list_sale_items(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM sale_items")
        rows=[dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def list_promoss(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM promos ORDER BY id")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def find_purchase(self, folio):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM purchases WHERE id=?", (folio,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_sale(self, sid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id=?", (sid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def next_sale_folio(self):
        return sqlite.next_counter("SALE_COUNTER", "V")
    def get_stats(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COUNT(*) FROM products"); total_products=cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM clients"); total_clients=cur.fetchone()[0]
        cur.execute("SELECT COALESCE(SUM(total),0) FROM sales WHERE status='Pagada'"); total_sales=cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM sales WHERE status='Pendiente'"); pending=cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM products WHERE stock < stock_min"); low=cur.fetchone()[0]
        conn.close()
        return {"total_sales": f"${total_sales:,.2f}", "total_products": total_products, "total_clients": total_clients, "pending_orders": pending, "low_stock_alerts": low}
    def get_top_products(self, n=5):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("""SELECT product_id, SUM(qty) as sold FROM sale_items JOIN sales ON sale_items.sale_id=sales.id WHERE sales.status!='Cancelada' GROUP BY product_id ORDER BY sold DESC LIMIT ?""", (n,))
        top=cur.fetchall()
        # include zero sold
        if len(top)<n:
            cur.execute("SELECT id FROM products")
            all_ids=[r[0] for r in cur.fetchall()]
            existing=[r[0] for r in top]
            for pid in all_ids:
                if pid not in existing:
                    # append zero
                    top.append((pid,0))
                    if len(top)>=n: break
        out=[]
        for pid, sold in top[:n]:
            cur.execute("SELECT * FROM products WHERE id=?", (pid,))
            prod=_row_to_dict(cur.fetchone())
            if prod:
                out.append({"id": pid, "name": prod["name"], "sold": sold})
        conn.close(); return out
    def get_least_sold(self, n=5):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("""SELECT product_id, SUM(qty) as sold FROM sale_items JOIN sales ON sale_items.sale_id=sales.id WHERE sales.status!='Cancelada' GROUP BY product_id""")
        cnt={r[0]: r[1] for r in cur.fetchall()}
        cur.execute("SELECT id, name FROM products")
        for pid, name in cur.fetchall():
            cnt.setdefault(pid, 0)
        least=sorted(cnt.items(), key=lambda x: x[1])[:n]
        out=[]
        for pid, sold in least:
            cur.execute("SELECT name FROM products WHERE id=?", (pid,))
            row=cur.fetchone()
            if row:
                out.append({"id": pid, "name": row[0], "sold": sold})
        conn.close(); return out
    def get_top_clients(self, n=5):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT client, COUNT(*), SUM(total) FROM sales WHERE status='Pagada' GROUP BY client ORDER BY COUNT(*) DESC LIMIT ?", (n,))
        rows=cur.fetchall(); conn.close()
        return [{"client": r[0], "orders": r[1], "total": r[2]} for r in rows]
    def get_top_sellers(self, n=5):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT vendedor, COUNT(*), SUM(total) FROM sales WHERE status='Pagada' GROUP BY vendedor ORDER BY COUNT(*) DESC LIMIT ?", (n,))
        rows=cur.fetchall(); conn.close()
        return [{"seller": r[0], "sales": r[1], "total": r[2]} for r in rows]
    def get_margin_per_product(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products")
        prods=[_row_to_dict(r) for r in cur.fetchall()]
        # sold count
        cur.execute("SELECT product_id, SUM(qty) FROM sale_items JOIN sales ON sale_items.sale_id=sales.id WHERE sales.status='Pagada' GROUP BY product_id")
        cnt={r[0]: r[1] for r in cur.fetchall()}
        out=[]
        for p in prods:
            sold=cnt.get(p["id"],0)
            price=p["price"]; cost=p.get("price_buy", price*0.7)
            mu=price-cost; mt=mu*sold; pct=(mu/price*100) if price else 0
            out.append({"sku": p["sku"], "name": p["name"], "sold": sold, "price": price, "cost": cost, "margin_unit": mu, "margin_total": mt, "margin_pct": pct})
        conn.close()
        out.sort(key=lambda x: x["margin_total"], reverse=True)
        return out
    def get_ticket_promedio(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT AVG(total) FROM sales WHERE status='Pagada'")
        v=cur.fetchone()[0] or 0; conn.close(); return v
    def get_ventas_por_periodo(self, rango="dia"):
        conn=sqlite.get_conn(); cur=conn.cursor()
        mapping={"dia":1,"semana":7,"mes":30,"año":365}
        days=mapping.get(rango,1)
        cur.execute(f"SELECT SUM(total), COUNT(*) FROM sales WHERE status!='Cancelada' AND date >= date('now','-{days-1} days')")
        row=cur.fetchone(); conn.close()
        return {"total": row[0] or 0, "count": row[1] or 0, "rango": rango}
    def get_sales_by_period(self, days=7):
        from datetime import datetime, timedelta
        conn=sqlite.get_conn(); cur=conn.cursor()
        # aggregate by date
        cur.execute("SELECT date, SUM(total) FROM sales WHERE status!='Cancelada' GROUP BY date")
        by_date={r[0]: r[1] for r in cur.fetchall()}
        conn.close()
        today=datetime.now().date()
        out=[]
        for i in range(days-1, -1, -1):
            d=today - timedelta(days=i)
            key=d.isoformat(); label=d.strftime("%m/%d")
            out.append({"day": label, "date": key, "total": by_date.get(key,0.0)})
        return out
    def get_category_sales(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT cat, SUM(stock) FROM products GROUP BY cat ORDER BY cat")
        rows=cur.fetchall(); conn.close()
        return [{"name": r[0], "stock": r[1], "value": r[1]} for r in rows]
    def get_sales_summary(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT status, COUNT(*) FROM sales GROUP BY status")
        cnt={r[0]: r[1] for r in cur.fetchall()}
        conn.close()
        for st in ("Pagada","Pendiente","Cancelada"):
            cnt.setdefault(st,0)
        return cnt
    def get_estado_resultados(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COALESCE(SUM(total),0) FROM sales WHERE status='Pagada'")
        ingresos=cur.fetchone()[0] or 0
        cur.execute("SELECT sale_items.qty, products.price_buy, products.price FROM sale_items JOIN sales ON sale_items.sale_id=sales.id JOIN products ON sale_items.product_id=products.id WHERE sales.status='Pagada'")
        costo=sum((r[1] or r[2]*0.7)*r[0] for r in cur.fetchall())
        cur.execute("SELECT COALESCE(SUM(tax),0) FROM sales WHERE status='Pagada'")
        impuestos=cur.fetchone()[0] or 0
        conn.close()
        bruto=ingresos - costo
        neto=bruto - impuestos*0.1
        return {"ingresos": ingresos, "costo": costo, "bruto": bruto, "impuestos": impuestos, "neto": neto}
    def get_flujo_efectivo(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COALESCE(SUM(paid),0) FROM sales WHERE status IN ('Pagada','Entregada','Facturada')")
        entradas=cur.fetchone()[0] or 0
        cur.execute("SELECT COALESCE(SUM(paid),0) FROM payables")
        salidas=cur.fetchone()[0] or 0
        conn.close()
        return {"entradas": entradas, "salidas": salidas, "neto": entradas - salidas}
    def get_valor_inventario(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COALESCE(SUM(price_buy*stock),0), COALESCE(SUM(price*stock),0), COALESCE(SUM(stock),0) FROM products")
        cost, sale, units = cur.fetchone()
        conn.close()
        return {"cost_value": cost or 0, "sale_value": sale or 0, "units": units or 0, "cost_fmt": f"${(cost or 0):,.2f}", "sale_fmt": f"${(sale or 0):,.2f}"}
    def get_impuestos_generados(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COALESCE(SUM(tax),0) FROM sales WHERE status='Pagada'")
        iva=cur.fetchone()[0] or 0
        conn.close()
        return {"iva_19": iva, "total": iva}
    def get_kpis(self):
        estado=self.get_estado_resultados()
        inv=self.get_valor_inventario()
        costo=estado["costo"] or 1
        inv_val=inv["cost_value"] or 1
        rotacion=costo/inv_val
        dias=365/rotacion if rotacion else 0
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COUNT(*) FROM sales WHERE status IN ('Pagada','Cotización','Pedido')")
        total_docs=cur.fetchone()[0] or 1
        cur.execute("SELECT COUNT(*) FROM sales WHERE status='Pagada'")
        pagadas=cur.fetchone()[0] or 0
        conn.close()
        conversion=pagadas/total_docs*100
        bruto_pct=(estado["bruto"]/estado["ingresos"]*100) if estado["ingresos"] else 0
        neto_pct=(estado["neto"]/estado["ingresos"]*100) if estado["ingresos"] else 0
        costos_fijos=5000000.0
        margen_bruto=bruto_pct/100 or 0.01
        equilibrio=costos_fijos/margen_bruto
        return {"rotacion": rotacion, "dias_inventario": dias, "conversion": conversion, "margen_bruto_pct": bruto_pct, "margen_neto_pct": neto_pct, "punto_equilibrio": equilibrio, "costos_fijos": costos_fijos}
    def export_reporte_csv(self, tipo="operativo"):
        import csv
        from datetime import datetime
        path = f"/tmp/reporte_{tipo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        if tipo=="operativo":
            with open(path, "w", newline="", encoding="utf-8") as f:
                w=csv.writer(f)
                w.writerow(["Operativo","Valor"])
                v=self.get_ventas_por_periodo("dia"); w.writerow(["Ventas dia", v["total"], v["count"]])
                v=self.get_ventas_por_periodo("semana"); w.writerow(["Ventas semana", v["total"]])
                v=self.get_ventas_por_periodo("mes"); w.writerow(["Ventas mes", v["total"]])
                w.writerow(["Ticket promedio", self.get_ticket_promedio()])
                for p in self.get_top_products(5):
                    w.writerow(["Top", p["name"], p["sold"]])
                for p in self.get_least_sold(5):
                    w.writerow(["Menos", p["name"], p["sold"]])
        elif tipo=="financiero":
            with open(path, "w", newline="", encoding="utf-8") as f:
                w=csv.writer(f)
                e=self.get_estado_resultados(); w.writerow(["Ingresos", e["ingresos"]]); w.writerow(["Costo", e["costo"]]); w.writerow(["Bruto", e["bruto"]]); w.writerow(["Impuestos", e["impuestos"]]); w.writerow(["Neto", e["neto"]])
                fl=self.get_flujo_efectivo(); w.writerow(["Flujo entradas", fl["entradas"]]); w.writerow(["Flujo salidas", fl["salidas"]])
                iv=self.get_valor_inventario(); w.writerow(["Inventario costo", iv["cost_value"]])
        elif tipo=="kpis":
            with open(path, "w", newline="", encoding="utf-8") as f:
                w=csv.writer(f)
                k=self.get_kpis()
                for kk, vv in k.items():
                    w.writerow([kk, vv])
        return path
    def export_reporte_pdf(self, tipo="operativo"):
        """Genera PDF con reportlab (tablas + encabezado Colombia COP). Retorna path."""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.lib.units import mm
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.lib import colors
        except ImportError:
            raise ValueError("Falta reportlab: pip install reportlab")
        from datetime import datetime
        path = f"/tmp/reporte_{tipo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        doc = SimpleDocTemplate(path, pagesize=letter, topMargin=15 * mm, bottomMargin=15 * mm)
        styles = getSampleStyleSheet()
        story = [Paragraph(f"Sistema de Ventas — Reporte {tipo} — Colombia COP", styles["Title"]),
                 Paragraph(f"Generado {datetime.now().strftime('%Y-%m-%d %H:%M')} — IVA 19% DIAN", styles["Normal"]),
                 Spacer(1, 6 * mm)]
        def _table(headers, rows):
            data = [headers] + [[str(c) for c in r] for r in rows]
            t = Table(data, repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1B5E20")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F8E9")]),
            ]))
            return t
        if tipo == "operativo":
            v_d = self.get_ventas_por_periodo("dia"); v_s = self.get_ventas_por_periodo("semana"); v_m = self.get_ventas_por_periodo("mes")
            story.append(_table(["Periodo", "Total COP", "Docs"],
                [["Día", f"${v_d['total']:,.0f}", v_d["count"]], ["Semana", f"${v_s['total']:,.0f}", v_s["count"]], ["Mes", f"${v_m['total']:,.0f}", v_m["count"]],
                 ["Ticket promedio", f"${self.get_ticket_promedio():,.0f}", ""]]))
            story.append(Spacer(1, 5 * mm))
            story.append(_table(["Top producto", "Vendidos"], [[p["name"][:30], p["sold"]] for p in self.get_top_products(10)]))
            story.append(Spacer(1, 5 * mm))
            story.append(_table(["Menos vendido", "Vendidos"], [[p["name"][:30], p["sold"]] for p in self.get_least_sold(5)]))
        elif tipo == "financiero":
            e = self.get_estado_resultados(); fl = self.get_flujo_efectivo(); iv = self.get_valor_inventario(); imp = self.get_impuestos_generados()
            story.append(_table(["Concepto", "Valor COP"],
                [["Ingresos", f"${e['ingresos']:,.0f}"], ["Costo", f"${e['costo']:,.0f}"], ["Bruto", f"${e['bruto']:,.0f}"],
                 ["Impuestos IVA", f"${e['impuestos']:,.0f}"], ["Neto", f"${e['neto']:,.0f}"],
                 ["Flujo entradas", f"${fl['entradas']:,.0f}"], ["Flujo salidas", f"${fl['salidas']:,.0f}"],
                 ["Flujo neto", f"${fl['neto']:,.0f}"], ["Inventario costo", f"${iv['cost_value']:,.0f}"],
                 ["IVA 19% generado", f"${imp['iva_19']:,.0f}"]]))
        elif tipo == "kpis":
            k = self.get_kpis()
            story.append(_table(["KPI", "Valor"], [[kk, (f"{vv:,.2f}" if isinstance(vv, float) else str(vv))] for kk, vv in k.items()]))
        else:
            raise ValueError(f"Tipo desconocido: {tipo}")
        doc.build(story)
        return path
    def find_product(self, pid): 
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=?", (pid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_product_by_sku(self, sku):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE lower(sku)=lower(?)", (sku.strip(),))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_product_by_barcode(self, barcode):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE barcode=?", (barcode.strip(),))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def search_products(self, q):
        q=(q or "").strip().lower()
        if not q: return self.list_products()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE lower(name) LIKE ? OR lower(sku) LIKE ? OR lower(cat) LIKE ? OR barcode LIKE ?", (f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%"))
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def find_client(self, name):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM clients WHERE lower(name)=lower(?)", (name.strip(),))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_client_by_id(self, cid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM clients WHERE id=?", (cid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def search_clients(self, q):
        q=(q or "").strip().lower()
        if not q: return self.list_clients()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM clients WHERE lower(name) LIKE ? OR lower(nit) LIKE ? OR lower(rfc) LIKE ? OR lower(phone) LIKE ? OR lower(email) LIKE ?", (f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%"))
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def find_supplier(self, sid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE id=?", (sid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def find_supplier_by_name(self, name):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE lower(name)=lower(?)", (name.strip(),))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def search_suppliers(self, q):
        q=(q or "").strip().lower()
        if not q: return self.list_suppliers()
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE lower(name) LIKE ? OR lower(nit) LIKE ? OR lower(rfc) LIKE ? OR lower(contact) LIKE ?", (f"%{q}%",f"%{q}%",f"%{q}%",f"%{q}%"))
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def find_purchase(self, folio):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM purchases WHERE id=?", (folio,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r

    def create_sale(self, *, client_name, total, payment, cart_items, promo_code=None, discount=0, tax=0, payments=None, doc_type=None):
        if isinstance(payment, dict):
            payments=payment
            has_credit=payments.get("credito",0)>0
            status="Pendiente" if has_credit else "Pagada"
            payment_str="+".join([k for k,v in payments.items() if v>0]) or "Mixto"
        else:
            if isinstance(payments, dict) and any(payments.values()):
                has_credit=payments.get("credito",0)>0
                status="Pendiente" if has_credit else "Pagada"
                payment_str="+".join([k for k,v in payments.items() if v>0]) or str(payment)
            else:
                payments=None
                status="Pendiente" if payment=="Credito" else "Pagada"
                payment_str=str(payment)
        folio=sqlite.next_counter("SALE_COUNTER","V")
        from datetime import datetime, timedelta
        try:
            subtotal_calc=sum(it.get("subtotal",0) for it in (cart_items or []))
        except Exception:
            subtotal_calc=total+discount-tax
        subtotal=subtotal_calc if subtotal_calc else (total+discount-tax)
        if isinstance(payments, dict):
            if status=="Pagada":
                paid_val=total
            else:
                paid_val=total - payments.get("credito",0)
        else:
            paid_val=total if status=="Pagada" else 0.0
        balance_val=0.0 if status=="Pagada" else (payments.get("credito", total) if isinstance(payments, dict) and "credito" in payments else total)
        # DIAN centralizado (data/dian.py): CUFE siempre se guarda como
        # referencia técnica; la UI lo oculta si DIAN está desactivado.
        from data import dian as dian_mod
        if not doc_type or doc_type == "Factura electrónica DIAN":
            doc_type = dian_mod.default_doc_type()
        cufe = dian_mod.generate_cufe(folio)
        dian_status="PENDIENTE_OFFLINE" if getattr(mock, "IS_OFFLINE", False) else "SINCRONIZADO"
        conn=sqlite.get_conn(); cur=conn.cursor()
        # vendedor actual
        vendedor="vendedor"
        try:
            from kivymd.app import MDApp
            app=MDApp.get_running_app()
            if app and getattr(app,"current_user", None):
                vendedor=app.current_user.get("username","vendedor")
        except Exception:
            pass
        cur.execute("""INSERT INTO sales (id, date, client, vendedor, total, subtotal, tax, discount, promo, status, doc_type, payment, payments_json, paid, balance, due, estado, dian_cufe, dian_status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (folio, datetime.now().strftime("%Y-%m-%d"), client_name, vendedor, total, subtotal, tax, discount, promo_code, status, doc_type, payment_str, json.dumps(payments or {payment_str.lower(): total}), paid_val, balance_val, (datetime.now()+timedelta(days=15)).strftime("%Y-%m-%d") if status=="Pendiente" else datetime.now().strftime("%Y-%m-%d"), status, cufe, dian_status))
        for it in cart_items:
            # update stock
            cur.execute("SELECT stock FROM products WHERE id=?", (it["id"],))
            row=cur.fetchone()
            if row:
                new_stock=row[0] - it["qty"]
                cur.execute("UPDATE products SET stock=? WHERE id=?", (new_stock, it["id"]))
            cur.execute("INSERT INTO sale_items (sale_id, product_id, qty, subtotal) VALUES (?,?,?,?)", (folio, it["id"], it["qty"], it["subtotal"]))
        if payments and payments.get("credito",0)>0:
            cur.execute("SELECT credit, balance FROM clients WHERE lower(name)=lower(?)", (client_name,))
            crow=cur.fetchone()
            if crow:
                cur.execute("UPDATE clients SET credit=?, balance=? WHERE lower(name)=lower(?)", (crow[0]+payments["credito"], crow[1]+payments["credito"], client_name))
        elif payment=="Credito":
            cur.execute("SELECT credit, balance FROM clients WHERE lower(name)=lower(?)", (client_name,))
            crow=cur.fetchone()
            if crow:
                cur.execute("UPDATE clients SET credit=?, balance=? WHERE lower(name)=lower(?)", (crow[0]+total, crow[1]+total, client_name))
        # caja
        cur.execute("SELECT * FROM caja WHERE id=1")
        caja=_row_to_dict(cur.fetchone())
        if caja and caja["open"]:
            try:
                sales_today=json.loads(caja["sales_today_json"] or "[]")
            except:
                sales_today=[]
            sales_today.append({"id": folio, "total": total})
            cur.execute("UPDATE caja SET sales_today_json=?, expected=? WHERE id=1", (json.dumps(sales_today), caja["opening_amount"] + sum(s["total"] for s in sales_today)))
        conn.commit(); conn.close()
        # return sale dict
        return {"id": folio, "date": datetime.now().strftime("%Y-%m-%d"), "client": client_name, "total": total, "subtotal": subtotal, "tax": tax, "discount": discount, "promo": promo_code, "status": status, "doc_type": doc_type, "payment": payment_str, "payments": payments or {payment_str.lower(): total}, "paid": paid_val, "balance": balance_val, "dian_cufe": cufe, "dian_status": dian_status, "estado": status}

    ESTADOS_VENTA = ["Cotización","Pedido","Facturada","Pagada","Entregada","Cerrada"]
    def find_sale(self, sid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id=?", (sid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def create_document(self, doc_type, client, total, user="sistema"):
        valid=["Cotización","Pedido","Remisión","Factura","Nota crédito","Nota cargo"]
        if doc_type not in valid:
            raise ValueError(f"doc_type debe ser {valid}")
        prefix={"Cotización":"COT","Pedido":"PED","Remisión":"REM","Factura":"V","Nota crédito":"NC","Nota cargo":"NCC"}[doc_type]
        counter={"Cotización":"QUOTE_COUNTER","Pedido":"ORDER_COUNTER","Remisión":"SALE_COUNTER","Factura":"SALE_COUNTER","Nota crédito":"CREDIT_NOTE_COUNTER","Nota cargo":"SALE_COUNTER"}[doc_type]
        folio=sqlite.next_counter(counter, prefix)
        from datetime import datetime
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("""INSERT INTO sales (id, date, client, vendedor, total, subtotal, tax, discount, status, doc_type, payment, payments_json, paid, balance, estado)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (folio, datetime.now().strftime("%Y-%m-%d"), client, user, float(total), float(total), 0, 0, doc_type, doc_type, "", "{}", 0.0, float(total), doc_type))
        conn.commit(); conn.close()
        self.log(user, f"doc_{doc_type.lower().replace(' ','_')}_creado", f"{folio} {client} ${total}")
        return self.find_sale(folio)
    def advance_sale_status(self, sale_id, new_status, user="sistema"):
        s=self.find_sale(sale_id)
        if not s: raise ValueError(f"Venta {sale_id} no encontrada")
        if s["status"]=="Cancelada": raise ValueError("Venta cancelada no avanza")
        if new_status=="Cancelada":
            conn=sqlite.get_conn(); cur=conn.cursor()
            cur.execute("UPDATE sales SET status='Cancelada', estado='Cancelada', balance=0 WHERE id=?", (sale_id,))
            conn.commit(); conn.close()
            self.log(user, "venta_cancelada", sale_id)
            return self.find_sale(sale_id)
        if new_status not in self.ESTADOS_VENTA and new_status!="Cancelada":
            raise ValueError(f"Estado debe ser {self.ESTADOS_VENTA + ['Cancelada']}")
        conn=sqlite.get_conn(); cur=conn.cursor()
        if new_status in ("Pagada","Entregada","Cerrada"):
            cur.execute("UPDATE sales SET status=?, estado=?, balance=0, paid=total WHERE id=?", (new_status,new_status,sale_id))
        else:
            cur.execute("UPDATE sales SET status=?, estado=? WHERE id=?", (new_status,new_status,sale_id))
        conn.commit(); conn.close()
        self.log(user, "venta_avance", f"{sale_id} -> {new_status}")
        return self.find_sale(sale_id)
    def create_credit_note(self, sale_id, amount, reason, user="sistema"):
        s=self.find_sale(sale_id)
        if not s: raise ValueError(f"Venta {sale_id} no encontrada")
        amount=float(amount)
        if amount<=0 or amount> s["total"]: raise ValueError("Monto inválido")
        if not reason.strip(): raise ValueError("Motivo requerido")
        note=self.create_document("Nota crédito", s["client"], amount, user=user)
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("UPDATE sales SET reason=?, ref=? WHERE id=?", (reason, sale_id, note["id"]))
        conn.commit(); conn.close()
        self.log(user, "nota_credito", f"{note['id']} ref {sale_id} ${amount} {reason[:20]}")
        return note
    def create_debit_note(self, sale_id, amount, reason, user="sistema"):
        s=self.find_sale(sale_id)
        if not s: raise ValueError(f"Venta {sale_id} no encontrada")
        amount=float(amount)
        if amount<=0: raise ValueError("Monto >0")
        if not reason.strip(): raise ValueError("Motivo requerido")
        note=self.create_document("Nota cargo", s["client"], amount, user=user)
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("UPDATE sales SET reason=?, ref=? WHERE id=?", (reason, sale_id, note["id"]))
        conn.commit(); conn.close()
        self.log(user, "nota_cargo", f"{note['id']} ref {sale_id} ${amount}")
        return note

    def list_receivables(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM sales WHERE balance>0 AND status NOT IN ('Cancelada','Cotización','Pedido')")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def get_client_statement(self, client_name):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM sales WHERE client=?", (client_name,))
        sales=[_row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        total_debt=sum(s.get("balance",0) for s in sales)
        total_paid=sum(s.get("paid",0) for s in sales)
        return {"sales": sales, "debt": total_debt, "paid": total_paid}
    def add_cxc_payment(self, sale_id, amount, method="Efectivo", user="sistema"):
        s=self.find_sale(sale_id)
        if not s: raise ValueError(f"Venta {sale_id} no encontrada")
        if s.get("balance",0)<=0: raise ValueError("Venta sin saldo pendiente")
        amount=float(amount)
        if amount<=0 or amount> s["balance"]: raise ValueError(f"Monto 0 < {amount} <= balance {s['balance']}")
        new_paid=s.get("paid",0)+amount
        new_bal=s.get("balance", s["total"])-amount
        new_status="Pagada" if new_bal<=0.01 else s["status"]
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("UPDATE sales SET paid=?, balance=?, status=?, estado=? WHERE id=?", (new_paid, 0 if new_bal<=0.01 else new_bal, new_status, new_status, sale_id))
        if new_bal<=0.01:
            cur.execute("SELECT credit, balance FROM clients WHERE lower(name)=lower(?)", (s["client"],))
            crow=cur.fetchone()
            if crow:
                cur.execute("UPDATE clients SET credit=?, balance=? WHERE lower(name)=lower(?)", (max(0,crow[0]-amount), max(0,crow[1]-amount), s["client"]))
        cur.execute("INSERT INTO payments_cxc (sale_id, date, amount, method, user) VALUES (?,?,?,?,?)", (sale_id, datetime.now().strftime("%Y-%m-%d"), amount, method, user))
        conn.commit(); conn.close()
        self.log(user, "cxc_abono", f"{sale_id} ${amount} {method} bal {0 if new_bal<=0.01 else new_bal:.2f}")
        return self.find_sale(sale_id)
    def calculate_mora(self, sale, rate=0.02):
        from datetime import datetime
        try:
            due=datetime.strptime(sale.get("due", sale["date"]), "%Y-%m-%d").date()
        except Exception:
            return 0.0
        today=datetime.now().date()
        if today<=due or sale.get("balance",0)<=0:
            return 0.0
        days_over=(today - due).days
        months=days_over/30
        return sale["balance"]*rate*months
    def list_payables(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM payables WHERE balance>0")
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def add_cxp_payment(self, payable_id, amount, method="Transferencia", user="sistema"):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM payables WHERE id=?", (payable_id,))
        p=_row_to_dict(cur.fetchone())
        if not p: conn.close(); raise ValueError(f"CxP {payable_id} no encontrada")
        bal=p.get("balance", p["amount"])
        amount=float(amount)
        if amount<=0 or amount> bal+0.01: conn.close(); raise ValueError(f"Monto inválido balance {bal}")
        new_paid=p.get("paid",0)+amount
        new_bal=bal-amount
        new_status="Pagada" if new_bal<=0.01 else p["status"]
        cur.execute("UPDATE payables SET paid=?, balance=?, status=? WHERE id=?", (new_paid, 0 if new_bal<=0.01 else new_bal, new_status, payable_id))
        cur.execute("INSERT INTO payments_cxp (payable_id, date, amount, method, user) VALUES (?,?,?,?,?)", (payable_id, datetime.now().strftime("%Y-%m-%d"), amount, method, user))
        # descuento pronto pago
        disc=0
        try:
            due=datetime.strptime(p["due"], "%Y-%m-%d").date()
            if datetime.now().date()<due and p.get("discount_early",0)>0:
                disc=amount * p["discount_early"]/100
        except Exception:
            pass
        conn.commit(); conn.close()
        self.log(user, "cxp_pago", f"{payable_id} ${amount} {method} bal {0 if new_bal<=0.01 else new_bal:.2f} desc {disc:.2f}")
        return self.find_payable(payable_id) if hasattr(self, 'find_payable') else _row_to_dict(cur.execute("SELECT * FROM payables WHERE id=?", (payable_id,)).fetchone()) if False else p, disc
    def find_payable(self, pid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM payables WHERE id=?", (pid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def add_promo(self, data):
        name=data.get("name","").strip()
        if len(name)<3: raise ValueError("Nombre promo ≥3")
        ptype=data.get("type","").strip()
        valid=["porcentaje","monto_fijo","2x1","3x2","volumen","cupon","happy_hour"]
        if ptype not in valid: raise ValueError(f"Tipo debe ser {valid}")
        val=float(data.get("value",0))
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("INSERT INTO promos (name, type, value, condition, code, active, desc) VALUES (?,?,?,?,?,?,?)",
            (name, ptype, val, data.get("condition",""), data.get("code", f"PROMO{len(self.list_promoss())+1}").upper(), 1 if data.get("active",True) else 0, data.get("desc","")))
        conn.commit()
        cur.execute("SELECT * FROM promos WHERE code=?", (data.get("code","").upper(),))
        r=_row_to_dict(cur.fetchone())
        if not r:
            cur.execute("SELECT * FROM promos WHERE name=?", (name,))
            r=_row_to_dict(cur.fetchone())
        conn.close(); return r
    def update_promo(self, pid, updates):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM promos WHERE id=?", (pid,))
        pr=_row_to_dict(cur.fetchone())
        if not pr: conn.close(); raise ValueError(f"Promo {pid} no encontrada")
        for k in ("name","type","value","condition","code","active","desc"):
            if k in updates and updates[k]!="":
                if k=="value":
                    v=float(updates[k])
                    cur.execute("UPDATE promos SET value=? WHERE id=?", (v,pid))
                elif k=="active":
                    v=1 if (updates[k] is True or str(updates[k]).lower() in ("si","true","1","activo")) else 0
                    cur.execute("UPDATE promos SET active=? WHERE id=?", (v,pid))
                else:
                    v=updates[k]
                    cur.execute(f"UPDATE promos SET {k}=? WHERE id=?", (v,pid))
        conn.commit()
        cur.execute("SELECT * FROM promos WHERE id=?", (pid,))
        r=_row_to_dict(cur.fetchone()); conn.close(); return r
    def delete_promo(self, pid):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("DELETE FROM promos WHERE id=?", (pid,))
        if cur.rowcount==0: conn.close(); raise ValueError(f"Promo {pid} no encontrada")
        conn.commit(); conn.close()
    def apply_promo(self, cart, promo_code):
        if not promo_code: return 0.0, None
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM promos WHERE lower(code)=lower(?) AND active=1", (promo_code.strip(),))
        promo=_row_to_dict(cur.fetchone()); conn.close()
        if not promo: raise ValueError(f"Promo {promo_code} no existe o inactiva")
        subtotal=sum(i["subtotal"] for i in cart)
        qty_total=sum(i["qty"] for i in cart)
        discount=0.0
        ptype=promo["type"]
        if ptype=="porcentaje":
            cond=promo.get("condition","").lower()
            if cond and cond not in ("min 5000","min 500000","qty>=10"):
                cat_total=sum(i["subtotal"] for i in cart if self.find_product(i["id"]) and self.find_product(i["id"])["cat"].lower()==cond)
                discount=cat_total*promo["value"]/100 if cat_total else 0
            else:
                discount=subtotal*promo["value"]/100
        elif ptype=="monto_fijo":
            try:
                min_val=float(promo.get("condition","").split("min")[-1].strip()) if "min" in promo.get("condition","") else 0
            except: min_val=0
            if subtotal>=min_val:
                discount=promo["value"]
        elif ptype=="2x1":
            sku=promo.get("condition","").strip()
            for it in cart:
                prod=self.find_product(it["id"])
                if prod and prod["sku"]==sku and it["qty"]>=2:
                    discount+=(it["qty"]//2)*prod["price"]
        elif ptype=="3x2":
            sku_or_cat=promo.get("condition","").strip().lower()
            for it in cart:
                prod=self.find_product(it["id"])
                if not prod: continue
                if prod["sku"].lower()==sku_or_cat or prod["cat"].lower()==sku_or_cat:
                    if it["qty"]>=3:
                        discount+=(it["qty"]//3)*prod["price"]
        elif ptype=="volumen":
            if qty_total>=10:
                discount=subtotal*promo["value"]/100
        elif ptype in ("cupon","happy_hour"):
            discount=subtotal*promo["value"]/100 if promo["value"] else 0
        discount=min(discount, subtotal)
        return discount, promo

    def open_caja(self, amount, user="sistema"):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT open FROM caja WHERE id=1")
        if cur.fetchone()[0]: conn.close(); raise ValueError("Caja ya abierta")
        amount=float(amount)
        cur.execute("UPDATE caja SET open=1, opening_amount=?, opening_ts=?, opening_user=?, sales_today_json='[]', expected=? WHERE id=1", (amount, datetime.now().isoformat(timespec="seconds"), user, amount))
        conn.commit(); conn.close()
        self.log(user, "caja_apertura", f"${amount:,.2f}")
        return self.get_caja_status()
    def close_caja(self, counted, user="sistema"):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM caja WHERE id=1")
        caja=_row_to_dict(cur.fetchone())
        if not caja or not caja["open"]: conn.close(); raise ValueError("Caja no abierta")
        counted=float(counted)
        try:
            sales_today=json.loads(caja["sales_today_json"] or "[]")
        except: sales_today=[]
        total_sales=sum(s["total"] for s in sales_today)
        expected=caja["opening_amount"] + total_sales
        diff=counted-expected
        self.log(user, "caja_cierre", f"esperado ${expected:,.2f} contado ${counted:,.2f} diff {diff:+.2f} ventas {len(sales_today)}")
        cur.execute("UPDATE caja SET open=0, opening_amount=0, opening_ts=NULL, opening_user=NULL, sales_today_json='[]', expected=0 WHERE id=1")
        conn.commit(); conn.close()
        return {"expected": expected, "counted": counted, "diff": diff, "sales_count": len(sales_today), "total_sales": total_sales}
    def get_caja_status(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM caja WHERE id=1")
        row=_row_to_dict(cur.fetchone())
        conn.close()
        if not row: return {"open": False, "opening_amount": 0, "total_sales": 0, "expected": 0, "sales_today": []}
        try:
            sales_today=json.loads(row.get("sales_today_json") or "[]")
        except: sales_today=[]
        total_sales=sum(s["total"] for s in sales_today)
        return {"open": bool(row["open"]), "opening_amount": row["opening_amount"] or 0, "opening_ts": row["opening_ts"], "opening_user": row["opening_user"], "sales_today": sales_today, "total_sales": total_sales, "expected": (row["opening_amount"] or 0) + total_sales}

    # CRUD Products etc already above; add remaining inventory
    def get_inventory_value(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT COALESCE(SUM(price_buy*stock),0), COALESCE(SUM(price*stock),0), COALESCE(SUM(stock),0) FROM products")
        cost,sale,units=cur.fetchone(); conn.close()
        return {"cost_value": cost or 0, "sale_value": sale or 0, "units": units or 0, "cost_fmt": f"${(cost or 0):,.2f}", "sale_fmt": f"${(sale or 0):,.2f}"}
    def get_inventory_alerts(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE stock < stock_min")
        low=[_row_to_dict(r) for r in cur.fetchall()]
        cur.execute("SELECT * FROM products WHERE stock > stock_max")
        excess=[_row_to_dict(r) for r in cur.fetchall()]
        cur.execute("SELECT * FROM products WHERE stock=0")
        out=[_row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return {"low": low, "excess": excess, "out": out}
    def low_stock_products(self, threshold=10):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM products WHERE stock < ?", (threshold,))
        rows=[_row_to_dict(r) for r in cur.fetchall()]; conn.close(); return rows
    def list_movements(self, limit=20):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT * FROM inventory_movements ORDER BY id DESC LIMIT ?", (limit,))
        rows=[dict(r) for r in cur.fetchall()]; conn.close()
        # map before_qty/after_qty to before/after for UI compat
        for r in rows:
            r["before"]=r.pop("before_qty", r.get("before"))
            r["after"]=r.pop("after_qty", r.get("after"))
        return list(reversed(rows))
    def scan_barcode(self, barcode):
        return self.find_product_by_barcode(barcode.strip())
    def adjust_stock(self, sku, qty_delta, reason, user="sistema", mtype="Ajuste"):
        if not reason or not reason.strip(): raise ValueError("Justificación requerida para ajuste")
        p=self.find_product_by_sku(sku)
        if not p: raise ValueError(f"SKU {sku} no encontrado")
        delta=int(qty_delta)
        if delta==0: raise ValueError("Cantidad no puede ser 0")
        before=p["stock"]; after=before+delta
        if after<0: raise ValueError(f"Stock insuficiente: {before} disponible, intenta {delta}")
        if mtype=="Ajuste": mtype="Entrada" if delta>0 else "Salida"
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("UPDATE products SET stock=? WHERE sku=?", (after, sku))
        cur.execute("INSERT INTO inventory_movements (ts, sku, product, type, qty, before_qty, after_qty, reason, user) VALUES (?,?,?,?,?,?,?,?,?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M"), sku, p["name"][:18], mtype, delta, before, after, reason[:40], user))
        conn.commit(); conn.close()
        self.log(user, f"inventario_{mtype.lower()}", f"{sku} {delta:+d} {before}->{after} {reason[:30]}")
        return {"ts": datetime.now().strftime("%Y-%m-%d %H:%M"), "sku": sku, "type": mtype, "qty": delta, "before": before, "after": after}
    def transfer_stock(self, sku, qty, to_location, reason, user="sistema"):
        p=self.find_product_by_sku(sku)
        if not p: raise ValueError(f"SKU {sku} no encontrado")
        if not to_location.strip(): raise ValueError("Ubicación destino requerida")
        if not reason.strip(): raise ValueError("Motivo requerido")
        qty=int(qty)
        if qty<=0 or qty> p["stock"]: raise ValueError(f"Cantidad inválida: stock {p['stock']}")
        before_loc=p.get("location","")
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("UPDATE products SET location=? WHERE sku=?", (to_location.strip(), sku))
        cur.execute("INSERT INTO inventory_movements (ts, sku, product, type, qty, before_qty, after_qty, reason, user) VALUES (?,?,?,?,?,?,?,?,?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M"), sku, p["name"][:18], "Transferencia", qty, p["stock"], p["stock"], f"{before_loc}->{to_location} {reason[:30]}", user))
        conn.commit(); conn.close()
        self.log(user, "inventario_transferencia", f"{sku} {qty} {before_loc}->{to_location}")
        return {"sku": sku, "qty": qty, "before": p["stock"], "after": p["stock"]}

    def create_purchase(self, supplier, sku, qty, user="sistema"):
        sup=self.find_supplier_by_name(supplier)
        if not sup: raise ValueError(f"Proveedor {supplier} no encontrado")
        prod=self.find_product_by_sku(sku)
        if not prod: raise ValueError(f"SKU {sku} no encontrado")
        qty=int(qty)
        if qty<=0: raise ValueError("Cantidad >0")
        total=prod.get("price_buy", prod["price"]*0.7)*qty
        folio=sqlite.next_counter("PURCHASE_COUNTER", "OC")
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("INSERT INTO purchases (id, date, supplier, total, status, items_json, notes) VALUES (?,?,?,?,?,?,?)",
            (folio, datetime.now().strftime("%Y-%m-%d"), sup["name"], total, "Pendiente", json.dumps([{"sku": sku, "qty": qty, "price_buy": prod.get("price_buy", prod["price"]*0.7)}]), f"Pedido {sku} x{qty}"))
        conn.commit(); conn.close()
        self.log(user, "compra_creada", f"{folio} {sup['name']} {sku} x{qty} ${total:,.0f}")
        return self.find_purchase(folio)
    def receive_purchase(self, folio, user="sistema"):
        po=self.find_purchase(folio)
        if not po: raise ValueError(f"Orden {folio} no encontrada")
        if po["status"]=="Recibida": raise ValueError(f"Orden {folio} ya recibida")
        if po["status"]=="Cancelada": raise ValueError(f"Orden {folio} cancelada")
        conn=sqlite.get_conn(); cur=conn.cursor()
        items=json.loads(po.get("items_json") or "[]") or po.get("items",[])
        for it in items:
            cur.execute("SELECT stock, name FROM products WHERE sku=?", (it["sku"],))
            row=cur.fetchone()
            if not row: continue
            before=row[0]; qty=int(it["qty"])
            cur.execute("UPDATE products SET stock=? WHERE sku=?", (before+qty, it["sku"]))
            cur.execute("INSERT INTO inventory_movements (ts, sku, product, type, qty, before_qty, after_qty, reason, user) VALUES (?,?,?,?,?,?,?,?,?)",
                (datetime.now().strftime("%Y-%m-%d %H:%M"), it["sku"], row[1][:18], "Entrada", qty, before, before+qty, f"Recepción {folio}", user))
        cur.execute("UPDATE purchases SET status='Recibida' WHERE id=?", (folio,))
        # payables
        due=(datetime.now()+timedelta(days=30)).strftime("%Y-%m-%d")
        disc=2 if po["supplier"]=="TecnoMayorista SAS" or "TecnoMayorista" in po["supplier"] else 0
        cur.execute("INSERT INTO payables (id, supplier, due, amount, paid, balance, discount_early, status) VALUES (?,?,?,?,?,?,?,?)",
            (folio, po["supplier"], due, po["total"], 0, po["total"], disc, "Pendiente"))
        conn.commit(); conn.close()
        self.log(user, "compra_recibida", f"{folio} {po['supplier']} ${po['total']:,.0f}")
        return self.find_purchase(folio)
    def cancel_purchase(self, folio, user="sistema"):
        po=self.find_purchase(folio)
        if not po: raise ValueError(f"Orden {folio} no encontrada")
        if po["status"]=="Recibida": raise ValueError("No se puede cancelar orden ya recibida")
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("UPDATE purchases SET status='Cancelada' WHERE id=?", (folio,))
        conn.commit(); conn.close()
        self.log(user, "compra_cancelada", folio)
        return self.find_purchase(folio)

    def import_products_csv(self, path):
        import csv, os
        if not os.path.exists(path): raise ValueError(f"Archivo no encontrado: {path}")
        count=0
        with open(path, newline="", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            for row in reader:
                sku=row.get("sku") or row.get("SKU")
                if not sku: continue
                if self.find_product_by_sku(sku): continue
                try:
                    self.add_product({"sku": sku.strip(), "name": row.get("name","") or row.get("nombre","") or sku, "cat": row.get("cat","General") or row.get("categoria","General"), "price": row.get("price","0") or row.get("precio","0"), "stock": row.get("stock","0") or "0"})
                    count+=1
                except Exception: continue
        return count
    def import_clients_csv(self, path):
        import csv, os
        if not os.path.exists(path): raise ValueError(f"Archivo no encontrado: {path}")
        count=0
        with open(path, newline="", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            for row in reader:
                name=(row.get("name") or row.get("nombre") or "").strip()
                if not name or self.find_client(name): continue
                try:
                    self.add_client({"name": name, "email": row.get("email",""), "phone": row.get("phone",""), "city": row.get("city",""), "nit": row.get("nit", row.get("rfc",""))})
                    count+=1
                except Exception: continue
        return count
    def import_suppliers_csv(self, path):
        import csv, os
        if not os.path.exists(path): raise ValueError(f"Archivo no encontrado: {path}")
        count=0
        with open(path, newline="", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            for row in reader:
                name=(row.get("name") or row.get("empresa") or "").strip()
                if not name or self.find_supplier_by_name(name): continue
                try:
                    self.add_supplier({"name": name, "contact": row.get("contact",""), "phone": row.get("phone",""), "email": row.get("email",""), "city": row.get("city",""), "nit": row.get("nit", row.get("rfc",""))})
                    count+=1
                except Exception: continue
        return count
    # ── Import tabular .csv/.xlsx (dispatcher por extensión) ──
    @staticmethod
    def _read_tabular(path):
        """Lee .csv o .xlsx y retorna lista de dicts con claves normalizadas."""
        import os
        if not os.path.exists(path): raise ValueError(f"Archivo no encontrado: {path}")
        ext = os.path.splitext(path)[1].lower()
        if ext == ".csv":
            import csv
            with open(path, newline="", encoding="utf-8-sig") as f:
                return [{(k or "").strip().lower(): (v or "") for k, v in row.items()} for row in csv.DictReader(f)]
        if ext in (".xlsx", ".xlsm"):
            try:
                import openpyxl
            except ImportError:
                raise ValueError("Falta openpyxl: pip install openpyxl")
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
            ws = wb.active
            rows = list(ws.iter_rows(values_only=True))
            wb.close()
            if not rows: return []
            headers = [(str(h or "").strip().lower()) for h in rows[0]]
            out = []
            for r in rows[1:]:
                if all(v is None or str(v).strip() == "" for v in r): continue
                out.append({h: ("" if v is None else str(v).strip()) for h, v in zip(headers, r)})
            return out
        raise ValueError(f"Extensión no soportada: {ext} (use .csv o .xlsx)")
    def import_products_excel(self, path):
        count = 0
        for row in self._read_tabular(path):
            sku = (row.get("sku") or "").strip()
            if not sku or self.find_product_by_sku(sku): continue
            try:
                data = {
                    "sku": sku,
                    "name": row.get("name") or row.get("nombre") or row.get("producto") or sku,
                    "cat": row.get("cat") or row.get("categoria") or row.get("categoría") or "General",
                    "price": row.get("price") or row.get("precio") or row.get("precio_venta") or "0",
                    "stock": row.get("stock") or row.get("existencia") or "0",
                }
                for src_keys, dst in ((("price_buy", "precio_compra", "costo"), "price_buy"),
                                      (("price_wholesale", "precio_mayoreo", "mayoreo"), "price_wholesale"),
                                      (("barcode", "codigo_barras", "ean", "codigo"), "barcode"),
                                      (("brand", "marca"), "brand"),
                                      (("location", "ubicacion", "ubicación"), "location"),
                                      (("lote",), "lote"),
                                      (("vencimiento", "caducidad"), "vencimiento")):
                    for k in src_keys:
                        if row.get(k):
                            data[dst] = row[k]
                            break
                self.add_product(data)
                count += 1
            except Exception: continue
        return count
    def import_clients_excel(self, path):
        count = 0
        for row in self._read_tabular(path):
            name = (row.get("name") or row.get("nombre") or row.get("cliente") or "").strip()
            if not name or self.find_client(name): continue
            try:
                self.add_client({"name": name, "email": row.get("email", ""), "phone": row.get("phone") or row.get("telefono") or row.get("teléfono") or "", "city": row.get("city") or row.get("ciudad") or "", "nit": row.get("nit") or row.get("rfc") or ""})
                count += 1
            except Exception: continue
        return count
    def import_suppliers_excel(self, path):
        count = 0
        for row in self._read_tabular(path):
            name = (row.get("name") or row.get("empresa") or row.get("proveedor") or "").strip()
            if not name or self.find_supplier_by_name(name): continue
            try:
                self.add_supplier({"name": name, "contact": row.get("contact") or row.get("contacto") or "", "phone": row.get("phone") or row.get("telefono") or "", "email": row.get("email", ""), "city": row.get("city") or row.get("ciudad") or "", "nit": row.get("nit") or row.get("rfc") or ""})
                count += 1
            except Exception: continue
        return count
    def import_products_file(self, path):
        """Dispatcher: .csv → import_products_csv, .xlsx → import_products_excel."""
        import os
        ext = os.path.splitext(path)[1].lower()
        if ext == ".csv": return self.import_products_csv(path)
        if ext in (".xlsx", ".xlsm"): return self.import_products_excel(path)
        raise ValueError(f"Extensión no soportada: {ext} (use .csv o .xlsx)")
    def import_clients_file(self, path):
        import os
        ext = os.path.splitext(path)[1].lower()
        if ext == ".csv": return self.import_clients_csv(path)
        if ext in (".xlsx", ".xlsm"): return self.import_clients_excel(path)
        raise ValueError(f"Extensión no soportada: {ext} (use .csv o .xlsx)")
    def import_suppliers_file(self, path):
        import os
        ext = os.path.splitext(path)[1].lower()
        if ext == ".csv": return self.import_suppliers_csv(path)
        if ext in (".xlsx", ".xlsm"): return self.import_suppliers_excel(path)
        raise ValueError(f"Extensión no soportada: {ext} (use .csv o .xlsx)")

    def log(self, user, action, detail=""):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("INSERT INTO audit_log (ts, user, action, detail) VALUES (?,?,?,?)", (datetime.now().isoformat(timespec="seconds"), user or "sistema", action, detail))
        conn.commit(); conn.close()
    def list_audit(self):
        conn=sqlite.get_conn(); cur=conn.cursor()
        cur.execute("SELECT ts, user, action, detail FROM audit_log ORDER BY id DESC LIMIT 100")
        rows=[{"ts": r[0], "user": r[1], "action": r[2], "detail": r[3]} for r in cur.fetchall()]
        conn.close(); return rows

repo = Repository()
