"""
Reportes §10 Colombia COP — Operativos, Financieros, KPIs + filtros día/semana/mes/año + export CSV
DIAN IVA 19% — genérico abarrotes/electrónica — offline tickets incluidos
Ref: kivymd uix card/graphics, repository.get_*
"""
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from components.topbar import create_topbar
from components.theme import action_bar, flex_columns
from data.repository import repo


class BarChart(MDCard):
    def __init__(self, data, title="", **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.orientation = "vertical"
        self.padding = "16dp"
        self.size_hint_y = None
        self.height = "320dp"
        self.add_widget(MDLabel(text=title, font_style="Title", role="medium", adaptive_height=True))
        self.chart_widget = BarChartWidget(data)
        self.add_widget(self.chart_widget)

class BarChartWidget(MDBoxLayout):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.size_hint_y = None
        self.height = "240dp"
        self.bind(pos=self.redraw, size=self.redraw)
    def redraw(self, *args):
        self.canvas.clear()
        if not self.data: return
        with self.canvas:
            max_val = max(d["value"] for d in self.data) if self.data else 1
            if max_val == 0: max_val = 1
            n = len(self.data)
            chart_width = self.width - 40
            chart_height = self.height - 40
            bar_width = (chart_width / n) * 0.7
            spacing = (chart_width / n) * 0.3
            bar_color = self.theme_cls.primaryColor
            for i, d in enumerate(self.data):
                bar_height = (d["value"] / max_val) * chart_height
                x = self.x + 20 + i * (bar_width + spacing)
                y = self.y + 20
                Color(rgba=bar_color)
                Rectangle(pos=(x, y), size=(bar_width, bar_height))

class HorizontalBarChart(MDCard):
    def __init__(self, data, title="", **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.orientation = "vertical"
        self.padding = "16dp"
        self.size_hint_y = None
        self.height = "360dp"
        self.add_widget(MDLabel(text=title, font_style="Title", role="medium", adaptive_height=True))
        bars_container = MDGridLayout(cols=2, spacing="8dp", padding=(0,"12dp",0,0), adaptive_height=True, size_hint_x=1, row_default_height="32dp", row_force_default=True)
        max_val = max(d["value"] for d in data) if data else 1
        if max_val == 0: max_val = 1
        for d in data:
            bars_container.add_widget(MDLabel(text=d["label"], font_style="Body", role="medium", halign="right", adaptive_height=True, size_hint_x=0.35))
            bar_box = MDBoxLayout(orientation="horizontal", spacing="8dp", adaptive_height=True, size_hint_x=0.65)
            bar_box.add_widget(HorizontalBar(value=d["value"], max_value=max_val))
            bar_box.add_widget(MDLabel(text=d["text"], font_style="Body", role="small", adaptive_height=True, size_hint_x=None, width="90dp"))
            bars_container.add_widget(bar_box)
        self.add_widget(bars_container)

class HorizontalBar(MDBoxLayout):
    def __init__(self, value, max_value, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.max_value = max_value
        self.size_hint_x = 1
        self.adaptive_height = True
        self.bind(pos=self.redraw, size=self.redraw)
    def redraw(self, *args):
        self.canvas.clear()
        ratio = self.value / self.max_value if self.max_value else 0
        with self.canvas:
            Color(rgba=[0.3,0.3,0.3,0.3])
            Rectangle(pos=self.pos, size=self.size)
            Color(rgba=self.theme_cls.primaryColor)
            Rectangle(pos=self.pos, size=(self.width * ratio, self.height))

class ReportsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "reports"
        self.current_filtro = "semana"
        self._build_ui()

    def _build_ui(self):
        self.clear_widgets()
        # Datos operativos
        ventas_dia = repo.get_ventas_por_periodo("dia")
        ventas_sem = repo.get_ventas_por_periodo("semana")
        ventas_mes = repo.get_ventas_por_periodo("mes")
        ventas_anio = repo.get_ventas_por_periodo("año")
        ticket = repo.get_ticket_promedio()
        top = repo.get_top_products(10)
        least = repo.get_least_sold(5)
        clients = repo.get_top_clients(5)
        sellers = repo.get_top_sellers(5)
        margin = repo.get_margin_per_product()[:5]
        # Financieros
        estado = repo.get_estado_resultados()
        flujo = repo.get_flujo_efectivo()
        inv = repo.get_valor_inventario()
        impuestos = repo.get_impuestos_generados()
        cxc_total = sum(s.get("balance",0) for s in repo.list_receivables())
        cxp_total = sum(p.get("balance",p["amount"]) for p in repo.list_payables())
        # KPIs
        kpis = repo.get_kpis()
        # 7 días para gráfico
        sales_by_period = repo.get_sales_by_period(7)

        # Filtros
        filt_row = MDBoxLayout(
            MDLabel(text="Filtros:", font_style="Title", role="small", adaptive_height=True, size_hint_x=None, width="70dp"),
            MDButton(MDButtonText(text="Día"), style="filled" if self.current_filtro=="dia" else "outlined", on_release=lambda x: self._set_filtro("dia")),
            MDButton(MDButtonText(text="Semana"), style="filled" if self.current_filtro=="semana" else "outlined", on_release=lambda x: self._set_filtro("semana")),
            MDButton(MDButtonText(text="Mes"), style="filled" if self.current_filtro=="mes" else "outlined", on_release=lambda x: self._set_filtro("mes")),
            MDButton(MDButtonText(text="Año"), style="filled" if self.current_filtro=="año" else "outlined", on_release=lambda x: self._set_filtro("año")),
            orientation="horizontal", adaptive_height=True, spacing="8dp",
        )
        export_row = action_bar(
            MDButton(MDButtonText(text="Export Operativo CSV"), style="outlined", on_release=lambda x: self._export("operativo")),
            MDButton(MDButtonText(text="Export Financiero CSV"), style="outlined", on_release=lambda x: self._export("financiero")),
            MDButton(MDButtonText(text="Export KPIs CSV"), style="text", on_release=lambda x: self._export("kpis")),
        )
        export_pdf_row = action_bar(
            MDButton(MDButtonText(text="PDF Operativo"), style="filled", on_release=lambda x: self._export_pdf("operativo")),
            MDButton(MDButtonText(text="PDF Financiero"), style="outlined", on_release=lambda x: self._export_pdf("financiero")),
            MDButton(MDButtonText(text="PDF KPIs"), style="text", on_release=lambda x: self._export_pdf("kpis")),
        )

        content = MDBoxLayout(orientation="vertical", adaptive_height=True, size_hint_x=1, padding="16dp", spacing="12dp")
        content.add_widget(MDLabel(text="Reportes e Inteligencia — Colombia COP DIAN", font_style="Headline", role="large", halign="center", adaptive_height=True))
        content.add_widget(MDLabel(text="Genérico abarrotes/electrónica — IVA 19% — offline tickets incluidos — COP", font_style="Body", role="small", halign="center", theme_text_color="Secondary", adaptive_height=True))
        content.add_widget(filt_row)
        content.add_widget(export_row)
        content.add_widget(export_pdf_row)

        # ── Operativos §10 ──
        content.add_widget(MDLabel(text="Operativos", font_style="Title", role="large", adaptive_height=True, padding=(0,"12dp",0,0)))
        op_grid = MDGridLayout(cols=2, spacing="10dp", adaptive_height=True, size_hint_x=1)
        for titulo, val, col in [
            (f"Ventas día ({ventas_dia['count']} docs)", f"${ventas_dia['total']:,.0f} COP", "#009688"),  # SUCCESS_BG
            (f"Ventas semana ({ventas_sem['count']})", f"${ventas_sem['total']:,.0f} COP", "#03a9f4"),  # INFO_BG
            (f"Ventas mes ({ventas_mes['count']})", f"${ventas_mes['total']:,.0f} COP", "#FFC107"),  # WARNING_BG
            (f"Ventas año ({ventas_anio['count']})", f"${ventas_anio['total']:,.0f} COP", "#00796b"),  # Púrpura
            ("Ticket promedio COP", f"${ticket:,.0f} COP", "#009688"),  # PRIMARY_COLOR
            ("Productos", f"{len(repo.list_products())} SKU", "#757575"),  # Marrón
        ]:
            op_grid.add_widget(MDCard(MDLabel(text=titulo, font_style="Body", role="small", halign="center", adaptive_height=True), MDLabel(text=val, font_style="Title", role="medium", halign="center", theme_text_color="Custom", text_color=col, adaptive_height=True), orientation="vertical", padding="12dp", size_hint_y=None, height="90dp", style="elevated"))
        content.add_widget(op_grid)

        # Gráfico 7 días
        sales_chart_data = [{"label": d["day"], "value": d["total"]} for d in sales_by_period]
        content.add_widget(BarChart(data=sales_chart_data, title="Ventas últimos 7 días COP"))

        # Top 10 y menos vendidos
        content.add_widget(HorizontalBarChart(data=[{"label": p["name"][:14], "value": p["sold"], "text": f"{p['sold']} uds"} for p in top], title="Top 10 productos más vendidos"))
        content.add_widget(HorizontalBarChart(data=[{"label": p["name"][:14], "value": p["sold"], "text": f"{p['sold']} uds"} for p in least], title="Productos menos vendidos (oportunidad)"))

        # Clientes y vendedores
        cli_data = [{"label": c["client"][:12], "value": c["total"], "text": f"${c['total']:,.0f}"} for c in clients]
        if cli_data:
            content.add_widget(HorizontalBarChart(data=cli_data, title="Clientes que más compran COP"))
        vend_data = [{"label": v["seller"][:12], "value": v["total"], "text": f"${v['total']:,.0f}"} for v in sellers]
        if vend_data:
            content.add_widget(HorizontalBarChart(data=vend_data, title="Vendedores más productivos COP"))

        # Margen por producto tabla
        self.margin_table = MDDataTable(size_hint=(1, None), height="280dp", use_pagination=False, column_data=flex_columns(1000, ("SKU", 1), ("Producto", 2.2), ("Vend", 0.9), ("Margen COP", 1.6), ("Margen %", 1.1)), row_data=[(m["sku"], m["name"][:12], str(m["sold"]), f"${m['margin_total']:,.0f}", f"{m['margin_pct']:.1f}%") for m in margin])
        content.add_widget(MDCard(MDLabel(text="Margen ganancia por producto COP", font_style="Title", role="small", adaptive_height=True), self.margin_table, orientation="vertical", padding="12dp", spacing="8dp", style="outlined", size_hint_y=None, height="340dp"))

        # ── Financieros §10 ──
        content.add_widget(MDLabel(text="Financieros", font_style="Title", role="large", adaptive_height=True, padding=(0,"12dp",0,0)))
        fin_grid = MDGridLayout(cols=2, spacing="10dp", adaptive_height=True, size_hint_x=1)
        for titulo, val, col in [
            ("Ingresos (Pagada)", f"${estado['ingresos']:,.0f} COP", "#009688"),  # SUCCESS_BG
            ("Costo ventas", f"${estado['costo']:,.0f} COP", "#F44336"),  # ERROR_BG
            ("Bruto", f"${estado['bruto']:,.0f} COP", "#03a9f4"),  # INFO_BG
            ("Impuestos IVA 19% DIAN", f"${impuestos['iva_19']:,.0f} COP", "#FFC107"),  # WARNING_BG
            ("Neto", f"${estado['neto']:,.0f} COP", "#00796b"),  # Púrpura
            ("Flujo neto", f"${flujo['neto']:,.0f} COP", "#009688"),  # PRIMARY_COLOR
        ]:
            fin_grid.add_widget(MDCard(MDLabel(text=titulo, font_style="Body", role="small", halign="center", adaptive_height=True), MDLabel(text=val, font_style="Title", role="medium", halign="center", theme_text_color="Custom", text_color=col, adaptive_height=True), orientation="vertical", padding="12dp", size_hint_y=None, height="90dp", style="elevated"))
        content.add_widget(fin_grid)
        # detalle flujo + valorizado + CxC/CxP
        content.add_widget(MDCard(
            MDLabel(text=f"Flujo efectivo: entradas ${flujo['entradas']:,.0f} COP — salidas ${flujo['salidas']:,.0f} COP — neto ${flujo['neto']:,.0f} COP", font_style="Body", role="small", adaptive_height=True),
            MDLabel(text=f"Valor inventario: costo {inv['cost_fmt']} COP / venta {inv['sale_fmt']} COP — {inv['units']} uds", font_style="Body", role="small", adaptive_height=True),
            MDLabel(text=f"CxC deuda ${cxc_total:,.0f} COP — CxP deuda ${cxp_total:,.0f} COP — impuestos IVA 19% ${impuestos['iva_19']:,.0f} COP", font_style="Body", role="small", adaptive_height=True),
            orientation="vertical", padding="12dp", spacing="4dp", style="outlined", size_hint_y=None, height="110dp",
        ))

        # ── KPIs §10 ──
        content.add_widget(MDLabel(text="KPIs", font_style="Title", role="large", adaptive_height=True, padding=(0,"12dp",0,0)))
        kpi_grid = MDGridLayout(cols=2, spacing="10dp", adaptive_height=True, size_hint_x=1)
        for titulo, val, col in [
            (f"Rotación inventario {kpis['rotacion']:.2f}x", f"Días {kpis['dias_inventario']:.0f} días", "#FFC107"),  # Naranja rojizo
            (f"Tasa conversión {kpis['conversion']:.0f}%", f"Margen bruto {kpis['margen_bruto_pct']:.1f}%", "#00796b"),  # Índigo
            (f"Margen neto {kpis['margen_neto_pct']:.1f}%", f"Punto equilibrio ${kpis['punto_equilibrio']:,.0f} COP", "#757575"),  # Azul gris
            ("Costos fijos mes", f"${kpis['costos_fijos']:,.0f} COP", "#757575"),  # Marrón
        ]:
            kpi_grid.add_widget(MDCard(MDLabel(text=titulo, font_style="Body", role="small", halign="center", adaptive_height=True), MDLabel(text=val, font_style="Title", role="small", halign="center", theme_text_color="Custom", text_color=col, adaptive_height=True), orientation="vertical", padding="12dp", size_hint_y=None, height="85dp", style="elevated"))
        content.add_widget(kpi_grid)
        content.add_widget(MDLabel(text="Fórmulas: Rotación=costo/promedio inventario | Días=365/rotación | Conversión=Pagada/(Cot+Ped+Pagada) | Equilibrio=fijos/margen bruto", font_style="Body", role="small", theme_text_color="Secondary", adaptive_height=True))

        # Stock por categoría
        cat_sales = repo.get_category_sales()
        content.add_widget(HorizontalBarChart(data=[{"label": c["name"][:12], "value": c["stock"], "text": f"{c['stock']} uds"} for c in cat_sales], title="Stock por categoría — abarrotes/electrónica"))

        self.add_widget(MDBoxLayout(create_topbar("Reportes"), MDScrollView(content, do_scroll_x=False), orientation="vertical"))

    def _set_filtro(self, rango):
        self.current_filtro = rango
        self._build_ui()
        MDSnackbar(MDSnackbarText(text=f"Filtro {rango}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.5).open()

    def _export(self, tipo):
        try:
            path = repo.export_reporte_csv(tipo)
            MDSnackbar(MDSnackbarText(text=f"Exportado {tipo}: {path}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.6).open()

    def _export_pdf(self, tipo):
        try:
            path = repo.export_reporte_pdf(tipo)
            MDSnackbar(MDSnackbarText(text=f"PDF {tipo}: {path}"), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.8).open()
        except ValueError as e:
            MDSnackbar(MDSnackbarText(text=str(e)), y=dp(24), pos_hint={"center_x":0.5}, size_hint_x=0.7).open()

    def on_enter(self, *args):
        self._build_ui()
