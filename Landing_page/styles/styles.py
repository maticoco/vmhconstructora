import reflex as rx
from enum import Enum

# Definir colores y tema
color = "blue"
accent_color = "cyan"

style = theme = rx.theme(
    appearance="dark",
    has_background=True,
    radius="large",
    accent_color=accent_color,
    scaling="100%"
)

# Definir tamaños en un Enum para una fácil reutilización
class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    TITLE = "1.5em"
    BIG = "2em"
    SUPERBIG = "5em"
    CARDSIZE = "7em"
    CALLOUTSIZE = "9em"
    IMGBIG = "15em"
    FORMCONTACT = "38em"
    FORMCONTACTBIG = "88em"
    SLIDERDESKTOP = "720px"  # Tamaño para desktop
    SLIDERMOBILE = "300px"   # Tamaño más pequeño para mobile/tablet

# Definir fuentes
font_families = {
    "body": "Roboto",       # Fuente para el texto general
    "heading": "Poppins",   # Fuente para los encabezados
}

# Estilos generales
global_styles = {
    "font_family": font_families["body"],
    "font_size": "16px",
}

# Estilo para el body
body_styles = {
    "background": rx.color_mode_cond(
        light="linear-gradient(to right, #007bff, #00d2ff)",  # Degradado para tema claro
        dark="linear-gradient(to right, #004085, #0056b3)",   # Degradado para tema oscuro
    ),
    "color": "#333",                # Color de texto oscuro para buena legibilidad
    "font_family": font_families["body"],
    "line_height": "1.6",           # Línea de texto más alta para mayor claridad
    "padding": "1em 2em",           # Espacio interior para dar sensación de amplitud
    "margin": "0",                  # Sin márgenes extras
    "min_height": "100vh",          # Asegura que el contenido llene la pantalla
}

# Estilos de tipografía
typography_styles = {
    "text": {
        "font_family": font_families["body"],
        "font_size": Size.DEFAULT.value,
        "line_height": "1.5",
    },
    "heading": {
        "font_family": font_families["heading"],
        "font_size": Size.TITLE.value,
        "font_weight": "600",
        "margin_bottom": "0.5em",
    },
}

# Estilos interactivos para botones y enlaces
interactive_styles = {
    "button": {
        "font_family": font_families["heading"],
        "padding": "0.75em 1.25em",
        "font_size": Size.DEFAULT.value,
        "border": "none",
        "border_radius": "0.25rem",
        "cursor": "pointer",
        "background_color": accent_color,  # Botón de color de acento
        "color": "#fff",
        "_hover": {
            "background_color": rx.color(accent_color, 7)
        },
    },
    "link": {
        "font_family": font_families["body"],
        "textDecoration": "none",
        "color": color,
        "fontWeight": "bold",
        "cursor": "pointer",
        "_hover": {
            "textDecoration": "underline",
            "opacity": 0.8,
        },
    },
}

# Estilos de layout para tarjetas y contenedores
layout_styles = {
    "card": {
        "padding": "1.5em",
        "margin": "1em",
        "justify": "center",
        "align": "center",
        "border_radius": "0.5rem",
        
        "background_color": "#fff",
    },
    "box": {
        "padding": "1em",
        "margin": "1em 0",
        "border_radius": "0.25rem",
        
    },
}

# Estilo de fondo con degradado y borde difuminado para secciones basado en el modo de color
section_style = {
    "background": rx.color_mode_cond(
        light="linear-gradient(to left, white, #E0FFFF)",  # Degradado de blanco a cyan casi blanco para tema claro
        dark="linear-gradient(to left, white, #B0E0E6)"   # Degradado de blanco a celeste muy claro para tema oscuro
    ),
    "box_shadow": "0 0 20px 10px rgba(224, 255, 255, 0.5)",  # Sombra difusa que se fusiona con el fondo
}

# Estilos para la barra de navegación
navbar_styles = {
    "position": "sticky",
    "top": "0",
    "width": "100%",
    "z_index": "200",
    # Fondo degradado sólido
    "background_image": "linear-gradient(144deg, #0080FF, #00DDFB)",  # Degradado azul a cyan sólido
    # Intensificar y extender la sombra azul
    "box_shadow": "rgba(0, 128, 255, 0.6) 0px 5px 35px 0px",  # Sombra azul más intensa y extendida hacia abajo
}

# Estilos para los botones de tema claro/oscuro
dark_light_button_styles = {
    "color": rx.color_mode_cond(light=rx.color(color, 7), dark=rx.color(accent_color, 1)),
    "background_color": rx.color_mode_cond(light=rx.color(accent_color, 8), dark=rx.color(accent_color, 7)),
}

# Estilos para el contenido del menú móvil
menu_mobile_content_styles = {
    "border_radius": "1em",
    "box_shadow": "rgba(38, 222, 129, 0.8) 0 15px 30px -10px",
    "background_image": rx.color_mode_cond(
        light="linear-gradient(144deg, #0080FF, #00AF80 50%, #00FF80)",  # Degradado azul a verde para tema claro
        dark="linear-gradient(144deg, #0040FF, #008080 50%, #00FF80)"    # Degradado azul a verde para tema oscuro
    ),
    "box_sizing": "border-box",
    "color": rx.color_mode_cond(light="black", dark="white"),
    "opacity": 1,
}

# Estilos para las notificaciones
style_notify_dark = {
    'position': 'fixed',
    'top': Size.CALLOUTSIZE.value,
    'right': '20px',
    'z-index': '10000',
    'background-color': '#333',
    'padding': '20px 30px',
    'border-radius': '8px',
    'border': '2px solid #555',
    'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.6)',
    'font-family': font_families["body"],
    'font-size': Size.DEFAULT.value,
    'color': '#fff',
}

style_notify_light = {
    'position': 'fixed',
    'top': '150px',
    'right': '20px',
    'z-index': '10000',
    'background-color': '#f9f9f9',
    'padding': '20px 30px',
    'border-radius': '8px',
    'border': '2px solid #ccc',
    'box-shadow': '0 8px 16px rgba(0, 0, 0, 0.2)',
    'font-family': font_families["body"],
    'font-size': Size.DEFAULT.value,
    'color': '#333',
}

# Estilos combinados por categorías
component_styles = {
    **typography_styles,
    **interactive_styles,
    **layout_styles,
}

# Estilos adicionales
textmenu_style = {
    "font_family": font_families["heading"],
    "font_size": "1.2em",
    "font_weight": "bold",
    "box_shadow": f"{rx.color(color, 6)} 5px 5px, {rx.color(accent_color, 6)} 10px 10px",
    "textDecoration": "none",
    "color": "inherit",
    "cursor": "pointer",
    "border_radius": "0.25rem",
    "_hover": {
        "opacity": 0.5,
    },
}
