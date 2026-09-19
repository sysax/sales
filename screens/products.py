"""
Catálogo §2 — Colombia COP — cierre módulo: imagen, lotes/caducidad, kits, barcode generar/imprimir
ABM + CSV + búsqueda + stock + IVA 19% DIAN — genérico abarrotes/electrónica
KivyMD 2.0.1
"""
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField, MDTextFieldLeadingIcon, MDTextFieldHintText, MDTextFieldHelperText
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp

from components.topbar import create_topbar
from components.theme import action_bar, flex_columns
from data.repository import repo


class ProductsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "products"
        self.dialog = None
        self._fields = {}
        self.search_field = None
        self.table = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        products = repo.list_products()

        # Tabla con kit y vencimiento
        def _estado(p):
            if p.get("is_kit"):
                return "Kit"
            if p["stock"] == 0:
                return "Agotado"
            if p.get("vencimiento"):
                try:
                    from datetime import datetime
                    venc = datetime.strptime(p["vencimiento"], "%Y-%m-%d").date()
                    if (venc - datetime.now().date()).days <= 30:
                        return "Por caducar"
                except Exception:
                    pass
            if p["stock"] < p.get("stock_min", 5):
                return "Bajo"
            return p.get("status", "activo")

        self.table = MDDataTable(
            size_hint=(1, None), height="340dp", use_pagination=True, rows_num=7,
            column_data=flex_columns(1150,
                ("SKU", 1.2),
                ("Producto", 2.5),
                ("Cat", 1.1),
                ("Precio COP", 1.4),
                ("Stock", 0.9),
                ("Lote", 1),
                ("Vence", 1.2),
                ("Estado", 1.3),
            ),
            row_data=[
                (
                    p["sku"], p["name"][:18], p["cat"][:10],
                    f"${p['price']:,.0f}", str(p["stock"]),
                    (p.get("lote") or "")[:10],
                    (p.get("vencimiento") or "")[:10],
                    _estado(p)[:12],
                ) for p in products
            ],
        )
        self.search_field = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar SKU / nombre / categoria / barcode — Colombia"),
            mode="outlined", size_hint_x=1,
        )
        self.search_field.bind(text=self.on_search)

        # Botonera 1 CRUD
        btn_row = action_bar(
            MDButton(MDButtonText(text="Agregar"), style="filled", on_release=lambda x: self._open_add_dialog()),
            MDButton(MDButtonText(text="Editar"), style="outlined", on_release=lambda x: self._open_edit_sku_dialog()),
            MDButton(MDButtonText(text="Eliminar"), style="text", on_release=lambda x: self._open_delete_dialog()),
            MDButton(MDButtonText(text="Importar CSV/Excel"), style="outlined", on_release=lambda x: self._open_csv_dialog()),
        )
        # Botonera 2 catálogo avanzado Colombia
        btn_row2 = action_bar(
            MDButton(MDButtonText(text="Barcode Gen"), style="outlined", on_release=lambda x: self._open_barcode_dialog()),
            MDButton(MDButtonText(text="Imprimir Barcode"), style="text", on_release=lambda x: self._open_print_barcode_dialog()),
            MDButton(MDButtonText(text="Crear Kit"), style="filled", on_release=lambda x: self._open_kit_dialog()),
            MDButton(MDButtonText(text="Por Caducar"), style="outlined", on_release=lambda x: self._show_caducidad()),
        )
        btn_row3 = action_bar(
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
            MDButton(MDButtonText(text="Ver Kit"), style="text", on_release=lambda x: self._open_view_kit()),
        )

        # Alertas
        low = repo.low_stock_products(10)
        cad = repo.get_products_by_vencimiento(30)
        kits = repo.get_kits()
        alert = f"Stock bajo {len(low)} · Por caducar 30d {len(cad)} · Kits {len(kits)} · Total {len(products)}"
        if low:
            alert += " | Bajo: " + ", ".join([f"{p['sku']}({p['stock']})" for p in low[:2]])
        if cad:
            alert += " | Caducan: " + ", ".join([f"{p['sku']} {p.get('vencimiento','')}" for p in cad[:2]])

        inner = MDBoxLayout(
            MDLabel(text="Catálogo de Productos — Colombia COP", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Genérico abarrotes/electrónica — IVA 19% DIAN — NIT — SKU/barcode EAN13 — imagen/lote/vencimiento/kit", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            self.search_field,
            btn_row,
            btn_row2,
            btn_row3,
            self.table,
            MDCard(MDLabel(text=alert, font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True), orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="56dp"),
            MDLabel(text="Campos: SKU·Nombre·Cat·Marca·Precio compra/venta/mayoreo·IVA 19%·Unidad·Stock min/max·Lote·Vencimiento·Imagen·Kit", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
            orientation="vertical", adaptive_height=True, spacing="8dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Productos"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *a):
        self.refresh()
    def on_search(self, inst, val):
        filtered = repo.search_products(val)
        def _estado(p):
            if p.get("is_kit"): return "Kit"
            if p["stock"]==0: return "Agotado"
            if p.get("vencimiento"):
                try:
                    from datetime import datetime
                    venc = datetime.strptime(p["vencimiento"], "%Y-%m-%d").date()
                    if (venc - datetime.now().date()).days <=30: return "Por caducar"
                except: pass
            if p["stock"] < p.get("stock_min",5): return "Bajo"
            return p.get("status","activo")
        if self.table:
            self.table.row_data = [
                (p["sku"], p["name"][:14], p["cat"][:8], f"${p['price']:,.0f}", str(p["stock"]), (p.get("lote") or "")[:8], (p.get("vencimiento") or "")[:10], _estado(p)[:10])
                for p in filtered
            ]

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador", "Almacén"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede modificar catálogo"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    # ── Agregar con imagen/lote/vencimiento ──
    def _open_add_dialog(self):
        if not self._require_write(): return
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="SKU *"), MDTextFieldHelperText(text="Unico", mode="persistent"), mode="outlined")
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="package-variant-closed"), MDTextFieldHintText(text="Nombre *"), mode="outlined")
        f_cat = MDTextField(MDTextFieldLeadingIcon(icon="tag"), MDTextFieldHintText(text="Categoria * Abarrotes/Electronica"), helper_text="Genérico", mode="outlined")
        f_price = MDTextField(MDTextFieldLeadingIcon(icon="currency-usd"), MDTextFieldHintText(text="Precio venta COP *"), mode="outlined")
        f_stock = MDTextField(MDTextFieldLeadingIcon(icon="warehouse"), MDTextFieldHintText(text="Stock *"), mode="outlined")
        f_lote = MDTextField(MDTextFieldLeadingIcon(icon="package-variant"), MDTextFieldHintText(text="Lote (ej L-202501)"), MDTextFieldHelperText(text="Abarrotes: Lote", mode="persistent"), mode="outlined")
        f_venc = MDTextField(MDTextFieldLeadingIcon(icon="calendar-clock"), MDTextFieldHintText(text="Vencimiento YYYY-MM-DD"), MDTextFieldHelperText(text="Abarrotes: caducidad", mode="persistent"), mode="outlined")
        f_image = MDTextField(MDTextFieldLeadingIcon(icon="image"), MDTextFieldHintText(text="Imagen path (/tmp/foto.jpg)"), MDTextFieldHelperText(text="Opcional, EAN impreso con barcode", mode="persistent"), mode="outlined")
        f_status = MDTextField(MDTextFieldLeadingIcon(icon="check-circle"), MDTextFieldHintText(text="Estado activo/descontinuado"), mode="outlined")
        self._fields = {"sku": f_sku, "name": f_name, "cat": f_cat, "price": f_price, "stock": f_stock, "lote": f_lote, "vencimiento": f_venc, "image": f_image, "status": f_status}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_sku, f_name, f_cat, f_price, f_stock, f_lote, f_venc, f_image, f_status]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Nuevo producto — Colombia"),
            MDDialogSupportingText(text="SKU/barcode EAN13 auto, lote/vencimiento para abarrotes, imagen opcional, kit vía Crear Kit"),
            grid,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Crear"), style="filled", on_release=lambda x: self._do_add()), spacing="8dp"),
            size_hint=(0.95, None),
        )
        self.dialog.open()

    def _do_add(self):
        try:
            data = {k: v.text.strip() for k, v in self._fields.items()}
            # mapear cat para que si es abarrotes se requiera lote? no obligatorio
            prod = repo.add_product(data)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "alta_producto", f"{prod['sku']} {prod['name']}")
            self.dialog.dismiss()
            # generar barcode automáticamente
            try:
                path = repo.generate_barcode(prod["sku"])
                MDSnackbar(MDSnackbarText(text=f"Producto {prod['sku']} creado + barcode {path}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
            except Exception:
                MDSnackbar(MDSnackbarText(text=f"Producto {prod['sku']} creado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Editar ──
    def _open_edit_sku_dialog(self):
        if not self._require_write(): return
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="SKU a editar *"), mode="outlined")
        self._fields = {"edit_sku": f_sku}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Editar producto"), f_sku, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Continuar"), style="filled", on_release=lambda x: self._open_edit_form()), spacing="8dp"))
        self.dialog.open()
    def _open_edit_form(self):
        sku = self._fields["edit_sku"].text.strip()
        p = repo.find_product_by_sku(sku)
        if not p:
            MDSnackbar(MDSnackbarText(text=f"SKU {sku} no encontrado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        self.dialog.dismiss()
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="package-variant-closed"), MDTextFieldHintText(text=f"Nombre ({p['name']})"), mode="outlined")
        f_cat = MDTextField(MDTextFieldLeadingIcon(icon="tag"), MDTextFieldHintText(text=f"Cat ({p['cat']})"), mode="outlined")
        f_price = MDTextField(MDTextFieldLeadingIcon(icon="currency-usd"), MDTextFieldHintText(text=f"Precio COP ({p['price']:.0f})"), mode="outlined")
        f_stock = MDTextField(MDTextFieldLeadingIcon(icon="warehouse"), MDTextFieldHintText(text=f"Stock ({p['stock']})"), mode="outlined")
        f_lote = MDTextField(MDTextFieldLeadingIcon(icon="package-variant"), MDTextFieldHintText(text=f"Lote ({p.get('lote','')})"), mode="outlined")
        f_venc = MDTextField(MDTextFieldLeadingIcon(icon="calendar-clock"), MDTextFieldHintText(text=f"Venc ({p.get('vencimiento','')}) YYYY-MM-DD"), mode="outlined")
        f_image = MDTextField(MDTextFieldLeadingIcon(icon="image"), MDTextFieldHintText(text=f"Imagen ({p.get('image','')})"), mode="outlined")
        f_status = MDTextField(MDTextFieldLeadingIcon(icon="check-circle"), MDTextFieldHintText(text=f"Estado ({p.get('status','')})"), mode="outlined")
        self._fields = {"sku": sku, "name": f_name, "cat": f_cat, "price": f_price, "stock": f_stock, "lote": f_lote, "vencimiento": f_venc, "image": f_image, "status": f_status}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_name, f_cat, f_price, f_stock, f_lote, f_venc, f_image, f_status]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text=f"Editando {sku} — lote/vencimiento/imagen"), MDDialogSupportingText(text="Vacío = no cambia — barcode se regenera si cambia SKU"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Guardar"), style="filled", on_release=lambda x: self._do_edit()), spacing="8dp"), size_hint=(0.95, None))
        self.dialog.open()
    def _do_edit(self):
        sku = self._fields["sku"]
        updates = {}
        for k in ("name","cat","price","stock","lote","vencimiento","image","status"):
            v = self._fields[k].text.strip()
            if v:
                updates[k] = v
        try:
            repo.update_product(sku, updates)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "edita_producto", f"{sku} {updates}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Producto {sku} actualizado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Eliminar ──
    def _open_delete_dialog(self):
        if not self._require_write(): return
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="delete"), MDTextFieldHintText(text="SKU a eliminar *"), mode="outlined")
        self._fields = {"del_sku": f_sku}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Eliminar producto"), f_sku, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Eliminar"), style="filled", on_release=lambda x: self._do_delete()), spacing="8dp"))
        self.dialog.open()
    def _do_delete(self):
        sku = self._fields["del_sku"].text.strip()
        try:
            repo.delete_product(sku)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "baja_producto", sku)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Producto {sku} eliminado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── CSV ──
    def _open_csv_dialog(self):
        if not self._require_write(): return
        f_path = MDTextField(MDTextFieldLeadingIcon(icon="file-delimited"), MDTextFieldHintText(text="Ruta CSV o Excel (.csv / .xlsx)"), MDTextFieldHelperText(text="sku,name,cat,price,stock,lote,vencimiento — acepta ES/EN", mode="persistent"), mode="outlined")
        self._fields = {"csv": f_path}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Importar CSV/Excel — Colombia"), MDDialogSupportingText(text="Genérico abarrotes/electrónica — lote/vencimiento opcional"), f_path, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Importar"), style="filled", on_release=lambda x: self._do_csv()), spacing="8dp"))
        self.dialog.open()
    def _do_csv(self):
        path = self._fields["csv"].text.strip()
        try:
            n = repo.import_products_file(path)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "import_productos", f"{path} +{n}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Importados {n} productos"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Barcode ──
    def _open_barcode_dialog(self):
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="SKU * para generar barcode EAN13"), MDTextFieldHelperText(text="Genera /tmp/barcodes/{SKU}.png", mode="persistent"), mode="outlined")
        self._fields = {"sku": f_sku}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Generar código de barras"), MDDialogSupportingText(text="EAN13 Colombia 770 — genera PNG para imprimir"), f_sku, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Generar"), style="filled", on_release=lambda x: self._do_barcode()), spacing="8dp"))
        self.dialog.open()
    def _do_barcode(self):
        sku = self._fields["sku"].text.strip()
        try:
            path = repo.generate_barcode(sku)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Barcode {sku} → {path}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
            # preview dialog
            self.dialog = MDDialog(MDDialogHeadlineText(text=f"Barcode {sku}"), MDDialogSupportingText(text=f"Generado: {path}\nImagen lista para imprimir — EAN13 770 — Colombia"), MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.dialog.dismiss()), spacing="8dp"))
            self.dialog.open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
    def _open_print_barcode_dialog(self):
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="printer"), MDTextFieldHintText(text="SKU * a imprimir"), mode="outlined")
        self._fields = {"sku": f_sku}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Imprimir barcode"), MDDialogSupportingText(text="Envía a impresora lp — fallback guarda PNG"), f_sku, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Imprimir"), style="filled", on_release=lambda x: self._do_print_barcode()), spacing="8dp"))
        self.dialog.open()
    def _do_print_barcode(self):
        sku = self._fields["sku"].text.strip()
        try:
            path, ok = repo.print_barcode(sku)
            self.dialog.dismiss()
            msg = f"Impreso {sku} → {path}" if ok else f"Guardado {path} (sin impresora)"
            MDSnackbar(MDSnackbarText(text=msg), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Kits ──
    def _open_kit_dialog(self):
        if not self._require_write(): return
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="package-variant-closed-plus"), MDTextFieldHintText(text="SKU Kit * (ej KIT01)"), mode="outlined")
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="tag"), MDTextFieldHintText(text="Nombre Kit *"), mode="outlined")
        f_comps = MDTextField(MDTextFieldLeadingIcon(icon="format-list-bulleted"), MDTextFieldHintText(text="Componentes SKU:qty, ..."), MDTextFieldHelperText(text="Ej: AB01:2, AB02:1 — stock kit = min(componentes)", mode="persistent"), mode="outlined")
        f_price = MDTextField(MDTextFieldLeadingIcon(icon="currency-usd"), MDTextFieldHintText(text="Precio (vacío = suma -5% desc)"), mode="outlined")
        self._fields = {"sku": f_sku, "name": f_name, "comps": f_comps, "price": f_price}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_sku, f_name, f_comps, f_price]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text="Crear Kit — producto compuesto"), MDDialogSupportingText(text="Genérico: abarrotes kit mercado, electrónica kit PC — valida stock componentes"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Crear Kit"), style="filled", on_release=lambda x: self._do_kit()), spacing="8dp"), size_hint=(0.95, None))
        self.dialog.open()
    def _do_kit(self):
        sku = self._fields["sku"].text.strip()
        name = self._fields["name"].text.strip()
        comps_raw = self._fields["comps"].text.strip()
        price_raw = self._fields["price"].text.strip()
        try:
            comps = []
            for pair in comps_raw.split(","):
                if ":" not in pair: continue
                s, q = pair.split(":")
                comps.append({"sku": s.strip(), "qty": int(q.strip())})
            price = float(price_raw) if price_raw else None
            kit = repo.create_kit(sku, name, comps, price, user=MDApp.get_running_app().current_user.get("username","sistema"))
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Kit {sku} creado stock {kit['stock']}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
    def _open_view_kit(self):
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="package-variant-closed"), MDTextFieldHintText(text="SKU Kit *"), mode="outlined")
        self._fields = {"sku": f_sku}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Ver Kit — componentes"), f_sku, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Ver"), style="filled", on_release=lambda x: self._do_view_kit()), spacing="8dp"))
        self.dialog.open()
    def _do_view_kit(self):
        sku = self._fields["sku"].text.strip()
        try:
            comps = repo.get_kit_components(sku)
            self.dialog.dismiss()
            txt = "\n".join([f"{c['sku']} x{c['qty']}" for c in comps]) or "Sin componentes"
            self.dialog = MDDialog(MDDialogHeadlineText(text=f"Kit {sku}"), MDDialogSupportingText(text=txt), MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.dialog.dismiss()), spacing="8dp"))
            self.dialog.open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Por caducar ──
    def _show_caducidad(self):
        cad = repo.get_products_by_vencimiento(30)
        if not cad:
            MDSnackbar(MDSnackbarText(text="Nada por caducar en 30 días — Colombia"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        txt = "\n".join([f"{p['sku']} {p['name'][:12]} lote {p.get('lote','')} vence {p.get('vencimiento','')} stock {p['stock']}" for p in cad[:5]])
        self.dialog = MDDialog(MDDialogHeadlineText(text=f"Por caducar 30d — {len(cad)} productos"), MDDialogSupportingText(text=txt), MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.dialog.dismiss()), spacing="8dp"))
        self.dialog.open()
