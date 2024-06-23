##AQUI PUEDES ESCRIBIR TU CODIGO
class Ficha:
    
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    
    def rotar(self):
        n1 = self.n1
        self.n1 = self.n2
        self.n2 = n1

    def __str__(self):
        return f"[ {self.n1} | {self.n2} ]"

class Tablero:
    
    def __init__(self,ficha_inicial):
        self.fichas = [ficha_inicial] 

    def ficha_valida(self,ficha):
        ficha_izquiera = self.fichas[0]
        ficha_derecha = self.fichas[-1]
        if ficha_izquiera.n1 == ficha.n1 or ficha_izquiera.n1 == ficha.n2 or ficha_derecha.n2 == ficha.n1 or ficha_derecha.n2 == ficha.n2:
                return True
        return False
    
    def agregar(self,ficha):
        ficha_izquiera = self.fichas[0]
        ficha_derecha = self.fichas[-1]
        if ficha_izquiera.n1 == ficha.n2:
            self.fichas.insert(0,ficha)
        elif ficha_izquiera.n1 == ficha.n1:
            ficha.rotar()
            self.fichas.insert(0,ficha)
        elif ficha_derecha.n2 == ficha.n1:
            self.fichas.append(ficha)
        elif ficha_derecha.n2 == ficha.n2:
            ficha.rotar()
            self.fichas.append(ficha)