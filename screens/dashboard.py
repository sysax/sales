"""
Panel principal estilo GesNet — 12 tarjetas de colores + comparativa.
Grilla 4 columnas con valor + etiqueta + icono en blanco; debajo panel
de comparativa ventas 7 días. Datos reales del repo, Colombia COP.
"""
from datetime import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.app import MDApp
from components.topbar import create_topbar
from components.theme import (
    action_bar, stat_card, stat_grid,
    DASH_BLUE, DASH_RED, DASH_GREEN, DASH_INDIGO, DASH_TEAL, DASH_LIME,
    DASH_ORANGE, DASH_SLATE, DASH_CRIMSON, DASH_CYAN, DASH_PINK, DASH_PURPLE,
)
from screens.reports import BarChart
from data.repository import repo


class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "dashboard"
        self._build_ui()

    def _money(self, v):
        return f"${v:,.0f}"

    def _build_ui(self):
        self.clear_widgets()
        go = lambda s: (lambda x: MDApp.get_running_app().navigate_to(s))
        month = datetime.now().strftime("%Y-%m")

        # ── Datos reales ──
        caja = repo.get_caja_status()
        caja_val = caja.get("expected", 0) if caja.get("open") else 0
        ventas_dia = repo.get_ventas_por_periodo("dia")["total"]
        try:
            compras_mes = sum(
                p["total"] for p in repo.list_purchases()
                if str(p.get("date", "")).startswith(month) and p.get("status") != "Cancelada"
            )
        except Exception:
            compras_mes = 0
        inv = repo.get_valor_inventario()
        try:
            cxp_deuda = sum(p.get("balance", p["amount"]) for p in repo.list_payables())
        except Exception:
            cxp_deuda = 0
        try:
            rec = repo.list_receivables()
            cxc_deuda = sum(s.get("balance", 0) for s in rec)
            vencidas = sum(1 for s in rec if repo.calculate_mora(s) > 0)
        except Exception:
            cxc_deuda, vencidas = 0, 0
        try:
            n_cats = len(repo.get_category_sales())
        except Exception:
            n_cats = 0
        try:
            movs = repo.list_movements(500)
            ingresados = sum(m["qty"] for m in movs
                             if m.get("type") == "Entrada" and str(m.get("ts", "")).startswith(month))
        except Exception:
            ingresados = 0
        try:
            caducar = len(repo.get_products_by_vencimiento(30))
        except Exception:
            caducar = 0
        try:
            n_clients = len(repo.list_clients())
        except Exception:
            n_clients = 0

        cards = [
            stat_card(DASH_BLUE, self._money(caja_val), "EN CAJA", "cash-register", go("pos")),
            stat_card(DASH_RED, self._money(compras_mes), "COMPRAS DEL MES", "shopping", go("purchases")),
            stat_card(DASH_GREEN, self._money(ventas_dia), "EN VENTAS DEL DÍA", "cash-plus", go("reports")),
            stat_card(DASH_INDIGO, self._money(inv["cost_value"]), "INVERTIDO EN STOCK", "tag", go("inventory")),
            stat_card(DASH_TEAL, self._money(cxp_deuda), "PROVEEDORES", "truck-delivery", go("payables")),
            stat_card(DASH_LIME, str(n_cats), "CATEGORÍAS", "shape", go("products")),
            stat_card(DASH_ORANGE, str(inv["units"]), "UNIDADES EN STOCK", "star-box", go("inventory")),
            stat_card(DASH_SLATE, str(ingresados), "PRODUCTOS INGRESADOS", "archive", go("inventory")),
            stat_card(DASH_CRIMSON, str(caducar), "POR CADUCAR 30D", "calendar-alert", go("products")),
            stat_card(DASH_CYAN, str(vencidas), "VENCERÁN EN 30 DÍAS", "calendar-clock", go("receivables")),
            stat_card(DASH_PINK, str(n_clients), "CLIENTES", "account-group", go("clients")),
            stat_card(DASH_PURPLE, self._money(cxc_deuda), "CRÉDITOS PENDIENTES", "credit-card", go("receivables")),
        ]

        # ── Comparativa ventas 7 días ──
        try:
            sales_by_period = repo.get_sales_by_period(7)
        except Exception:
            sales_by_period = []
        chart_data = [{"label": d["day"], "value": d["total"]} for d in sales_by_period]
        # Panel comparativa (Box sin ripple: MDCard anidado rompe el FBO)
        chart_panel = MDBoxLayout(
            MDLabel(text="COMPARATIVA VENTAS ÚLTIMOS 7 DÍAS — COP", font_style="Title",
                    role="medium", adaptive_height=True, padding=(0, 0, 0, "8dp")),
            BarChart(data=chart_data, title=""),
            orientation="vertical", padding="8dp", spacing="8dp",
            size_hint_x=1, adaptive_height=True,
        )

        quick = action_bar(
            MDButton(MDButtonText(text="POS — Vender"), style="filled", on_release=lambda x: MDApp.get_running_app().navigate_to("pos")),
            MDButton(MDButtonText(text="Productos"), style="outlined", on_release=lambda x: MDApp.get_running_app().navigate_to("products")),
            MDButton(MDButtonText(text="Clientes"), style="outlined", on_release=lambda x: MDApp.get_running_app().navigate_to("clients")),
            MDButton(MDButtonText(text="Reportes"), style="filled", on_release=lambda x: MDApp.get_running_app().navigate_to("reports")),
        )

        inner = MDBoxLayout(
            stat_grid(cards, cols=4),
            chart_panel,
            MDLabel(text="Accesos rápidos", font_style="Title", role="small",
                    halign="center", adaptive_height=True),
            quick,
            orientation="vertical", adaptive_height=True, spacing="8dp",
            padding="8dp", size_hint_x=1,
        )
        self.add_widget(MDBoxLayout(create_topbar("Inicio"), MDScrollView(inner, do_scroll_x=False), orientation="vertical"))

    def on_enter(self, *args):
        self._build_ui()
