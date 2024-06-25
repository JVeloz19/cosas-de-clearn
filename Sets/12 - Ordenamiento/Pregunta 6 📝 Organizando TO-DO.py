from funciones import *
class Tarea:

    def __init__(self, nombre, estado, importancia, dias_restantes):
        self.nombre = nombre
        self.estado = estado
        self.importancia = importancia
        self.dias_restantes = dias_restantes

def criterio1(item):
    urgencia = item.importancia/item.dias_restantes
    return item.estado[-1:],urgencia
    #Esta linea anterio es pura suerte que la ultima letra de cada estado
    #Coincide justo al revés, ej: "En progresO", "PendientE" o "TerminadA"
    #O,E,A por ende si entregamos el reves, seran A,E,O, que casualmente nos sirve
    # Por esto mismo, al hacer reves, las obtengo ordenadas como corresponde
    # Igualemento esto es muy especifico del caso, poniendo una serie de if funciona
    # de forma mas general
# ༼ つ ◕_◕ ༽つ Completa el codigo ༼ つ ◕_◕ ༽つ
def mostrar_tareas_ordenadas(lista_tareas):
    ordenada = sorted(lista_tareas,key=criterio1,reverse=True)
    mostrar_tareas(ordenada)