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
