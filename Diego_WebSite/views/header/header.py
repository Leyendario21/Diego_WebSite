import reflex as rx
from Diego_WebSite.components.link_icon import link_icon
from Diego_WebSite.components.info_text import info_text
from Diego_WebSite.styles.styles import Size as Size
from Diego_WebSite.styles.colors import TextColor as TextColor
from Diego_WebSite.styles.colors import Color as Color


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                    fallback='DC', 
                    size='7',
                    src='avatar.jpg',
                    color=TextColor.BODY.value,
                    bg=Color.PRIMARY.value,
                    border='3px solid',
                    border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading('👋😊 Diego Catrileo.', size='5', margin_top='23px'),
                rx.text('@Leyendario', margin_bottom='5px', color=TextColor.BODY.value),
                rx.hstack(
                    link_icon(
                        'icons/instagram.svg', 
                        'https://www.instagram.com/',
                        'instagram'
                    ),
                    link_icon(
                        'icons/x.svg', 
                        'https://x.com/?lang=es',
                        'Twitter/X'
                    ),
                    link_icon(
                        'icons/facebook.svg', 
                        'https://www.facebook.com/?locale=es_LA',
                        'Facebook/Meta'
                    ),
                    spacing=Size.DEFAULT.value
                ),
                spacing='0px'
            ),
            spacing=Size.DEFAULT.value
        ),
        
        rx.flex(
            info_text('1', 'año de experiencia'),
            rx.spacer(),
            info_text('Tesis', 'Deteccion de fuga de hidrógeno utilizando Python'),
            rx.spacer(),
            info_text('Elba Denisse', 'es mi Polola y dice que solo pueden contactarme por asuntos laborales, nada de peucas locas 👀'),
            width='100%'
        ),
        rx.text(
            '''Soy un Ingeniero civil industrial recién titulado con una sólida formación académica y un firme compromiso con el desarrollo profesional. 
            A pesar de no contar con experiencia laboral previa en la industria, me encuentro emocionado por la oportunidad de aplicar mis conocimientos 
            teóricos en un entorno práctico y dinámico, además estoy dispuesto a aprender y aportar de manera proactiva al éxito de su empresa.''',
            text_align='justify',
            color= TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items='start'
    )