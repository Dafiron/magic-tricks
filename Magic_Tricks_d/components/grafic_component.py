import reflex as rx
from State.Grafic_State import GraficState
from State.Global_State import GlobalState
from State.help_State import HelpState
from State.info_State import InfoState
from Magic_Tricks_d.Styles.styles import Color, TextColor,Size_numbers
from Magic_Tricks_d.components.components import field_form_general_component_visual


def line_simple()->rx.Component:
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="votos",
        ),
        rx.recharts.x_axis(data_key="hora"),
        rx.recharts.y_axis(),
        rx.recharts.graphing_tooltip(
            wrapper_style={
                "backgroundColor": Color.PRINCIPAL.value,
                "borderRadius": "8px",
                "padding": "5px",
            },
            content_style={
                "backgroundColor": Color.PRINCIPAL.value,
                "borderRadius": "4px",
                "padding": "8px",
            },
            item_style={"color": TextColor.PRINCIPAL.value}
        ),
        rx.recharts.legend(),
        data=GraficState.h_v,
        width="100%",
        height=300,
    )

def box_info_dia()->rx.Component:
    return rx.box(
        rx.heading(
            f"Universidad : {GraficState.uni}"
        ),
        rx.text(
            f"Dia : {GraficState.dia}"
        ),
        rx.flex(
            rx.text(
                f"Votos Totales : {GraficState.total}"
            ),
            rx.text(
                f"Votos Propios : {GraficState.total_propios}"
            ),
            direction="column"
        ),
        style={
            "border": "1px solid #ddd",
            "border-radius": "5px",
            "padding":"2px"
        }
    )

def info_icon() -> rx.Component:
    return rx.box(
        rx.center(
            rx.image(
                src="../badge-info.svg",
                on_click=InfoState.info_event,
                width="100%"
            ),
        ),
        width="12%"
    )

def grafic_component()->rx.Component:
    return rx.box(
        rx.box(
            rx.flex(
                info_icon(),
                field_form_general_component_visual(
                        "UNI",
                        GraficState.set_uni,
                        "uni"
                    ),
                field_form_general_component_visual(
                        "año",
                        GraficState.set_año,
                        "año"
                    ),
                field_form_general_component_visual(
                        "dia",
                        GraficState.set_dia,
                        "dia"
                    ),
                    
                    rx.flex(
                        rx.button(
                            rx.center(rx.icon("line-chart")),
                            on_click=GraficState.TestService,
                            disabled=GraficState.validate_fields_t,
                            
                            style={"border-radius": "5px 5px 5px 5px"}
                        ),
                        width="25%",
                    ),
                direction="row",
                align="center",
                justify="center",
                spacing=Size_numbers.SMALL.value
            ),
            rx.cond(
            InfoState.event_info,
            rx.box(
                rx.callout(
                    rx.flex(
                        rx.center(rx.icon("badge-info")),
                        rx.text("""Se suele usar este tipo de graficos, en compania de los horarios de cursada para comparar "nustras
                        cursadas fuertes" con nustros resultados preliminares."""),
                        direction= "row",
                        spacing=Size_numbers.SMALL.value,
                    )
                ),
                style={
                    "margin-top":"8px",
                    "margin-bottom":"8px"
                    }
            ),
        ),
                rx.cond(
                    GraficState.success,
                    rx.box(
                        box_info_dia(),
                        rx.box(
                            line_simple(),
                            style={
                                "padding-top":"8px",
                                "margin-top":"4px"
                                }
                            ),
                        bar_chart_multi(GraficState.datos_grafico_varchart),
                        spacing=Size_numbers.SMALL.value,
                        style={
                            "margin-top":"2px"
                        }
                    ),
                    rx.box(
                        rx.flex(
                            rx.image(
                                src="/metricas_finite3.png",
                                align="center",
                                title="background de graficos",
                                ),
                            width="100%",
                            justify="center",
                            align="center",
                        ),
                        style={
                            "margin-top":"16px",
                            }
                    ),
                    
                ),
        ),
        width="100%"
    )

def box_info_global()->rx.Component:
    return rx.box(
        rx.heading(
            f"Universidad : {GlobalState.uni}"
        ),
        rx.flex(
            rx.text(
                f"Votos Totales : {GlobalState.global_total}"
            ),
            rx.text(
                f"Votos Propios : {GlobalState.global_propios}"
            ),
            rx.text(
                f"Porcion Propia : {GlobalState.porcentaje} %"
            ),
            rx.text(
                f"Porcion Rival : {GlobalState.porcentaje_r} %"
            ),
            direction="column"
        ),
        style={
            "border": "1px solid #ddd",
            "border-radius": "5px",
            "padding":"2px"
        }
    )


def pie_chart_simple(data_format) -> rx.Component:
    return rx.recharts.pie_chart(
                rx.recharts.pie(
            data=data_format,
            data_key="votos",
            name_key="faccion",
            fill= Color.ACENTUADO.value,
            label=True,
        ),
        rx.recharts.graphing_tooltip(
            wrapper_style={
                "backgroundColor": Color.PRINCIPAL.value,
                "borderRadius": "8px",
                "padding": "5px",
                "color": TextColor.PRINCIPAL.value
            },
            content_style={
                "backgroundColor": Color.PRINCIPAL.value,
                "borderRadius": "4px",
                "padding": "8px",
                "color": TextColor.PRINCIPAL.value
            },
            item_style={ "color": TextColor.PRINCIPAL.value}, 
            is_animation_active=True
        ),
        width="100%",
        height=300,
    )


def bar_chart_multi(data_barchart) -> rx.Component:
    return rx.box(
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key="total_votos",
                name="Votos Totales",
                stroke=rx.color("gray", 9),
                fill=rx.color("gray", 8),
            ),
            rx.recharts.bar(
                data_key="propios_votos",
                name="Votos Propios",
                stroke=rx.color("accent", 9),
                fill=rx.color("accent", 8),
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(
            wrapper_style={
                "backgroundColor": Color.PRINCIPAL.value,
                "borderRadius": "8px",
                "padding": "5px",
            },
            content_style={
                "backgroundColor": Color.PRINCIPAL.value,
                "borderRadius": "4px",
                "padding": "8px",
            },
            item_style={"color": TextColor.PRINCIPAL.value}
        ),
            data=data_barchart,
            width="100%",
            height=300,
        )
    )

def grafic_Component_global() -> rx.Component:
    return rx.box(
        rx.box(
            rx.flex(
                field_form_general_component_visual(
                    "UNI",
                    GlobalState.set_uni,
                    "uni"
                ),
                field_form_general_component_visual(
                    "año",
                    GlobalState.set_año,
                    "año"
                ),
                rx.image(
                    src="../badge-info.svg",
                    on_click=HelpState.info_event,
                    width="12%",
                ),
                field_form_general_component_visual(
                    "depuracion",
                    GlobalState.set_purga,
                    "purga"
                ),
                rx.button(
                    rx.center(rx.icon("package-search")),
                    on_click=GlobalState.GlobalService,
                    disabled=GlobalState.validate_fields_g,
                    width="15%",
                    style={"border-radius": "5px 5px 5px 5px"}
                ),
                padding="2px",
                spacing=Size_numbers.SMALL.value,
                align="center"
            ),
            rx.cond(
                HelpState.event_info,
                rx.box(
                    rx.callout(
                        rx.flex(
                            rx.center(rx.icon("badge-info")),
                            rx.text(f"""La depuracion se usa para se usa para intentar prever las perdidas de votos no contabilizadas;
                            El numero de votos se multiplicara por este, por eso deve ser 0.X (cero punto algo), 
                            se suele usarse 0.98 en una eleccion tranquila, priviendo una perdida de 2% de los votos"""),
                            direction= "row",
                            spacing=Size_numbers.SMALL.value,
                        )
                    )
                ),
            ),
            rx.cond(
                    GlobalState.success,
                    rx.box(
                        box_info_global(),
                        pie_chart_simple(GlobalState.dict_format),
                        bar_chart_multi(GlobalState.datos_grafico_varchart),
                        style={
                            "border": "1px solid #ddd",
                            "border-radius": "5px",
                        }
                    ),
                    rx.box(
                        rx.flex(
                            rx.image(src="/metricas_finite3.png"),
                            width="100%",
                            justify="center",
                            align="center",
                        ),
                        
                        style={
                            "margin-top":"16px",
                            }
                    )
                )
        ),
        width="100%"
    )