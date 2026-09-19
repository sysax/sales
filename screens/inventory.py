"""
Pantalla de Inventario / Almacén §5 — corazón del sistema
Entradas/Salidas/Transferencias, stock físico vs sistema, valorizado,
PEPS/Promedio, inventario cíclico, alertas, scanner, ajustes con justificación, rotación
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


class InventoryScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "inventory"
        self.dialog = None
        self._fields = {}
        self.search_field = None
        self.scanner_field = None
        self.table = None
        self.mov_table = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        val = repo.get_inventory_value()
        alerts = repo.get_inventory_alerts()
        low = alerts["low"]
        excess = alerts["excess"]
        out = alerts["out"]
        products = repo.list_products()
        movements = repo.list_movements(12)

        # ── KPIs valorizado ──
        kpi = MDGridLayout(cols=3, spacing="12dp", adaptive_height=True, size_hint_x=1, padding="12dp")
        for title, value, color in [
            ("Valorizado costo", val["cost_fmt"], "#4CAF50"),
            ("Valorizado venta", val["sale_fmt"], "#2196F3"),
            ("Unidades totales", str(val["units"]), "#9C27B0"),
            (f"Stock bajo <min ({len(low)})", ", ".join([p["sku"] for p in low[:3]]) or "OK", "#F44336" if low else "#4CAF50"),
            (f"Exceso >max ({len(excess)})", ", ".join([p["sku"] for p in excess[:3]]) or "OK", "#FF9800" if excess else "#4CAF50"),
            (f"Agotado 0 ({len(out)})", ", ".join([p["sku"] for p in out[:3]]) or "0", "#F44336" if out else "#4CAF50"),
        ]:
            kpi.add_widget(
                MDCard(
                    MDLabel(text=title, font_style="Title", role="small", adaptive_height=True, halign="center"),
                    MDLabel(text=value, font_style="Headline", role="small", halign="center", theme_text_color="Custom", text_color=color, adaptive_height=True),
                    orientation="vertical", padding="12dp", size_hint_y=None, height="90dp", style="elevated",
                )
            )

        # ── Tabla stock ──
        def _estado(p):
            if p["stock"] == 0:
                return "Agotado"
            if p["stock"] < p.get("stock_min", 5):
                return "Bajo"
            if p["stock"] > p.get("stock_max", 9999):
                return "Exceso"
            return "OK"

        self.table = MDDataTable(
            size_hint=(1, None), height="340dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1150,
                ("SKU", 1.2),
                ("Producto", 2.5),
                ("Stock", 1),
                ("Min", 0.9),
                ("Max", 0.9),
                ("Ubicacion", 1.3),
                ("Estado", 1.2),
                ("Valor costo", 1.6),
            ),
            row_data=[
                (
                    p["sku"], p["name"][:18], str(p["stock"]), str(p.get("stock_min",5)), str(p.get("stock_max",50)), p.get("location","")[:12], _estado(p), f"${p.get('price_buy',0)*p['stock']:,.0f}"
                )
                for p in products
            ],
        )

        # ── Búsqueda + scanner ──
        self.search_field = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar SKU / nombre / categoria / barcode..."),
            mode="outlined", size_hint_x=1,
        )
        self.search_field.bind(text=self.on_search)

        self.scanner_field = MDTextField(
            MDTextFieldLeadingIcon(icon="barcode-scan"),
            MDTextFieldHintText(text="Escanear código de barras (EAN) + Enter"),
            MDTextFieldHelperText(text="Ej 7501234560011 → P001", mode="persistent"),
            mode="outlined", size_hint_x=1,
        )
        # Enter triggers scan
        self.scanner_field.bind(text=self._on_barcode_text)

        # Botonera
        btn_row = action_bar(
            MDButton(MDButtonText(text="Ajustar Stock"), style="filled", on_release=lambda x: self._open_adjust_dialog()),
            MDButton(MDButtonText(text="Entrada"), style="outlined", on_release=lambda x: self._open_adjust_dialog(pref_type="Entrada")),
            MDButton(MDButtonText(text="Salida"), style="outlined", on_release=lambda x: self._open_adjust_dialog(pref_type="Salida")),
            MDButton(MDButtonText(text="Transferencia"), style="text", on_release=lambda x: self._open_transfer_dialog()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
        )
        btn_row2 = action_bar(
            MDButton(MDButtonText(text="Escanear"), style="text", on_release=lambda x: self._do_scan()),
            MDButton(MDButtonText(text="Generar Orden Compra"), style="outlined", on_release=lambda x: self._goto_purchases()),
        )

        # Movimientos
        self.mov_table = MDDataTable(
            size_hint=(1, None), height="260dp", use_pagination=False,
            column_data=flex_columns(1050,
                ("Fecha", 1.8),
                ("SKU", 1),
                ("Tipo", 1.4),
                ("Cant", 0.9),
                ("Antes→Después", 1.6),
                ("Motivo", 2.4),
                ("Usuario", 1.2),
            ),
            row_data=[
                (m["ts"], m["sku"], m["type"], f"{m['qty']:+d}", f"{m['before']}→{m['after']}", m["reason"][:22], m["user"])
                for m in movements
            ],
        )

        inner = MDBoxLayout(
            MDLabel(text="Inventario / Almacén", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Entradas (compras/devolucion cliente) · Salidas (ventas/merma/robos) · Transferencias · Ajustes con justificación · PEPS/Promedio", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            kpi,
            self.search_field,
            self.scanner_field,
            btn_row,
            btn_row2,
            MDLabel(text="Stock físico vs sistema — Inventario valorizado", font_style="Title", role="small", adaptive_height=True, padding=(0,"8dp",0,0)),
            self.table,
            MDCard(
                MDLabel(text="Movimientos recientes (cíclico) — últimas 12 operaciones", font_style="Title", role="small", adaptive_height=True),
                self.mov_table,
                orientation="vertical", padding="12dp", spacing="8dp", style="outlined", size_hint_y=None, height="320dp",
            ),
            MDLabel(text="Método valuación: Promedio (costo medio) · PEPS y Costo específico soportados vía repo.get_inventory_value()", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
            orientation="vertical", adaptive_height=True, spacing="12dp", padding="16dp",
        )

        self.add_widget(MDBoxLayout(create_topbar("Inventario"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *args):
        self.refresh()
    def on_search(self, instance, value):
        filtered = repo.search_products(value)
        def _estado(p):
            if p["stock"] == 0: return "Agotado"
            if p["stock"] < p.get("stock_min",5): return "Bajo"
            if p["stock"] > p.get("stock_max",9999): return "Exceso"
            return "OK"
        if self.table:
            self.table.row_data = [
                (p["sku"], p["name"][:14], str(p["stock"]), str(p.get("stock_min",5)), str(p.get("stock_max",50)), p.get("location",""), _estado(p), f"${p.get('price_buy',0)*p['stock']:,.0f}")
                for p in filtered
            ]
    def _on_barcode_text(self, instance, value):
        # auto-scan al escribir 13 dígitos
        if len(value.strip()) == 13 and value.strip().isdigit():
            self._do_scan()

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Almacén"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede modificar inventario (solo Almacén/Admin)"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    def _do_scan(self):
        code = (self.scanner_field.text or "").strip()
        if not code:
            MDSnackbar(MDSnackbarText(text="Ingrese código de barras"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()
            return
        prod = repo.scan_barcode(code)
        if not prod:
            # probar SKU
            prod = repo.find_product_by_sku(code)
        if prod:
            MDSnackbar(MDSnackbarText(text=f"{prod['sku']} {prod['name']} stock {prod['stock']} ub {prod.get('location','')}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
            # filtrar tabla a ese producto
            self.search_field.text = prod["sku"]
        else:
            MDSnackbar(MDSnackbarText(text=f"Barcode/SKU {code} no encontrado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def _goto_purchases(self):
        MDApp.get_running_app().navigate_to("purchases")

    # ── Ajuste ──
    def _open_adjust_dialog(self, pref_type="Ajuste"):
        if not self._require_write():
            return
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="SKU *"), MDTextFieldHelperText(text="Ej P001", mode="persistent"), mode="outlined")
        f_qty = MDTextField(MDTextFieldLeadingIcon(icon="plus-minus"), MDTextFieldHintText(text="Cantidad * (+ entrada / - salida)"), MDTextFieldHelperText(text="ej +5 o -3", mode="persistent"), mode="outlined")
        f_reason = MDTextField(MDTextFieldLeadingIcon(icon="comment-text"), MDTextFieldHintText(text="Justificación *"), MDTextFieldHelperText(text="Obligatoria: compra, merma, ajuste, devolucion...", mode="persistent"), mode="outlined")
        if pref_type != "Ajuste":
            f_reason.helper_text = f"{pref_type}: " + f_reason.helper_text if hasattr(f_reason, 'helper_text') else ""
        self._fields = {"sku": f_sku, "qty": f_qty, "reason": f_reason, "ptype": pref_type}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_sku, f_qty, f_reason]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text=f"{pref_type} de inventario" if pref_type!="Ajuste" else "Ajuste de inventario"),
            MDDialogSupportingText(text="Stock físico vs sistema debe coincidir — justificación obligatoria"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Aplicar"), style="filled", on_release=lambda x: self._do_adjust()),
                spacing="8dp",
            ),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_adjust(self):
        sku = self._fields["sku"].text.strip()
        qty = self._fields["qty"].text.strip()
        reason = self._fields["reason"].text.strip()
        ptype = self._fields["ptype"]
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        try:
            mov = repo.adjust_stock(sku, qty, reason, user=user, mtype=ptype)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"{mov['type']} {sku} {mov['qty']:+d} {mov['before']}→{mov['after']}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Transferencia ──
    def _open_transfer_dialog(self):
        if not self._require_write():
            return
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="SKU *"), mode="outlined")
        f_qty = MDTextField(MDTextFieldLeadingIcon(icon="warehouse"), MDTextFieldHintText(text="Cantidad *"), mode="outlined")
        f_to = MDTextField(MDTextFieldLeadingIcon(icon="map-marker"), MDTextFieldHintText(text="Ubicación destino * (ej B2-E3)"), MDTextFieldHelperText(text="Pasillo-Estante", mode="persistent"), mode="outlined")
        f_reason = MDTextField(MDTextFieldLeadingIcon(icon="comment-text"), MDTextFieldHintText(text="Motivo *"), mode="outlined")
        self._fields = {"sku": f_sku, "qty": f_qty, "to": f_to, "reason": f_reason}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_sku, f_qty, f_to, f_reason]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Transferencia entre almacenes"),
            MDDialogSupportingText(text="Sucursal/Pasillo origen → destino"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Transferir"), style="filled", on_release=lambda x: self._do_transfer()),
                spacing="8dp",
            ),
            size_hint=(0.92, None),
        )
        self.dialog.open()

    def _do_transfer(self):
        sku = self._fields["sku"].text.strip()
        qty = self._fields["qty"].text.strip()
        to = self._fields["to"].text.strip()
        reason = self._fields["reason"].text.strip()
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        try:
            mov = repo.transfer_stock(sku, qty, to, reason, user=user)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Transferencia {sku} x{qty} → {to}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
