"""Magic Tricks"""

import reflex as rx
from Magic_Tricks_d.Styles.styles import BASE_STYLE,STYLESHEETS
from rxconfig import config
from Magic_Tricks_d.page.index import index
from Magic_Tricks_d.page.load import load
from Magic_Tricks_d.page.alchemist import alchemist
from State.Login_State import LoginState



class State(rx.State):
    """The app state."""



app = rx.App(
    style=BASE_STYLE,
    stylesheets= STYLESHEETS
)

app.add_page(index)
app.add_page(load)
app.add_page(alchemist)