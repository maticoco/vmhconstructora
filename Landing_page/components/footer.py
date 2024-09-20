import reflex as rx
from ..styles.styles import color , Size

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href,is_external=True)

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", href="https://www.instagram.com/"),
        

        spacing="3",
        justify="end",
        width="100%",
    )

def footer() -> rx.Component:
    return      rx.el.footer(
                    rx.vstack(
                        rx.divider(),
                        rx.hstack(
                            rx.hstack(
                                    footer_item("Privacy Policy", "/#"),
                                    footer_item("Terms of Service", "/#"),
                                    spacing="4",
                                    align="center",
                                    width="100%",
                                    ),
                                    socials(),
                                    justify="between",
                                    width="100%",
                                ),
                                spacing="5",
                                width="100%",
                            ),
                            
                            width="100%",
                            height="100%",
                            padding="1em",
                            bg=rx.color(color, 3),
                            
                            
                            )