import reflex as rx
from State.help_State import HelpState
from Magic_Tricks_d.components.components import text_small
from Magic_Tricks_d.components.float_button import float_botton
from Magic_Tricks_d.Styles.styles import Size_numbers,badge_help_button
from Magic_Tricks_d.Styles.Colors import Color



def button_help()->rx.Component:
    return float_botton(
        icon=rx.image(src=badge_help_button),
        on_click=HelpState.scroll_to_help,
        style={
            "position": "fixed",
            "bottom": "30px",
            "border-radius": "1xp 1px 1px 1px",
            "background-color": Color.PRINCIPAL.value,
            "cursor": "pointer"
        }
    ),



def content_help()->rx.Component:
    return rx.box(
        rx.cond(
            HelpState.event_help,
            rx.center(
                rx.box(
                    rx.text(
                        """A tener en cuenta a la hora de ingresar datos:
                        """,
                        align="left",
                        size=Size_numbers.DEFAULT.value,
                        margin_left="4px"
                    ),
                    rx.flex(
                        text_small("* Todos los campos son obligatorios."),
                        text_small(
                            """* El ingreso debe ser con números enteros, en todos los casos,
                            excepto en el campo "hora" y "universidad"."""
                        ),
                        text_small(
                            """* En el campo "hora" debe ingresarse con un entero seguido de un decimal separado por un ' . ' (punto),
                            de esta forma para referirse a las 12:00 h se debe ingresar 12.00."""
                        ),
                        text_small(
                            """* La aplicación es sensible a mayúsculas y minúsculas, por esto si el dato de "universidad" fue
                            ingresado con mayúsculas debe mantenerse ,
                            de esta forma si se ingresó "UNMDP" los siguientes NO pueden ser unmdp, ni Unmdp."""
                        ),
                        text_small(
                            """* Los accidentes ocurren, por esto recomendamos tener soporte en papel, ante cualquier eventualidad, al final de
                            la página encontrará un link de drive para descargar e imprimir un PDF (en blanco) para el respaldo."""
                        ),
                        direction="column",
                    ),
                    id="help_section",
                    bg= Color.PRINCIPAL.value,
                    style={
                        "margin-top": "10px",
                        "padding": "10px",
                        "border": "1px solid #ddd",
                        "border-radius": "5px",
                    }
                ),
            ),
        )
    )


