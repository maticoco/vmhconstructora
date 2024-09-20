import reflex as rx

from rxconfig import config
from ..components.navbar import navbar_user
from ..components.footer import footer
from ..components.contact_form import contact_form
from ..components.whatsapp_button import whatsapp_button
from ..styles.styles import color , Size, style
from ..services.email_service import EmailServiceState


@rx.page(route="/contact", title="Contacto",on_load=EmailServiceState.clear)
def contact() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar_user(),
        whatsapp_button(),
        
        contact_form(),
        footer(),
        
        
        spacing="5",
        #justify="center",
        min_height="100vh",
        align="center",
        
    width="100%",    
    )
