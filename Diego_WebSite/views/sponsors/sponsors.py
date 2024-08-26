import reflex as rx
from Diego_WebSite.components.title import title
from Diego_WebSite.components.link_sponsor import link_sponsor
from Diego_WebSite.styles.styles import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title('Colaboran'),
        rx.flex(
            link_sponsor(
                'elgato.png',
                'https://naruto.fandom.com/es/wiki/Naruto_Wiki',
                'Naruto'
            ),
            link_sponsor(
                'mvp.png',
                'https://jkanime.net/naruto-shippuden/',
                'Naruto alzando en brazos a Hinata'
            ),
            spacing=Size.LARGE.value,
            flex_wrap='wrap'
        ),
        width='100%',
        spacing=Size.DEFAULT.value
    )