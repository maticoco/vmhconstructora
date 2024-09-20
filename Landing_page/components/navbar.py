import reflex as rx
from reflex.style import toggle_color_mode
from ..styles.styles import color, accent_color, Size, textmenu_style, navbar_styles, dark_light_button_styles, menu_mobile_content_styles
from .body import nombre_constructora

# Botón para cambiar el tema claro/oscuro
def dark_light_theme() -> rx.Component:
    return rx.button(
        rx.color_mode_cond(
            light=rx.icon("moon"),
            dark=rx.icon("sun"),
        ),
        **dark_light_button_styles,
        on_click=toggle_color_mode,
    )

# Componente de link en la navbar
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text, 
            size="5", 
            weight="medium", 
            style=textmenu_style, 
            padding_x=Size.BIG.value,
            padding_y=Size.SMALL.value,
            color=rx.color_mode_cond(light=rx.color(color, 11), dark=rx.color(accent_color, 1))  # Cambio de color en el link según el modo
        ), 
        href=url,
        high_contrast=True
    )

# Navbar para desktop y mobile
def navbar_user() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                heading_component(),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Contacto", "/contact"),
                    spacing="5",
                    justify="between"
                ),
                rx.spacer(),
                rx.vstack(
                    #dark_light_theme(),
                    padding=Size.DEFAULT.value,
                    align="end"
                ),
                align="center",
                padding_x=Size.DEFAULT.value,
                padding_bottom=Size.SMALL.value,
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                heading_component(),
                rx.spacer(),
                menu_mobile(),
                padding=Size.SMALL.value
            ),
            justify="between",
            align_items="center",
        ),
        **navbar_styles,
    )

# Componente del logo y nombre de la constructora
def heading_component() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/logo.png",
            width=Size.SUPERBIG.value,
            height="auto",
            border_radius="25%",
        ),
        rx.heading(
            nombre_constructora, 
            size="7", 
            weight="bold", 
            color=rx.color_mode_cond(light=rx.color(color, 11), dark=rx.color(color, 2)),
            high_contrast=True
        ),
        justify="start",
        align_items="center",
        padding=Size.DEFAULT.value,
    )

# Menú móvil
def menu_mobile() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.icon("menu", size=50)
        ),
        rx.menu.content(
            rx.menu.item("Home", on_click=rx.redirect("/#")),
            rx.menu.item("Contacto", on_click=rx.redirect("/contact")),
            **menu_mobile_content_styles
        ),
        justify="end",
    )
