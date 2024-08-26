import reflex as rx
import Diego_WebSite.styles.styles as styles
from Diego_WebSite.styles.styles import Size as Size
from Diego_WebSite.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.spacer(),
            rx.text('Diego', color=Color.PRIMARY.value),
            rx.text('WebSite', color=Color.SECONDARY.value, margin_left='-5px'),
            style=styles.navbar_title_style
        ),
        position='sticky',
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index='999',
        top='0'
    )