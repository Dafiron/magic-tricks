import reflex as rx
from Magic_Tricks_d.components.grafic_component import grafic_component,grafic_Component_global
from Magic_Tricks_d.view.nabvar import navbar_alchemist
from Magic_Tricks_d.view.footer import footer_alchemy
from Magic_Tricks_d.Styles.styles import Size_numbers
from Magic_Tricks_d.components.Alchemy_component import alchemy_dhont, alchemy_cocientes_resto,alchemy_max_min,head
from Magic_Tricks_d.components.security_component import security_block
from State.Login_State import LoginState

#La Gestion de datos de componentes graficos utilizan base de datos en mysql
#Los componentes alchemy_dhont,alchemy_cocientes_resto,alchemy_max_min se hacen sobre la base de lo ingresado por el usuario

@rx.page(
    route="/alchemist",
    title="alchemist",
    on_load=LoginState.security_service
)

def alchemist()-> rx.components:
    return rx.box(
        rx.cond(
            LoginState.blocking,
            security_block(),
            rx.box(
                navbar_alchemist(),
                rx.container(
                    rx.flex(
                        grafic_Component_global(),
                        grafic_component(),
                        spacing=Size_numbers.DEFAULT.value,
                        direction="column",
                        width="100%",
                    ),
                    head(),
                    alchemy_dhont(),
                    alchemy_cocientes_resto(),
                    alchemy_max_min(),
                ),
                footer_alchemy()
            )
        ),
        
    )