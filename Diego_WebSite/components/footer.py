import reflex as rx
import datetime
from Diego_WebSite.styles.styles import Size as Size
from Diego_WebSite.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='logo.png', 
            height='100px',
            alt='Logotipo de Diego WebSite. Una \'de\' entre llaves.' #accecibilidad
        ),
        rx.link(
            f'© 2024-{datetime.date.today().year} Diego By Diego Catrileo.',
            font_size=Size.MEDIUM.value,
            href='https://chatgpt.com/',
            is_external=True,  
        ),
        rx.text('INGENIERO CIVIL INDUSTRIAL.', 
                font_size=Size.MEDIUM.value
        ),
        spacing='0px',
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        color= TextColor.FOOTER.value,
        align_items='center'
    )