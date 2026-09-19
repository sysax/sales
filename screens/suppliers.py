"""
Proveedores Colombia NIT — abarrotes/electrónica genérico — DIAN
KivyMD 2.0.1
"""
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
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


class SuppliersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "suppliers"
        self.dialog = None
        self._fields = {}
        self.search_field = None
        self.table = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        suppliers = repo.list_suppliers()
        self.table = MDDataTable(
            size_hint=(1, None),
            height="340dp",
            use_pagination=True,
            rows_num=8,
            column_data=flex_columns(1100,
                ("ID", 0.6),
                ("Empresa", 2.4),
                ("NIT", 1.5),
                ("Contacto", 1.9),
                ("Telefono", 1.4),
                ("Ciudad", 1.3),
                ("Entrega", 1.3),
            ),
            row_data=[
                (str(s["id"]), s["name"][:18], s.get("nit", s.get("rfc",""))[:14], s["contact"][:18], s["phone"][:12], s["city"][:12], s.get("lead_time","")[:12])
                for s in suppliers
            ],
        )
        self.search_field = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar empresa / NIT / contacto — Colombia"),
            mode="outlined",
            size_hint_x=1,
        )
        self.search_field.bind(text=self.on_search)
        btn_row = action_bar(
            MDButton(MDButtonText(text="Agregar"), style="filled", on_release=lambda x: self._open_add_dialog()),
            MDButton(MDButtonText(text="Editar"), style="outlined", on_release=lambda x: self._open_edit_dialog()),
            MDButton(MDButtonText(text="Eliminar"), style="text", on_release=lambda x: self._open_delete_dialog()),
            MDButton(MDButtonText(text="Importar CSV/Excel"), style="outlined", on_release=lambda x: self._open_csv_dialog()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
        )
        inner = MDBoxLayout(
            MDLabel(text="Proveedores — Colombia", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Aplica abarrotes/electrónica — NIT DIAN, catálogo, entrega, pago — Bogotá/Medellín/Cali/Barranquilla", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            self.search_field,
            btn_row,
            self.table,
            MDCard(
                MDLabel(text=f"Total proveedores: {len(suppliers)}", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
                orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="48dp",
            ),
            orientation="vertical",
            adaptive_height=True, spacing="12dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Proveedores"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *args):
        self.refresh()
    def on_search(self, instance, value):
        filtered = repo.search_suppliers(value)
        if self.table:
            self.table.row_data = [(str(s["id"]), s["name"][:14], s.get("nit", s.get("rfc",""))[:12], s["contact"][:14], s["phone"], s["city"], s.get("lead_time","")) for s in filtered]

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Almacén"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede modificar proveedores"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    # Agregar
    def _open_add_dialog(self):
        if not self._require_write():
            return
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="truck-delivery"), MDTextFieldHintText(text="Empresa *"), mode="outlined")
        f_rfc = MDTextField(MDTextFieldLeadingIcon(icon="card-account-details"), MDTextFieldHintText(text="NIT *"), MDTextFieldHelperText(text="Ej 800123456-9 DIAN", mode="persistent"), mode="outlined")
        f_contact = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Contacto / representante"), mode="outlined")
        f_phone = MDTextField(MDTextFieldLeadingIcon(icon="phone"), MDTextFieldHintText(text="Telefono"), mode="outlined")
        f_email = MDTextField(MDTextFieldLeadingIcon(icon="email"), MDTextFieldHintText(text="Email"), mode="outlined")
        f_city = MDTextField(MDTextFieldLeadingIcon(icon="city"), MDTextFieldHintText(text="Ciudad"), mode="outlined")
        f_catalog = MDTextField(MDTextFieldLeadingIcon(icon="package-variant-closed"), MDTextFieldHintText(text="Catalogo que surte"), MDTextFieldHelperText(text="ej Laptops, Monitores", mode="persistent"), mode="outlined")
        f_lead = MDTextField(MDTextFieldLeadingIcon(icon="clock"), MDTextFieldHintText(text="Lead time"), MDTextFieldHelperText(text="ej 3 dias", mode="persistent"), mode="outlined")
        f_pay = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Condiciones pago"), MDTextFieldHelperText(text="ej 30 dias / Contado", mode="persistent"), mode="outlined")
        self._fields = {"name": f_name, "nit": f_rfc, "rfc": f_rfc, "contact": f_contact, "phone": f_phone, "email": f_email, "city": f_city, "catalog": f_catalog, "lead_time": f_lead, "payment_terms": f_pay}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_name, f_rfc, f_contact, f_phone, f_email, f_city, f_catalog, f_lead, f_pay]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Nuevo proveedor"),
            MDDialogSupportingText(text="* obligatorio"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Crear"), style="filled", on_release=lambda x: self._do_add()),
                spacing="8dp",
            ),
            size_hint=(0.95, None),
        )
        self.dialog.open()

    def _do_add(self):
        try:
            data = {k: v.text.strip() for k,v in self._fields.items()}
            sup = repo.add_supplier(data)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "alta_proveedor", f"{sup['id']} {sup['name']}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Proveedor {sup['name']} creado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # Editar
    def _open_edit_dialog(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="ID a editar *"), mode="outlined")
        self._fields = {"edit_id": f_id}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Editar proveedor"),
            MDDialogSupportingText(text="Ingrese ID"),
            f_id,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Continuar"), style="filled", on_release=lambda x: self._open_edit_form()),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def _open_edit_form(self):
        try:
            sid = int(self._fields["edit_id"].text.strip())
        except Exception:
            MDSnackbar(MDSnackbarText(text="ID numérico"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        s = repo.find_supplier(sid)
        if not s:
            MDSnackbar(MDSnackbarText(text=f"ID {sid} no encontrado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        self.dialog.dismiss()
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="truck-delivery"), MDTextFieldHintText(text=f"Empresa ({s['name']})"), mode="outlined")
        f_rfc = MDTextField(MDTextFieldLeadingIcon(icon="card-account-details"), MDTextFieldHintText(text=f"NIT ({s.get('nit', s.get('rfc',''))})"), mode="outlined")
        f_contact = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text=f"Contacto ({s['contact']})"), mode="outlined")
        f_phone = MDTextField(MDTextFieldLeadingIcon(icon="phone"), MDTextFieldHintText(text=f"Tel ({s['phone']})"), mode="outlined")
        f_city = MDTextField(MDTextFieldLeadingIcon(icon="city"), MDTextFieldHintText(text=f"Ciudad ({s['city']})"), mode="outlined")
        f_catalog = MDTextField(MDTextFieldLeadingIcon(icon="package-variant-closed"), MDTextFieldHintText(text=f"Catalogo ({s.get('catalog','')})"), mode="outlined")
        f_lead = MDTextField(MDTextFieldLeadingIcon(icon="clock"), MDTextFieldHintText(text=f"Entrega ({s.get('lead_time','')})"), mode="outlined")
        f_pay = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text=f"Pago ({s.get('payment_terms','')})"), mode="outlined")
        self._fields = {"sid": sid, "name": f_name, "nit": f_rfc, "rfc": f_rfc, "contact": f_contact, "phone": f_phone, "city": f_city, "catalog": f_catalog, "lead_time": f_lead, "payment_terms": f_pay}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_name, f_rfc, f_contact, f_phone, f_city, f_catalog, f_lead, f_pay]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text=f"Editando ID {sid}"),
            MDDialogSupportingText(text="Vacío = no cambia"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Guardar"), style="filled", on_release=lambda x: self._do_edit()),
                spacing="8dp",
            ),
            size_hint=(0.95, None),
        )
        self.dialog.open()

    def _do_edit(self):
        sid = self._fields["sid"]
        updates = {}
        for k in ("name","nit","rfc","contact","phone","city","catalog","lead_time","payment_terms"):
            v = self._fields[k].text.strip()
            if v:
                updates[k]=v
        try:
            repo.update_supplier(sid, updates)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "edita_proveedor", f"{sid} {updates}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Proveedor {sid} actualizado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # Eliminar
    def _open_delete_dialog(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="delete"), MDTextFieldHintText(text="ID a eliminar *"), mode="outlined")
        self._fields = {"del_id": f_id}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Eliminar proveedor"),
            f_id,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Eliminar"), style="filled", on_release=lambda x: self._do_delete()),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def _do_delete(self):
        try:
            sid = int(self._fields["del_id"].text.strip())
        except Exception:
            MDSnackbar(MDSnackbarText(text="ID numérico"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        try:
            repo.delete_supplier(sid)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "baja_proveedor", str(sid))
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Proveedor {sid} eliminado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # CSV
    def _open_csv_dialog(self):
        if not self._require_write():
            return
        f_path = MDTextField(MDTextFieldLeadingIcon(icon="file-delimited"), MDTextFieldHintText(text="Ruta CSV o Excel (.csv / .xlsx)"), MDTextFieldHelperText(text="Columnas: name,contact,phone,email,city,nit — acepta ES/EN — DIAN", mode="persistent"), mode="outlined")
        self._fields = {"csv": f_path}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Importar proveedores CSV/Excel"),
            f_path,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Importar"), style="filled", on_release=lambda x: self._do_csv()),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def _do_csv(self):
        path = self._fields["csv"].text.strip()
        try:
            n = repo.import_suppliers_file(path)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "import_proveedores", f"{path} +{n}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Importados {n} proveedores"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
