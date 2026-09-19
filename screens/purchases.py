"""
Pantalla de Compras §11 — Reabastecimiento
Flujo: stock bajo detectado → orden → enviar proveedor → recibir mercancía (valida vs orden) → actualiza inventario → registra CxP
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


class PurchasesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "purchases"
        self.dialog = None
        self._fields = {}
        self.search_field = None
        self.table = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        purchases = repo.list_purchases()
        # KPIs flujo
        pending = sum(1 for p in purchases if p["status"] == "Pendiente")
        transit = sum(1 for p in purchases if p["status"] == "En tránsito")
        received = sum(1 for p in purchases if p["status"] == "Recibida")
        low = repo.low_stock_products(10)
        kpi = MDGridLayout(cols=4, spacing="12dp", adaptive_height=True, size_hint_x=1, padding="12dp")
        for title, val, color in [
            ("Pendiente", str(pending), "#FF9800"),
            ("En tránsito", str(transit), "#2196F3"),
            ("Recibida", str(received), "#4CAF50"),
            (f"Stock bajo {len(low)}", ", ".join([p["sku"] for p in low[:2]]) or "OK", "#F44336" if low else "#4CAF50"),
        ]:
            kpi.add_widget(MDCard(
                MDLabel(text=title, font_style="Title", role="small", adaptive_height=True, halign="center"),
                MDLabel(text=val, font_style="Headline", role="small", halign="center", theme_text_color="Custom", text_color=color, adaptive_height=True),
                orientation="vertical", padding="12dp", size_hint_y=None, height="90dp", style="elevated",
            ))

        self.table = MDDataTable(
            size_hint=(1, None), height="340dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1000,
                ("Folio", 1),
                ("Fecha", 1.2),
                ("Proveedor", 2.2),
                ("Total", 1.2),
                ("Estado", 1.2),
                ("Items", 2),
            ),
            row_data=[
                (
                    p["id"], p["date"], p["supplier"][:14], f"${p['total']:,.0f}", p["status"],
                    ", ".join([f"{it['sku']}x{it['qty']}" for it in p.get("items", [])])[:22]
                )
                for p in purchases
            ],
        )
        self.search_field = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar folio / proveedor..."),
            mode="outlined", size_hint_x=1,
        )
        self.search_field.bind(text=self.on_search)

        btn_row = action_bar(
            MDButton(MDButtonText(text="Nueva Orden"), style="filled", on_release=lambda x: self._open_create_dialog()),
            MDButton(MDButtonText(text="Recepción"), style="outlined", on_release=lambda x: self._open_receive_dialog()),
            MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self._open_cancel_dialog()),
            MDButton(MDButtonText(text="Detectar Stock Bajo"), style="outlined", on_release=lambda x: self._detect_low_stock()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
        )

        inner = MDBoxLayout(
            MDLabel(text="Ordenes de Compra", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="1. Sistema detecta stock bajo → 2. Genera orden → 3. Envía proveedor → 4. Recibe (valida vs orden) → 5. Actualiza inventario → 6. Registra CxP", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            kpi,
            self.search_field,
            btn_row,
            self.table,
            MDCard(
                MDLabel(text="Flujo tienda electrónica (fases.md): Distribuidora XYZ → 20 laptops → escaneo almacén → inventario → venta Juan Pérez 3 laptops → factura → ticket → -3 stock → corte caja", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
                orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="56dp",
            ),
            orientation="vertical", adaptive_height=True, spacing="12dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Compras"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *args):
        self.refresh()
    def on_search(self, instance, value):
        q = value.strip().lower()
        filtered = [p for p in repo.list_purchases() if q in p["id"].lower() or q in p["supplier"].lower()]
        if self.table:
            self.table.row_data = [
                (p["id"], p["date"], p["supplier"][:14], f"${p['total']:,.0f}", p["status"], ", ".join([f"{it['sku']}x{it['qty']}" for it in p.get("items", [])])[:22])
                for p in filtered
            ]

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Almacén","Contador"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede gestionar compras"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    # ── Crear orden ──
    def _open_create_dialog(self):
        if not self._require_write():
            return
        suppliers = repo.list_suppliers()
        sup_hint = ", ".join([s["name"] for s in suppliers[:3]])
        f_sup = MDTextField(MDTextFieldLeadingIcon(icon="truck-delivery"), MDTextFieldHintText(text="Proveedor *"), MDTextFieldHelperText(text=f"Ej {sup_hint}", mode="persistent"), mode="outlined")
        f_sku = MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="SKU *"), MDTextFieldHelperText(text="Ej P001 (se valida vs catálogo)", mode="persistent"), mode="outlined")
        f_qty = MDTextField(MDTextFieldLeadingIcon(icon="counter"), MDTextFieldHintText(text="Cantidad *"), MDTextFieldHelperText(text="entero >0", mode="persistent"), mode="outlined")
        self._fields = {"supplier": f_sup, "sku": f_sku, "qty": f_qty}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_sup, f_sku, f_qty]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Nueva orden de compra"),
            MDDialogSupportingText(text="Se calcula total = precio compra × cantidad"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Crear Pendiente"), style="filled", on_release=lambda x: self._do_create()),
                spacing="8dp",
            ),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_create(self):
        sup = self._fields["supplier"].text.strip()
        sku = self._fields["sku"].text.strip()
        qty = self._fields["qty"].text.strip()
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        try:
            po = repo.create_purchase(sup, sku, qty, user=user)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Orden {po['id']} {sup} {sku} x{qty} ${po['total']:,.0f} Pendiente"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Recepción ──
    def _open_receive_dialog(self):
        if not self._require_write():
            return
        f_folio = MDTextField(MDTextFieldLeadingIcon(icon="clipboard-check"), MDTextFieldHintText(text="Folio OC * (ej OC002)"), MDTextFieldHelperText(text="Valida vs orden: proveedor, items, total", mode="persistent"), mode="outlined")
        self._fields = {"folio": f_folio}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Recepción de mercancía"),
            MDDialogSupportingText(text="Valida contra orden, escanea items, actualiza inventario y registra CxP"),
            f_folio,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Recepcionar"), style="filled", on_release=lambda x: self._do_receive()),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def _do_receive(self):
        folio = self._fields["folio"].text.strip().upper()
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        try:
            po = repo.receive_purchase(folio, user=user)
            self.dialog.dismiss()
            # Mostrar resumen
            items_str = ", ".join([f"{it['sku']} x{it['qty']}" for it in po.get("items", [])])
            MDSnackbar(MDSnackbarText(text=f"{folio} Recibida {items_str} → stock actualizado + CxP registrada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.9).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Cancelar ──
    def _open_cancel_dialog(self):
        if not self._require_write():
            return
        f_folio = MDTextField(MDTextFieldLeadingIcon(icon="cancel"), MDTextFieldHintText(text="Folio OC a cancelar *"), mode="outlined")
        self._fields = {"folio": f_folio}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Cancelar orden"),
            f_folio,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cerrar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Cancelar OC"), style="filled", on_release=lambda x: self._do_cancel()),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def _do_cancel(self):
        folio = self._fields["folio"].text.strip().upper()
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        try:
            repo.cancel_purchase(folio, user=user)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Orden {folio} Cancelada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Detección stock bajo §11 paso 1 ──
    def _detect_low_stock(self):
        low = repo.low_stock_products(10)
        # también detectar con stock_min personalizado
        alerts = repo.get_inventory_alerts()
        low2 = alerts["low"]
        # unir
        combined = {p["sku"]: p for p in low + low2}.values()
        if not combined:
            MDSnackbar(MDSnackbarText(text="No hay stock bajo — inventario OK"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        # Dialogo que lista y ofrece crear órdenes
        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.label import MDLabel
        content = MDBoxLayout(orientation="vertical", adaptive_height=True, spacing="4dp", padding="8dp")
        for p in list(combined)[:6]:
            need = max(1, p.get("stock_max",20) - p["stock"])
            content.add_widget(MDLabel(text=f"{p['sku']} {p['name'][:14]} stock {p['stock']}/{p.get('stock_min',5)} → pedir {need} a {p.get('supplier','')}", font_style="Body", role="small", adaptive_height=True))
        if len(list(combined)) > 6:
            content.add_widget(MDLabel(text=f"... y {len(list(combined))-6} más", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True))
        self.dialog = MDDialog(
            MDDialogHeadlineText(text=f"Stock bajo detectado: {len(list(combined))} productos"),
            MDDialogSupportingText(text="¿Generar órdenes pendientes automáticamente (qty = max - actual)?"),
            content,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cerrar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text=f"Generar {len(list(combined))} órdenes"), style="filled", on_release=lambda x: self._do_generate_low_orders(list(combined))),
                spacing="8dp",
            ),
            size_hint=(0.95, None),
        )
        self.dialog.open()

    def _do_generate_low_orders(self, products):
        app = MDApp.get_running_app()
        user = app.current_user.get("username","sistema") if app.current_user else "sistema"
        count = 0
        for p in products:
            qty = max(1, p.get("stock_max",20) - p["stock"])
            try:
                repo.create_purchase(p.get("supplier","Distribuidora XYZ"), p["sku"], qty, user=user)
                count += 1
            except Exception:
                continue
        self.dialog.dismiss()
        MDSnackbar(MDSnackbarText(text=f"Generadas {count} órdenes por stock bajo"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
        self.refresh()
