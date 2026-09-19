"""Sistema UI/UX central — paleta pastel clara + layout óptimo.

Paleta: KivyMD 2.0 genera el esquema Material 3 desde un seed color, que
puede ser cualquier hex (no solo paletas base). Usamos seeds pastel con
theme_style claro: nada oscuro.

Layout óptimo:
- action_bar(): rejilla adaptable — los botones reparten el ancho por igual
  y saltan de fila en pantallas angostas (adiós botones aplastados).
- flex_columns(): columnas de MDDataTable proporcionales que llenan el
  ancho disponible en vez de dejar huecos o cortar texto.
"""
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel, MDIcon

# ── Paleta pastel ──
PASTEL_PRIMARY = "#7FCEA0"      # menta pastel (seed del esquema M3)
PASTEL_SECONDARY = "#F5C99B"    # melocotón (referencia)
PASTEL_TERTIARY = "#C3B2E8"     # lavanda (referencia)

# Estados en tonos pastel (texto sobre fondo claro)
SUCCESS = "#2E7D4F"   # verde legible sobre pastel
SUCCESS_BG = "#A5D6A7"
WARNING = "#B26A00"
WARNING_BG = "#FFCC80"
ERROR = "#C62828"
ERROR_BG = "#EF9A9A"
INFO = "#1565C0"
INFO_BG = "#90CAF9"

# ── Paleta panel tipo GesNet: tarjetas sólidas, texto blanco ──
DASH_BLUE = "#29ABE2"    # caja
DASH_RED = "#E74C3C"     # compras mes
DASH_GREEN = "#5CB85C"   # ventas día
DASH_INDIGO = "#6C7EB8"  # invertido stock
DASH_TEAL = "#26A69A"    # proveedores
DASH_LIME = "#8BC34A"    # marcas/categorías
DASH_ORANGE = "#F39C12"  # presentaciones/unidades
DASH_SLATE = "#78909C"   # productos ingresados
DASH_CRIMSON = "#E53935" # perecederos/por caducar
DASH_CYAN = "#26C6DA"    # vencerán 30 días
DASH_PINK = "#EC407A"    # clientes
DASH_PURPLE = "#AB47BC"  # créditos pendientes


def stat_card(color_hex, value, label, icon, on_release=None):
    """Tarjeta estadística sólida estilo panel: valor grande + etiqueta
    en blanco a la izquierda, icono blanco a la derecha. Altura 110dp."""
    left = MDBoxLayout(
        MDLabel(text=value, font_style="Headline", role="medium",
                theme_text_color="Custom", text_color="white",
                adaptive_height=True),
        MDLabel(text=label, font_style="Label", role="small",
                theme_text_color="Custom", text_color=(1, 1, 1, 0.85),
                adaptive_height=True),
        orientation="vertical", spacing="2dp", adaptive_height=True,
        size_hint_x=0.7,
    )
    right = MDBoxLayout(
        MDIcon(icon=icon, theme_text_color="Custom", text_color=(1, 1, 1, 0.9),
               font_size="44sp", halign="right", valign="middle"),
        size_hint_x=0.3,
    )
    body = MDBoxLayout(left, right, orientation="horizontal",
                       spacing="8dp", padding="12dp", adaptive_height=True)
    card = MDCard(
        body, orientation="vertical", padding="4dp",
        size_hint_y=None, height="110dp", style="elevated",
    )
    if on_release is not None:
        card.bind(on_release=on_release)
    card.md_bg_color = get_color_from_hex(color_hex)
    return card


def stat_grid(cards, cols=4):
    """Grilla de tarjetas estadísticas que llena el ancho."""
    return MDGridLayout(
        *cards, cols=cols, spacing="12dp", padding="12dp",
        adaptive_height=True, size_hint_x=1,
    )


def apply_theme(app):
    """Tema claro pastel global. Llamar en MDApp.build()."""
    app.theme_cls.theme_style = "Light"
    app.theme_cls.primary_palette = PASTEL_PRIMARY
    app.theme_cls.theme_style_switch_animation = True


def action_bar(*buttons, per_row=3):
    """Barra de acciones: reparte ancho por igual y envuelve filas.

    - 1-3 botones → una fila; 4 → 2+2; 5-6 → 3+3; 7+ → de a `per_row`.
    Cada botón ocupa su fracción óptima (size_hint_x=1) con altura 40dp.
    """
    n = len(buttons)
    if n <= 3:
        cols = max(n, 1)
    elif n == 4:
        cols = 2
    else:
        cols = per_row
    for b in buttons:
        try:
            # theme_width Custom: si no, MDButton se encoge al texto
            # y size_hint_x no tiene efecto.
            b.theme_width = "Custom"
            b.size_hint_x = 1
            b.size_hint_y = None
            b.height = dp(40)
        except Exception:
            pass
    return MDGridLayout(
        *buttons,
        cols=cols,
        spacing="8dp",
        padding=(0, "6dp", 0, "6dp"),
        adaptive_height=True,
        size_hint_x=1,
    )


def flex_columns(total, *specs):
    """Columnas proporcionales para MDDataTable.

    total: ancho objetivo en dp (llenar el área de contenido).
    specs: tuplas (nombre, peso). Retorna column_data con dp() que suman
    exactamente `total` (corrige redondeo en la última columna).
    """
    weights = [max(float(w), 0.1) for _, w in specs]
    acc = sum(weights)
    widths = [round(total * w / acc) for w in weights]
    widths[-1] += total - sum(widths)  # ajuste de redondeo
    return [(name, dp(w)) for (name, _), w in zip(specs, widths)]
