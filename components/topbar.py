"""
TopAppBar reutilizable para todas las pantallas autenticadas.
Ref: kivymd-reference.md - kivymd.uix.appbar.appbar — + indicador offline Colombia
"""
from kivy.utils import get_color_from_hex
from kivymd.uix.appbar import (
    MDTopAppBar,
    MDTopAppBarLeadingButtonContainer,
    MDTopAppBarTrailingButtonContainer,
    MDActionTopAppBarButton,
    MDTopAppBarTitle,
)
from kivymd.app import MDApp


def create_topbar(title: str) -> MDTopAppBar:
    """
    Crea un MDTopAppBar con:
    - Boton hamburguesa (izquierda)
    - Titulo centrado
    - Indicador offline/online (derecha) + sync
    """
    # indicador offline: usa data.offline.is_online()
    try:
        from data.offline import is_online, get_queue
        online = is_online()
        queued = len(get_queue())
        icon = "wifi" if online else "wifi-off"
        badge = f" {queued}" if queued else ""
    except Exception:
        icon = "wifi"
        online = True
        badge = ""
        queued = 0

    def _toggle_offline(x):
        try:
            from data import mock_data as db
            db.IS_OFFLINE = not getattr(db, "IS_OFFLINE", False)
            # toast via snackbar if app running
            try:
                from kivy.metrics import dp
                from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
                MDSnackbar(MDSnackbarText(text=f"{'OFFLINE' if db.IS_OFFLINE else 'Online'} — cola {len(get_queue())}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            except Exception:
                pass
        except Exception:
            pass

    def _sync(x):
        try:
            from data.offline import sync_queue
            from data.repository import repo as _repo
            synced, pending = sync_queue(_repo)
            from kivy.metrics import dp
            from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
            MDSnackbar(MDSnackbarText(text=f"Sincronizados {synced}, pendientes {pending}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
        except Exception as e:
            try:
                from kivy.metrics import dp
                from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
                MDSnackbar(MDSnackbarText(text=f"Sync error: {e}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()
            except Exception:
                pass

    topbar = MDTopAppBar(
        MDTopAppBarLeadingButtonContainer(
            MDActionTopAppBarButton(
                icon="menu",
                on_release=lambda x: MDApp.get_running_app().toggle_drawer(),
            ),
        ),
        MDTopAppBarTitle(
            text=title + (f" ● {badge.strip()} offline" if not online else ""),
        ),
        MDTopAppBarTrailingButtonContainer(
            MDActionTopAppBarButton(icon=icon, on_release=_toggle_offline),
            MDActionTopAppBarButton(icon="sync", on_release=_sync),
        ),
        type="small",
    )
    topbar.md_bg_color = get_color_from_hex("#009688")  # Primary color
    return topbar