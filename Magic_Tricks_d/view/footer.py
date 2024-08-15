import reflex as rx
from Magic_Tricks_d.components.components import text_small
from Magic_Tricks_d.components.help_buttom import button_help
from Magic_Tricks_d.Styles.Colors import Color

#La diferencia entre los footers radica en la ausencia del boton flotante en "footer_alchemy"

LINK_DRIVE="https://drive.google.com/drive/folders/1DPl7I9CiPOqfxhTkORlNYqkjqKW1lqo7?usp=drive_link"

def footer_load()-> rx.Component:
    return rx.container(rx.hstack(
        rx.flex(
            rx.flex(
                rx.text(
                    "El siguiente link lleva al "
                ),
                rx.link(
                    " Soporte en papel.",
                    href=LINK_DRIVE,
                    is_external=True
                ),
                spacing="1",
                direction="row"
            ),
            rx.box(
                text_small(
                    """Web en version BETA, confeccionada en 2024, 
                    por Dafion para "Pensar Futuro", aun así, se reservan todos los derechos..."""
                    ),
                text_small(
                    "excepto el código, llámenme y se los paso..."
                    ),
                spacing="1",
                direction="column"
            ),
            align="center",
            direction="column"
        ),
        button_help(),
        bg=Color.BACKGROND.value,
        style={
            "margin-top": "30px",
        }
    ))

def footer_alchemy()-> rx.Component:
    return rx.container(rx.hstack(
        rx.flex(
            rx.flex(
                rx.text(
                    "El siguiente link lleva al "
                ),
                rx.link(
                    " Soporte en papel.",
                    href=LINK_DRIVE,
                    is_external=True
                ),
                spacing="1",
                direction="row"
            ),
            rx.box(
                text_small(
                    """Web en version BETA, confeccionada en 2024, 
                    por Dafion para el MUE, aun así, se reservan todos los derechos..."""
                    ),
                text_small(
                    "excepto el código, llámenme y se los paso..."
                    ),
                spacing="1",
                direction="column"
            ),
            align="center",
            direction="column"
        ),
        bg=Color.BACKGROND.value,
        style={
            "margin-top": "30px",
        }
    ))