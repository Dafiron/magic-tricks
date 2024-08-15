import reflex as rx

class Alchemy_Max_Min(rx.State):
    nombre : str = ""
    votos : int = 0
    total_votos: int = 0
    candidaturas: list[dict] = []
    resultados: list[dict] = []
    success: bool = False


    def añadir_candidatura(self):
        self.candidaturas.append({"id": len(self.candidaturas),'faccion': self.nombre, 'votos': int(self.votos)})
        self.resultados_totales()

    def resultados_totales(self):
        if self.candidaturas:
            #Calcula el total votos, con la cantidad de votos individuales de cada faccion
            self.total_votos = sum(c['votos'] for c in self.candidaturas)
            resultados = []
            #Iteranuevamente nuevamente pero con el total de votos
            for c in self.candidaturas:
                porcentaje = round(c['votos'] / self.total_votos * 100, 2)
                resultados.append({"nombre": c['faccion'], "porcentaje": f"{porcentaje}%"})
            self.resultados = resultados


    def eliminar_candidatura(self, id):
        self.candidaturas = [c for c in self.candidaturas if c["id"] != id]

    def max_min_event(self):
        self.success = not self.success

