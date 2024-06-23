# Aqui puedes empezar a programar 😀
class Mascota:
    def __init__(self,nombre,patas):
        self.nombre = nombre
        self.patas = int(patas)
    
    def saludar(self):
        print(f"Hola, Humano! Un gusto poder hablarte, mi nombre es {self.nombre} y tengo {self.patas} patas!")

    def __str__(self):
        return f"Mascota: {str(self.nombre)}"
    
nombre = input()
patas = input()
m = Mascota(nombre,patas)
print(m)
m.saludar()