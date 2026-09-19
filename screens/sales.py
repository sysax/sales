"""
Ventas y Facturación Colombia DIAN §7 — Factura electrónica DIAN + CUFE
Doc: Cotización/Pedido/Remisión/Factura electrónica/Nota crédito/cargo — Estados 6 — genérico comercio
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


class SalesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "sales"
        self.dialog = None
        self._fields = {}
        self.search_field = None
        self.table = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        sales = repo.list_sales()
        # KPIs
        summary = repo.get_sales_summary()
        # contar por estado extendido
        cnt_status = {}
        for s in sales:
            cnt_status[s.get("estado", s["status"])] = cnt_status.get(s.get("estado", s["status"]), 0) + 1
        kpi = MDGridLayout(cols=4, spacing="12dp", adaptive_height=True, size_hint_x=1, padding="12dp")
        for st in ["Cotización","Pedido","Facturada","Pagada","Entregada","Cancelada"]:
            col = "#2196F3" if st in ("Cotización","Pedido") else "#4CAF50" if st=="Pagada" else "#9C27B0" if st=="Facturada" else "#FF9800" if st=="Entregada" else "#F44336"
            kpi.add_widget(MDCard(
                MDLabel(text=st, font_style="Title", role="small", halign="center", adaptive_height=True),
                MDLabel(text=str(cnt_status.get(st,0)), font_style="Headline", role="small", halign="center", theme_text_color="Custom", text_color=col, adaptive_height=True),
                orientation="vertical", padding="12dp", size_hint_y=None, height="80dp", style="elevated",
            ))

        self.table = MDDataTable(
            size_hint=(1, None), height="380dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1200,
                ("Folio", 1.1),
                ("Fecha", 1.3),
                ("Cliente", 2.2),
                ("Doc", 1.1),
                ("Estado", 1.3),
                ("Total", 1.4),
                ("Saldo", 1.3),
                ("Pago", 1.5),
            ),
            row_data=[
                (s["id"], s["date"], s["client"][:16], s.get("doc_type","Factura")[:9], s.get("estado", s["status"])[:11], f"${s['total']:,.0f}", f"${s.get('balance',0):,.0f}", (s.get("payment","")[:16] or "-"))
                for s in sales
            ],
        )
        self.search_field = MDTextField(MDTextFieldLeadingIcon(icon="magnify"), MDTextFieldHintText(text="Buscar folio / cliente / doc..."), mode="outlined", size_hint_x=1)
        self.search_field.bind(text=self.on_search)

        btn_row = action_bar(
            MDButton(MDButtonText(text="Nuevo Doc"), style="filled", on_release=lambda x: self._open_new_doc()),
            MDButton(MDButtonText(text="Avanzar Estado"), style="outlined", on_release=lambda x: self._open_advance()),
            MDButton(MDButtonText(text="Facturar"), style="outlined", on_release=lambda x: self._open_facturar()),
            MDButton(MDButtonText(text="Nota Crédito"), style="text", on_release=lambda x: self._open_credito()),
            MDButton(MDButtonText(text="Nota Cargo"), style="text", on_release=lambda x: self._open_cargo()),
            MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self._open_cancel()),
        )
        btn_row2 = action_bar(
            MDButton(MDButtonText(text="Ver Detalle"), style="text", on_release=lambda x: self._open_detail()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
            MDButton(MDButtonText(text=self._dian_toggle_label()), style="outlined", on_release=lambda x: self._toggle_dian()),
        )
        try:
            from data import dian as dian_mod
            dian_on = dian_mod.is_enabled()
        except Exception:
            dian_on = False
        subtitle = "Colombia DIAN §7: Cotización → Pedido → Remisión → Factura electrónica (CUFE) → Nota crédito/cargo — Estados 6 — NIT" if dian_on else "Cotización → Pedido → Remisión → Factura interna → Nota crédito/cargo — Estados 6 — NIT — DIAN desactivado (documentos sin validez fiscal)"
        flujo = "Flujo Colombia: Cotización (no reserva) → Pedido (reserva) → Facturada DIAN (CUFE) → Pagada → Entregada → Cerrada — COP" if dian_on else "Flujo: Cotización (no reserva) → Pedido (reserva) → Facturada (interna) → Pagada → Entregada → Cerrada — COP — active DIAN en este botón cuando la necesite"
        inner = MDBoxLayout(
            MDLabel(text="Ventas y Facturación", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text=subtitle, font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            kpi,
            self.search_field,
            btn_row,
            btn_row2,
            self.table,
            MDCard(MDLabel(text=flujo, font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True), orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="48dp"),
            orientation="vertical", adaptive_height=True, spacing="10dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Ventas"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *a):
        self.refresh()
    def on_search(self, inst, val):
        q = val.strip().lower()
        filt = [s for s in repo.list_sales() if q in s["id"].lower() or q in s["client"].lower() or q in s.get("doc_type","").lower() or q in s.get("estado","").lower()]
        if self.table:
            self.table.row_data = [(s["id"], s["date"], s["client"][:12], s.get("doc_type","Factura")[:7], s.get("estado", s["status"])[:9], f"${s['total']:,.0f}", f"${s.get('balance',0):,.0f}", (s.get("payment","")[:12] or "-")) for s in filt]

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Vendedor","Cajero"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede modificar ventas"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    # Nuevo documento
    def _open_new_doc(self):
        if not self._require_write():
            return
        f_type = MDTextField(MDTextFieldLeadingIcon(icon="file-document"), MDTextFieldHintText(text="Doc * Cotización/Pedido/Remisión/Factura"), MDTextFieldHelperText(text="Escribir exacto", mode="persistent"), mode="outlined")
        f_client = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Cliente *"), MDTextFieldHelperText(text="Ej Juan Perez", mode="persistent"), mode="outlined")
        f_total = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Total *"), MDTextFieldHelperText(text="ej 5000", mode="persistent"), mode="outlined")
        self._fields = {"type": f_type, "client": f_client, "total": f_total}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_type, f_client, f_total]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text="Nuevo documento"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Crear"), style="filled", on_release=lambda x: self._do_new_doc()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_new_doc(self):
        try:
            doc = repo.create_document(self._fields["type"].text.strip(), self._fields["client"].text.strip(), self._fields["total"].text.strip(), user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"{doc['id']} {doc['doc_type']} creado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # Avanzar estado
    def _open_advance(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="Folio *"), mode="outlined")
        f_new = MDTextField(MDTextFieldLeadingIcon(icon="arrow-right"), MDTextFieldHintText(text="Nuevo estado * (Pedido/Facturada/Pagada/Entregada/Cerrada)"), mode="outlined")
        self._fields = {"id": f_id, "new": f_new}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id, f_new]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text="Avanzar estado"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Avanzar"), style="filled", on_release=lambda x: self._do_advance()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_advance(self):
        try:
            repo.advance_sale_status(self._fields["id"].text.strip(), self._fields["new"].text.strip(), user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"{self._fields['id'].text.strip()} → {self._fields['new'].text.strip()}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _dian_on(self):
        try:
            from data import dian as dian_mod
            return dian_mod.is_enabled()
        except Exception:
            return False

    def _dian_toggle_label(self):
        return "DIAN: ON" if self._dian_on() else "DIAN: OFF"

    def _toggle_dian(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role", "") if app.current_user else ""
        if role != "Administrador":
            MDSnackbar(MDSnackbarText(text="Solo Administrador puede activar DIAN"), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.7).open()
            return
        try:
            from data import dian as dian_mod
            dian_mod.set_enabled(not dian_mod.is_enabled(), user=app.current_user.get("username", "sistema"))
        except Exception as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()
            return
        self.refresh()
        MDSnackbar(MDSnackbarText(text=self._dian_toggle_label() + (" — facturación electrónica simulada" if self._dian_on() else " — documentos internos")), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.7).open()

    def _open_facturar(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="file-document"), MDTextFieldHintText(text="Folio Pedido/Cotización *"), mode="outlined")
        self._fields = {"id": f_id}
        if self._dian_on():
            title, body, btn = "Facturar (DIAN simulado)", "Convierte Pedido/Cotización a Factura electrónica DIAN + genera CUFE/XML (simulado) — Colombia COP", "Facturar DIAN"
        else:
            title, body, btn = "Facturar (interna)", "Convierte Pedido/Cotización a Factura interna — sin validez fiscal DIAN. Active DIAN arriba cuando la necesite.", "Facturar"
        self.dialog = MDDialog(MDDialogHeadlineText(text=title), MDDialogSupportingText(text=body), f_id, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text=btn), style="filled", on_release=lambda x: self._do_facturar()), spacing="8dp"))
        self.dialog.open()
    def _do_facturar(self):
        try:
            repo.advance_sale_status(self._fields["id"].text.strip(), "Facturada", user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            msg = f"{self._fields['id'].text.strip()} Facturada DIAN CUFE OK — COP" if self._dian_on() else f"{self._fields['id'].text.strip()} Facturada (interna) — COP"
            MDSnackbar(MDSnackbarText(text=msg), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # Nota crédito/cargo
    def _open_credito(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="Folio venta *"), mode="outlined")
        f_amt = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Monto *"), mode="outlined")
        f_reason = MDTextField(MDTextFieldLeadingIcon(icon="comment-text"), MDTextFieldHintText(text="Motivo devolución *"), mode="outlined")
        self._fields = {"id": f_id, "amt": f_amt, "reason": f_reason}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id, f_amt, f_reason]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text="Nota de crédito (devolución)"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Generar NC"), style="filled", on_release=lambda x: self._do_credito()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_credito(self):
        try:
            note = repo.create_credit_note(self._fields["id"].text.strip(), self._fields["amt"].text.strip(), self._fields["reason"].text.strip(), user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"NC {note['id']} ${note['total']:.0f} ref {self._fields['id'].text.strip()}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
    def _open_cargo(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="Folio venta *"), mode="outlined")
        f_amt = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Monto ajuste *"), mode="outlined")
        f_reason = MDTextField(MDTextFieldLeadingIcon(icon="comment-text"), MDTextFieldHintText(text="Motivo cargo *"), mode="outlined")
        self._fields = {"id": f_id, "amt": f_amt, "reason": f_reason}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id, f_amt, f_reason]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text="Nota de cargo (ajuste)"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Generar NCargo"), style="filled", on_release=lambda x: self._do_cargo()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_cargo(self):
        try:
            note = repo.create_debit_note(self._fields["id"].text.strip(), self._fields["amt"].text.strip(), self._fields["reason"].text.strip(), user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"N Cargo {note['id']} ${note['total']:.0f}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
    def _open_cancel(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="cancel"), MDTextFieldHintText(text="Folio a cancelar *"), mode="outlined")
        self._fields = {"id": f_id}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Cancelar venta/documento"), f_id, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cerrar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Cancelar"), style="filled", on_release=lambda x: self._do_cancel()), spacing="8dp"))
        self.dialog.open()
    def _do_cancel(self):
        try:
            repo.advance_sale_status(self._fields["id"].text.strip(), "Cancelada", user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"{self._fields['id'].text.strip()} Cancelada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
    def _open_detail(self):
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="Folio *"), mode="outlined")
        self._fields = {"id": f_id}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Detalle venta"), f_id, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cerrar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Ver"), style="filled", on_release=lambda x: self._do_detail()), spacing="8dp"))
        self.dialog.open()
    def _do_detail(self):
        s = repo.find_sale(self._fields["id"].text.strip())
        if not s:
            MDSnackbar(MDSnackbarText(text="No encontrado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()
            return
        self.dialog.dismiss()
        cufe_line = f" CUFE:{s.get('dian_cufe','CUFE-'+s['id'])}" if self._dian_on() else ""
        fiscal_note = "" if self._dian_on() else " — documento interno sin validez fiscal"
        self.dialog = MDDialog(
            MDDialogHeadlineText(text=f"{s['id']} {s.get('doc_type','Factura')} {s.get('estado', s['status'])}"),
            MDDialogSupportingText(text=f"Cliente: {s['client']} NIT\nFecha: {s['date']} Doc: {s.get('doc_type','Factura')}{cufe_line}\nTotal ${s['total']:,.0f} COP Desc ${s.get('discount',0):,.0f} IVA 19% ${s.get('tax',0):,.0f} COP\nPagado ${s.get('paid',0):,.0f} Saldo ${s.get('balance',0):,.0f} COP Vence {s.get('due','')}\nPago: {s.get('payment','')} Promo:{s.get('promo','-')} — Comercio genérico{fiscal_note}"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.dialog.dismiss()), spacing="8dp"),
        )
        self.dialog.open()
