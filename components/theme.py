"""Sistema UI/UX central — paleta Material Design Teal + layout óptimo.

Paleta: Colores basados en Material Design con tonos teal/turquesa como
color principal, azul claro como acento, y esquema de texto estándar.

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

# ── Paleta Material Design Teal ──
PRIMARY_COLOR = "#009688"         # Primary color - teal
LIGHT_PRIMARY = "#b2dfdb"         # Light primary color
DARK_PRIMARY = "#00796b"          # Dark primary color
ACCENT_COLOR = "#03a9f4"          # Accent color - light blue

# Text & Icons
TEXT_ICONS = "#FFFFFF"            # Text / Icons on colored backgrounds
PRIMARY_TEXT = "#212121"          # Primary text color
SECONDARY_TEXT = "#757575"        # Secondary text color
DIVIDER_COLOR = "#BDBDBD"         # Divider color

# Fondos y superficies
SURFACE_LIGHT = "#F5F5F5"         # fondo claro
SURFACE_CARD = "#FFFFFF"          # tarjetas
BACKGROUND_GRADIENT_START = "#FAFAFA"
BACKGROUND_GRADIENT_END = "#EEEEEE"

# Estados con mejor contraste
SUCCESS = "#FFFFFF"
SUCCESS_BG = "#4CAF50"
WARNING = "#FFFFFF"
WARNING_BG = "#FFC107"
ERROR = "#FFFFFF"
ERROR_BG = "#F44336"
INFO = "#FFFFFF"
INFO_BG = "#2196F3"

# ── Paleta dashboard teal/azul ──
DASH_BLUE = "#03a9f4"       # ventas - accent blue
DASH_RED = "#ef5350"        # compras - red
DASH_GREEN = "#66bb6a"      # ganancias - green
DASH_INDIGO = "#5c6bc0"     # productos - indigo
DASH_TEAL = "#009688"       # clientes - primary teal
DASH_LIME = "#9ccc65"       # proveedores - lime
DASH_ORANGE = "#ffa726"     # alertas - orange
DASH_SLATE = "#78909c"      # histórico - blue grey
DASH_CRIMSON = "#ec407a"    # por vencer - pink
DASH_CYAN = "#26c6da"       # créditos - cyan
DASH_PINK = "#ab47bc"       # promociones - purple
DASH_PURPLE = "#7e57c2"     # usuarios - deep purple


def stat_card(color_hex, value, label, icon, on_release=None):
    """Tarjeta estadística con gradiente sutil y sombra."""
    left = MDBoxLayout(
        MDLabel(text=value, font_style="Headline", role="medium",
                theme_text_color="Custom", text_color=get_color_from_hex(TEXT_ICONS),
                adaptive_height=True),
        MDLabel(text=label, font_style="Body", role="medium",
                theme_text_color="Custom", text_color=get_color_from_hex("#E0E0E0"),
                adaptive_height=True),
        orientation="vertical", spacing="4dp", adaptive_height=True,
        size_hint_x=0.7,
    )
    right = MDBoxLayout(
        MDIcon(icon=icon, theme_text_color="Custom", text_color=get_color_from_hex("#E0E0E0"),
               font_size="48sp", halign="right", valign="middle"),
        size_hint_x=0.3,
    )
    body = MDBoxLayout(left, right, orientation="horizontal",
                       spacing="12dp", padding="16dp", adaptive_height=True)
    card = MDCard(
        body, orientation="vertical", padding="2dp",
        size_hint_y=None, height="120dp", style="filled",
        radius=[12, 12, 12, 12],
    )
    if on_release is not None:
        card.bind(on_release=on_release)
    card.md_bg_color = get_color_from_hex(color_hex)
    return card


def stat_grid(cards, cols=4):
    """Grilla de tarjetas estadísticas que llena el ancho."""
    return MDGridLayout(
        *cards, cols=cols, spacing="16dp", padding="16dp",
        adaptive_height=True, size_hint_x=1,
    )


def apply_theme(app):
    """Tema claro Material Design con paleta teal. Llamar en MDApp.build()."""
    app.theme_cls.theme_style = "Light"
    app.theme_cls.primary_palette = PRIMARY_COLOR
    app.theme_cls.accent_palette = ACCENT_COLOR
    app.theme_cls.theme_style_switch_animation = True


def action_bar(*buttons, per_row=3):
    """Barra de acciones: reparte ancho por igual y envuelve filas.

    - 1-3 botones → una fila; 4 → 2+2; 5-6 → 3+3; 7+ → de a `per_row`.
    Cada botón ocupa su fracción óptima (size_hint_x=1) con altura 44dp.
    Botones uniformes con esquinas redondeadas.
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
            b.height = dp(44)
            b.radius = [8, 8, 8, 8]  # esquinas redondeadas uniformes
        except Exception:
            pass
    return MDGridLayout(
        *buttons,
        cols=cols,
        spacing="10dp",
        padding=(0, "8dp", 0, "8dp"),
        adaptive_height=True,
        size_hint_x=1,
    )


def flex_columns(total, *specs):
    """Columnas proporcionales para MDDataTable.

    total: ancho objetivo en dp (llenar el área de contenido).
    specs: tuplas (nombre, peso). Retorna column_data con dp() que suman
    exactamente `total` (corrige redondeo en la última columna).
    
    Ahora con anchos más equilibrados para evitar columnas muy anchas.
    """
    weights = [max(float(w), 0.1) for _, w in specs]
    acc = sum(weights)
    widths = [round(total * w / acc) for w in weights]
    widths[-1] += total - sum(widths)  # ajuste de redondeo
    return [(name, dp(w)) for (name, _), w in zip(specs, widths)]


def uniform_button(text, style="filled", on_release=None, icon=None):
    """Crea un botón uniforme con estilo consistente."""
    from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
    
    content = []
    if icon:
        content.append(MDButtonIcon(icon=icon))
    content.append(MDButtonText(text=text))
    
    btn = MDButton(
        *content,
        style=style,
        theme_width="Custom",
        size_hint_x=None,
        size_hint_y=None,
        height=dp(44),
        width=dp(140),
        radius=[8, 8, 8, 8],
    )
    if on_release:
        btn.bind(on_release=on_release)
    return btn
