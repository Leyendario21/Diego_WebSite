import reflex as rx
from Diego_WebSite.components.link_button import link_button
from Diego_WebSite.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title('Comunidad'),
        link_button(
            'Twitch', 
            'Los mejores Directos',
            'icons/twitch.gif', 
            'https://www.twitch.tv/',
            '#8a2be2'
        ),
        link_button(
            'YouTube', 
            'Video de curiosidades',
            'icons/youtube.gif', 
            'https://www.youtube.com/',
            '#b22222'
        ),
        link_button(
            'YouTube (Canal Secundario)', 
            'Videos de chismes \n(De los que le gusta a mi Polola)', 
            'icons/youtube.gif', 
            'https://www.youtube.com/watch?v=TLo9ryHrMB4',
            '#b22222'
        ),
        link_button(
            'Discord', 
            'La mejor comunidad',
            'icons/discord.svg', 
            'https://discord.com/',
            '#6a5acd'
        ),
        title('Contacto'),
        link_button(
            'Gmail', 
            'Correo Personal',
            'icons/gmail.svg', 
            'https://mail.google.com/mail/u/1/#inbox?compose=GTvVlcSBpDwRQsqKhgNVHHFDzmsrKkbxBtbjQDMQKqKQQCbhDssnfvZVtRGhsrlxbsdqVkpGvRPTn', #A parecer en Celular no funciona bien
            '#4169e1'
        ),
        link_button(
            'My Public Inbox', 
            'Respuestas rapidas y con preferencia \n(Pero solo para mi polola o me pega :C)',
            'icons/inbox.svg', 
            'https://mypublicinbox.com/',
            '#ff6347',
        ),
        white_space='pre-wrap',
        width='100%',
        align_items='center'      
    )