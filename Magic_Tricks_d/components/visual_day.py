import reflex as rx
from State.Visual_State import VisualState
from Magic_Tricks_d.Styles.styles import Size_numbers
from Magic_Tricks_d.components.components import field_form_general_component_visual,table_general


def visual_day()-> rx.components:
    return rx.box(
            rx.vstack(
                rx.heading("Dia"),
                rx.flex(
                    field_form_general_component_visual(
                        "UNI",
                        VisualState.set_uni,
                        "uni"
                    ),
                    field_form_general_component_visual(
                        "año",
                        VisualState.set_año,
                        "año"
                    ),
                    field_form_general_component_visual(
                        "dia",
                        VisualState.set_dia,
                        "dia"
                    ),
                    justify="start",
                    direction="row",
                    style={
                        "width":"100%"
                    },
                ),
                style={
                    "width":"100%"
                },
            ),
            rx.scroll_area(
                rx.box(
                    table_general(VisualState.rough)
                ),
                type="always",
                scrollbars="vertical",
                style={
                    "height": 380,
                    "margin-top":"4px",
                    "border-width": "1px",
                    "border-radius" : "5px 5px 0 5px"
                    },
            ),
            rx.flex(
                rx.button(  # Añadir botón de descarga CSV
                        rx.center(
                            rx.icon("file-down")
                        ),
                        on_click=VisualState.download_csv_data,  # Asignar la función de descarga al evento on_click
                        disabled=VisualState.loader,  # Deshabilitar el botón si se están cargando datos
                        width="25%",
                        style={"border-radius": "0 0 10px 10px", "margin-left": "10px"}
                    ),
                rx.button(
                    rx.center(
                        rx.icon("list")
                    ),
                    on_click=VisualState.Visual_Service,
                    disabled=VisualState.validate_fields_t,
                    width="25%",
                    style={"border-radius": "0 0 10px 10px"}
                    ),
                spacing=Size_numbers.SMALL.value,
                align="end",
                justify="end"
            ),
        style={
            "padding":"5.5px 5px 5px 25px"
        }
    )