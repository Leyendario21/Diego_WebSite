import reflex as rx


def gif() -> rx.Component:
    return rx.image(
            src='naruto.gif',
            height='175px',
            margin_top='20px'
        )