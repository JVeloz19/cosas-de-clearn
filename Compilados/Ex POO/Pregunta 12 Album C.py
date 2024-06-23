class Lamina:
    def __init__(self, numero, cantidad):
        self.numero = numero
        self.cantidad = cantidad

    def esta_repetida(self):
        return self.cantidad != 1


class Puzzle:
    def __init__(self, n_inicial, n_final):
        self.numero_inicial = n_inicial
        self.numero_final = n_final


class Album:
    def __init__(self, nombre, n):
        self.nombre = nombre
        self.puzzles = []
        self.n = n

    def agregar_puzzle(self, n_inicial, n_final):
        p = Puzzle(n_inicial, n_final)
        self.puzzles.append(p)


class Coleccion:
    def __init__(self, a):
        self.laminas = []
        self.album = a

    def agregar_lamina(self,num):
        repetida = False
        for lamina in self.laminas:
            if lamina.numero == num:
                lamina.cantidad +=1
                repetida = True
        if repetida == False:
            self.laminas.append(Lamina(num,1))

    def numero_repetidas(self):
        contador = 0 
        for lamina in self.laminas:
            if lamina.cantidad > 1:
                contador += 1
        return contador

    def numero_puzzles_completos(self):
        contador_puzzles = 0
        for puzzle in self.album.puzzles:
            contador = 0
            for num in range(puzzle.numero_inicial,puzzle.numero_final+1):
                for lamina in self.laminas:
                    if lamina.numero == num:
                        contador += 1
            if contador == (puzzle.numero_final - puzzle.numero_inicial +1):
                contador_puzzles +=1
        return contador_puzzles