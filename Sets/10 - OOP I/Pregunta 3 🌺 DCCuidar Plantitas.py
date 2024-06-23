# Aqui puedes empezar a programar 😀
class Planta:
    def __init__(self,nombre,frecuencia_riego):
        self.nombre = nombre
        self.frecuencia_riego = frecuencia_riego
        self.proximo_riego = 0
    
    def se_riega_hoy(self):
        if self.proximo_riego == 0:
            return True
        else:
            return False
    
    def regar(self):
        self.proximo_riego = self.frecuencia_riego


cantidad = int(input())
lista_plantas = []
for i in range(cantidad):
    lista = (input().split(","))
    lista_plantas.append(Planta(lista[0],int(lista[1])))
dias = int(input())
contador = 0
while contador<dias:
    print(f"DIA {contador+1}")
    ninguna = True
    for planta in lista_plantas:
        if planta.se_riega_hoy() == True:
            planta.regar()
            ninguna = False
            print(f"Se ha regado {planta.nombre}")
        planta.proximo_riego -=1

    if ninguna == True:
        print("Nada que regar hoy :)")
    contador+=1