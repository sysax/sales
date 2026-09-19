"""
ProductRepository — Gestión de productos, inventario y códigos de barras
Responsabilidad única: manejo del catálogo de productos
"""
import json
import os
from datetime import datetime, timedelta
from data import db as sqlite


class ProductRepository:
    """Repositorio especializado en productos"""
    
    def __init__(self, audit_callback=None):
        """
        Args:
            audit_callback: Función opcional para logging de auditoría
        """
        self.audit_callback = audit_callback

    def _log(self, user, action, detail=""):
        """Log de auditoría si hay callback"""
        if self.audit_callback:
            self.audit_callback(user, action, detail)

    def _row_to_dict(self, row):
        """Convierte fila SQLite a dict con decodificación JSON"""
        if row is None:
            return None
        d = dict(row)
        # Decodificar campos JSON
        for json_field in ["payments_json", "items_json", "sales_today_json", "kit_json"]:
            if json_field in d and d[json_field]:
                try:
                    d[json_field.replace("_json", "")] = json.loads(d[json_field])
                except Exception:
                    d[json_field.replace("_json", "")] = {} if json_field != "items_json" else []
        return d

    # ── Consultas de productos ──
    def list_products(self):
        """Lista todos los productos"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products ORDER BY id")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def find_product(self, pid):
        """Busca producto por ID"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id=?", (pid,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def find_product_by_sku(self, sku):
        """Busca producto por SKU (case-insensitive)"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE lower(sku)=lower(?)", (sku.strip(),))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def find_product_by_barcode(self, barcode):
        """Busca producto por código de barras"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE barcode=?", (barcode.strip(),))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def search_products(self, q):
        """Búsqueda full-text en nombre, SKU, categoría y barcode"""
        q = (q or "").strip().lower()
        if not q:
            return self.list_products()
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM products WHERE "
            "lower(name) LIKE ? OR lower(sku) LIKE ? OR lower(cat) LIKE ? OR barcode LIKE ?",
            (f"%{q}%", f"%{q}%", f"%{q}%", f"%{q}%")
        )
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    # ── CRUD de productos ──
    def add_product(self, data):
        """Crea nuevo producto con validaciones completas"""
        sku = data.get("sku", "").strip()
        if not sku:
            raise ValueError("SKU requerido")
        if self.find_product_by_sku(sku):
            raise ValueError(f"SKU {sku} ya existe")
        
        name = data.get("name", "").strip()
        if len(name) < 2:
            raise ValueError("Nombre mínimo 2 caracteres")
        
        try:
            price = float(data.get("price", 0))
            stock = int(data.get("stock", 0))
        except Exception:
            raise ValueError("Precio/stock numérico")
        
        if price <= 0 or stock < 0:
            raise ValueError("Precio >0 y stock >=0")
        
        # Numéricos opcionales toleran "" (vienen de Excel/CSV)
        try:
            price_buy = float(data.get("price_buy") or price * 0.7)
            price_ws = float(data.get("price_wholesale") or price * 0.9)
        except Exception:
            raise ValueError("price_buy/price_wholesale numérico")
        
        # Imagen, lote, vencimiento, kit
        image = data.get("image")
        lote = data.get("lote")
        venc = data.get("vencimiento")
        
        # Si es abarrotes y no tiene vencimiento, sugerir 180 días
        if not venc and data.get("cat", "") == "Abarrotes":
            venc = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")
        
        is_kit = 1 if data.get("is_kit") else 0
        kit_json = data.get("kit_json", "[]")
        if isinstance(kit_json, list):
            kit_json = json.dumps(kit_json)
        
        # Validación de kit
        if is_kit:
            try:
                comps = json.loads(kit_json) if isinstance(kit_json, str) else kit_json
                if not comps:
                    raise ValueError("Kit debe tener componentes")
                for c in comps:
                    if not self.find_product_by_sku(c.get("sku", "")):
                        raise ValueError(f"Componente {c.get('sku')} no existe")
            except ValueError:
                raise
            except Exception:
                raise ValueError("kit_json inválido")
        
        # Generar barcode EAN13 si no existe
        barcode = data.get("barcode", f"770{abs(hash(sku)) % 10000000000:010d}")
        if not barcode or len(barcode) < 8:
            barcode = f"770{abs(hash(sku)) % 10000000000:010d}"
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO products (
                sku, barcode, name, description, cat, subcat, brand, supplier,
                price, price_buy, price_wholesale, tax, unit, stock, stock_min,
                stock_max, location, status, image, lote, vencimiento, is_kit, kit_json
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (sku, barcode, name, data.get("description", ""), data.get("cat", "General"),
             data.get("subcat", ""), data.get("brand", ""), data.get("supplier", ""),
             price, price_buy, price_ws, data.get("tax", "IVA 19%"),
             data.get("unit", "unidad"), stock, int(data.get("stock_min", 5)),
             int(data.get("stock_max", stock + 50)), data.get("location", ""),
             data.get("status", "activo"), image, lote, venc, is_kit, kit_json)
        )
        conn.commit()
        cur.execute("SELECT * FROM products WHERE sku=?", (sku,))
        r = self._row_to_dict(cur.fetchone())
        conn.close()
        return r

    def update_product(self, sku, updates):
        """Actualiza producto existente"""
        p = self.find_product_by_sku(sku)
        if not p:
            raise ValueError(f"Producto SKU {sku} no encontrado")
        
        conn = sqlite.get_conn()
        cur = conn.cursor()
        
        for k in ("name", "cat", "price", "stock", "stock_min", "stock_max",
                  "status", "price_buy", "brand", "location", "image", "lote",
                  "vencimiento", "is_kit", "kit_json", "barcode"):
            if k in updates and updates[k] != "":
                if k in ("price", "price_buy", "price_wholesale"):
                    try:
                        v = float(updates[k])
                        if v <= 0:
                            raise ValueError
                    except Exception:
                        conn.close()
                        raise ValueError(f"{k} debe ser número >0")
                    cur.execute(f"UPDATE products SET {k}=? WHERE sku=?", (v, sku))
                
                elif k in ("stock", "stock_min", "stock_max", "is_kit"):
                    try:
                        v = int(updates[k])
                        if k != "is_kit" and v < 0:
                            raise ValueError
                    except Exception:
                        conn.close()
                        raise ValueError(f"{k} debe ser entero >=0")
                    cur.execute(f"UPDATE products SET {k}=? WHERE sku=?", (v, sku))
                
                else:
                    v = updates[k].strip() if isinstance(updates[k], str) else updates[k]
                    # kit_json puede ser lista
                    if k == "kit_json" and isinstance(v, list):
                        v = json.dumps(v)
                    cur.execute(f"UPDATE products SET {k}=? WHERE sku=?", (v, sku))
        
        conn.commit()
        r = self.find_product_by_sku(sku)
        conn.close()
        return r

    def delete_product(self, sku):
        """Elimina producto por SKU"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM products WHERE sku=?", (sku,))
        if cur.rowcount == 0:
            conn.close()
            raise ValueError(f"SKU {sku} no encontrado")
        conn.commit()
        conn.close()

    # ── Códigos de barras ──
    def generate_barcode(self, sku):
        """Genera imagen de código de barras EAN13 en /tmp/barcodes/{sku}.png"""
        p = self.find_product_by_sku(sku)
        if not p:
            raise ValueError(f"SKU {sku} no encontrado")
        
        barcode = p.get("barcode") or f"770{abs(hash(sku)) % 10000000000:010d}"
        if len(barcode) < 12:
            barcode = barcode.ljust(12, "0")
        barcode = barcode[:13]
        
        out_dir = "/tmp/barcodes"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{sku}.png")
        
        # Intentar python-barcode
        try:
            import barcode as bc
            from barcode.writer import ImageWriter
            from barcode import get_barcode_class
            
            ean = get_barcode_class('ean13')
            writer = ImageWriter()
            obj = ean(barcode[:12], writer=writer)
            filename = obj.save(os.path.join(out_dir, sku))
            
            if os.path.exists(filename):
                conn = sqlite.get_conn()
                cur = conn.cursor()
                cur.execute("UPDATE products SET barcode=? WHERE sku=?", (barcode, sku))
                conn.commit()
                conn.close()
                return filename
        except Exception:
            pass
        
        # Fallback PIL texto
        try:
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (400, 100), color='white')
            d = ImageDraw.Draw(img)
            try:
                font = ImageFont.load_default()
            except Exception:
                font = None
            d.text((10, 10), f"SKU: {sku}", fill='black', font=font)
            d.text((10, 35), f"BARCODE: {barcode}", fill='black', font=font)
            d.rectangle([10, 60, 390, 90], outline='black')
            # Barras simuladas
            for i, ch in enumerate(barcode):
                w = 2 if int(ch) % 2 == 0 else 4
                d.rectangle([10 + i * 20, 62, 10 + i * 20 + w, 88], fill='black')
            img.save(out_path, 'PNG')
            
            conn = sqlite.get_conn()
            cur = conn.cursor()
            cur.execute("UPDATE products SET barcode=? WHERE sku=?", (barcode, sku))
            conn.commit()
            conn.close()
            return out_path
        except Exception:
            # Fallback txt
            txt_path = os.path.join(out_dir, f"{sku}.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(f"SKU {sku}\nBARCODE {barcode}\n")
            return txt_path

    def print_barcode(self, sku):
        """Genera e intenta imprimir código de barras"""
        path = self.generate_barcode(sku)
        try:
            import subprocess
            subprocess.run(["lp", path], check=True, capture_output=True)
            return True
        except Exception:
            return False

    # ── Vencimientos y Kits ──
    def get_products_by_vencimiento(self, days=30):
        """Productos próximos a vencer"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cutoff = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        cur.execute(
            "SELECT * FROM products WHERE vencimiento IS NOT NULL AND vencimiento <= ? ORDER BY vencimiento",
            (cutoff,)
        )
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def get_kits(self):
        """Lista todos los kits"""
        conn = sqlite.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE is_kit=1")
        rows = [self._row_to_dict(r) for r in cur.fetchall()]
        conn.close()
        return rows

    def create_kit(self, sku, name, components, price=None, user="sistema"):
        """
        Crea un producto kit con componentes.
        components: lista de dicts {sku, qty}
        """
        # Validar componentes
        for c in components:
            if not self.find_product_by_sku(c.get("sku", "")):
                raise ValueError(f"Componente {c.get('sku')} no existe")
        
        data = {
            "sku": sku,
            "name": name,
            "price": price or 0,
            "is_kit": 1,
            "kit_json": components,
            "cat": "Kits",
            "stock": 999,  # Stock virtual
        }
        result = self.add_product(data)
        self._log(user, "kit_creado", f"SKU={sku}, componentes={len(components)}")
        return result

    def get_kit_components(self, sku):
        """Obtiene componentes de un kit"""
        p = self.find_product_by_sku(sku)
        if not p or not p.get("is_kit"):
            return None
        return p.get("kit_json", [])
