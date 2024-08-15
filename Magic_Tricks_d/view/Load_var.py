import reflex as rx
from Magic_Tricks_d.components.components import field_form_component_general_load
from State.Load_State import LoadState
from Magic_Tricks_d.Styles.Colors import Color
from Magic_Tricks_d.Styles.styles import Size_numbers

# Es importante el orden que tienen los forms y el sumint, ya que al aterarlos se alterma en demasia el compotamiento del codigo.

def Load_var()-> rx.Component:
    return rx.flex(
                rx.vstack(
                    rx.heading(
                        "Carga de datos",
                            size=Size_numbers.MEDIUM.value
                        ),
                    rx.vstack(
                        rx.flex(
                            rx.form(
                                rx.flex(
                                    field_form_component_general_load(
                                        "año",
                                        "año",
                                        LoadState.set_año,
                                    ),
                                    field_form_component_general_load(
                                        "uni",
                                        "uni",
                                        LoadState.set_uni,
                                    ),
                                    field_form_component_general_load(
                                        "dia",
                                        "dia",
                                        LoadState.set_dia,
                                    ),
                                    field_form_component_general_load(
                                        "ronda",
                                        "ronda",
                                        LoadState.set_ronda,
                                    ),
                                    field_form_component_general_load(
                                        "hora",
                                        "hora",
                                        LoadState.set_hora,
                                    ),
                                    field_form_component_general_load(
                                        "votos",
                                        "votos",
                                        LoadState.set_votos,
                                    ),
                                    field_form_component_general_load(
                                        "propios",
                                        "propios",
                                        LoadState.set_propios,
                                    ),
                                    rx.form.submit(
                                    rx.cond(
                                        LoadState.loader,
                                        rx.chakra.spinner(color=Color.SECONDARY, size="xs"), #Forma parte de un uso antiguo de reflex pero todabia funcional
                                        rx.cond(
                                            LoadState.success,
                                            rx.button(
                                                rx.center(
                                                    "✓ Carga"
                                                ),
                                                disabled=LoadState.validate_fields_,
                                                width="100%"
                                            ),
                                            rx.button(
                                                rx.center(
                                                    "Carga"
                                                ),
                                                disabled=LoadState.validate_fields_,
                                                width="100%"
                                            ),
                                        ),
                                    ),
                                    as_child=True
                                ),
                                    direction="column",
                                    align="start",
                                    justify="start",
                                    spacing="2",
                                
                                ),
                            on_submit=LoadState.LoadService,
                            reset_on_submit=True,
                            ),
                        ),
                        rx.vstack(
                                rx.flex(
                                    rx.form(
                                        rx.cond(
                                            LoadState.delete_success,
                                            rx.button(
                                                rx.center(
                                                    "✓",
                                                    rx.icon("Trash-2"),
                                                ),
                                                on_click=LoadState.DeleteService,
                                                disabled=LoadState.validate_fields_,
                                                width="100%"
                                            ),
                                            rx.button(
                                                rx.center(
                                                    rx.icon("Trash-2"),
                                                ),
                                                on_click=LoadState.DeleteService,
                                                disabled=LoadState.validate_fields_,
                                                width="100%"
                                            ),
                                        ),
                                    ),
                                    width="100%"
                                ),
                                rx.flex(
                                    rx.form(
                                        rx.cond(
                                            LoadState.put_success,
                                            rx.button(
                                                rx.center(
                                                    "✓",
                                                    rx.icon("refresh-ccw",),
                                                ),
                                                on_click=LoadState.PutService,
                                                disabled=LoadState.validate_fields_,
                                                width="100%",
                                            ),
                                            rx.button(
                                                rx.center(
                                                    rx.icon("refresh-ccw",),
                                                ),
                                                on_click=LoadState.PutService,
                                                disabled=LoadState.validate_fields_,
                                                width="100%"
                                            ),
                                        ),
                                    ),
                                    width="100%"
                                ),
                                
                                spacing=Size_numbers.SMALL.value,
                                width="100%",
                            direction="row",
                        ),
                        style={
                            "margin_top":"10px",
                        },
                    ),
                ),
    )

