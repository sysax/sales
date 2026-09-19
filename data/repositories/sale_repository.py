"""
SaleRepository — Gestión de ventas, documentos y notas crédito/cargo
Responsabilidad única: ciclo completo de ventas
"""
import json
from datetime import datetime, timedelta
from data import db as sqlite
from data import dian as dian_mod
from data import mock_data as mock


class SaleRepository:
    """Repositorio especializado en ventas y documentos comerciales"""
    
    ESTADOS_VENTA = ["Cotización", "Pedido", "Facturada", "Pagada", "Entregada", "Cerrada"]
    
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
        for json_field in ["payments_json", "items_json", "sales_today_json"]:
            if json_field in d and d[json_field]:
                try:
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = {}
        return d

    # ── Consultas ──
    def list_sales(self):
        """Lista todas las ventas ordenadas por fecha"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales ORDER BY date DESC, id DESC")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def find_sale(self, sid):
        """Busca venta por ID/folio"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id=?", (sid,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def list_sale_items(self):
        """Lista todos los items de ventas"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sale_items ORDER BY id DESC")
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    # ── Creación de ventas ──
    def create_sale(self, *, client_name, total, payment, cart_items, 
                    promo_code=None, discount=0, tax=0, payments=None, doc_type=None):
        """
        Crea una nueva venta con manejo de pagos, inventario y DIAN.
        
        Args:
            client_name: Nombre del cliente
            total: Total de la venta
            payment: Método de pago principal
            cart_items: Lista de items [{id, qty, subtotal, ...}]
            promo_code: Código de promoción aplicado
            discount: Descuento aplicado
            tax: Impuestos
            payments: Dict de pagos {efectivo: X, credito: Y, ...}
            doc_type: Tipo de documento (Factura, Ticket, etc.)
        
        Returns:
            dict con datos de la venta creada
        """
        # Procesar pagos
        if isinstance(payment, dict):
            payments = payment
            has_credit = payments.get("credito", 0) > 0
            status = "Pendiente" if has_credit else "Pagada"
            payment_str = "+".join([k for k, v in payments.items() if v > 0]) or "Mixto"
        else:
            if isinstance(payments, dict) and any(payments.values()):
                has_credit = payments.get("credito", 0) > 0
                status = "Pendiente" if has_credit else "Pagada"
                payment_str = "+".join([k for k, v in payments.items() if v > 0]) or str(payment)
            else:
                payments = None
                status = "Pendiente" if payment == "Credito" else "Pagada"
                payment_str = str(payment)
        
        folio = sqlite.next_counter("SALE_COUNTER", "V")
        
        # Calcular subtotal
        try:
            subtotal_calc = sum(it.get("subtotal", 0) for it in (cart_items or []))
        except Exception:
            subtotal_calc = total + discount - tax
        
        subtotal = subtotal_calc if subtotal_calc else (total + discount - tax)
        
        # Calcular valores de pago
        if isinstance(payments, dict):
            paid_val = total if status == "Pagada" else total - payments.get("credito", 0)
        else:
            paid_val = total if status == "Pagada" else 0.0
        
        balance_val = (0.0 if status == "Pagada" else 
                      (payments.get("credito", total) if isinstance(payments, dict) and "credito" in payments 
                       else total))
        
        # Generar CUFE DIAN
        if not doc_type or doc_type == "Factura electrónica DIAN":
            doc_type = dian_mod.default_doc_type()
        cufe = dian_mod.generate_cufe(folio)
        dian_status = "PENDIENTE_OFFLINE" if getattr(mock, "IS_OFFLINE", False) else "SINCRONIZADO"
        
        # Obtener vendedor actual
        vendedor = "vendedor"
        try:
            from kivymd.app import MDApp
            app = MDApp.get_running_app()
            if app and getattr(app, "current_user", None):
                vendedor = app.current_user.get("username", "vendedor")
        except Exception:
            pass
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        
        # Insertar venta
        cur.execute(
            """INSERT INTO sales (
                id, date, client, vendedor, total, subtotal, tax, discount, promo,
                status, doc_type, payment, payments_json, paid, balance, due,
                estado, dian_cufe, dian_status
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (folio, datetime.now().strftime("%Y-%m-%d"), client_name, vendedor,
             total, subtotal, tax, discount, promo_code, status, doc_type,
             payment_str, json.dumps(payments or {payment_str.lower(): total}),
             paid_val, balance_val,
             (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d") if status == "Pendiente" 
             else datetime.now().strftime("%Y-%m-%d"),
             status, cufe, dian_status)
        )
        
        # Procesar items y actualizar stock
        for it in cart_items:
            cur.execute("SELECT stock FROM products WHERE id=?", (it["id"],))
            row = cur.fetchone()
            if row:
                new_stock = row[0] - it["qty"]
                cur.execute("UPDATE products SET stock=? WHERE id=?", (new_stock, it["id"]))
            cur.execute(
                "INSERT INTO sale_items (sale_id, product_id, qty, subtotal) VALUES (?,?,?,?)",
                (folio, it["id"], it["qty"], it["subtotal"])
            )
        
        # Actualizar crédito del cliente si aplica
        if payments and payments.get("credito", 0) > 0:
            cur.execute("SELECT credit, balance FROM clients WHERE lower(name)=lower(?)", (client_name,))
            crow = cur.fetchone()
            if crow:
                cur.execute(
                    "UPDATE clients SET credit=?, balance=? WHERE lower(name)=lower(?)",
                    (crow[0] + payments["credito"], crow[1] + payments["credito"], client_name)
                )
        elif payment == "Credito":
            cur.execute("SELECT credit, balance FROM clients WHERE lower(name)=lower(?)", (client_name,))
            crow = cur.fetchone()
            if crow:
                cur.execute(
                    "UPDATE clients SET credit=?, balance=? WHERE lower(name)=lower(?)",
                    (crow[0] + total, crow[1] + total, client_name)
                )
        
        # Actualizar caja
        cur.execute("SELECT * FROM caja WHERE id=1")
        caja = self._row_to_dict(cur.fetchone())
        if caja and caja["open"]:
            try:
                sales_today = json.loads(caja["sales_today_json"] or "[]")
            except Exception:
                sales_today = []
            sales_today.append({"id": folio, "total": total})
            cur.execute(
                "UPDATE caja SET sales_today_json=?, expected=? WHERE id=1",
                (json.dumps(sales_today), caja["opening_amount"] + sum(s["total"] for s in sales_today))
            )
        
        conn.commit()
        conn.close()
        
        result = {
            "id": folio, "date": datetime.now().strftime("%Y-%m-%d"),
            "client": client_name, "total": total, "subtotal": subtotal,
            "tax": tax, "discount": discount, "promo": promo_code,
            "status": status, "doc_type": doc_type, "payment": payment_str,
            "payments": payments or {payment_str.lower(): total},
            "paid": paid_val, "balance": balance_val,
            "dian_cufe": cufe, "dian_status": dian_status, "estado": status
        }
        return result

    # ── Documentos comerciales ──
    def create_document(self, doc_type, client, total, user="sistema"):
        """Crea documento comercial (Cotización, Pedido, Remisión, etc.)"""
        valid = ["Cotización", "Pedido", "Remisión", "Factura", "Nota crédito", "Nota cargo"]
        if doc_type not in valid:
            raise ValueError(f"doc_type debe ser {valid}")
        
        prefix_map = {
            "Cotización": "COT", "Pedido": "PED", "Remisión": "REM",
            "Factura": "V", "Nota crédito": "NC", "Nota cargo": "NCC"
        }
        counter_map = {
            "Cotización": "QUOTE_COUNTER", "Pedido": "ORDER_COUNTER",
            "Remisión": "SALE_COUNTER", "Factura": "SALE_COUNTER",
            "Nota crédito": "CREDIT_NOTE_COUNTER", "Nota cargo": "SALE_COUNTER"
        }
        
        prefix = prefix_map[doc_type]
        counter = counter_map[doc_type]
        folio = sqlite.next_counter(counter, prefix)
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO sales (
                id, date, client, vendedor, total, subtotal, tax, discount,
                status, doc_type, payment, payments_json, paid, balance, estado
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (folio, datetime.now().strftime("%Y-%m-%d"), client, user,
             float(total), float(total), 0, 0, doc_type, doc_type, "", "{}",
             0.0, float(total), doc_type)
        )
        conn.commit()
        conn.close()
        
        self._log(user, f"doc_{doc_type.lower().replace(' ', '_')}_creado", f"{folio} {client} ${total}")
        return self.find_sale(folio)

    def advance_sale_status(self, sale_id, new_status, user="sistema"):
        """Avanza el estado de una venta en el flujo"""
        s = self.find_sale(sale_id)
        if not s:
            raise ValueError(f"Venta {sale_id} no encontrada")
        if s["status"] == "Cancelada":
            raise ValueError("Venta cancelada no avanza")
        
        if new_status == "Cancelada":
            conn = sqlite.get_conn()
            cur = conn.cursor()
            cur.execute("UPDATE sales SET status='Cancelada', estado='Cancelada', balance=0 WHERE id=?", (sale_id,))
            conn.commit()
            conn.close()
            self._log(user, "venta_cancelada", sale_id)
            return self.find_sale(sale_id)
        
        if new_status not in self.ESTADOS_VENTA and new_status != "Cancelada":
            raise ValueError(f"Estado debe ser {self.ESTADOS_VENTA + ['Cancelada']}")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        if new_status in ("Pagada", "Entregada", "Cerrada"):
            cur.execute(
                "UPDATE sales SET status=?, estado=?, balance=0, paid=total WHERE id=?",
                (new_status, new_status, sale_id)
            )
        else:
            cur.execute(
                "UPDATE sales SET status=?, estado=? WHERE id=?",
                (new_status, new_status, sale_id)
            )
        conn.commit()
        conn.close()
        self._log(user, "venta_avance", f"{sale_id} -> {new_status}")
        return self.find_sale(sale_id)

    def create_credit_note(self, sale_id, amount, reason, user="sistema"):
        """Crea nota crédito asociada a una venta"""
        s = self.find_sale(sale_id)
        if not s:
            raise ValueError(f"Venta {sale_id} no encontrada")
        
        amount = float(amount)
        if amount <= 0 or amount > s["total"]:
            raise ValueError("Monto inválido")
        if not reason.strip():
            raise ValueError("Motivo requerido")
        
        note = self.create_document("Nota crédito", s["client"], amount, user=user)
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE sales SET reason=?, ref=? WHERE id=?", (reason, sale_id, note["id"]))
        conn.commit()
        conn.close()
        
        self._log(user, "nota_credito", f"{note['id']} ref {sale_id} ${amount} {reason[:20]}")
        return note

    def create_debit_note(self, sale_id, amount, reason, user="sistema"):
        """Crea nota cargo asociada a una venta"""
        s = self.find_sale(sale_id)
        if not s:
            raise ValueError(f"Venta {sale_id} no encontrada")
        
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Monto >0")
        if not reason.strip():
            raise ValueError("Motivo requerido")
        
        note = self.create_document("Nota cargo", s["client"], amount, user=user)
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE sales SET reason=?, ref=? WHERE id=?", (reason, sale_id, note["id"]))
        conn.commit()
        conn.close()
        
        self._log(user, "nota_cargo", f"{note['id']} ref {sale_id} ${amount}")
        return note
