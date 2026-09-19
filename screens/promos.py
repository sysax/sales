"""
Promociones y Descuentos §12 — 2x1, 3x2, % , monto fijo, volumen, cupón, happy hour
CRUD + activación + aplicación en POS vía repo.apply_promo
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


class PromosScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "promos"
        self.dialog = None
        self._fields = {}
        self.table = None
        self.search_field = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        promos = repo.list_promoss()
        self.table = MDDataTable(
            size_hint=(1, None), height="380dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1050,
                ("ID", 0.5),
                ("Nombre", 2.4),
                ("Tipo", 1.4),
                ("Valor", 1),
                ("Condición", 1.8),
                ("Código", 1.2),
                ("Activa", 0.9),
            ),
            row_data=[(str(p["id"]), p["name"][:18], p["type"], str(p["value"]), p.get("condition","")[:14], p.get("code",""), "Sí" if p["active"] else "No") for p in promos],
        )
        self.search_field = MDTextField(MDTextFieldLeadingIcon(icon="magnify"), MDTextFieldHintText(text="Buscar nombre / tipo / código..."), mode="outlined", size_hint_x=1)
        self.search_field.bind(text=self.on_search)
        btn_row = action_bar(
            MDButton(MDButtonText(text="Nueva"), style="filled", on_release=lambda x: self._open_add()),
            MDButton(MDButtonText(text="Editar"), style="outlined", on_release=lambda x: self._open_edit()),
            MDButton(MDButtonText(text="Activar/Desactivar"), style="text", on_release=lambda x: self._toggle()),
            MDButton(MDButtonText(text="Eliminar"), style="text", on_release=lambda x: self._open_delete()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
        )
        inner = MDBoxLayout(
            MDLabel(text="Promociones Colombia — COP", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Genérico abarrotes/electrónica: porcentaje (10% Electrónica), monto_fijo ($50k COP > $500k), 2x1 (P005), 3x2 (Accesorios), volumen 10+ 5%, ABAR10 10% Abarrotes — aplica en POS por código DIAN", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            self.search_field, btn_row, self.table,
            MDCard(MDLabel(text="Códigos activos Colombia: 2X1AUD, ELEC10, 50KOFF, VOL5, ABAR10 — pruébalos en POS — COP", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True), orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="48dp"),
            orientation="vertical", adaptive_height=True, spacing="10dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Promociones"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self): self._build_ui()
    def on_enter(self, *a): self.refresh()
    def on_search(self, inst, val):
        q=val.strip().lower()
        filt=[p for p in repo.list_promoss() if q in p["name"].lower() or q in p["type"].lower() or q in p.get("code","").lower()]
        if self.table:
            self.table.row_data=[(str(p["id"]), p["name"][:18], p["type"], str(p["value"]), p.get("condition","")[:14], p.get("code",""), "Sí" if p["active"] else "No") for p in filt]

    def _require_write(self):
        app=MDApp.get_running_app()
        role=app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Vendedor"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede gestionar promos"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    def _open_add(self):
        if not self._require_write(): return
        f_name=MDTextField(MDTextFieldLeadingIcon(icon="tag"), MDTextFieldHintText(text="Nombre * ej 15% Volumen"), mode="outlined")
        f_type=MDTextField(MDTextFieldLeadingIcon(icon="shape"), MDTextFieldHintText(text="Tipo * porcentaje/monto_fijo/2x1/3x2/volumen/cupon"), MDTextFieldHelperText(text="Ver tipos abajo", mode="persistent"), mode="outlined")
        f_value=MDTextField(MDTextFieldLeadingIcon(icon="percent"), MDTextFieldHintText(text="Valor * (10 para 10% o 500)"), mode="outlined")
        f_cond=MDTextField(MDTextFieldLeadingIcon(icon="filter"), MDTextFieldHintText(text="Condición (categoria/sku/min)"), MDTextFieldHelperText(text="Ej Electronica / P005 / min 5000 / qty>=10", mode="persistent"), mode="outlined")
        f_code=MDTextField(MDTextFieldLeadingIcon(icon="barcode"), MDTextFieldHintText(text="Código * (ej VOL15)"), mode="outlined")
        self._fields={"name":f_name,"type":f_type,"value":f_value,"condition":f_cond,"code":f_code}
        from kivymd.uix.gridlayout import MDGridLayout
        grid=MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_name,f_type,f_value,f_cond,f_code]: grid.add_widget(w)
        self.dialog=MDDialog(MDDialogHeadlineText(text="Nueva promoción"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Crear"), style="filled", on_release=lambda x: self._do_add()), spacing="8dp"), size_hint=(0.95, None))
        self.dialog.open()
    def _do_add(self):
        try:
            data={k: v.text.strip() for k,v in self._fields.items()}
            # value numeric
            promo=repo.add_promo({"name":data["name"],"type":data["type"].lower(),"value":data["value"] or 0,"condition":data["condition"],"code":data["code"] or f"PROMO{len(repo.list_promoss())+1}","active":True,"desc":data["name"]})
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Promo {promo['code']} creada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _open_edit(self):
        if not self._require_write(): return
        f_id=MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="ID *"), mode="outlined")
        f_val=MDTextField(MDTextFieldLeadingIcon(icon="percent"), MDTextFieldHintText(text="Nuevo valor (deje vacío no cambia)"), mode="outlined")
        f_cond=MDTextField(MDTextFieldLeadingIcon(icon="filter"), MDTextFieldHintText(text="Nueva condición"), mode="outlined")
        self._fields={"id":f_id,"value":f_val,"condition":f_cond}
        from kivymd.uix.gridlayout import MDGridLayout
        grid=MDGridLayout(cols=1, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_id,f_val,f_cond]: grid.add_widget(w)
        self.dialog=MDDialog(MDDialogHeadlineText(text="Editar promo"), grid, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Guardar"), style="filled", on_release=lambda x: self._do_edit()), spacing="8dp"), size_hint=(0.9, None))
        self.dialog.open()
    def _do_edit(self):
        try:
            pid=int(self._fields["id"].text.strip())
            updates={}
            if self._fields["value"].text.strip(): updates["value"]=self._fields["value"].text.strip()
            if self._fields["condition"].text.strip(): updates["condition"]=self._fields["condition"].text.strip()
            repo.update_promo(pid, updates)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Promo {pid} actualizada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _toggle(self):
        if not self._require_write(): return
        f_id=MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="ID a toggle *"), mode="outlined")
        self._fields={"id":f_id}
        self.dialog=MDDialog(MDDialogHeadlineText(text="Activar/Desactivar"), f_id, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Toggle"), style="filled", on_release=lambda x: self._do_toggle()), spacing="8dp"))
        self.dialog.open()
    def _do_toggle(self):
        try:
            pid=int(self._fields["id"].text.strip())
            pr=next((p for p in repo.list_promoss() if p["id"]==pid), None)
            if not pr: raise ValueError("No encontrado")
            repo.update_promo(pid, {"active": not pr["active"]})
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Promo {pid} {'Activa' if not pr['active'] else 'Inactiva'}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def _open_delete(self):
        if not self._require_write(): return
        f_id=MDTextField(MDTextFieldLeadingIcon(icon="delete"), MDTextFieldHintText(text="ID a eliminar *"), mode="outlined")
        self._fields={"id":f_id}
        self.dialog=MDDialog(MDDialogHeadlineText(text="Eliminar promo"), f_id, MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Eliminar"), style="filled", on_release=lambda x: self._do_delete()), spacing="8dp"))
        self.dialog.open()
    def _do_delete(self):
        try:
            pid=int(self._fields["id"].text.strip())
            repo.delete_promo(pid)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Promo {pid} eliminada"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
