"""
CxP §9 — Facturas pendientes, programación pagos, pagos parciales, descuento pronto pago
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


class PayablesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "payables"
        self.dialog = None
        self._fields = {}
        self.table = None
        self.search_field = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        pay = repo.list_payables()
        total = sum(p.get("balance", p["amount"]) for p in pay)
        kpi = MDGridLayout(cols=3, spacing="12dp", adaptive_height=True, size_hint_x=1, padding="12dp")
        for title, val, color in [
            ("Deuda proveedores", f"${total:,.0f}", "#F44336"),
            ("Facturas pendientes", str(len(pay)), "#FF9800"),
            ("Con pronto pago", str(sum(1 for p in pay if p.get("discount_early",0)>0)), "#4CAF50"),
        ]:
            kpi.add_widget(MDCard(MDLabel(text=title, font_style="Title", role="small", halign="center", adaptive_height=True), MDLabel(text=val, font_style="Headline", role="small", halign="center", theme_text_color="Custom", text_color=color, adaptive_height=True), orientation="vertical", padding="12dp", size_hint_y=None, height="80dp", style="elevated"))

        self.table = MDDataTable(
            size_hint=(1, None), height="380dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1100,
                ("Folio", 1),
                ("Proveedor", 2.2),
                ("Vence", 1.2),
                ("Monto", 1.2),
                ("Saldo", 1.2),
                ("DescPP", 0.9),
                ("Estado", 1.1),
            ),
            row_data=[(p["id"], p["supplier"][:14], p["due"], f"${p['amount']:.0f}", f"${p.get('balance', p['amount']):.0f}", f"{p.get('discount_early',0)}%", p["status"]) for p in pay],
        )
        self.search_field = MDTextField(MDTextFieldLeadingIcon(icon="magnify"), MDTextFieldHintText(text="Buscar proveedor / folio..."), mode="outlined", size_hint_x=1)
        self.search_field.bind(text=self.on_search)
        btn_row = action_bar(
            MDButton(MDButtonText(text="Pagar"), style="filled", on_release=lambda x: self._open_pago()),
            MDButton(MDButtonText(text="Programar"), style="outlined", on_release=lambda x: self._open_programar()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
        )
        inner = MDBoxLayout(
            MDLabel(text="Cuentas por Pagar", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Programación pagos, parciales, pronto pago 2% si paga antes de vencimiento", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            kpi, self.search_field, btn_row, self.table,
            MDCard(MDLabel(text="Pagar: ingrese folio OC y monto ≤ saldo — si vence antes de due y tiene descuento, se aplica automático y se loguea", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True), orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="48dp"),
            orientation="vertical", adaptive_height=True, spacing="10dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Cuentas por Pagar"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self): self._build_ui()
    def on_enter(self, *a): self.refresh()
    def on_search(self, inst, val):
        q=val.strip().lower()
        filt=[p for p in repo.list_payables() if q in p["id"].lower() or q in p["supplier"].lower()]
        if self.table:
            self.table.row_data=[(p["id"], p["supplier"][:14], p["due"], f"${p['amount']:.0f}", f"${p.get('balance', p['amount']):.0f}", f"{p.get('discount_early',0)}%", p["status"]) for p in filt]

    def _require_write(self):
        app=MDApp.get_running_app()
        role=app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Contador","Almacén"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede pagar"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    def _open_pago(self):
        if not self._require_write(): return
        f_id=MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="Folio OC *"), mode="outlined")
        f_amt=MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Monto * ≤ saldo"), mode="outlined")
        f_method=MDTextField(MDTextFieldLeadingIcon(icon="bank-transfer"), MDTextFieldHintText(text="Método Transferencia/Efectivo"), mode="outlined", text="Transferencia")
        self._fields={"id":f_id,"amt":f_amt,"method":f_method}
        from kivymd.uix.gridlayout import MDGridLayout
        grid=MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id,f_amt,f_method]: grid.add_widget(w)
        self.dialog=MDDialog(MDDialogHeadlineText(text="Pago a proveedor"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Pagar"), style="filled", on_release=lambda x: self._do_pago()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_pago(self):
        try:
            pay, disc = repo.add_cxp_payment(self._fields["id"].text.strip(), self._fields["amt"].text.strip(), self._fields["method"].text.strip() or "Transferencia", user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            msg=f"Pagado ${self._fields['amt'].text.strip()} a {pay['id']} saldo ${pay.get('balance',0):.0f}"
            if disc>0:
                msg+=f" Desc PP ${disc:.0f} (2%)"
            MDSnackbar(MDSnackbarText(text=msg), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _open_programar(self):
        f_id=MDTextField(MDTextFieldLeadingIcon(icon="calendar"), MDTextFieldHintText(text="Folio OC *"), mode="outlined")
        f_date=MDTextField(MDTextFieldLeadingIcon(icon="calendar-clock"), MDTextFieldHintText(text="Nueva fecha vencimiento YYYY-MM-DD *"), MDTextFieldHelperText(text="Ej 2026-09-30", mode="persistent"), mode="outlined")
        self._fields={"id":f_id,"date":f_date}
        from kivymd.uix.gridlayout import MDGridLayout
        grid=MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id,f_date]: grid.add_widget(w)
        self.dialog=MDDialog(MDDialogHeadlineText(text="Programar pago"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Programar"), style="filled", on_release=lambda x: self._do_programar()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_programar(self):
        folio=self._fields["id"].text.strip()
        date=self._fields["date"].text.strip()
        pay=repo.find_purchase(folio) or next((p for p in repo.list_payables() if p["id"]==folio), None)
        if not pay:
            MDSnackbar(MDSnackbarText(text="Folio no encontrado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        # buscar en PAYABLES
        rec=next((p for p in repo.list_payables() if p["id"]==folio), None)
        if not rec:
            MDSnackbar(MDSnackbarText(text="CxP no encontrada (quizá ya pagada)"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        rec["due"]=date
        repo.log(MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema", "cxp_programar", f"{folio} -> {date}")
        self.dialog.dismiss()
        MDSnackbar(MDSnackbarText(text=f"Pago {folio} programado al {date}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
        self.refresh()
