import reflex as rx
from Diego_WebSite.components.navbar import navbar
from Diego_WebSite.components.footer import footer
from Diego_WebSite.views.header.header import header
from Diego_WebSite.views.links.links import links
from Diego_WebSite.views.sponsors.sponsors import sponsors
from Diego_WebSite.components.gifs import gif
import Diego_WebSite.styles.styles as styles
from Diego_WebSite.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                gif(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.BIG.value,
                padding= Size.SMALL.value, #Quisas probar con otro tamaño de padding
                align_items='center'  
            )     
        ),
        footer()
    )
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title= 'Diego WebSite | Prueba de pagina web',
    description= 'Hola, mi nombre es Diego Catrileo. Soy Ingeninero Civil Industrial',
)

#'reflex deploy' (despliega la pagina)
#'reflex deployments delete diegowebsite' (linea de comando para eliminar mi pagina desplegada)
#'reflex export --frontend-only (exportar para subir a un servidor)
