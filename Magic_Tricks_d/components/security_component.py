import reflex as rx

def security_block() -> rx.Component:
    return rx.box(
        rx.center(
            rx.flex(
                rx.heading(
                    "¡¡Tu No Pasaras!!"
                    
                ),
                rx.image(
                    src="../you-shall-not-pass-removebg-preview2.png",
                    height="auto",
                    alt="imagen de gandalf caticaturizada sosteniendo un cartel de contramano",
                    name="opps por aca sin permiso NO",
                    on_click=rx.redirect("/")
                ),
                rx.text(
                    "autor: Wirdou.com"
                ),
                direction="column",
                width="100%",
                align="center",
                justify="center"
            ),
        ),
    )