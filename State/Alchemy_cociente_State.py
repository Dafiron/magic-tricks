import reflex as rx

class Alchemy_Cociente(rx.State):
    total_votos : int = 0
    votos_validos : int = 0
    lugares : int = 0
    blancos : int = 0
    nulos : int = 0
    nombre : str = ""
    votos : int = 0
    candidaturas: list[dict] = []
    resultados: list[dict] = []
    orden_asuncion: list[dict] = []
    choice : bool = False
    cociente : int = 0
    success : bool = False

    def añadir_candidatura(self):
        self.candidaturas.append({"id": len(self.candidaturas),'nombre': self.nombre, 'votos': int(self.votos)})
        self.calcular_resultado()



    def eliminar_candidatura(self, id):
        self.candidaturas = [c for c in self.candidaturas if c["id"] != id]
        self.calcular_resultado()


    def cociente_calculate(self):
        #choice define el uso o no de los numeros blancos y nulos 
        if self.choice == False:
            self.cociente=self.total_votos/self.lugares
        else:
            self.cociente=self.votos_validos/self.lugares

    def calcular_resultado(self):
        # Calcular total de votos dependiendo de la elección
        if not self.choice:
            votos_total = self.blancos + self.nulos + sum([c['votos'] for c in self.candidaturas])
            self.total_votos = votos_total
            self.cociente_calculate()
        else:
            votos_validos_sin_bn_ni_nulos = sum([c['votos'] for c in self.candidaturas])
            self.votos_validos = votos_validos_sin_bn_ni_nulos
            self.cociente_calculate()

        # Calcular escaños iniciales y restos
        escaños_asignados = {}
        restos = {}
        for c in self.candidaturas:
            escaños_asignados[c['nombre']] = int(c['votos'] // self.cociente)
            restos[c['nombre']] = c['votos'] % self.cociente

        # Calcular escaños restantes y ordenar restos
        escaños_restantes = max(0, int(self.lugares - sum(escaños_asignados.values())))
        restos_ordenados = sorted(restos.items(), key=lambda item: item[1], reverse=True)
        self.orden_asuncion = []

        lugar = 1
        for nombre, escaños in escaños_asignados.items():
            for _ in range(escaños):
                self.orden_asuncion.append({'nombre': nombre, 'orden': lugar})
                lugar += 1

        for i in range(escaños_restantes):
            if i < len(restos_ordenados):
                nombre = restos_ordenados[i][0]
                escaños_asignados[nombre] += 1
                self.orden_asuncion.append({'nombre': nombre, 'orden': lugar})
                lugar += 1

        # Ordenar el resultado final
        self.resultados = [{'nombre': nombre, 'escaños': escaños_asignados[nombre]} for nombre in escaños_asignados]
        self.resultados.sort(key=lambda x: (-x['escaños'], x['nombre']))


    def for_choice_total(self):
        #Variable choice tambien define que se va a mostrar como resultado
        if self.choice == False:
            return self.total_votos
        else:
            return self.votos_validos

    def cociente_event(self):
        self.success = not self.success
