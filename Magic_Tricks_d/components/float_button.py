import reflex as rx
from Magic_Tricks_d.Styles.Colors import Color

# Boton Flotante (componente de una libreria externa)

class FloatButton(rx.Component):
    library="antd"
    tag="FloatButton"
    icon: rx.Var[rx.el.Img]
    badge ={"dot":True,"color":Color.PRINCIPAL.value}

float_botton=FloatButton.create