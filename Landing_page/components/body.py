import reflex as rx
from ..styles.styles import Size, typography_styles, layout_styles, section_style, body_styles
from .slider import slider_component

# Definir las variables que se podrán cambiar
nombre_constructora = "VMH Constructora"

# Componente para mostrar un encabezado con el estilo correspondiente
def heading(text, size=Size.TITLE.value,):
    style = typography_styles["heading"].copy()
    style["font_size"] = size
    
    return rx.heading(text, **style)

# Componente para mostrar un párrafo con el estilo correspondiente
def paragraph(text):
    return rx.text(text, **typography_styles["text"])



# Sección principal de bienvenida
def seccion_bienvenida():
    return rx.grid(
        rx.box(
            rx.flex(
            heading(f"Bienvenidos a {nombre_constructora}",size=Size.BIG.value),
            seccion_slider_renders(),
            direction="column",
            justify="center",
            align="center",
            ),
            heading(f"El Futuro de la Vivienda Sostenible y Duradera"),
            paragraph(
                f"En {nombre_constructora}, nuestra misión es transformar la manera en que construimos y vivimos, proporcionando soluciones habitacionales que no solo cumplen, sino que superan las expectativas del mercado actual. Nuestras casas, construidas con placas EPS y columnas reforzadas, representan una verdadera innovación en el sector de la construcción. Nos especializamos en crear hogares que ofrecen una durabilidad incomparable, eficiencia energética, y un diseño moderno que se adapta a las necesidades de las familias del siglo XXI."
            ),
            **layout_styles["box"],
            **section_style,  # Aplicar estilo de la sección con sombra difusa
        ),
        columns="1fr",
        spacing="4",
        
    )

# Sección para los sliders de modelos
def seccion_slider_modelos():
    return rx.grid(
        rx.box(
            seccion_slider_eps(),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Sección para EPS y columnas reforzadas
def seccion_eps_columnas():
    return rx.grid(
        rx.box(
            heading("Placas EPS y Columnas Reforzadas: Innovación al Servicio del Bienestar"),
            paragraph(
                f"En {nombre_constructora}, creemos firmemente que la calidad de un hogar comienza en sus cimientos. Por eso, hemos adoptado el uso de placas EPS, un material revolucionario que cambia las reglas del juego en la construcción, y columnas reforzadas, que proporcionan el soporte estructural más sólido posible."
            ),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Slider para Modelos y diseños
def seccion_slider_renders():
    return slider_component([
        {"src": "18.jpeg"},
        {"src": "23.jpeg"},
        {"src": "24.jpeg"},
        {"src": "26.jpeg"},
        {"src": "22.jpeg"},
        {"src": "22bis.jpg"},
    ])

# Slider para EPS y columnas
def seccion_slider_eps():
    return slider_component([
        {"src": "19.jpeg"},
        {"src": "20.jpeg"},
        {"src": "21.jpeg"},
    ])

# Sección para describir las placas EPS
def seccion_placas_eps():
    return rx.grid(
        rx.box(
            heading("¿Qué son las Placas EPS?"),
            paragraph("Las placas EPS son un material compuesto de polímeros avanzados que destacan por su ligereza, flexibilidad y, al mismo tiempo, su extrema resistencia estructural. Estas son algunas de sus principales características:"),
            rx.grid(
                rx.box(
                    paragraph("• Resistencia superior: Ideal para soportar cargas pesadas sin comprometer la integridad estructural."),
                    paragraph("• Longevidad: Resistente a la corrosión, a los impactos climáticos y a los factores externos como la humedad."),
                    paragraph("• Ligero pero resistente: Reduce el tiempo y costo de construcción."),
                    direction="column",
                    spacing="2"
                ),
                columns="1fr",
                
            ),
            rx.image(src="25.jpeg"),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Sección para las columnas reforzadas
def seccion_columnas_reforzadas():
    return rx.grid(
        rx.box(
            heading("Columnas Reforzadas: La Base de la Seguridad"),
            paragraph("Las columnas reforzadas aseguran que cada vivienda esté preparada para enfrentar cualquier reto estructural, desde movimientos sísmicos hasta condiciones climáticas adversas."),
            rx.grid(
                rx.box(
                    paragraph("• Tecnología de punta: Columnas reforzadas con materiales de acero de alta resistencia."),
                    paragraph("• Preparadas para el futuro: Diseño modular que facilita futuras expansiones."),
                    paragraph("• Estabilidad a largo plazo: Diseñadas para durar décadas sin mantenimiento intensivo."),
                    direction="column",
                    spacing="2"
                ),
                columns="1fr",
                
            ),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Sección para diseño inteligente y eficiencia energética
def seccion_diseno_eficiencia():
    return rx.grid(
        rx.box(
            heading("Diseño Inteligente y Eficiencia Energética: Hogares Pensados para el Mañana"),
            paragraph(
                f"En {nombre_constructora}, entendemos que un hogar no es solo un espacio físico; es un lugar donde las familias crecen y los sueños se hacen realidad. Nuestras viviendas están diseñadas para ser eficientes y sostenibles."
            ),
            heading("Eficiencia Energética"),
            rx.grid(
                rx.box(
                    paragraph("Las placas EPS actúan como un excelente aislante térmico, lo que significa que las viviendas mantienen temperaturas interiores estables con un consumo mínimo de energía."),
                    paragraph("• Aislamiento de primer nivel: Mantiene el hogar fresco en verano y cálido en invierno."),
                    paragraph("• Reducción de emisiones: Materiales de bajo impacto ambiental que reducen las emisiones de CO₂."),
                    direction="column",
                    spacing="2"
                ),
                columns="1fr",
                
            ),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Sección para sistemas de energía renovable
def seccion_energia_renovable():
    return rx.grid(
        rx.box(
            heading("Sistemas de Energía Renovable Integrados"),
            paragraph("Nuestras viviendas están diseñadas para ser compatibles con soluciones de energía renovable, como paneles solares y sistemas de recolección de agua de lluvia."),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Sección de llamado a la acción
def seccion_llamado_accion():
    return rx.grid(
        rx.box(
            heading("¡Haz Realidad Tu Hogar Ideal con Nosotros!"),
            paragraph(
                f"En {nombre_constructora}, estamos comprometidos a construir no solo casas, sino hogares para el futuro. Cada proyecto está diseñado para ofrecer lo mejor en términos de calidad, sostenibilidad y tecnología."
            ),
            paragraph("No dejes pasar esta oportunidad de invertir en el hogar que siempre soñaste. Contáctanos hoy mismo para recibir más información."),
            **layout_styles["box"],
            **section_style,
        ),
        columns="1fr",
        spacing="4",
        
    )

# Componente principal del body que agrega todas las secciones
def body():
    return rx.grid(
        seccion_bienvenida(),
        seccion_slider_modelos(),
        rx.divider(),
        seccion_eps_columnas(),
        rx.divider(),
        seccion_placas_eps(),
        rx.divider(),
        seccion_columnas_reforzadas(),
        rx.divider(),
        seccion_diseno_eficiencia(),
        rx.divider(),
        seccion_energia_renovable(),
        rx.divider(),
        seccion_llamado_accion(),
        spacing="7",
        padding_x=Size.SUPERBIG.value,
        padding_y=Size.SUPERBIG.value,
        direction="column",
        align="center",
        **body_styles
    )
