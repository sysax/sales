"""
Clientes CRM Colombia — NIT, régimen DIAN, crédito, descuento, bloqueo morosos
Genérico cualquier comercio (abarrotes/electrónica) — COP
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


class ClientsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "clients"
        self.dialog = None
        self._fields = {}
        self.search_field = None
        self.table = None
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        clients = repo.list_clients()
        self.table = MDDataTable(
            size_hint=(1, None),
            height="340dp",
            use_pagination=True,
            rows_num=8,
            column_data=flex_columns(1200,
                ("ID", 0.6),
                ("Nombre", 2.2),
                ("NIT", 1.5),
                ("Email", 2.4),
                ("Telefono", 1.4),
                ("Ciudad", 1.3),
                ("Credito COP", 1.5),
                ("Desc%", 0.9),
            ),
            row_data=[
                (str(c["id"]), c["name"][:18], c.get("nit", c.get("rfc",""))[:14], c["email"][:22], c["phone"][:12], c["city"][:12], f"${c.get('credit',0):,.0f}", str(c.get("discount",0)))
                for c in clients
            ],
        )
        self.search_field = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar nombre / NIT / teléfono — Colombia DIAN"),
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
            MDLabel(text="Clientes (CRM) — Colombia", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="NIT, régimen DIAN (Responsable/No responsable/Simple), límite crédito COP, descuento, bloqueo morosos — genérico abarrotes/electrónica", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            self.search_field,
            btn_row,
            self.table,
            MDCard(
                MDLabel(text=f"Total clientes: {len(clients)}  •  Con credito pendiente: {sum(1 for c in clients if c.get('credit',0)>0)}", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
                orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="48dp",
            ),
            orientation="vertical",
            adaptive_height=True, spacing="12dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Clientes"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *args):
        self.refresh()
    def on_search(self, instance, value):
        filtered = repo.search_clients(value)
        if self.table:
            self.table.row_data = [(str(c["id"]), c["name"][:14], c.get("nit", c.get("rfc",""))[:12], c["email"][:18], c["phone"], c["city"], f"${c.get('credit',0):,.0f}", str(c.get("discount",0))) for c in filtered]

    def _require_write(self):
        app = MDApp.get_running_app()
        role = app.current_user.get("role","") if app.current_user else ""
        if role not in ("Administrador","Vendedor"):
            MDSnackbar(MDSnackbarText(text=f"Rol {role} no puede modificar clientes"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return False
        return True

    # ── Agregar ──
    def _open_add_dialog(self):
        if not self._require_write():
            return
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Nombre *"), mode="outlined")
        f_rfc = MDTextField(MDTextFieldLeadingIcon(icon="card-account-details"), MDTextFieldHintText(text="NIT *"), MDTextFieldHelperText(text="Ej 900123456-7 DIAN", mode="persistent"), mode="outlined")
        f_email = MDTextField(MDTextFieldLeadingIcon(icon="email"), MDTextFieldHintText(text="Email"), mode="outlined")
        f_phone = MDTextField(MDTextFieldLeadingIcon(icon="phone"), MDTextFieldHintText(text="Teléfono"), mode="outlined")
        f_city = MDTextField(MDTextFieldLeadingIcon(icon="city"), MDTextFieldHintText(text="Ciudad (Bogotá/Medellín/Cali)"), mode="outlined")
        f_limit = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text="Límite crédito COP"), MDTextFieldHelperText(text="Ej 5000000", mode="persistent"), mode="outlined")
        f_disc = MDTextField(MDTextFieldLeadingIcon(icon="percent"), MDTextFieldHintText(text="Descuento %"), MDTextFieldHelperText(text="0-100", mode="persistent"), mode="outlined")
        f_reg = MDTextField(MDTextFieldLeadingIcon(icon="file-document"), MDTextFieldHintText(text="Régimen DIAN"), MDTextFieldHelperText(text="Responsable/No responsable/Simple", mode="persistent"), mode="outlined")
        self._fields = {"name": f_name, "nit": f_rfc, "rfc": f_rfc, "email": f_email, "phone": f_phone, "city": f_city, "credit_limit": f_limit, "discount": f_disc, "regimen": f_reg}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_name, f_rfc, f_email, f_phone, f_city, f_limit, f_disc, f_reg]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Nuevo cliente"),
            MDDialogSupportingText(text="* obligatorio"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Crear"), style="filled", on_release=lambda x: self._do_add()),
                spacing="8dp",
            ),
            size_hint=(0.92, None),
        )
        self.dialog.open()

    def _do_add(self):
        try:
            data = {k: v.text.strip() for k,v in self._fields.items()}
            cli = repo.add_client(data)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "alta_cliente", f"{cli['id']} {cli['name']}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Cliente {cli['name']} creado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    # ── Editar ──
    def _open_edit_dialog(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="identifier"), MDTextFieldHintText(text="ID a editar *"), mode="outlined")
        self._fields = {"edit_id": f_id}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Editar cliente"),
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
            cid = int(self._fields["edit_id"].text.strip())
        except Exception:
            MDSnackbar(MDSnackbarText(text="ID numérico"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        c = repo.find_client_by_id(cid)
        if not c:
            MDSnackbar(MDSnackbarText(text=f"ID {cid} no encontrado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        self.dialog.dismiss()
        f_name = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text=f"Nombre ({c['name']})"), mode="outlined")
        f_rfc = MDTextField(MDTextFieldLeadingIcon(icon="card-account-details"), MDTextFieldHintText(text=f"NIT ({c.get('nit', c.get('rfc',''))})"), mode="outlined")
        f_email = MDTextField(MDTextFieldLeadingIcon(icon="email"), MDTextFieldHintText(text=f"Email ({c['email']})"), mode="outlined")
        f_phone = MDTextField(MDTextFieldLeadingIcon(icon="phone"), MDTextFieldHintText(text=f"Tel ({c['phone']})"), mode="outlined")
        f_city = MDTextField(MDTextFieldLeadingIcon(icon="city"), MDTextFieldHintText(text=f"Ciudad ({c['city']})"), mode="outlined")
        f_limit = MDTextField(MDTextFieldLeadingIcon(icon="cash"), MDTextFieldHintText(text=f"Limite ({c.get('credit_limit',0)})"), mode="outlined")
        f_disc = MDTextField(MDTextFieldLeadingIcon(icon="percent"), MDTextFieldHintText(text=f"Desc ({c.get('discount',0)})"), mode="outlined")
        f_status = MDTextField(MDTextFieldLeadingIcon(icon="account-cancel"), MDTextFieldHintText(text=f"Estado ({c.get('status','activo')})"), MDTextFieldHelperText(text="activo/bloqueado", mode="persistent"), mode="outlined")
        self._fields = {"cid": cid, "name": f_name, "nit": f_rfc, "rfc": f_rfc, "email": f_email, "phone": f_phone, "city": f_city, "credit_limit": f_limit, "discount": f_disc, "status": f_status, "regimen": f_rfc}
        from kivymd.uix.gridlayout import MDGridLayout
        grid = MDGridLayout(cols=2, spacing="8dp", adaptive_height=True, padding="8dp")
        for w in [f_name, f_rfc, f_email, f_phone, f_city, f_limit, f_disc, f_status]:
            grid.add_widget(w)
        self.dialog = MDDialog(
            MDDialogHeadlineText(text=f"Editando ID {cid}"),
            MDDialogSupportingText(text="Vacío = no cambia"),
            grid,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Guardar"), style="filled", on_release=lambda x: self._do_edit()),
                spacing="8dp",
            ),
            size_hint=(0.92, None),
        )
        self.dialog.open()

    def _do_edit(self):
        cid = self._fields["cid"]
        updates = {}
        for k in ("name","nit","rfc","email","phone","city","credit_limit","discount","status","regimen"):
            v = self._fields[k].text.strip()
            if v:
                updates[k]=v
        try:
            repo.update_client(cid, updates)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "edita_cliente", f"{cid} {updates}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Cliente {cid} actualizado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Eliminar ──
    def _open_delete_dialog(self):
        if not self._require_write():
            return
        f_id = MDTextField(MDTextFieldLeadingIcon(icon="delete"), MDTextFieldHintText(text="ID a eliminar *"), mode="outlined")
        self._fields = {"del_id": f_id}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Eliminar cliente"),
            MDDialogSupportingText(text="Irreversible"),
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
            cid = int(self._fields["del_id"].text.strip())
        except Exception:
            MDSnackbar(MDSnackbarText(text="ID numérico"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        try:
            repo.delete_client(cid)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "baja_cliente", str(cid))
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Cliente {cid} eliminado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── CSV ──
    def _open_csv_dialog(self):
        if not self._require_write():
            return
        f_path = MDTextField(MDTextFieldLeadingIcon(icon="file-delimited"), MDTextFieldHintText(text="Ruta CSV o Excel (.csv / .xlsx)"), MDTextFieldHelperText(text="Columnas: name,email,phone,city,nit — acepta ES/EN — Colombia DIAN", mode="persistent"), mode="outlined")
        self._fields = {"csv": f_path}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Importar clientes CSV/Excel"),
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
            n = repo.import_clients_file(path)
            app = MDApp.get_running_app()
            repo.log(app.current_user.get("username","sistema"), "import_clientes", f"{path} +{n}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Importados {n} clientes"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
