# Aqui puedes empezar a programar 😀
from chess import *
class Celda:

    def __init__(self,fila,columna):
        self.pieza = ""
        self.fila = fila
        self.columna = columna

class Ajedrez:

    def __init__(self):
        self.dimension = 8
        self.tablero = []

    def crear_tablero(self):
        for i in range(self.dimension):
            fila = []
            for j in range(self.dimension):
                fila.append(Celda(i,j))
            self.tablero.append(fila)

    def anadir_pieza(self,pieza,fila,columna):
        celda = self.tablero[fila][columna] 
        celda.pieza = pieza

    def comprobar_jaque(self):
        lista = []
        for i in self.tablero:
            for celda in i:
                if celda.pieza == "Rey":
                    fila_rey = celda.fila
                    columna_rey = celda.columna
        for i in self.tablero:
            for cell in i:
                if cell.pieza in ["Alfil", "Torre" , "Dama"]:
                    posibles_mov = obtener_posibles_movimientos(cell.pieza, cell.fila, cell.columna)
                    if [fila_rey,columna_rey] in posibles_mov:
                        lista.append(cell)
        return lista