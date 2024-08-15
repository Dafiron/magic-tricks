import reflex as rx
from Magic_Tricks_d.Styles.Colors import TextColor
from Magic_Tricks_d.Styles.styles import Size_numbers
from State.Alchemy_State import Alchemy
from State.Alchemy_cociente_State import Alchemy_Cociente
from State.Alchemy_Max_Min import Alchemy_Max_Min

#El name_var va a definir la key del dict
def field_form_component(
    label:str, placeholder:str, name_var:str,
    on_change_function, type_field:str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(
                label,
                style={"color":TextColor.PRINCIPAL.value}
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name_var,
                    type=type_field,
                    required=True,
                    style={
                        "backgroundColor": "#0e1724",
                        "color": "#ffffff"
                    }
                ),
                as_child=True
            ),
            rx.form.message(
                "El campo no puede ser nulo",
                match="valueMissing",
                color="red",
            ),
            direction="column",
            spacing="2",
            align="stretch"
        ),
        name=name_var,
        width="30vw"
    )

def field_form_component_general(
    label:str, placeholder:str,message_validate:str,name:str,
    on_change_function, show
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(
                label,
                style={
                    "color":TextColor.SECONDARY.value,
                }
                ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name,
                    required=True,
                    radius="small",
                    style={
                        "backgroundColor": "#0e1724",
                        "color": "#ffffff"
                    }
                ),
                as_child=True,
            ),
            rx.form.message(
                message_validate,
                name=name,
                match="valueMissing",
                force_match=show,
                color=TextColor.PRINCIPAL.value
            ),
            direction="column",
            spacing="2",
            align="stretch"
        ),
        name=name,
        width="30vw"
    )



def field_form_component_general_load(
    placeholder:str,name:str,
    on_change_function,
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    on_change=on_change_function,
                    name=name,
                    required=True,
                ),
                as_child=True
            ),
            direction="row",
            spacing="2",
            align="start",
            style={
                "padding":"2px",
                "width":"100%"
            }
        ),
        name=name,
    )

def text_small(text:str) -> rx.Component:
    return rx.text(
        text,
        align="left",
        as_ ="span",
        size= Size_numbers.SMALL.value,
        margin_left="1px"
        )




def field_form_general_component_visual(placeholder_on:str,on_change_funcion,name_on:str) -> rx.Component:
    return rx.form(
        rx.input(
            placeholder=placeholder_on,
            on_change=on_change_funcion,
            name=name_on
        ),
        
    )

#El dato hora en sql es un dato de tipo time por eso requiere combersion al llegar y al enviarse... 

def float_to_str(hora: float) -> str:
    horas = int(hora)
    minutos = int((hora - horas)*60)
    return (f"{horas}:{minutos}:00")

def seg_h(segundos):
    return float(segundos / 3600)

def segundos_a_hora_decimal(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    return float(f"{horas}.{minutos:02}")


#Las funciones table simpre van con otra... una determina los parametros de la table y otra contiene los datos..
#--------------------------------------------------------------------------#
def table_general(rougt) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Ronda"),
                rx.table.column_header_cell("Hora"),
                rx.table.column_header_cell("Votos"),
                rx.table.column_header_cell("Propios"),
            ),
        ),
        rx.table.body(
            rx.foreach(rougt,row_chuster),
            
        ),
    ),

def row_chuster(lista:list[list]) -> rx.Component:
    return rx.table.row(
        rx.table.cell(lista[0]),
        rx.table.cell(lista[1]),
        rx.table.cell(lista[2]),
        rx.table.cell(lista[3]),
    )
#--------------------------------------------------------------------------#
def table_alchemy(candidaturas: list[dict]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Votos"),
            ),
        ),
        rx.table.body(
            rx.foreach(candidaturas, row_chuster_alchemy)
        ),
    )

def row_chuster_alchemy(candidatura: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(candidatura["nombre"]),
        rx.table.cell(candidatura["votos"]),
        rx.table.cell(
            rx.button("Eliminar", on_click=lambda: Alchemy.eliminar_candidatura(candidatura["id"]))
        )
    )
#--------------------------------------------------------------------------#
def table_resultados(resultados: list[dict]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Lugares"),
            ),
        ),
        rx.table.body(
            rx.foreach(resultados, row_resultado)
        ),
    )

def row_resultado(resultado: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(resultado["nombre"]),
        rx.table.cell(resultado["escaños"]),
    )

#--------------------------------------------------------------------------#
def table_orden_asuncion(orden_asuncion: list[dict]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Lugar"),
                rx.table.column_header_cell("Partido"),
            ),
        ),
        rx.table.body(
            rx.foreach(orden_asuncion, row_asuncion)
        ),
    )

def row_asuncion(asuncion: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(asuncion["orden"]),
        rx.table.cell(asuncion["nombre"]),
    )

#--------------------------------------------------------------------------#
def table_alchemy_cociente(candidaturas: list[dict]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Votos"),
            ),
        ),
        rx.table.body(
            rx.foreach(candidaturas, row_chuster_alchemy_cociente)
        ),
    )

def row_chuster_alchemy_cociente(candidatura: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(candidatura["nombre"]),
        rx.table.cell(candidatura["votos"]),
        rx.table.cell(
            rx.button("Eliminar", on_click=lambda: Alchemy_Cociente.eliminar_candidatura(candidatura["id"]))
        )
    )
#--------------------------------------------------------------------------#
def table_alchemy_max_min(candidaturas: list[dict]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Votos"),
            ),
        ),
        rx.table.body(
            rx.foreach(candidaturas, row_chuster_alchemy_max_min)
        ),
    )

def row_chuster_alchemy_max_min(candidatura: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(candidatura["faccion"]),
        rx.table.cell(candidatura["votos"]),
        rx.table.cell(
            rx.button("Eliminar", on_click=lambda: Alchemy_Max_Min.eliminar_candidatura(candidatura["id"]))
        )
    )
#--------------------------------------------------------------------------#
def table_resultados_max_min(resultados: list[dict]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Porcentaje"),
            ),
        ),
        rx.table.body(
            rx.foreach(resultados, row_resultado_max_min)
        ),
    )

def row_resultado_max_min(resultado: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(resultado["nombre"]),
        rx.table.cell(resultado["porcentaje"]),
    )
#--------------------------------------------------------------------------#





