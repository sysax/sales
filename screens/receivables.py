"""
CxC §8 — Saldos por cliente, anticipos, estados cuenta, recordatorios vencimiento, intereses moratorios
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


class ReceivablesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "receivables"
        self.dialog = None
        self._fields = {}
        self.table = None
        self.search_field = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        rec = repo.list_receivables()
        total_debt = sum(s.get("balance",0) for s in rec)
        vencidas = sum(1 for s in rec if repo.calculate_mora(s) > 0)
        # KPIs
        kpi = MDGridLayout(cols=3, spacing="12dp", adaptive_height=True, size_hint_x=1, padding="12dp")
        for title, val, color in [
            ("Deuda total", f"${total_debt:,.0f}", "#F44336"),  # ERROR_BG
            ("Cuentas pendientes", str(len(rec)), "#FFC107"),  # WARNING_BG
            ("Vencidas mora>0", str(vencidas), "#00796b"),  # Púrpura
        ]:
            kpi.add_widget(MDCard(MDLabel(text=title, font_style="Title", role="small", halign="center", adaptive_height=True), MDLabel(text=val, font_style="Headline", role="small", halign="center", theme_text_color="Custom", text_color=color, adaptive_height=True), orientation="vertical", padding="12dp", size_hint_y=None, height="80dp", style="elevated"))

        self.table = MDDataTable(
            size_hint=(1, None), height="380dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1150,
                ("Folio", 1),
                ("Fecha", 1.2),
                ("Cliente", 2),
                ("Total", 1.2),
                ("Saldo", 1.2),
                ("Vence", 1.2),
                ("Mora", 1),
                ("Estado", 1.1),
            ),
            row_data=[
                (s["id"], s["date"], s["client"][:12], f"${s['total']:.0f}", f"${s.get('balance',0):.0f}", s.get("due",""), f"${repo.calculate_mora(s):.0f}", s.get("estado", s["status"]))
                for s in rec
            ],
        )
        self.search_field = MDTextField(MDTextFieldLeadingIcon(icon="magnify"), MDTextFieldHintText(text="Buscar cliente / folio..."), mode="outlined", size_hint_x=1)
        self.search_field.bind(text=self.on_search)
        btn_row = action_bar(
            MDButton(MDButtonText(text="Abonar"), style="filled", on_release=lambda x: self._open_abono()),
            MDButton(MDButtonText(text="Estado Cuenta"), style="outlined", on_release=lambda x: self._open_estado()),
            MDButton(MDButtonText(text="Recordatorio"), style="text", on_release=lambda x: self._send_reminder()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
        )
        inner = MDBoxLayout(
            MDLabel(text="Cuentas por Cobrar", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Anticipos, abonos parciales, intereses moratorios 2% mensual si vencida, saldo por cliente", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            kpi, self.search_field, btn_row, self.table,
            MDCard(MDLabel(text="Doble click Abonar para registrar pago parcial — si saldo 0 pasa a Pagada y descuenta crédito cliente", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True), orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="48dp"),
            orientation="vertical", adaptive_height=True, spacing="10dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Cuentas por Cobrar"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *a):
        self.refresh()
    def on_search(self, inst, val):
        q = val.strip().lower()
        filt = [s for s in repo.list_receivables() if q in s["id"].lower() or q in s["client"].lower()]
        if self.table:
            self.table.row_data = [(s["id"], s["date"], s["client"][:12], f"${s['total']:.0f}", f"${s.get('balance',0):.0f}", s.get("due",""), f"${repo.calculate_mora(s):.0f}", s.get("estado", s["status"])) for s in filt]

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Contador","Cajero"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede cobrar"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    def _open_abono(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="Folio Venta * (ej V003)"), mode="outlined")
        f_amt = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Monto abono *"), MDTextFieldHelperText(text="<= saldo", mode="persistent"), mode="outlined")
        f_method = MDTextField(MDTextFieldLeadingIcon(icon="credit-card"), MDTextFieldHintText(text="Método Efectivo/Tarjeta/Transferencia"), mode="outlined", text="Efectivo")
        self._fields = {"id": f_id, "amt": f_amt, "method": f_method}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id, f_amt, f_method]:
            grid.add_widget(w)
        self.dialog = MDDialog(MDDialogHeadlineText(text="Registrar abono CxC"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Abonar"), style="filled", on_release=lambda x: self._do_abono()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_abono(self):
        try:
            sale = repo.add_cxc_payment(self._fields["id"].text.strip(), self._fields["amt"].text.strip(), self._fields["method"].text.strip() or "Efectivo", user=MDApp.get_running_app().current_user.get("username","sistema") if MDApp.get_running_app().current_user else "sistema")
            self.dialog.dismiss()
            mora = repo.calculate_mora(sale)
            MDSnackbar(MDSnackbarText(text=f"Abonado {self._fields['amt'].text.strip()} a {sale['id']} saldo ${sale.get('balance',0):.0f} mora ${mora:.0f}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _open_estado(self):
        f_client = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Cliente * (ej Carlos Ruiz)"), mode="outlined")
        self._fields = {"client": f_client}
        self.dialog = MDDialog(MDDialogHeadlineText(text="Estado de cuenta"), f_client, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cerrar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Ver"), style="filled", on_release=lambda x: self._do_estado()), spacing="8dp"))
        self.dialog.open()
    def _do_estado(self):
        name = self._fields["client"].text.strip()
        stmt = repo.get_client_statement(name)
        if not stmt["sales"]:
            MDSnackbar(MDSnackbarText(text="Cliente no encontrado o sin ventas"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        self.dialog.dismiss()
        detail = "\n".join([f"{s['id']} {s['date']} ${s['total']:.0f} pag ${s.get('paid',0):.0f} sal ${s.get('balance',0):.0f} {s.get('estado','')}" for s in stmt["sales"][:6]])
        self.dialog = MDDialog(MDDialogHeadlineText(text=f"Estado {name}"), MDDialogSupportingText(text=f"Deuda ${stmt['debt']:.0f} Pagado ${stmt['paid']:.0f}\n{detail}"), MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.dialog.dismiss()), spacing="8dp"))
        self.dialog.open()

    def _send_reminder(self):
        rec = repo.list_receivables()
        vencidas = [s for s in rec if repo.calculate_mora(s)>0]
        if not vencidas:
            MDSnackbar(MDSnackbarText(text="No hay vencidas para recordar"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        txt = "\n".join([f"{s['id']} {s['client']} vence {s.get('due','')} mora ${repo.calculate_mora(s):.0f}" for s in vencidas[:5]])
        self.dialog = MDDialog(MDDialogHeadlineText(text=f"Recordatorios vencimiento ({len(vencidas)})"), MDDialogSupportingText(text=txt), MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Enviar (simulado)"), style="filled", on_release=lambda x: (self.dialog.dismiss(), MDSnackbar(MDSnackbarText(text=f"Recordatorios enviados a {len(vencidas)} clientes"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open())), spacing="8dp"))
        self.dialog.open()
