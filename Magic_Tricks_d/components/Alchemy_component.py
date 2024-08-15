import reflex as rx
from State.Alchemy_State import Alchemy
from State.Alchemy_cociente_State import Alchemy_Cociente
from State.Alchemy_Max_Min import Alchemy_Max_Min
from Magic_Tricks_d.Styles.Colors import Color,TextColor
from Magic_Tricks_d.Styles.styles import Size_numbers
from State.info_State import InfoState
from Magic_Tricks_d.components.components import table_alchemy,table_resultados, table_orden_asuncion, table_alchemy_cociente, table_alchemy_max_min, table_resultados_max_min
from Magic_Tricks_d.components.grafic_component import pie_chart_simple


def alchemy_dhont()->rx.Component:
    return rx.box(
        rx.box(
            rx.flex(
                rx.text(
                    "Sistema D'Hondt",
                    size=Size_numbers.MEDIUM.value,
                ),
                rx.cond(
                    Alchemy.success,
                    rx.icon(
                        "chevron-down",
                        on_click=Alchemy.d_dondt_event
                    ),
                    rx.icon(
                        "chevron-up",
                        on_click=Alchemy.d_dondt_event
                    )
                ),
                bg=Color.PRINCIPAL.value,
                spacing=Size_numbers.SMALL.value,
                style={
                    "padding-left":"2px",
                }
            ),
        ),
        rx.cond(
            Alchemy.success,
            rx.flex(
                rx.box(
                    rx.flex(
                        rx.text(
                            "Lugares en disputas:",
                        ),
                        rx.input(
                            placeholder="Lugares",
                            name="lugares",
                            on_change=Alchemy.set_lugares
                        ),
                        rx.text(
                            "Porsentaje minimo:",
                        ),
                        rx.input(
                            placeholder="Porcentaje",
                            name="Porcentaje",
                            on_change=Alchemy.set_porcentaje_min
                        ),
                        rx.text(
                            "Total de votos:",
                        ),
                        rx.input(
                            placeholder="Total de votos",
                            name="total_votos",
                            on_change=Alchemy.set_total_votos
                        ),
                        rx.text(
                            "Votos en blanco:",
                        ),
                        rx.input(
                            placeholder="Blancos",
                            name="Blancos",
                            on_change=Alchemy.set_blancos
                        ),
                        rx.text(
                            "Votos nulos:",
                        ),
                        rx.input(
                            placeholder="nulos",
                            name="nulos",
                            on_change=Alchemy.set_nulos
                        ),
                        direction="column",
                        align="start",
                        spacing=Size_numbers.SMALL.value,
                    ),
                ),
                rx.box(
                    rx.text(
                        "Ingrese las fuerzas que se estan midiendo:",
                        size=Size_numbers.MEDIUM.value,
                        style={
                            "color":TextColor.SECONDARY.value,
                            "margin-bottom":"6px"
                        }
                        ),
                    rx.flex(
                        rx.input(
                            placeholder="Nombre", 
                            id="nombre", name="nombre", 
                            on_change= Alchemy.set_nombre,
                            width="33%"),
                        rx.input(
                            placeholder="Votos",
                            id="votos",name="votos",
                            on_change= Alchemy.set_votos,
                            width="33%"
                            ),
                        rx.button(
                            "Añadir", 
                            on_click= Alchemy.añadir_candidatura,
                            width="33%"
                        ),
                        direction="row",
                        align="center",
                        width="100%",
                        spacing=Size_numbers.SMALL.value,
                    ),
                    table_alchemy(Alchemy.candidaturas),
                    table_resultados(Alchemy.resultados),
                    width="100%",
                    style={
                        "margin-left":"16px",
                        "margin-right":"4px",
                    }
                ),
                width="100%",
                direction="row"
            )
        ),
    )

def alchemy_cocientes_resto() -> rx.Component:
    return rx.box(
            rx.flex(
                rx.text(
                    "Sistema de Cosiente Electoral",
                    size=Size_numbers.MEDIUM.value,
                ),
                rx.cond(
                    Alchemy_Cociente.success,
                    rx.icon(
                        "chevron-down",
                        on_click=Alchemy_Cociente.cociente_event
                    ),
                    rx.icon(
                        "chevron-up",
                        on_click=Alchemy_Cociente.cociente_event
                    )
                ),
                bg=Color.PRINCIPAL.value,
                spacing=Size_numbers.SMALL.value,
                style={
                    "padding-left":"2px",
                    "margin-top":"8px"
                }
            ),
            rx.cond(
                Alchemy_Cociente.success,
                rx.box(
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.text(
                                    "Lugares en disputas:",
                                ),
                                rx.input(
                                    placeholder="Lugares",
                                    name="lugares",
                                    on_change=Alchemy_Cociente.set_lugares
                                ),
                                rx.text(
                                    "Votos en blanco:",
                                ),
                                rx.input(
                                    placeholder="Blancos",
                                    name="Blancos",
                                    on_change=Alchemy_Cociente.set_blancos
                                ),
                                rx.text(
                                    "Votos nulos:",
                                ),
                                rx.input(
                                    placeholder="nulos",
                                    name="nulos",
                                    on_change=Alchemy_Cociente.set_nulos
                                ),
                                rx.text("Active el switch para NO contavilizar los blancos ni nulos:"),
                                rx.switch(on_change=Alchemy_Cociente.set_choice),
                                
                                direction="column",
                                align="start",
                                spacing=Size_numbers.SMALL.value,
                            ),
                        ),
                        rx.box(
                            rx.text(
                                "Ingrese las fuerzas que se estan midiendo:",
                                size=Size_numbers.MEDIUM.value,
                                style={
                                    "color":TextColor.SECONDARY.value,
                                    "margin-bottom":"6px"
                                }
                                ),
                            rx.flex(
                                rx.input(
                                    placeholder="Nombre", 
                                    id="nombre", name="nombre", 
                                    on_change= Alchemy_Cociente.set_nombre,
                                    width="33%"),
                                rx.input(
                                    placeholder="Votos",
                                    id="votos",name="votos",
                                    on_change= Alchemy_Cociente.set_votos,
                                    width="33%"
                                    ),
                                rx.button(
                                    "Añadir", 
                                    on_click= Alchemy_Cociente.añadir_candidatura,
                                    width="33%"
                                ),
                                direction="row",
                                align="center",
                                width="100%",
                                spacing=Size_numbers.SMALL.value,
                            ),
                            table_alchemy_cociente(Alchemy_Cociente.candidaturas),
                            
                            width="100%",
                            style={
                                "margin-left":"16px",
                                "margin-right":"4px",
                            }
                        )
                    ),
                    rx.box(
                        rx.flex(
                            rx.text(
                                "Resultados:"
                            ),
                            rx.cond(
                                Alchemy_Cociente.choice,
                                rx.text(
                                    f"Votos totales: {Alchemy_Cociente.votos_validos}"
                                ),
                                rx.text(
                                    f"Votos totales: {Alchemy_Cociente.total_votos}"
                                ),
                            ),
                            rx.flex(
                                f"Lugares en disputa:{Alchemy_Cociente.lugares}",
                                style={"color":TextColor.PRINCIPAL.value}
                            ),
                            rx.flex(
                                f"Cociente: {Alchemy_Cociente.cociente:.2f}",
                                style={"color":TextColor.PRINCIPAL.value}
                            ),
                            table_resultados(Alchemy_Cociente.resultados),
                            table_orden_asuncion(Alchemy_Cociente.orden_asuncion),
                            
                            direction="column",
                            spacing=Size_numbers.SMALL.value
                        ),
                        
                        style={
                            "backgroundColor": Color.PRINCIPAL.value,
                            "borderRadius": "8px",
                            "padding": "5px",
                            "margin-top":"8px"
                        },
                    ),
                ),
            ),
            
        ),

def alchemy_max_min() -> rx.Component:
    return rx.box(
            rx.flex(
                rx.text(
                    "Sistema de MAyorias y Minorias",
                    size=Size_numbers.MEDIUM.value,
                ),
                rx.cond(
                    Alchemy_Max_Min.success,
                    rx.icon(
                        "chevron-down",
                        on_click=Alchemy_Max_Min.max_min_event
                    ),
                    rx.icon(
                        "chevron-up",
                        on_click=Alchemy_Max_Min.max_min_event
                    )
                ),
                bg=Color.PRINCIPAL.value,
                spacing=Size_numbers.SMALL.value,
                style={
                    "padding-left":"2px",
                    "margin-top":"8px"
                }
            ),
            rx.cond(
                Alchemy_Max_Min.success,
                rx.box(
                    rx.flex(
                        rx.input(
                            placeholder="Nombre", 
                            id="nombre", name="nombre", 
                            on_change= Alchemy_Max_Min.set_nombre,
                            width="33%"
                        ),
                        rx.input(
                            placeholder="Votos",
                            id="votos",name="votos",
                            on_change= Alchemy_Max_Min.set_votos,
                            width="33%"
                        ),
                        rx.button(
                            "Añadir", 
                            on_click= Alchemy_Max_Min.añadir_candidatura,
                            width="33%"
                        ),
                        spacing=Size_numbers.SMALL.value,
                    ),
                    table_alchemy_max_min(Alchemy_Max_Min.candidaturas),
                    rx.flex(
                        rx.flex(
                            rx.text(
                                f"Total: {Alchemy_Max_Min.total_votos}",
                                style={
                                    "margin-top":"8px",
                                    "padding-left":"8px",
                                }
                            ),
                            table_resultados_max_min(Alchemy_Max_Min.resultados),
                            width="100%",
                            direction="column",
                        ),
                        pie_chart_simple(Alchemy_Max_Min.candidaturas),
                        direction="row",
                        spacing=Size_numbers.SMALL.value,
                        width="100%"
                    ),
                    style={
                        "margin-top":"8px"
                    }
                ),
            ),
            style={
                "margin-top":"8px"
            }
        )

def head()-> rx.Component:
    return rx.box(
            rx.flex(
                rx.heading(
                    "Alquimias",
                    align="left",
                ),
                rx.icon(
                    "badge-info",
                    on_click= InfoState.alchemy_event
                ),
                spacing=Size_numbers.SMALL.value,
                direction="row",
                align="start",
                justify="center",
                
            ),
            rx.cond(
                InfoState.event_alchemy,
                rx.box(
                    rx.callout(
                        rx.flex(
                            rx.center(rx.icon("badge-info")),
                            f"""Las Herraminetas presentadas son, para poder hacer aproximaciones del estado general de la 
                            eleccion,cada casa de altos estudios tiene normativa espesifica para contabilizar y asignar esñaloso (lugares), aqui
                            intentamos mostrar los 3 principales sistemas, mayorias y minorias, dhont y de cocientes y restos; En este apartado 
                            lo mas importante es el "olfato" del compañero que este armando la "alquimia", ya que es en un porcentaje importante 
                            ESPECULACION""",
                            direction= "row",
                            spacing=Size_numbers.SMALL.value,
                        )
                    ),
                    style={
                        "margin-top":"8px",
                        "margin-bottom":"4px",
                    },
                ),
            ),
            style={
                "margin-top":"16px",
                "margin-bottom":"8px",
            },
            
        ),