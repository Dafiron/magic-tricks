import reflex as rx
import requests as rq

#Gestiona el ingreso del ususario y el bloqueo de la visualizacion de contenido si este no fue debidamente acreditado o su token 
#se encuentre fuera de tiempo de uso

#Instruccion donde esta el back:
back ="https://magic-back.onrender.com"

class LoginState(rx.State):
    loader: bool = False
    username: str = ""
    password: str = ""
    token: str = rx.LocalStorage(sync=True)
    error: bool = False
    response:dict = {}
    blocking : bool = True

    @rx.background
    async def loginService(self, data: dict):
        async with self:
            self.loader = True
            self.error = False
            response = rq.post(f"{back}/login/", data=data)
            if response.status_code == 200:
                self.response = response.json()
                self.loader = False
                self.token = self.response["access_token"]
                return rx.redirect("/load")
            else:
                self.loader = False
                self.error = True

    @rx.background
    async def security_service(self):
        async with self:
            self.blocking = True
            headers = {"Authorization": f"Bearer {self.token}"}
            response = rq.get(f"{back}/login/verify-token", headers=headers, timeout= 30)
            if response.status_code == 200:
                self.blocking = False
            else:
                self.blocking = True
    @rx.var
    def user_empty(self) -> bool:
        return not self.username.strip()
    @rx.var
    def password_empty(self) -> bool:
        return not self.password.strip()
    @rx.var
    def validate_fields(self) -> bool:
        return self.user_empty or self.password_empty
    
    def clean(self):
        return [
            rx.clear_local_storage(),
        ]

