import reflex as rx

#hay variables a drede de mas, decidi dejarla para un futuro update

class Alchemy(rx.State):
    lugares : int = 0
    nombre : str = ""
    votos : int = 0
    porcentaje_min : int = 0
    total_votos: int = 0
    blancos : int = 0
    nulos : int = 0
    candidaturas: list[dict] = []
    resultados: list[dict] = []
    success: bool = False



    def añadir_candidatura(self):
        self.candidaturas.append({"id": len(self.candidaturas),'nombre': self.nombre, 'votos': int(self.votos)})
        self.calcular_resultado()

    def calcular_resultado(self):
        # Calcular el número de escaños disponibles
        escaños = self.lugares
        
        # Crear una lista de cocientes para cada candidatura
        cocientes = []
        for c in self.candidaturas:
            votos = c['votos']
            for divisor in range(1, escaños + 1):
                cocientes.append((votos / divisor, c['nombre'], divisor))
        
        # Ordenar los cocientes en orden descendente
        cocientes.sort(reverse=True, key=lambda x: x[0])
        
        # Verificar si hay suficientes cocientes para asignar todos los escaños
        if len(cocientes) < escaños:
            escaños = len(cocientes)  # Ajustar el número de escaños a los disponibles

        # Asignar los escaños
        escaños_asignados = {}
        for i in range(escaños):
            cociente = cocientes[i]
            nombre = cociente[1]
            if nombre in escaños_asignados:
                escaños_asignados[nombre] += 1
            else:
                escaños_asignados[nombre] = 1
        
        # Actualizar el resultado
        self.resultados = [{'nombre': nombre, 'escaños': escaños_asignados.get(nombre, 0)} for nombre in escaños_asignados]

    def eliminar_candidatura(self, id):
        self.candidaturas = [c for c in self.candidaturas if c["id"] != id]
        self.calcular_resultado()

    def d_dondt_event(self):
        self.success = not self.success

