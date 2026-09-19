"""
ClientRepository y SupplierRepository — Gestión de clientes y proveedores
Responsabilidad única: manejo de terceros (clientes y proveedores)
"""
from data import db as sqlite


class ClientRepository:
    """Repositorio especializado en clientes"""
    
    def __init__(self, audit_callback=None):
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        """Convierte fila SQLite a dict con decodificación JSON"""
        if row is None:
            return None
        d = dict(row)
        for json_field in ["payments_json", "items_json"]:
            if json_field in d and d[json_field]:
                try:
                    import json
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = {}
        return d

    # ── Consultas ──
    def list_clients(self):
        """Lista todos los clientes"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients ORDER BY id")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def find_client(self, name):
        """Busca cliente por nombre (case-insensitive)"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE lower(name)=lower(?)", (name.strip(),))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def find_client_by_id(self, cid):
        """Busca cliente por ID"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE id=?", (cid,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def search_clients(self, q):
        """Búsqueda full-text en nombre, NIT, RFC, teléfono y email"""
        q = (q or "").strip().lower()
        if not q:
            return self.list_clients()
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM clients WHERE "
            "lower(name) LIKE ? OR lower(nit) LIKE ? OR lower(rfc) LIKE ? "
            "OR lower(phone) LIKE ? OR lower(email) LIKE ?",
            (f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%")
        )
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    # ── CRUD ──
    def add_client(self, data):
        """Crea nuevo cliente con validaciones"""
        name = data.get("name", "").strip()
        if len(name) < 2:
            raise ValueError("Nombre mínimo 2 caracteres")
        if self.find_client(name):
            raise ValueError("Cliente ya existe")
        
        nit = data.get("nit", data.get("rfc", "")).strip()
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO clients (
                name, nit, rfc, nit_dv, razon, regimen, responsabilidad,
                email, phone, address, city, credit, credit_limit, discount,
                balance, price_list, status
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (name, nit, nit,
             nit.split("-")[-1] if "-" in nit else "",
             data.get("razon", name),
             data.get("regimen", "No responsable IVA"),
             data.get("responsabilidad", data.get("regimen", "No responsable IVA")),
             data.get("email", ""), data.get("phone", ""),
             data.get("address", ""), data.get("city", ""),
             float(data.get("credit", 0)),
             float(data.get("credit_limit", 5000000)),
             int(data.get("discount", 0)),
             float(data.get("balance", 0)),
             data.get("price_list", "detal"),
             data.get("status", "activo"))
        )
        conn.commit()
        cur.execute("SELECT * FROM clients WHERE name=?", (name,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def update_client(self, cid, updates):
        """Actualiza cliente existente"""
        c = self.find_client_by_id(cid)
        if not c:
            raise ValueError(f"Cliente ID {cid} no encontrado")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        
        for k in ("name", "nit", "rfc", "email", "phone", "city", "address",
                  "credit_limit", "discount", "status", "price_list", "regimen", "responsabilidad"):
            if k in updates and updates[k] != "":
                if k == "credit_limit":
                    try:
                        v = float(updates[k])
                    except Exception:
                        conn.close()
                        raise ValueError("Límite crédito numérico")
                    cur.execute("UPDATE clients SET credit_limit=? WHERE id=?", (v, cid))
                
                elif k == "discount":
                    try:
                        v = int(updates[k])
                        assert 0 <= v <= 100
                    except Exception:
                        conn.close()
                        raise ValueError("Descuento 0-100")
                    cur.execute("UPDATE clients SET discount=? WHERE id=?", (v, cid))
                
                else:
                    v = updates[k].strip() if isinstance(updates[k], str) else updates[k]
                    col = "nit" if k == "nit" else k
                    cur.execute(f"UPDATE clients SET {col}=? WHERE id=?", (v, cid))
                    if k == "nit":
                        cur.execute("UPDATE clients SET rfc=? WHERE id=?", (v, cid))
        
        conn.commit()
        r = self.find_client_by_id(cid)
        conn.close()
        return r

    def delete_client(self, cid):
        """Elimina cliente por ID"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM clients WHERE id=?", (cid,))
        if cur.rowcount == 0:
            conn.close()
            raise ValueError(f"Cliente ID {cid} no encontrado")
        conn.commit()
        conn.close()


class SupplierRepository:
    """Repositorio especializado en proveedores"""
    
    def __init__(self, audit_callback=None):
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        """Convierte fila SQLite a dict con decodificación JSON"""
        if row is None:
            return None
        d = dict(row)
        for json_field in ["payments_json", "items_json"]:
            if json_field in d and d[json_field]:
                try:
                    import json
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = {}
        return d

    # ── Consultas ──
    def list_suppliers(self):
        """Lista todos los proveedores"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM suppliers ORDER BY id")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def find_supplier(self, sid):
        """Busca proveedor por ID"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE id=?", (sid,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def find_supplier_by_name(self, name):
        """Busca proveedor por nombre (case-insensitive)"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM suppliers WHERE lower(name)=lower(?)", (name.strip(),))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def search_suppliers(self, q):
        """Búsqueda full-text en nombre, NIT, RFC y contacto"""
        q = (q or "").strip().lower()
        if not q:
            return self.list_suppliers()
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM suppliers WHERE "
            "lower(name) LIKE ? OR lower(nit) LIKE ? OR lower(rfc) LIKE ? OR lower(contact) LIKE ?",
            (f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%")
        )
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    # ── CRUD ──
    def add_supplier(self, data):
        """Crea nuevo proveedor con validaciones"""
        name = data.get("name", "").strip()
        if len(name) < 2:
            raise ValueError("Empresa mínimo 2 caracteres")
        if self.find_supplier_by_name(name):
            raise ValueError("Proveedor ya existe")
        
        nit = data.get("nit", data.get("rfc", "")).strip()
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO suppliers (
                name, nit, rfc, contact, phone, email, city, address,
                catalog, lead_time, payment_terms, balance
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (name, nit, nit, data.get("contact", ""), data.get("phone", ""),
             data.get("email", ""), data.get("city", ""), data.get("address", ""),
             data.get("catalog", ""), data.get("lead_time", ""),
             data.get("payment_terms", ""), float(data.get("balance", 0)))
        )
        conn.commit()
        cur.execute("SELECT * FROM suppliers WHERE name=?", (name,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def update_supplier(self, sid, updates):
        """Actualiza proveedor existente"""
        s = self.find_supplier(sid)
        if not s:
            raise ValueError(f"Proveedor ID {sid} no encontrado")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        
        for k in ("name", "nit", "rfc", "contact", "phone", "email", "city",
                  "catalog", "lead_time", "payment_terms"):
            if k in updates and updates[k] != "":
                v = updates[k].strip() if isinstance(updates[k], str) else updates[k]
                col = k
                cur.execute(f"UPDATE suppliers SET {col}=? WHERE id=?", (v, sid))
                if k == "nit":
                    cur.execute("UPDATE suppliers SET rfc=? WHERE id=?", (v, sid))
        
        conn.commit()
        r = self.find_supplier(sid)
        conn.close()
        return r

    def delete_supplier(self, sid):
        """Elimina proveedor por ID"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM suppliers WHERE id=?", (sid,))
        if cur.rowcount == 0:
            conn.close()
            raise ValueError(f"Proveedor ID {sid} no encontrado")
        conn.commit()
        conn.close()
