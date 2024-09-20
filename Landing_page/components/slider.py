import reflex as rx
from ..styles.styles import Size

class Slider(rx.Component):
    library = "nuka-carousel"
    tag = "Carousel"
    autoplay: rx.Var[bool]
    showDots: rx.Var[bool]
    wrapMode: rx.Var[str]
    autoplayInterval: rx.Var[int]
    scrollDistance: rx.Var[str]

# Definir el componente slider para desktop
def slider_component_desktop(images):
    image_components = [
        rx.image(src=img["src"], width="90vw", height=Size.SLIDERDESKTOP.value) for img in images
    ]
    
    return Slider(
        children=image_components,  # Los componentes de imagen se pasan como hijos
        autoplay=True,
        showDots=True,
        autoplayInterval=5000,
        scrollDistance="slide",
        wrapMode="wrap",
    )

# Definir el componente slider para mobile/tablet con otro tamaño
def slider_component_mobile(images):
    image_components = [
        rx.image(src=img["src"], width="90vw", height=Size.SLIDERMOBILE.value)  # Nuevo tamaño para mobile/tablet
        for img in images
    ]
    
    return Slider(
        children=image_components,  # Los componentes de imagen se pasan como hijos
        autoplay=True,
        showDots=True,
        autoplayInterval=5000,
        scrollDistance="slide",
        wrapMode="wrap",
    )

# Componente que maneja las dos versiones según el dispositivo
def slider_component(images):
    return rx.fragment(
        rx.desktop_only(
            slider_component_desktop(images)  # Solo mostrar en desktop
        ),
        rx.mobile_and_tablet(
            slider_component_mobile(images)  # Solo mostrar en mobile/tablet
        )
    )
