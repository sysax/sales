"""
Gestión de Usuarios y Roles §1 — Colombia — cierre módulo
Alta, edición rol, bloqueo/desbloqueo, reset password, bitácora detallada con búsqueda/export
PBKDF2, lockout 3 intentos 5 min, permisos por módulo, audit trail
KivyMD 2.0.1 — MDTopAppBar, MDCard, MDDataTable, MDDialog, MDSnackbar — COP
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
from data.mock_data import ROLES


class UsersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "users"
        self.dialog = None
        self._fields = {}
        self.search_user = None
        self.search_audit = None
        self.users_table = None
        self.audit_table = None
        self._audit_cache = []
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        users = repo.list_users()
        audit = repo.list_audit()  # 100 últimos
        self._audit_cache = audit

        # Tabla usuarios — Colombia
        self.users_table = MDDataTable(
            size_hint=(1, None), height="300dp", use_pagination=True, rows_num=6,
            column_data=flex_columns(1150,
                ("Usuario", 1.6),
                ("Rol", 1.7),
                ("Activo", 0.9),
                ("2FA", 0.7),
                ("Intentos", 1),
                ("Bloqueo", 1.7),
                ("Último login", 2),
            ),
            row_data=[
                (
                    u["username"], u["role"],
                    "Sí" if u.get("active",1) else "No",
                    "Sí" if u.get("totp_enabled") else "No",
                    str(u.get("failed_attempts",0) or 0),
                    (u.get("locked_until","") or "")[:16],
                    (u.get("last_login","") or "")[:16],
                ) for u in users
            ],
        )
        self.search_user = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar usuario / rol — Colombia"),
            mode="outlined", size_hint_x=1,
        )
        self.search_user.bind(text=self.on_search_user)

        self.audit_table = MDDataTable(
            size_hint=(1, None), height="300dp", use_pagination=True, rows_num=8,
            column_data=flex_columns(1000,
                ("Fecha", 1.6),
                ("Usuario", 1.1),
                ("Acción", 1.3),
                ("Detalle", 2.2),
            ),
            row_data=[(a["ts"], a["user"], a["action"], a["detail"][:22]) for a in audit[:20]],
        )
        self.search_audit = MDTextField(
            MDTextFieldLeadingIcon(icon="magnify"),
            MDTextFieldHintText(text="Buscar bitácora: usuario / acción / detalle"),
            mode="outlined", size_hint_x=1,
        )
        self.search_audit.bind(text=self.on_search_audit)

        btn_row1 = action_bar(
            MDButton(MDButtonText(text="Agregar"), style="filled", on_release=lambda x: self._open_add_dialog()),
            MDButton(MDButtonText(text="Editar Rol"), style="outlined", on_release=lambda x: self._open_edit_role()),
            MDButton(MDButtonText(text="Bloquear"), style="outlined", on_release=lambda x: self._open_block(True)),
            MDButton(MDButtonText(text="Desbloquear"), style="text", on_release=lambda x: self._open_block(False)),
        )
        btn_row2 = action_bar(
            MDButton(MDButtonText(text="Reset Pass"), style="outlined", on_release=lambda x: self._open_reset()),
            MDButton(MDButtonText(text="Eliminar"), style="text", on_release=lambda x: self._open_delete_dialog()),
            MDButton(MDButtonText(text="Refrescar"), style="text", on_release=lambda x: self.refresh()),
            MDButton(MDButtonText(text="Export Audit CSV"), style="outlined", on_release=lambda x: self._export_audit()),
        )
        btn_row3 = action_bar(
            MDButton(MDButtonText(text="Activar 2FA"), style="filled", on_release=lambda x: self._open_2fa_activate()),
            MDButton(MDButtonText(text="Confirmar 2FA"), style="outlined", on_release=lambda x: self._open_2fa_confirm()),
            MDButton(MDButtonText(text="Desactivar 2FA"), style="text", on_release=lambda x: self._open_2fa_disable()),
            MDButton(MDButtonText(text="Regen Códigos"), style="text", on_release=lambda x: self._open_2fa_regen()),
        )

        inner = MDBoxLayout(
            MDLabel(text="Gestión de Usuarios y Roles — Colombia", font_style="Headline", role="large", halign="center", adaptive_height=True),
            MDLabel(text="Autenticación PBKDF2 + lockout 3 intentos 5 min + active — solo Administrador — DIAN COP", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True),
            MDCard(MDLabel(text="Usuarios — NIT no aplica aquí, es acceso sistema (ABARROTES/ELECTRÓNICA genérico)", font_style="Body", role="small", adaptive_height=True), orientation="vertical", padding="8dp", style="outlined", size_hint_y=None, height="40dp"),
            self.search_user,
            btn_row1,
            btn_row2,
            btn_row3,
            MDCard(MDLabel(text="Usuarios registrados — toque fila no selecciona, use botones con usuario exacto", font_style="Title", role="small", adaptive_height=True), self.users_table, orientation="vertical", padding="12dp", spacing="8dp", style="elevated", size_hint_y=None, height="380dp"),
            MDLabel(text="Bitácora (quién hizo qué y cuándo) — últimos 100 — búsqueda + export", font_style="Title", role="medium", adaptive_height=True, padding=(0,"8dp",0,0)),
            self.search_audit,
            MDCard(self.audit_table, orientation="vertical", padding="12dp", style="outlined", size_hint_y=None, height="360dp"),
            MDLabel(text="Roles: Administrador (todo) · Vendedor (POS+clientes+stock) · Cajero (solo cobros) · Almacén (inventario/compras) · Contador (reportes/CxC/CxP) — sidebar filtra por rol", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True),
            orientation="vertical", adaptive_height=True, spacing="12dp", padding="16dp",
        )
        self.add_widget(MDBoxLayout(create_topbar("Usuarios y Roles"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def refresh(self):
        self._build_ui()
    def on_enter(self, *args):
        self.refresh()
    def on_search_user(self, inst, val):
        q = val.strip().lower()
        if not q:
            self.refresh(); return
        filtered = [u for u in repo.list_users() if q in u["username"].lower() or q in u["role"].lower()]
        if self.users_table:
            self.users_table.row_data = [
                (u["username"], u["role"], "Sí" if u.get("active",1) else "No", "Sí" if u.get("totp_enabled") else "No", str(u.get("failed_attempts",0) or 0), (u.get("locked_until","") or "")[:16], (u.get("last_login","") or "")[:16])
                for u in filtered
            ]
    def on_search_audit(self, inst, val):
        q = val.strip().lower()
        if not q:
            filtered = self._audit_cache[:20]
        else:
            filtered = [a for a in self._audit_cache if q in a["user"].lower() or q in a["action"].lower() or q in a["detail"].lower()][:20]
        if self.audit_table:
            self.audit_table.row_data = [(a["ts"], a["user"], a["action"], a["detail"][:22]) for a in filtered]

    def _require_admin(self):
        app = MDApp.get_running_app()
        if not app.current_user or app.current_user.get("role") != "Administrador":
            MDSnackbar(MDSnackbarText(text="Solo Administrador"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return False
        return True

    # ── Agregar ──
    def _open_add_dialog(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), MDTextFieldHelperText(text="min 3, sin espacios", mode="persistent"), mode="outlined")
        f_pass = MDTextField(MDTextFieldLeadingIcon(icon="lock"), MDTextFieldHintText(text="Contraseña *"), MDTextFieldHelperText(text="min 4, se guarda hash PBKDF2", mode="persistent"), mode="outlined", password=True)
        f_role = MDTextField(MDTextFieldLeadingIcon(icon="shield-account"), MDTextFieldHintText(text=f"Rol * {', '.join(ROLES)}"), mode="outlined")
        self._fields = {"user": f_user, "pwd": f_pass, "role": f_role}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Nuevo usuario — Colombia"),
            MDDialogSupportingText(text="Se guarda hash PBKDF2-SHA256 100k, no texto plano"),
            MDBoxLayout(f_user, f_pass, f_role, orientation="vertical", spacing="12dp", adaptive_height=True, padding="12dp"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Crear"), style="filled", on_release=lambda x: self._do_add()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()
    def _do_add(self):
        u = self._fields["user"].text.strip()
        p = self._fields["pwd"].text.strip()
        r = self._fields["role"].text.strip()
        if len(u) < 3 or len(p) < 4:
            MDSnackbar(MDSnackbarText(text="Usuario min 3 / contraseña min 4"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        if r not in ROLES:
            MDSnackbar(MDSnackbarText(text=f"Rol debe ser {', '.join(ROLES)}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        try:
            repo.add_user(u, p, r)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "alta_usuario", f"{u} rol={r}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Usuario {u} creado (hash)"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Editar Rol ──
    def _open_edit_role(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), mode="outlined")
        f_role = MDTextField(MDTextFieldLeadingIcon(icon="shield-account"), MDTextFieldHintText(text=f"Nuevo rol {', '.join(ROLES)}"), mode="outlined")
        self._fields = {"user": f_user, "role": f_role}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Editar rol"),
            MDBoxLayout(f_user, f_role, orientation="vertical", spacing="12dp", adaptive_height=True, padding="12dp"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Guardar"), style="filled", on_release=lambda x: self._do_edit_role()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()
    def _do_edit_role(self):
        u = self._fields["user"].text.strip()
        r = self._fields["role"].text.strip()
        if r not in ROLES:
            MDSnackbar(MDSnackbarText(text=f"Rol inválido: {', '.join(ROLES)}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        try:
            repo.update_user(u, role=r)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "edita_rol", f"{u}->{r}")
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Rol {u} → {r}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Bloquear / Desbloquear ──
    def _open_block(self, block=True):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account-cancel" if block else "account-check"), MDTextFieldHintText(text="Usuario *"), mode="outlined")
        self._fields = {"user": f_user, "block": block}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Bloquear usuario" if block else "Desbloquear usuario"),
            MDDialogSupportingText(text="Bloqueado no puede iniciar sesión (active=0)" if block else "Desbloquea y resetea intentos"),
            f_user,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Confirmar"), style="filled", on_release=lambda x: self._do_block()), spacing="8dp"),
        )
        self.dialog.open()
    def _do_block(self):
        u = self._fields["user"].text.strip()
        block = self._fields["block"]
        try:
            repo.set_user_active(u, not block)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Usuario {u} {'bloqueado' if block else 'desbloqueado'}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Reset Pass ──
    def _open_reset(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), mode="outlined")
        f_pass = MDTextField(MDTextFieldLeadingIcon(icon="lock-reset"), MDTextFieldHintText(text="Nueva contraseña * min 4"), mode="outlined", password=True)
        self._fields = {"user": f_user, "pwd": f_pass}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Reset contraseña"),
            MDDialogSupportingText(text="Se re-hashea PBKDF2 y desbloquea cuenta"),
            MDBoxLayout(f_user, f_pass, orientation="vertical", spacing="12dp", adaptive_height=True, padding="12dp"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Reset"), style="filled", on_release=lambda x: self._do_reset()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()
    def _do_reset(self):
        u = self._fields["user"].text.strip()
        p = self._fields["pwd"].text.strip()
        try:
            repo.reset_password(u, p)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Password {u} reseteado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── Eliminar ──
    def _open_delete_dialog(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account-remove"), MDTextFieldHintText(text="Usuario a eliminar *"), mode="outlined")
        self._fields = {"del_user": f_user}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Eliminar usuario"),
            MDDialogSupportingText(text="No se puede eliminar 'admin'"),
            f_user,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Eliminar"), style="filled", on_release=lambda x: self._do_delete()), spacing="8dp"),
        )
        self.dialog.open()
    def _do_delete(self):
        u = self._fields["del_user"].text.strip()
        try:
            repo.delete_user(u)
            repo.log(MDApp.get_running_app().current_user.get("username","sistema"), "baja_usuario", u)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"Usuario {u} eliminado"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def _export_audit(self):
        try:
            import csv
            from datetime import datetime
            path = f"/tmp/audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["ts","user","action","detail"])
                for a in repo.list_audit():
                    w.writerow([a["ts"], a["user"], a["action"], a["detail"]])
            MDSnackbar(MDSnackbarText(text=f"Audit exportado {path}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
        except Exception as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    # ── 2FA admin ──
    def _open_2fa_activate(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), mode="outlined")
        self._fields = {"user": f_user}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Activar 2FA — paso 1/2"),
            MDDialogSupportingText(text="Genera secreto TOTP. Entréguelo al usuario para su app autenticadora, luego Confirme con un código."),
            f_user,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Generar secreto"), style="filled", on_release=lambda x: self._do_2fa_activate()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_2fa_activate(self):
        u = self._fields["user"].text.strip()
        try:
            secret = repo.enable_2fa(u)
            from data.totp import provisioning_uri
            uri = provisioning_uri(secret, u)
            left = repo.recovery_codes_left(u)
            self.dialog.dismiss()
            self.dialog = MDDialog(
                MDDialogHeadlineText(text=f"Secreto 2FA — {u}"),
                MDDialogSupportingText(text=f"Secreto (escribir en app): {secret}\nURI: {uri}\nLuego use Confirmar 2FA con un código de 6 dígitos. Códigos respaldo se generan al confirmar."),
                MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: (self.dialog.dismiss(), self.refresh())), spacing="8dp"),
                size_hint=(0.95, None),
            )
            self.dialog.open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def _open_2fa_confirm(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), mode="outlined")
        f_code = MDTextField(MDTextFieldLeadingIcon(icon="shield-key"), MDTextFieldHintText(text="Código 6 dígitos *"), mode="outlined")
        self._fields = {"user": f_user, "code": f_code}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Confirmar 2FA — paso 2/2"),
            MDBoxLayout(f_user, f_code, orientation="vertical", spacing="12dp", adaptive_height=True, padding="12dp"),
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Activar"), style="filled", on_release=lambda x: self._do_2fa_confirm()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_2fa_confirm(self):
        u = self._fields["user"].text.strip()
        c = self._fields["code"].text.strip()
        try:
            codes = repo.confirm_2fa(u, c)
            self.dialog.dismiss()
            self.dialog = MDDialog(
                MDDialogHeadlineText(text=f"2FA activo — {u}"),
                MDDialogSupportingText(text="Códigos de recuperación (un solo uso, guárdelos):\n" + "\n".join(codes)),
                MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: (self.dialog.dismiss(), self.refresh())), spacing="8dp"),
                size_hint=(0.9, None),
            )
            self.dialog.open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def _open_2fa_disable(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), mode="outlined")
        self._fields = {"user": f_user}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Desactivar 2FA"),
            f_user,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Desactivar"), style="filled", on_release=lambda x: self._do_2fa_disable()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_2fa_disable(self):
        u = self._fields["user"].text.strip()
        try:
            repo.disable_2fa(u)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text=f"2FA desactivado {u}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            self.refresh()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def _open_2fa_regen(self):
        if not self._require_admin(): return
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario con 2FA *"), mode="outlined")
        self._fields = {"user": f_user}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Regenerar códigos recuperación"),
            MDDialogSupportingText(text="Invalida los anteriores y genera 8 nuevos (un solo uso)."),
            f_user,
            MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()), MDButton(MDButtonText(text="Regenerar"), style="filled", on_release=lambda x: self._do_2fa_regen()), spacing="8dp"),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_2fa_regen(self):
        u = self._fields["user"].text.strip()
        try:
            codes = repo.regenerate_recovery_codes(u)
            self.dialog.dismiss()
            self.dialog = MDDialog(
                MDDialogHeadlineText(text=f"Nuevos códigos — {u}"),
                MDDialogSupportingText(text="\n".join(codes)),
                MDDialogButtonContainer(MDWidget(), MDButton(MDButtonText(text="OK"), style="filled", on_release=lambda x: self.dialog.dismiss()), spacing="8dp"),
                size_hint=(0.9, None),
            )
            self.dialog.open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def on_enter(self, *args):
        self.refresh()
