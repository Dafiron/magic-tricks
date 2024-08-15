import reflex as rx
import requests as rq

#Este estado gestiona el ingreso de datos su borrado y actualizacion originalmente busque hacerlo en 2 estados cosa por la forma 
# que tenia de representarlo luego no lo pude realizar. y por eso la importancia del orden de su representacion de form el cuerpo de la page

#Instruccion donde esta el back:
back ="https://magic-back.onrender.com"

class LoadState(rx.State):
    loader: bool = False
    id_accion: int | None = None
    ronda: int = 0
    hora: float = 0.0
    votos: int = 0
    propios: int = 0
    uni: str = ""
    año: int = 0
    dia: int = 0
    error: bool = False
    success: bool = False
    delete_success: bool = False
    put_success:bool = False
    response: dict = {}
    bars: list = [0]

#Carga del dato
    @rx.background
    async def LoadService(self, data: dict):
        async with self:
            self.loader = True
            self.error = False
            self.success = False
            response = rq.post(f"{back}/number/on_numbers", json=data)
            if response.status_code == 201:
                self.response = response.json()
                self.loader = False
                self.success = True
            else:
                self.loader = False
                self.error = True

#Borrado del dato
#Indican como obligatorio todos los campos auque luego con "uni","año","dia","ronda" se puede encontrar el dato..

    @rx.background
    async def DeleteService(self):
        async with self:
            self.loader = True
            self.error = False
            self.delete_success = False
            data = {
                "uni": self.uni,
                "año": self.año,
                "dia": self.dia,
                "ronda": self.ronda,
                "hora": self.hora,
                "votos": self.votos,
                "propios": self.propios,
            }
            response = rq.delete(f"{back}/number/del_numbers", json=data)
            if response.status_code == 204:
                self.loader = False
                self.delete_success = True
            else:
                self.loader = False
                self.error = True

#Actualizador del dato
#Indican como obligatorio todos los campos auque luego con "uni","año","dia","ronda" se puede encontrar el dato..
    @rx.background
    async def PutService(self):
        async with self:
            self.loader = True
            self.error = False
            self.put_success = False
            data = {
                "uni": self.uni,
                "año": self.año,
                "dia": self.dia,
                "ronda": self.ronda,
                "hora": self.hora,
                "votos": self.votos,
                "propios": self.propios,
            }
            response = rq.put(f"{back}/number/up_numbers", json=data)
            if response.status_code == 200:
                self.loader = False
                self.put_success= True
            else:
                self.loader = False
                self.error = True

    @rx.var
    def ronda_empty(self) -> bool:
        return self.ronda == 0

    @rx.var
    def hora_empty(self) -> bool:
        return self.hora == 0.0

    @rx.var
    def votos_empty(self) -> bool:
        return self.votos == 0

    @rx.var
    def propios_empty(self) -> bool:
        return self.propios == 0

    @rx.var
    def uni_empty(self) -> bool:
        return not self.uni.strip()

    @rx.var
    def año_empty(self) -> bool:
        return self.año == 0

    @rx.var
    def dia_empty(self) -> bool:
        return self.dia == 0

    @rx.var
    def validate_fields_(self) -> bool:
        return (
            self.ronda_empty or 
            self.hora_empty or 
            self.votos_empty or 
            self.propios_empty or 
            self.uni_empty or 
            self.año_empty or 
            self.dia_empty
        )

