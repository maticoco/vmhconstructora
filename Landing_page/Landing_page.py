"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components.navbar import navbar_user
from .components.footer import footer
from .components.body import body
from .components.whatsapp_button import whatsapp_button
from .styles.styles import color , Size, style

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar_user(),
        whatsapp_button(),
        body(),
        footer(),
        
        
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center",
        
    width="100%",    
    )


app = rx.App(style=style,
             stylesheets=[
                "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto:wght@400;500&display=swap",
                    ],
            overlay_components=[rx.toast.provider()],)
app.add_page(index)
