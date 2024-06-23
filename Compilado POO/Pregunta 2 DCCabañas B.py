# Escribe tu código aquí
class Cabana:

    def __init__(self,numero,capacidad):
        self.numero = numero
        self.capacidad = int(capacidad)
        self.ocupacion = 0

    def esta_vacia(self):
        if self.ocupacion == 0:
            return True
        return False
    
    def ocupar(self,numero_personas):
        if numero_personas <= self.capacidad and self.ocupacion ==0:
            self.ocupacion += numero_personas
            return True
        return False

    def __str__(self):
        return f"{self.numero} ({self.ocupacion}/{self.capacidad})"

class Camping:

    def __init__(self,nom):
        self.nom = nom
        self.cabanas = []

    def instalar(self,c):
        self.cabanas.append(c)

    def disponibles(self):
        contador = 0
        for cabana in self.cabanas:
            if cabana.ocupacion == 0:
                contador +=1
        return contador

    def achicar(self,c):
        ocupantes = c.ocupacion
        posibles = []
        for cabana in self.cabanas:
            if cabana.esta_vacia():
                if ocupantes <= cabana.capacidad < c.capacidad:
                    posibles.append(cabana.numero)
        return posibles