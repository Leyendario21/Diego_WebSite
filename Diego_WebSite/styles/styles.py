import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight


# Constantes
MAX_WIDTH='560px'

#fuentes
STYLESHEETS=[
        'https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700'
        '&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'
]

#Tamaños
class Size(Enum):
    ZERO='0em'
    SMALL='0.5em'
    MEDIUM= '0.8em'
    DEFAULT='1em'
    LARGE='1.5em'
    BIG='2em'
    VERY_BIG='8em'


#styles
BASE_STYLE= {
    'font_family' : Font.DEFAULT.value,
    'font_weight' : FontWeight.LIGHT.value,
    'background_color' : Color.BACKGROUND.value,
    rx.heading: {
        'color': TextColor.HEADER.value,
        'font_family' : Font.TITLE.value,
        'font_weight' : FontWeight.MEDIUM.value,
    },
    rx.button: {
        'width':'100%',
        'height':'100%',
        'padding': Size.SMALL.value,
        'border_radius': Size.DEFAULT.value,
        'background_color' : Color.CONTENT.value,
        'text_aling' : 'start',        
        '_hover':{
            'background_color' : Color.CONTENT.value
        }
    },
    rx.link:{
        'text_decoration': 'none',
        '_hover': {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size= Size.LARGE.value
)
title_style = dict(
    width='100%', 
    padding_top= Size.DEFAULT.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size= Size.DEFAULT.value, 
)

button_body_style = dict(
    font_size= Size.MEDIUM.value,
    color= TextColor.BODY.value 
)