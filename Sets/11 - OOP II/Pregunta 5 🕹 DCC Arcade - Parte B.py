from random import randint
from funciones import *
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

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
        self.tickets = 0
        self.premios = []

    def jugar_maquina(self,arcade,nombre_maquina):
        for maquina in arcade.maquinas:
            if maquina.nombre == nombre_maquina:
                if maquina.encendida == False:
                    print(f"La maquina {maquina.nombre} no esta encendida... pinche arcade {arcade.nombre} wey D:")
                else:
                    print(f"Voy a jugar a la maquina {maquina.nombre}!" )
                    juego = maquina.jugar()
                    self.tickets += juego[0]
                    if juego[0] == 0:
                        print("Pucha perdi :c")
                    elif juego[1] == True:
                        print(f"WOW he ganado {juego[0]} tickets")
                    elif juego[1] == False:
                        print(f"WOW he ganado {juego[0]} tickets, pero debi ganar {maquina.tickets_premio} tickets... :(\nLlamare a un encargado antes de irme aunque no me de los tickets >:(")
                        llamar_encargado_tickets(maquina)
    
    def canjear_premio(self,arcade):
        premio = arcade.entregar_premio(self.tickets)
        if premio[0] != "":
            self.premios.append(premio[0])
            self.tickets -= premio[1]
            print(f"He canjeado el premio {premio[0]}")
    
    def __str__(self):
        return f"Soy {self.nombre} tengo {self.tickets} tickets y {len(self.premios)} premios!"


def ejecutar_acciones(arcade,persona,lista_acciones):
    for accion in lista_acciones:
        if accion == "canjear premio":
            persona.canjear_premio(arcade)
        accion = accion.split(" ")
        accion_ = accion.pop(0)
        nombre = " ".join(accion)
        for maquina in arcade.maquinas:
            if maquina.nombre == nombre:
                objeto_maquina = maquina
        if "jugar" in accion_:
            persona.jugar_maquina(arcade,nombre)
        elif "apagar" in accion_:
            objeto_maquina.apagar()
        elif "encender" in accion_:
            objeto_maquina.encender()