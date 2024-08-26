import reflex as rx
from Diego_WebSite.styles.styles import Size as Size
from Diego_WebSite.styles.colors import Color as Color
from Diego_WebSite.styles.colors import TextColor as TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.spacer(title, font_weight='bold', color=Color.PRIMARY.value),
        body, 
        spacing='4px',
        font_size=Size.MEDIUM.value,
        color= TextColor.BODY.value
    )