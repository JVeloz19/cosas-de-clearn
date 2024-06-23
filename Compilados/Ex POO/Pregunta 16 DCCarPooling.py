from dccarpooling import distancia

class Pasajero:
    def __init__(self, nombre, origen, destino):
        self.nombre = nombre
        self.origen = origen
        self.destino = destino



class Conductor:
    def __init__(self, nombre, origen, destinos, asientos):
        self.nombre = nombre
        self.origen = origen
        self.destinos = destinos
        self.disponibles = asientos
        self.pasajeros = []

    def tiene_asientos_libres(self):
        if self.disponibles - len(self.pasajeros) >0:
            return True
        return False

class VoyA:
    def __init__(self, pasajeros, conductores):
        self.pasajeros = pasajeros
        self.conductores = conductores

    def conductores_disponibles(self):
        disponibles = []
        for conductor in self.conductores:
            if conductor.tiene_asientos_libres():
                disponibles.append(conductor)
        return disponibles

    def pasajeros_sin_conductor(self): 
        lista = []
        for pasajero in self.pasajeros:
            tiene = False
            for conductor in self.conductores:
                if pasajero in conductor.pasajeros:
                    tiene = True
            if tiene == False:
                lista.append(pasajero)
        return lista
            
    def conductores_por_destino(self, destino):
        lista = []
        for conductor in self.conductores:
            if conductor.tiene_asientos_libres() and destino in conductor.destinos:
                lista.append(conductor)
        return lista

    def escoger_conductor(self, pas): 
        conductores = self.conductores_por_destino(pas.destino)
        if len(conductores) == 1:
            return conductores[0]
        else:
            for i in range(len(conductores)):
                conductor = conductores[i]
                dis = distancia(pas.origen,conductor.origen)
                if i == 0:
                    menor_distancia = dis
                    menor_conductor = conductor
                elif dis < menor_distancia:
                    menor_distancia = dis
                    menor_conductor =conductor
            return menor_conductor

    def asignar_pasajeros(self): 
        pasajeros = self.pasajeros_sin_conductor()
        for pasajero in pasajeros:
            conductor = self.escoger_conductor(pasajero)
            conductor.pasajeros.append(pasajero)