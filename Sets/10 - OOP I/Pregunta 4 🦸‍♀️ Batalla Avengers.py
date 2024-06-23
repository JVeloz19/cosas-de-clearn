class Superheroe:

    def __init__(self, nombre, vida, fuerza, defensa):
        self.nombre = nombre
        self.vida = int(vida)
        self.fuerza = int(fuerza)
        self.defensa = int(defensa)

    def golpear(self, other):
        daño = max(self.fuerza - other.defensa, 0)
        if daño<other.vida:
            other.vida -= daño
        else:
            other.vida = 0

    def __str__(self):
        return f"{self.nombre} {self.vida}"

def combate(superheroe_1, superheroe_2, rounds):
    contador = 1
    while contador <= rounds and superheroe_1.vida>0 and superheroe_2.vida>0:
        if contador %2 != 0:#Turno Sup1
            superheroe_1.golpear(superheroe_2)
        elif contador %2 == 0: #Turno Sup2
            superheroe_2.golpear(superheroe_1)
        contador+=1
    if superheroe_2.vida < superheroe_1.vida:
        lista = [superheroe_1,superheroe_2]
    else :
        lista = [superheroe_2,superheroe_1]
    return lista