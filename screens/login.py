"""
Pantalla de Login refactorizada.
Ref: mdcard_03.py - Uso de MDRelativeLayout con posicionamiento absoluto
"""
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp
from data.repository import repo


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "login"
        self.md_bg_color = self.theme_cls.backgroundColor
        
        self.user_field = None
        self.pass_field = None
        self.dialog = None
        self._fields = {}
        self._pending_user = None
        
        # Construir UI directamente (sin Clock.schedule_once)
        self._build_ui()
    
    def _build_ui(self):
        """Construye la UI usando MDRelativeLayout con posicionamiento absoluto."""
        
        # Campos de texto
        self.user_field = MDTextField(
            MDTextFieldLeadingIcon(icon="account"),
            MDTextFieldHintText(text="Usuario"),
            MDTextFieldHelperText(text="Prueba: admin", mode="persistent"),
            mode="outlined",
            size_hint_x=1,
            size_hint_y=None,
            height="60dp",
        )
        
        self.pass_field = MDTextField(
            MDTextFieldLeadingIcon(icon="lock"),
            MDTextFieldHintText(text="Contraseña"),
            MDTextFieldHelperText(text="Prueba: admin123", mode="persistent"),
            mode="outlined",
            password=True,
            size_hint_x=1,
            size_hint_y=None,
            height="60dp",
        )
        
        # MDCard con MDRelativeLayout interno
        card = MDCard(
            MDRelativeLayout(
                # Primer label FIJADO ARRIBA
                MDLabel(
                    text="Sistema de Ventas",
                    halign="center",
                    pos_hint={"top": 1, "center_x": 0.5},
                    size_hint_y=None,
                    height="32dp",
                    font_style="Headline",
                    role="large",
                ),
                
                # Segundo label (subtítulo)
                MDLabel(
                    text="Inicia sesión para continuar",
                    pos_hint={"top": 0.85, "center_x": 0.5},
                    halign="center",
                    font_style="Body",
                    role="medium",
                    theme_text_color="Secondary",
                    size_hint_y=None,
                    height="20dp",
                ),
                
                # BoxLayout para los campos y botón
                MDBoxLayout(
                    self.user_field,
                    self.pass_field,
                    MDButton(
                        MDButtonText(text="Iniciar sesión"),
                        style="filled",
                        theme_width="Custom",
                        size_hint_x=1,
                        size_hint_y=None,
                        height="48dp",
                        pos_hint={"center_x": 0.5},
                        on_release=self.do_login,
                    ),
                    MDButton(
                        MDButtonText(text="¿Olvidaste tu contraseña?"),
                        style="text",
                        theme_width="Custom",
                        size_hint_x=1,
                        size_hint_y=None,
                        height="36dp",
                        pos_hint={"center_x": 0.5},
                        on_release=self.open_recovery,
                    ),
                    orientation="vertical",
                    spacing="8dp",
                    pos_hint={"center_x": 0.5, "center_y": 0.38},
                    size_hint=(0.9, None),
                    height="260dp",
                    padding=("16dp", "0dp", "16dp", "0dp"),
                ),
            ),
            # Propiedades de la tarjeta
            style="elevated",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding="4dp",
            size_hint=(None, None),
            size=("480dp", "360dp"),
        )
        
        self.add_widget(card)
    
    def do_login(self, *args):
        """Valida con hash PBKDF2, controla active/bloqueo 3 intentos → 5 min lockout (Colombia)."""
        if not self.user_field or not self.pass_field:
            return
        user = self.user_field.text.strip()
        pwd = self.pass_field.text.strip()
        if not user or not pwd:
            MDSnackbar(MDSnackbarText(text="Ingrese usuario y contraseña"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        # 1) existe y activo
        meta = repo.find_user_by_name(user)
        if not meta:
            repo.log(user, "login_fallido", "usuario no existe")
            MDSnackbar(MDSnackbarText(text="Usuario no existe"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            return
        if not meta.get("active", 1):
            repo.log(user, "login_bloqueado", "desactivado")
            MDSnackbar(MDSnackbarText(text="Usuario bloqueado — contacte Administrador"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
            return
        locked = meta.get("locked_until")
        if locked:
            try:
                from datetime import datetime
                dt = datetime.fromisoformat(locked)
                if datetime.now() < dt:
                    mins = int((dt - datetime.now()).total_seconds()/60) + 1
                    MDSnackbar(MDSnackbarText(text=f"Cuenta bloqueada {mins} min por 3 intentos fallidos"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
                    return
            except Exception:
                pass
        found = repo.find_user(user, pwd)
        if found:
            # 2FA: si activo, pedir segundo factor antes de entrar
            try:
                needs_2fa = repo.is_2fa_enabled(user)
            except Exception:
                needs_2fa = False
            if needs_2fa:
                self._pending_user = found
                self._open_2fa_dialog(user)
                return
            self._enter_app(found)
        else:
            # fallido — revisar intentos restantes
            meta2 = repo.find_user_by_name(user)
            attempts = meta2.get("failed_attempts", 0) if meta2 else 0
            remaining = max(0, 3 - attempts)
            if remaining == 0:
                MDSnackbar(MDSnackbarText(text="3 intentos fallidos — cuenta bloqueada 5 min"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
                repo.log(user, "login_bloqueo_5min", f"intentos {attempts}")
            else:
                MDSnackbar(MDSnackbarText(text=f"Credenciales incorrectas — quedan {remaining} intentos"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()
                repo.log(user, "login_fallido", f"intentos {attempts}")

    def _enter_app(self, found):
        app = MDApp.get_running_app()
        app.current_user = found
        repo.log(found["username"], "login", "ok")
        if self.user_field:
            self.user_field.text = ""
        if self.pass_field:
            self.pass_field.text = ""
        self._pending_user = None
        try:
            app.refresh_sidebar()
        except Exception:
            pass
        app.navigate_to("dashboard")

    # ── 2FA segundo factor ──
    def _open_2fa_dialog(self, username):
        f_code = MDTextField(
            MDTextFieldLeadingIcon(icon="shield-key"),
            MDTextFieldHintText(text="Código 6 dígitos o recuperación XXXX-XXXX"),
            MDTextFieldHelperText(text="App autenticadora o código de respaldo", mode="persistent"),
            mode="outlined",
        )
        self._fields = {"code": f_code}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text=f"Verificación 2FA — {username}"),
            MDDialogSupportingText(text="Ingrese el código de su app autenticadora. Si la perdió, use un código de recuperación."),
            f_code,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: (self.dialog.dismiss(), setattr(self, "_pending_user", None))),
                MDButton(MDButtonText(text="Verificar"), style="filled", on_release=lambda x: self._do_2fa(username)),
                spacing="8dp",
            ),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_2fa(self, username):
        code = self._fields["code"].text.strip()
        try:
            ok = repo.verify_2fa(username, code)
        except Exception:
            ok = False
        if ok:
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text="2FA verificado"), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()
            self._enter_app(self._pending_user or {"username": username, "role": (repo.find_user_by_name(username) or {}).get("role", "")})
        else:
            repo.log(username, "login_2fa_fallido", "")
            MDSnackbar(MDSnackbarText(text="Código 2FA inválido"), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()

    # ── Recuperación contraseña ──
    def open_recovery(self, *args):
        f_user = MDTextField(
            MDTextFieldLeadingIcon(icon="account"),
            MDTextFieldHintText(text="Usuario *"),
            mode="outlined",
        )
        self._fields = {"rec_user": f_user}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Recuperar contraseña"),
            MDDialogSupportingText(text="Se genera un token válido 30 min (un solo uso). Sin servidor de correo, se muestra aquí y en bitácora."),
            f_user,
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Generar token"), style="filled", on_release=lambda x: self._do_request_recovery()),
                spacing="8dp",
            ),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_request_recovery(self):
        username = self._fields["rec_user"].text.strip()
        if not username:
            MDSnackbar(MDSnackbarText(text="Ingrese usuario"), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()
            return
        try:
            token, exp = repo.request_recovery(username)
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()
            return
        self.dialog.dismiss()
        f_user = MDTextField(MDTextFieldLeadingIcon(icon="account"), MDTextFieldHintText(text="Usuario *"), mode="outlined", text=username)
        f_token = MDTextField(MDTextFieldLeadingIcon(icon="key"), MDTextFieldHintText(text="Token *"), mode="outlined")
        f_new = MDTextField(MDTextFieldLeadingIcon(icon="lock-reset"), MDTextFieldHintText(text="Nueva contraseña * min 4"), mode="outlined", password=True)
        self._fields = {"user": f_user, "token": f_token, "new": f_new}
        self.dialog = MDDialog(
            MDDialogHeadlineText(text="Restablecer con token"),
            MDDialogSupportingText(text=f"Token para {username}: {token} (expira {exp}). Guárdelo, solo se muestra una vez."),
            MDBoxLayout(f_user, f_token, f_new, orientation="vertical", spacing="12dp", adaptive_height=True, padding="12dp"),
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(MDButtonText(text="Cancelar"), style="text", on_release=lambda x: self.dialog.dismiss()),
                MDButton(MDButtonText(text="Restablecer"), style="filled", on_release=lambda x: self._do_redeem_recovery()),
                spacing="8dp",
            ),
            size_hint=(0.9, None),
        )
        self.dialog.open()

    def _do_redeem_recovery(self):
        username = self._fields["user"].text.strip()
        token = self._fields["token"].text.strip()
        new = self._fields["new"].text.strip()
        try:
            repo.redeem_recovery(username, token, new)
            self.dialog.dismiss()
            MDSnackbar(MDSnackbarText(text="Contraseña restablecida — inicie sesión"), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.7).open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.7).open()