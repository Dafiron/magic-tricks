import reflex as rx
from enum import Enum
from Magic_Tricks_d.Styles.Font import Font,FontWeight
from Magic_Tricks_d.Styles.Colors import Color,TextColor

MAX_WIDTH ="600px"

#Sizes / Tamaños
class Size(Enum):
    SMALL="0.5em"
    MEDIUM ="0.8em"
    DEFAULT="1em"
    DEF_PLUS="1.5em"
    BIG="2em"
    VERY_BIG="5em"


class Size_numbers(Enum):
    SMALL="2"
    MEDIUM ="4"
    DEFAULT="5"
    BIG="7"
    X_BIG="9"



BASE_STYLE ={
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROND.value,
    rx.heading:{
        "size":"5",
        "color":TextColor.PRINCIPAL.value,
        "font_family":Font.DEFAULT.value,
        "font_weight": FontWeight.MIDIUM.value,
    },

    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "background_color": Color.ACENTUADO.value,
        "color": TextColor.PRINCIPAL.value,
        "_hover": {
            "background_color": Color.PRINCIPAL.value,
        },
    },
    rx.link:{
        "text_decoration":"none",
        "_hover": {}
    },
    rx.input: {
        "background_color": "#0e1724",  # Fondo azul oscuro
        "color": TextColor.PRINCIPAL.value,  # Texto en blanco
        "font_family": Font.DEFAULT.value,
        "border": "0.3px solid #888888",  # Borde del mismo color que los botones
        "& input::placeholder": {"color": "#888888"},
        "input": {"color": TextColor.PRINCIPAL.value}
    },
    rx.text:{
        "color":TextColor.PRINCIPAL.value
    },
    rx.table.row:{
        "color":TextColor.SECONDARY.value
    },
    rx.table.root:{"border": "0.3px solid #888888"},
}

STYLESHEETS =[
    'https://fonts.googleapis.com/css2?family=Gideon+Roman&family=Kanit:wght@100;400&display=swap'
]


style_section = {
    "height":"90vh",
    "width": "80%",
    "margin": "auto"
}

# Tuve que resolver el boton de la siguiente forma por que no me reconocia la forma extandar de reflex

badge_help_button="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMi40IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWJhZGdlLWhlbHAiPjxwYXRoIGQ9Ik0zLjg1IDguNjJhNCA0IDAgMCAxIDQuNzgtNC43NyA0IDQgMCAwIDEgNi43NCAwIDQgNCAwIDAgMSA0Ljc4IDQuNzggNCA0IDAgMCAxIDAgNi43NCA0IDQgMCAwIDEtNC43NyA0Ljc4IDQgNCAwIDAgMS02Ljc1IDAgNCA0IDAgMCAxLTQuNzgtNC43NyA0IDQgMCAwIDEgMC02Ljc2WiIvPjxwYXRoIGQ9Ik05LjA5IDlhMyAzIDAgMCAxIDUuODMgMWMwIDItMyAzLTMgMyIvPjxsaW5lIHgxPSIxMiIgeDI9IjEyLjAxIiB5MT0iMTciIHkyPSIxNyIvPjwvc3ZnPg=="

navbar_style=style={
    "color": TextColor.PRINCIPAL.value,
    "size": Size.VERY_BIG.value,
    "font-family": Font.LOGO.value,
    "font-weight": "400",
    "font-style": "normal"
    }