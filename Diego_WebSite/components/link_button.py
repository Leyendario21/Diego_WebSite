import reflex as rx
import Diego_WebSite.styles.styles as styles
from Diego_WebSite.styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str, color: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    height='35px',
                    margin=styles.Size.MEDIUM.value,
                    alt=title #accecibilidad
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing=styles.Size.SMALL.value,
                    margin=styles.Size.SMALL.value,
                    align_items='center',
                    pagging_right= Size.SMALL.value
                    
                ),
                width= '100%',
                justify_content='center'
            ),
             style={
                'background_color': color,
            }
        ),
        justify_content='center',   
        href=url,
        is_external=True,
        width='100%'
    )
