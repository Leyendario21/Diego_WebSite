import reflex as rx
from Diego_WebSite.styles.styles import Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value,
            alt=alt #accecibilidad
        ),
        href=url,
        is_external=True,
    )