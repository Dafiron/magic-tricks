import reflex as rx
from Magic_Tricks_d.Styles.styles import Size,Size_numbers,navbar_style
from Magic_Tricks_d.Styles.Colors import Color

#La diferencia entre ambas varras es el boton de navegacion interna
def navbar_load() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.flex(
                rx.heading(
                    "Magic Tricks",
                    align="center",
                    style=navbar_style,
                    on_click=rx.redirect("/")
                ),
                rx.box(
                    rx.button(
                        rx.flex(
                            rx.text(
                                "Alquimia",
                            ),
                            rx.icon("test-tubes"),
                            spacing=Size_numbers.SMALL.value,
                            align="center"
                        ),
                        on_click=rx.redirect(
                            "/alchemist",
                            external=False,
                        ),
                    )
                ),
                direction="row",
                justify="between",
                width="100%"
            ),
            width="100%"
        ),
        position="sticky",
        bg=Color.BACKGROND.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index = "999",
        top="0",
        style={
            "border-bottom": f"6px solid {Color.PRINCIPAL.value}",
        }
        #el estilado para fijar la navbar arriva
    )

def navbar_alchemist() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.flex(
                rx.heading(
                    "Magic Tricks",
                    align="center",
                    style=navbar_style,
                    on_click=rx.redirect("/")
                ),
                rx.box(
                    rx.button(
                        rx.flex(
                            rx.text(
                                "Carga de datos",
                            ),
                            rx.icon("clipboard-list"),
                            spacing=Size_numbers.SMALL.value,
                            align="center"
                        ),
                        on_click=rx.redirect(
                            "/load",
                            external=False,
                        ),
                    )
                ),
                direction="row",
                justify="between",
                width="100%"
            ),
            width="100%"
        ),
        position="sticky",
        bg=Color.BACKGROND.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index = "999",
        top="0",
        style={
            "border-bottom": f"6px solid {Color.PRINCIPAL.value}",
        }
        #el estilado para fijar la navbar arriva
    )