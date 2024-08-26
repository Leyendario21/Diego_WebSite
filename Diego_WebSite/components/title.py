import reflex as rx
import Diego_WebSite.styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size='6',
        style=styles.title_style
    )