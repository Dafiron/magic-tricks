import reflex as rx
import requests as rq
from Magic_Tricks_d.components.components import segundos_a_hora_decimal

#Instruccion donde esta el back:
back ="https://magic-back.onrender.com"

class GraficState(rx.State):
    loader: bool = False
    rough : list[list] #bruto
    h_v: list[dict]
    dia: int = 0
    año : int = 0
    uni : str = ""
    total : int = 0
    datos_grafico_varchart : list[dict]
    total_propios : int = 0
    error: bool = False
    success: bool = False

    @rx.background
    async def TestService(self):
        async with self:
            self.loader = True
            self.error = False
            self.success = False
            try:
                response = rq.get(f"{back}/number/call_uad", params={"uni": self.uni, "año": self.año, "dia": self.dia})
                if response.status_code == 200:
                    rough_data = response.json()
                    #Ordenamiento de los datos [[ronda, hora, votos, propios]]
                    #Los datos hora llengan en bruto en segundos, por eso se combierten a decimales para el trabajo (ejemplo 12.30)
                    self.rough = [[row[0],segundos_a_hora_decimal(row[1]),row[2],row[3]]for row in rough_data]
                    self.h_v = [{"hora": i[1], "votos": i[3]} for i in self.rough]
                    self.suma_totales()
                    self.preparar_datos_para_grafico()
                    self.loader = False
                    self.success = True
                else:
                    self.loader = False
                    self.error = True
            except Exception as e:
                self.loader = False
                self.error = True
                print(f"Error: {e}")


    def preparar_datos_para_grafico(self):
        # Preprara los datos para el grafico de barras [{},{}]
        datos_grafico = []
        datos = self.rough
        for i in datos:
            hora = float(i[1])
            total_votos = int((i[2]))
            propios_votos = int((i[3]))
            datos_grafico.append({"name": f"{hora} hs", "total_votos": total_votos, "propios_votos": propios_votos})
        self.datos_grafico_varchart = datos_grafico


    def suma_totales(self):
        self.total = 0
        self.total_propios = 0
        for i in self.rough:
            self.total += i[2]
            self.total_propios += i[3]


    def set_dia(self, value: int):
        self.dia = value


    def set_año(self, value: int):
        self.año = value

    def set_uni(self, value: str):
        self.uni = value

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
    def validate_fields_t(self) -> bool:
        return (self.uni_empty or self.año_empty or self.dia_empty)