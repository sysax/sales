"""
NavigationDrawer reutilizable con el menu del sistema.
Ref: kivymd-reference.md - kivymd.uix.navigationdrawer.navigationdrawer
MDScreenManager + MDNavigationLayout, MDTopAppBar p.7-11, MDNavigationDrawer*

12 módulos fases.md + Dashboard + Usuarios
"""
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerItem,
    MDNavigationDrawerItemLeadingIcon,
    MDNavigationDrawerItemText,
    MDNavigationDrawerDivider,
)
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


def create_sidebar() -> MDNavigationDrawer:
    """
    Crea el menu lateral filtrado por rol (Colombia) — solo muestra módulos permitidos.
    Usa data.repository.can_access; si no hay usuario (pre-login) muestra todo para admin preview.
    """
    app = MDApp.get_running_app()
    # Import lazy para evitar ciclo
    try:
        from data.repository import repo
    except Exception:
        repo = None

    # (icon, texto, screen_name)
    menu_items = [
        ("view-dashboard", "Dashboard", "dashboard"),
        ("point-of-sale", "Punto de Venta", "pos"),
        ("package-variant-closed", "Productos", "products"),
        ("warehouse", "Inventario", "inventory"),
        ("account-group", "Clientes", "clients"),
        ("truck-delivery", "Proveedores", "suppliers"),
        ("shopping", "Compras", "purchases"),
        ("cart", "Ventas", "sales"),
        ("cash-plus", "Cuentas por Cobrar", "receivables"),
        ("cash-minus", "Cuentas por Pagar", "payables"),
        ("chart-bar", "Reportes", "reports"),
        ("tag", "Promociones", "promos"),
        ("account-cog", "Usuarios y Roles", "users"),
    ]

    items = []
    # Determinar rol actual
    role = None
    try:
        if app and getattr(app, "current_user", None):
            role = app.current_user.get("role")
    except Exception:
        role = None
    for icon, text, screen in menu_items:
        # filtrar si hay rol y repo disponible
        if role and repo and not repo.can_access(role, screen):
            continue
        items.append(
            MDNavigationDrawerItem(
                MDNavigationDrawerItemLeadingIcon(icon=icon),
                MDNavigationDrawerItemText(text=text),
                on_release=lambda x, s=screen: app.navigate_to(s),
            )
        )
    # Si filtra y queda vacío (Cajero muy limitado) al menos Dashboard
    if not items:
        items.append(
            MDNavigationDrawerItem(
                MDNavigationDrawerItemLeadingIcon(icon="view-dashboard"),
                MDNavigationDrawerItemText(text="Dashboard"),
                on_release=lambda x: app.navigate_to("dashboard"),
            )
        )

    return MDNavigationDrawer(
        MDNavigationDrawerMenu(
            MDNavigationDrawerHeader(
                MDLabel(
                    text="Sistema de Ventas",
                    font_style="Title",
                    role="large",
                    adaptive_height=True,
                    padding=("16dp", "16dp", "16dp", "4dp"),
                    theme_text_color="Custom",
                    text_color=get_color_from_hex("#FFFFFF"),
                ),
                MDLabel(
                    text="v1.0 - KivyMD 2.0.1",
                    font_style="Body",
                    role="medium",
                    theme_text_color="Custom",
                    text_color=get_color_from_hex("#E0E0E0"),
                    adaptive_height=True,
                    padding=("16dp", "0dp", "16dp", "16dp"),
                ),
                orientation="vertical",
                adaptive_height=True,
                md_bg_color=get_color_from_hex("#009688"),  # Primary color
            ),
            MDNavigationDrawerDivider(),
            MDNavigationDrawerLabel(text="Modulos"),
            *items,
            MDNavigationDrawerDivider(),
            MDNavigationDrawerLabel(text="Sesion"),
            MDNavigationDrawerItem(
                MDNavigationDrawerItemLeadingIcon(icon="logout"),
                MDNavigationDrawerItemText(text="Cerrar sesion"),
                on_release=lambda x: MDApp.get_running_app().logout(),
            ),
        ),
        radius=(0, dp(16), dp(16), 0),
        md_bg_color=get_color_from_hex("#FFFFFF"),  # Surface card
    )
