from random import randint
class Maquina:

    def __init__(self, nombre, probabilidad_ganar, tickets_premio):
        self.nombre = nombre
        self.probabilidad_ganar = probabilidad_ganar
        self.tickets_premio = tickets_premio
        self.tickets_disponibles = 5000
        self.encendida = True

    def apagar(self):
        self.encendida = False
    
    def encender(self):
        self.encendida = True

    def jugar(self):
        numero = randint(0, 100)
        if numero <= self.probabilidad_ganar:
            if self.tickets_disponibles >= self.tickets_premio:
                self.tickets_disponibles -= self.tickets_premio
                return [self.tickets_premio,True]
            self.tickets_disponibles = 0
            return [self.tickets_disponibles - self.tickets_premio,False]
        return [0,True]

class Arcade:

    def __init__(self, nombre, maquinas, premios):
        self.nombre = nombre
        self.premios_disponibles = premios
        self.maquinas = maquinas

    def agregar_premio(self,premio):
        self.premios_disponibles.append(premio)

    def entregar_premio(self,tickets):
        mayor = ["",0]
        tickets_mayor = 0
        for elem in self.premios_disponibles:
            if tickets>=elem[1] > tickets_mayor:
                tickets_mayor = elem[1]
                mayor = elem
        if mayor != ["",0]:
            self.premios_disponibles.remove(mayor)
        return mayor