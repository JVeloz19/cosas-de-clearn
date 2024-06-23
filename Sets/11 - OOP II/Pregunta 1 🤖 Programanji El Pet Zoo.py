# Aqui puedes empezar a programar 😀
class Animal:

    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"El animal {self.nombre} es de tipo {self.tipo}"

class Zoologico:

    def __init__(self,nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animales(self,isntancia_animal):
        self.animales.append(isntancia_animal)