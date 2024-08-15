import reflex as rx
import requests as rq
from Magic_Tricks_d.components.components import segundos_a_hora_decimal

#Instruccion donde esta el back:
back ="https://magic-back.onrender.com"

class GlobalState(rx.State):
    loader: bool = False
    rough : list[list] #bruto
    h_v: list[dict]
    dict_format:list[dict]
    año : int = 0
    uni : str = ""
    dic_sobre_dias : dict = {}
    purga : float = 0.00
    global_total : int = 0
    global_propios : int = 0
    datos_grafico_varchart : list[dict]
    porcentaje : float = 0.00
    porcentaje_r : float = 0.00
    info_success : bool =False
    error: bool = False
    success: bool = False

    @rx.background
    async def GlobalService(self):
        async with self:
            self.loader = True
            self.error = False
            self.success = False
            try:
                response = rq.get(f"{back}/number/call_ua", params={"uni": self.uni, "año": self.año})
                if response.status_code == 200:
                    rough_data = response.json()
                    rough_data = self.depuracion(rough_data)
                    #Los datos brutos llegan con la variable hora en segundos por eso se pasan a decimal para mejor trabajo "ejemplo 12.30"
                    # oden de los datos [[dia, ronda, hora, votos, propios]]
                    self.rough = [[row[0],row[1],segundos_a_hora_decimal(row[2]),row[3],row[4]]for row in rough_data]
                    self.h_v = [{"hora": i[1], "votos": i[3]} for i in self.rough]
                    self.global_total = int(sum(i[3]for i in self.rough))
                    self.global_propios = int(sum(i[4]for i in self.rough))
                    self.porsentaje()
                    self.dividir_por_dia(rough_data)
                    # Los graficos de barras y de torata requieren una presentacion de datos != por eso la discriminacion
                    self.formateo_paicha()
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

    def set_año(self, value: int):
        self.año = value

    def set_uni(self, value: str):
        self.uni = value
    
    def set_purga(self, value: float):
        self.purga = value

    def porsentaje(self):
        #Calcula los porsentajes en relacion del rival en relacion a los propios y los totales
        if self.global_total != 0:
            self.porcentaje=round((self.global_propios/self.global_total)*100, 2)
            rival= self.global_total-self.global_propios
            self.porcentaje_r=round((rival/self.global_total)*100, 2)
        else:
            self.porcentaje = 0.00
            self.porcentaje_r = 0.00

    def dividir_por_dia(self, data):
        # Ordena un diccionario con los resultados por dia
        dias = {}
        for entrada in data:
            dia = entrada[0]
            if dia not in dias:
                dias[dia] = []
            dias[dia].append(entrada)
        
        self.dic_sobre_dias = {dia: list(entradas) for dia, entradas in dias.items()}

    def formateo_paicha(self):
        # Prepara los datos para el grafico de torta
        if self.global_propios >= 1 and self.global_total >= 1:
            dict_fotmat =[]
            votos = self.global_propios
            globales = self.global_total
            rival = globales - votos
            dict_fotmat.append({"faccion":"Propios","votos": votos})
            dict_fotmat.append({"faccion":"Rival","votos":rival})
            self.dict_format = dict_fotmat
        else:
            print("condicion de formateo_paicha no cumplida")
    
    def preparar_datos_para_grafico(self):
        # Prepara los datos para el grafico de barras
        datos_grafico = []
        dias = self.dic_sobre_dias 
        for dia, entradas in dias.items():
            total_votos = int(sum(entrada[3] for entrada in entradas))
            propios_votos = int(sum(entrada[4] for entrada in entradas))
            datos_grafico.append({"name": f"Dia {dia}", "total_votos": total_votos, "propios_votos": propios_votos})
        self.datos_grafico_varchart = datos_grafico


    def depuracion (self,rough):
        # La depuracion es una depuracion simple donde el total se multiplica por un numero X (debiera ser 0.9X para que de un numero razonable) 
        purga_format = self.purga
        rough_purged=[]
        contador= 0
        if self.purga != 0: 
            for row in rough:
                row[4]= float(purga_format)*float(row[4])
                contador += 1
                rough_purged.append(row)
        return rough_purged

    @rx.var
    def uni_empty(self) -> bool:
        return not self.uni.strip()

    @rx.var
    def año_empty(self) -> bool:
        return self.año == 0

    @rx.var
    def purga_empty(self) -> bool:
        return self.purga == 0.0

    @rx.var
    def validate_fields_g(self) -> bool:
        return (self.uni_empty or self.año_empty or self.purga_empty)