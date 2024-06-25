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
# ༼ つ ◕_◕ ༽つ Completa el codigo ༼ つ ◕_◕ ༽つ
def mostrar_tareas_ordenadas(lista_tareas):
    ordenada = sorted(lista_tareas,key=criterio1,reverse=True)
    mostrar_tareas(ordenada)