import reflex as rx
from Magic_Tricks_d.view.nabvar import navbar_load
from Magic_Tricks_d.view.Load_var import Load_var
from Magic_Tricks_d.components.help_buttom import content_help
from Magic_Tricks_d.components.visual_day import visual_day
from Magic_Tricks_d.view.footer import footer_load
from Magic_Tricks_d.components.security_component import security_block
from State.Login_State import LoginState
from rxconfig import config


@rx.page(
    route="/load",
    title="load",
    on_load=LoginState.security_service
)
def load() -> rx.Component:
    return rx.box(
        rx.cond(
            LoginState.blocking,
            security_block(),
            rx.box(
                navbar_load(),
                rx.container(
                    rx.heading(
                        "Hoja de Gestion de datos",
                        align="center",
                        style={"margin_top": "16px"}
                    ),
                    content_help()
                ),
                rx.container(
                    rx.center(
                        rx.flex(
                            Load_var(),
                            visual_day(),
                            direction="row",
                            style={"margin_top": "8px"}
                            
                        ),
                        
                    ),
                    
                ),
            footer_load()
            ),
        )
    )