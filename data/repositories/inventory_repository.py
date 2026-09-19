"""
InventoryRepository, CajaRepository, PromoRepository, PurchaseRepository, AuditRepository
Repositorios especializados para inventario, caja, promociones, compras y auditoría
"""
import json
from datetime import datetime
from data import db as sqlite


class InventoryRepository:
    """Repositorio especializado en gestión de inventario"""
    
    def __init__(self, audit_callback=None):
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        if row is None:
            return None
        d = dict(row)
        for json_field in ["kit_json"]:
            if json_field in d and d[json_field]:
                try:
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = []
        return d

    def get_inventory_value(self):
        """Calcula valor del inventario (costo y venta)"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT COALESCE(SUM(price_buy*stock),0), "
            "COALESCE(SUM(price*stock),0), "
            "COALESCE(SUM(stock),0) FROM products"
        )
        cost, sale, units = cur.fetchone()
        conn.close()
        return {
            "cost_value": cost or 0,
            "sale_value": sale or 0,
            "units": units or 0,
            "cost_fmt": f"${(cost or 0):,.2f}",
            "sale_fmt": f"${(sale or 0):,.2f}"
        }

    def get_inventory_alerts(self):
        """Obtiene alertas de inventario (bajo, exceso, agotado)"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM products WHERE stock < stock_min")
        low = [self._row_to_dict(r) for r in cur.fetchall()]
        
        cur.execute("SELECT * FROM products WHERE stock > stock_max")
        excess = [self._row_to_dict(r) for r in cur.fetchall()]
        
        cur.execute("SELECT * FROM products WHERE stock=0")
        out = [self._row_to_dict(r) for r in cur.fetchall()]
        
        conn.close()
        return {"low": low, "excess": excess, "out": out}

    def low_stock_products(self, threshold=10):
        """Productos con stock bajo un umbral"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE stock < ?", (threshold,))
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def adjust_stock(self, sku, qty_delta, reason, user="sistema", mtype="Ajuste"):
        """Ajusta stock de producto con registro de movimiento"""
        from data.repositories.product_repository import ProductRepository
        prod_repo = ProductRepository(audit_callback=self._log)
        
        p = prod_repo.find_product_by_sku(sku)
        if not p:
            raise ValueError(f"Producto SKU {sku} no encontrado")
        
        new_stock = p["stock"] + int(qty_delta)
        if new_stock < 0:
            raise ValueError("Stock no puede ser negativo")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE products SET stock=? WHERE sku=?",
            (new_stock, sku)
        )
        cur.execute(
            "INSERT INTO movements (product_id, sku, type, qty, reason, date, user) VALUES (?,?,?,?,?,?,?)",
            (p["id"], sku, mtype, qty_delta, reason, datetime.now().strftime("%Y-%m-%d"), user)
        )
        conn.commit()
        conn.close()
        
        self._log(user, f"ajuste_inventario_{mtype.lower()}", f"SKU={sku}, qty={qty_delta}, razón={reason[:30]}")
        return {"sku": sku, "old_stock": p["stock"], "new_stock": new_stock, "delta": qty_delta}

    def transfer_stock(self, sku, qty, to_location, reason, user="sistema"):
        """Transfiere stock entre ubicaciones"""
        from data.repositories.product_repository import ProductRepository
        prod_repo = ProductRepository(audit_callback=self._log)
        
        p = prod_repo.find_product_by_sku(sku)
        if not p:
            raise ValueError(f"Producto SKU {sku} no encontrado")
        if p["stock"] < qty:
            raise ValueError(f"Stock insuficiente: {p['stock']} < {qty}")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE products SET stock=?, location=? WHERE sku=?",
            (p["stock"] - qty, to_location, sku)
        )
        cur.execute(
            "INSERT INTO movements (product_id, sku, type, qty, reason, date, user) VALUES (?,?,?,?,?,?,?)",
            (p["id"], sku, "Traslado", -qty, f"A {to_location}: {reason}", 
             datetime.now().strftime("%Y-%m-%d"), user)
        )
        conn.commit()
        conn.close()
        
        self._log(user, "traslado_inventario", f"SKU={sku}, qty={qty}, destino={to_location}")
        return {"sku": sku, "new_stock": p["stock"] - qty, "location": to_location}

    def list_movements(self, limit=20):
        """Lista últimos movimientos de inventario"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM movements ORDER BY id DESC LIMIT ?", (limit,))
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
        return rows


class CajaRepository:
    """Repositorio especializado en gestión de caja"""
    
    def __init__(self, audit_callback=None):
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        if row is None:
            return None
        d = dict(row)
        if "sales_today_json" in d and d["sales_today_json"]:
            try:
                d["sales_today"] = json.loads(d["sales_today_json"])
            except Exception:
                d["sales_today"] = []
        return d

    def open_caja(self, amount, user="sistema"):
        """Abre caja con monto inicial"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT open FROM caja WHERE id=1")
        if cur.fetchone()[0]:
            conn.close()
            raise ValueError("Caja ya abierta")
        
        amount = float(amount)
        cur.execute(
            "UPDATE caja SET open=1, opening_amount=?, opening_ts=?, opening_user=?, "
            "sales_today_json='[]', expected=? WHERE id=1",
            (amount, datetime.now().isoformat(timespec="seconds"), user, amount)
        )
        conn.commit()
        conn.close()
        
        self._log(user, "caja_apertura", f"${amount:,.2f}")
        return self.get_caja_status()

    def close_caja(self, counted, user="sistema"):
        """Cierra caja con conteo final"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM caja WHERE id=1")
        caja = self._row_to_dict(cur.fetchone())
        
        if not caja or not caja["open"]:
            conn.close()
            raise ValueError("Caja no abierta")
        
        counted = float(counted)
        sales_today = caja.get("sales_today", [])
        total_sales = sum(s["total"] for s in sales_today)
        expected = caja["opening_amount"] + total_sales
        diff = counted - expected
        
        self._log(user, "caja_cierre", 
                 f"esperado ${expected:,.2f} contado ${counted:,.2f} diff {diff:+.2f} ventas {len(sales_today)}")
        
        cur.execute(
            "UPDATE caja SET open=0, opening_amount=0, opening_ts=NULL, "
            "opening_user=NULL, sales_today_json='[]', expected=0 WHERE id=1"
        )
        conn.commit()
        conn.close()
        
        return {
            "expected": expected,
            "counted": counted,
            "diff": diff,
            "sales_count": len(sales_today),
            "total_sales": total_sales
        }

    def get_caja_status(self):
        """Obtiene estado actual de caja"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM caja WHERE id=1")
        row = self._row_to_dict(cur.fetchone())
        conn.close()
        
        if not row:
            return {
                "open": False, "opening_amount": 0, "total_sales": 0,
                "expected": 0, "sales_today": []
            }
        
        sales_today = row.get("sales_today", [])
        total_sales = sum(s["total"] for s in sales_today)
        
        return {
            "open": bool(row["open"]),
            "opening_amount": row["opening_amount"] or 0,
            "opening_ts": row["opening_ts"],
            "opening_user": row["opening_user"],
            "sales_today": sales_today,
            "total_sales": total_sales,
            "expected": (row["opening_amount"] or 0) + total_sales
        }


class PromoRepository:
    """Repositorio especializado en promociones"""
    
    VALID_TYPES = ["porcentaje", "monto_fijo", "2x1", "3x2", "volumen", "cupon", "happy_hour"]
    
    def __init__(self, audit_callback=None):
        self.audit_callback = audit_callback
        self.product_callback = None  # Se inyectará para buscar productos

    def _log(self, user, action, detail=""):
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        if row is None:
            return None
        d = dict(row)
        for json_field in ["condition_json"]:
            if json_field in d and d[json_field]:
                try:
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = {}
        return d

    def set_product_finder(self, finder_func):
        """Inyecta función para buscar productos (evita circular import)"""
        self.product_callback = finder_func

    def _find_product(self, pid):
        if self.product_callback:
            return self.product_callback(pid)
        return None

    def list_promos(self):
        """Lista todas las promociones"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM promos ORDER BY id DESC")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def add_promo(self, data):
        """Crea nueva promoción"""
        name = data.get("name", "").strip()
        if len(name) < 3:
            raise ValueError("Nombre promo ≥3")
        
        ptype = data.get("type", "").strip()
        if ptype not in self.VALID_TYPES:
            raise ValueError(f"Tipo debe ser {self.VALID_TYPES}")
        
        val = float(data.get("value", 0))
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO promos (name, type, value, condition, code, active, desc) VALUES (?,?,?,?,?,?,?)",
            (name, ptype, val, data.get("condition", ""),
             data.get("code", f"PROMO{len(self.list_promos())+1}").upper(),
             1 if data.get("active", True) else 0, data.get("desc", ""))
        )
        conn.commit()
        cur.execute("SELECT * FROM promos WHERE code=?", (data.get("code", "").upper(),))
        r = self._row_to_dict(cur.fetchone())
        if not r:
            cur.execute("SELECT * FROM promos WHERE name=?", (name,))
            r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def update_promo(self, pid, updates):
        """Actualiza promoción existente"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM promos WHERE id=?", (pid,))
        pr = self._row_to_dict(cur.fetchone())
        
        if not pr:
            conn.close()
            raise ValueError(f"Promo {pid} no encontrada")
        
        for k in ("name", "type", "value", "condition", "code", "active", "desc"):
            if k in updates and updates[k] != "":
                if k == "value":
                    v = float(updates[k])
                    cur.execute("UPDATE promos SET value=? WHERE id=?", (v, pid))
                elif k == "active":
                    v = 1 if (updates[k] is True or str(updates[k]).lower() in ("si", "true", "1", "activo")) else 0
                    cur.execute("UPDATE promos SET active=? WHERE id=?", (v, pid))
                else:
                    v = updates[k]
                    cur.execute(f"UPDATE promos SET {k}=? WHERE id=?", (v, pid))
        
        conn.commit()
        cur.execute("SELECT * FROM promos WHERE id=?", (pid,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def delete_promo(self, pid):
        """Elimina promoción"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM promos WHERE id=?", (pid,))
        if cur.rowcount == 0:
            conn.close()
            raise ValueError(f"Promo {pid} no encontrada")
        conn.commit()
        conn.close()

    def apply_promo(self, cart, promo_code):
        """Aplica promoción a un carrito de compras"""
        if not promo_code:
            return 0.0, None
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM promos WHERE lower(code)=lower(?) AND active=1", (promo_code.strip(),))
        promo = self._row_to_dict(cur.fetchone())
        conn.close()
        
        if not promo:
            raise ValueError(f"Promo {promo_code} no existe o inactiva")
        
        subtotal = sum(i["subtotal"] for i in cart)
        qty_total = sum(i["qty"] for i in cart)
        discount = 0.0
        ptype = promo["type"]
        
        if ptype == "porcentaje":
            cond = promo.get("condition", "").lower()
            if cond and cond not in ("min 5000", "min 500000", "qty>=10"):
                cat_total = sum(
                    i["subtotal"] for i in cart 
                    if self._find_product(i["id"]) and 
                    self._find_product(i["id"])["cat"].lower() == cond
                )
                discount = cat_total * promo["value"] / 100 if cat_total else 0
            else:
                discount = subtotal * promo["value"] / 100
        
        elif ptype == "monto_fijo":
            try:
                min_val = float(promo.get("condition", "").split("min")[-1].strip()) if "min" in promo.get("condition", "") else 0
            except Exception:
                min_val = 0
            if subtotal >= min_val:
                discount = promo["value"]
        
        elif ptype == "2x1":
            sku = promo.get("condition", "").strip()
            for it in cart:
                prod = self._find_product(it["id"])
                if prod and prod["sku"] == sku and it["qty"] >= 2:
                    discount += (it["qty"] // 2) * prod["price"]
        
        elif ptype == "3x2":
            sku_or_cat = promo.get("condition", "").strip().lower()
            for it in cart:
                prod = self._find_product(it["id"])
                if not prod:
                    continue
                if prod["sku"].lower() == sku_or_cat or prod["cat"].lower() == sku_or_cat:
                    if it["qty"] >= 3:
                        discount += (it["qty"] // 3) * prod["price"]
        
        elif ptype == "volumen":
            if qty_total >= 10:
                discount = subtotal * promo["value"] / 100
        
        elif ptype in ("cupon", "happy_hour"):
            discount = subtotal * promo["value"] / 100 if promo["value"] else 0
        
        discount = min(discount, subtotal)
        return discount, promo


class PurchaseRepository:
    """Repositorio especializado en compras a proveedores"""
    
    def __init__(self, audit_callback=None):
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        if row is None:
            return None
        d = dict(row)
        for json_field in ["items_json"]:
            if json_field in d and d[json_field]:
                try:
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = []
        return d

    def list_purchases(self):
        """Lista todas las compras"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM purchases ORDER BY date DESC")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def find_purchase(self, folio):
        """Busca compra por folio"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM purchases WHERE id=?", (folio,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def create_purchase(self, supplier, sku, qty, user="sistema"):
        """Crea orden de compra"""
        from data.repositories.product_repository import ProductRepository
        prod_repo = ProductRepository(audit_callback=self._log)
        
        p = prod_repo.find_product_by_sku(sku)
        if not p:
            raise ValueError(f"Producto SKU {sku} no encontrado")
        
        folio = sqlite.next_counter("PURCHASE_COUNTER", "OC")
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO purchases (folio, supplier, sku, product_id, qty, status, date, user) VALUES (?,?,?,?,?,?,?,?)",
            (folio, supplier, sku, p["id"], qty, "Pendiente", datetime.now().strftime("%Y-%m-%d"), user)
        )
        conn.commit()
        conn.close()
        
        self._log(user, "compra_creada", f"Folio={folio}, Proveedor={supplier}, SKU={sku}, Qty={qty}")
        return self.find_purchase(folio)

    def receive_purchase(self, folio, user="sistema"):
        """Recibe compra y actualiza inventario"""
        from data.repositories.product_repository import ProductRepository
        from data.repositories.inventory_repository import InventoryRepository
        
        purch = self.find_purchase(folio)
        if not purch:
            raise ValueError(f"Compra {folio} no encontrada")
        if purch["status"] != "Pendiente":
            raise ValueError(f"Compra {folio} no está pendiente")
        
        inv_repo = InventoryRepository(audit_callback=self._log)
        result = inv_repo.adjust_stock(purch["sku"], purch["qty"], f"Recepción OC {folio}", user, "Entrada")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE purchases SET status='Recibida', received_date=? WHERE id=?",
                   (datetime.now().strftime("%Y-%m-%d"), folio))
        conn.commit()
        conn.close()
        
        self._log(user, "compra_recibida", f"Folio={folio}, {result}")
        return result

    def cancel_purchase(self, folio, user="sistema"):
        """Cancela orden de compra pendiente"""
        purch = self.find_purchase(folio)
        if not purch:
            raise ValueError(f"Compra {folio} no encontrada")
        if purch["status"] != "Pendiente":
            raise ValueError(f"Compra {folio} no se puede cancelar (estado: {purch['status']})")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE purchases SET status='Cancelada' WHERE id=?", (folio,))
        conn.commit()
        conn.close()
        
        self._log(user, "compra_cancelada", f"Folio={folio}")
        return True


class AuditRepository:
    """Repositorio especializado en auditoría y logs"""
    
    def __init__(self):
        pass

    def log(self, user, action, detail=""):
        """Registra evento de auditoría"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO audit_log (username, action, detail, ts) VALUES (?,?,?,?)",
            (user, action, detail, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()
        conn.close()

    def list_audit(self, limit=100):
        """Lista logs de auditoría"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM audit_log ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
        return rows
