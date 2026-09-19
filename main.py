"""
Aplicacion principal del Sistema de Ventas - Fase 1
Orquesta todos los modulos y pantallas.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout

# Screens — 12 módulos fases.md
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.products import ProductsScreen
from screens.sales import SalesScreen
from screens.inventory import InventoryScreen
from screens.clients import ClientsScreen
from screens.pos import POSScreen
from screens.purchases import PurchasesScreen
from screens.receivables import ReceivablesScreen
from screens.reports import ReportsScreen
from screens.suppliers import SuppliersScreen
from screens.payables import PayablesScreen
from screens.promos import PromosScreen
from screens.users import UsersScreen

# Components
from components.sidebar import create_sidebar
from data.repository import repo


class SalesApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user = None
        self.nav_drawer = None
        self.sm = None

    def build(self):
        # Tema pastel claro (components/theme.py) — Material 3 desde seed menta
        from components.theme import apply_theme
        apply_theme(self)

        # 1. Creamos el ScreenManager totalmente vacío temporalmente
        self.sm = MDScreenManager()

        # 2. Creamos el Sidebar reutilizable
        self.nav_drawer = create_sidebar()

        # 3. Retornamos el Layout raiz como nodo principal
        return MDNavigationLayout(
            self.sm,
            self.nav_drawer,
        )

    def on_start(self):
        """
        Maximiza la ventana al inicio con manejo robusto de errores.
        Garantiza que el contexto OpenGL tenga dimensiones antes de cargar pantallas.
        """
        try:
            Window.maximize()
        except Exception as e:
            print(f"[WARN] Window.maximize() fallo: {e}")
            try:
                Window.size = (1920, 1080)
                Window.left = 0
                Window.top = 0
            except Exception:
                pass

        # Forzar actualización inmediata del entorno gráfico de Kivy
        Window.canvas.ask_update()

        # Ahora que la ventana tiene dimensiones reales, inyectamos los componentes de forma segura
        for ScreenCls in (
            LoginScreen,
            DashboardScreen,
            ProductsScreen,
            SalesScreen,
            InventoryScreen,
            ClientsScreen,
            POSScreen,
            PurchasesScreen,
            ReceivablesScreen,
            ReportsScreen,
            SuppliersScreen,
            PayablesScreen,
            PromosScreen,
            UsersScreen,
        ):
            try:
                self.sm.add_widget(ScreenCls())
            except Exception as e:
                print(f"[ERROR] No se pudo cargar {ScreenCls.__name__}: {e}")

        # Establecemos la pantalla inicial de la aplicación de manera explícita
        self.sm.current = "login"

    def refresh_sidebar(self):
        """Reconstruye drawer filtrado por rol actual (Colombia)"""
        try:
            from components.sidebar import create_sidebar
            # MDNavigationLayout es self.root (si existe)
            root = self.root
            if root and self.nav_drawer:
                try:
                    root.remove_widget(self.nav_drawer)
                except Exception:
                    pass
                self.nav_drawer = create_sidebar()
                # MDNavigationLayout espera manager primero, drawer segundo — añadir al final funciona
                root.add_widget(self.nav_drawer)
        except Exception as e:
            print(f"[WARN] refresh_sidebar fallo: {e}")

    def navigate_to(self, screen_name: str):
        """Navega a una pantalla y cierra el drawer. Respeta permisos por rol (§1) Colombia."""
        # login siempre permitido
        if screen_name != "login" and not self.current_user:
            self._snack("Debes iniciar sesión")
            self.sm.current = "login"
            self.nav_drawer.set_state("close")
            return
        if self.current_user:
            role = self.current_user.get("role", "")
            if not repo.can_access(role, screen_name):
                self._snack(f"Acceso denegado para rol {role}: {screen_name}")
                repo.log(self.current_user.get("username"), "acceso_denegado", screen_name)
                self.nav_drawer.set_state("close")
                return
            # bitácora de navegación
            repo.log(self.current_user.get("username"), "navegar", screen_name)
        self.sm.current = screen_name
        self.nav_drawer.set_state("close")

    def _snack(self, msg: str):
        try:
            from kivy.metrics import dp
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
            MDSnackbar(MDSnackbarText(text=msg), y=dp(24), pos_hint={"center_x": 0.5}, size_hint_x=0.6).open()
        except Exception:
            print(f"[SNACK] {msg}")

    def toggle_drawer(self):
        """Abre/cierra el NavigationDrawer. Bloqueado si no hay sesión (excepto login no debería abrirse)."""
        # El drawer existe siempre, pero si no hay usuario evitamos abrirlo
        if not self.current_user and self.sm.current == "login":
            return
        self.nav_drawer.set_state("toggle")

    def logout(self):
        """Cierra sesion y regresa al login."""
        if self.current_user:
            repo.log(self.current_user.get("username"), "logout", "")
        self.current_user = None
        self.nav_drawer.set_state("close")
        try:
            self.refresh_sidebar()
        except Exception:
            pass
        self.sm.current = "login"


if __name__ == "__main__":
    SalesApp().run()
