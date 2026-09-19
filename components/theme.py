"""Sistema UI/UX central — paleta vibrante moderna + layout óptimo.

Paleta: Colores vibrantes y modernos con buen contraste para una interfaz
llamativa pero profesional. Usamos tonos saturados que destacan sin cansar
la vista.

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

# ── Paleta vibrante moderna ──
VIBRANT_PRIMARY = "#6C63FF"      # violeta vibrante (color principal)
VIBRANT_SECONDARY = "#00D9FF"    # cyan eléctrico (secundario)
VIBRANT_ACCENT = "#FF6582"       # rosa coral (acentos)
VIBRANT_SUCCESS = "#00C897"      # verde menta (éxito)
VIBRANT_WARNING = "#FFB400"      # amarillo dorado (advertencia)
VIBRANT_ERROR = "#FF3B30"        # rojo intenso (error)
VIBRANT_INFO = "#5E5CE6"         # índigo (información)

# Fondos y superficies
SURFACE_LIGHT = "#F8F9FA"        # fondo claro
SURFACE_CARD = "#FFFFFF"         # tarjetas
BACKGROUND_GRADIENT_START = "#F5F7FA"
BACKGROUND_GRADIENT_END = "#E8ECF1"

# Estados con mejor contraste
SUCCESS = "#FFFFFF"
SUCCESS_BG = "#00C897"
WARNING = "#FFFFFF"
WARNING_BG = "#FFB400"
ERROR = "#FFFFFF"
ERROR_BG = "#FF3B30"
INFO = "#FFFFFF"
INFO_BG = "#5E5CE6"

# ── Paleta dashboard vibrante ──
DASH_BLUE = "#4A90E2"       # ventas
DASH_RED = "#E74C3C"        # compras
DASH_GREEN = "#2ECC71"      # ganancias
DASH_INDIGO = "#6C63FF"     # productos
DASH_TEAL = "#00D9FF"       # clientes
DASH_LIME = "#C1E746"       # proveedores
DASH_ORANGE = "#FF9F43"     # alertas
DASH_SLATE = "#8395A7"      # histórico
DASH_CRIMSON = "#FD79A8"    # por vencer
DASH_CYAN = "#00CEC9"       # créditos
DASH_PINK = "#FF6582"       # promociones
DASH_PURPLE = "#A29BFE"     # usuarios


def stat_card(color_hex, value, label, icon, on_release=None):
    """Tarjeta estadística con gradiente sutil y sombra."""
    left = MDBoxLayout(
        MDLabel(text=value, font_style="Headline", role="medium",
                theme_text_color="Custom", text_color="white",
                adaptive_height=True),
        MDLabel(text=label, font_style="Body", role="medium",
                theme_text_color="Custom", text_color=(1, 1, 1, 0.9),
                adaptive_height=True),
        orientation="vertical", spacing="4dp", adaptive_height=True,
        size_hint_x=0.7,
    )
    right = MDBoxLayout(
        MDIcon(icon=icon, theme_text_color="Custom", text_color=(1, 1, 1, 0.85),
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
    """Tema claro vibrante global. Llamar en MDApp.build()."""
    app.theme_cls.theme_style = "Light"
    app.theme_cls.primary_palette = VIBRANT_PRIMARY
    app.theme_cls.accent_palette = VIBRANT_ACCENT
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
