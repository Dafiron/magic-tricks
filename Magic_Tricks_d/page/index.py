import reflex as rx
from State.Login_State import LoginState
from Magic_Tricks_d.components.components import field_form_component, field_form_component_general
from Magic_Tricks_d.Styles.Colors import Color
from Magic_Tricks_d.Styles.styles import style_section


@rx.page(
)

def index() -> rx.Component:
    return rx.container(
        rx.section(
            rx.flex(
                rx.image(
                    src="/LOGO-blanco finite.png",
                    width="100 px",
                    height="auto",
                    border_radius="15px 50px",
                    bg=Color.ACENTUADO.value,
                    border=f"5px solid {Color.PRINCIPAL.value}",
                    on_click=rx.redirect("https://pensarfuturo.com.ar/",external=True)
                ),
                rx.heading(
                    "Inicio de sesion",
                    style={
                        "margin-top":"8px"
                    }
                    ),
                rx.form.root(
                    rx.flex(
                        field_form_component_general(
                            "Usuario",
                            "Ingrese el Usuario",
                            "ingrese un usuario valido",
                            "username",
                            LoginState.set_username,
                            LoginState.user_empty
                        ),
                        field_form_component(
                            "Contraseña",
                            "Ingrese la contraseña",
                            "password",
                            LoginState.set_password,
                            "password"
                        ),
                        rx.form.submit(
                            rx.cond(
                                LoginState.loader,
                                rx.chakra.spinner(color=Color.SECONDARY, size="xs"),
                                rx.button(
                                    "iniciar sesion",
                                    disabled=LoginState.validate_fields,
                                    width="30vw"
                                ),
                            ),
                            as_child=True
                        ),
                        rx.button(
                            rx.flex(
                                rx.text("Cerrado Seguro"),
                                direction="row",
                                justify="center",
                                align="center",
                                spacing="2"
                            ),
                            width="30vw",
                            on_click=LoginState.clean
                        ),
                        direction="column",
                        align="center",
                        justify="center",
                        spacing="2",
                    ),
                    rx.cond(
                        LoginState.error,
                        rx.callout.root(
                            rx.callout.icon(rx.icon("TriangleAlert")),
                            rx.callout.text(
                                "Credenciales incorrectas",
                                style={
                                    "color":"#F3F6FD",
                                    }
                                ),
                            color_scheme="brown",
                            role="alert",
                            style={"margin_top":"10px"}
                        ),
                    ),
                    on_submit=LoginState.loginService,
                    reset_on_submit=True,
                    width="80%",
                ),
                direction="column",
                align="center",
                justify="center",
            ),
        ),
        on_mount=LoginState.clean,
        style=style_section,
        justify="center",
        width="100%",
    )

