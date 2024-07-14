# Escribe tu código aquí!
from dccine import *
arch = open("subtitulos.txt")
sub = arch.readlines()
arch.close()

for i in range(len(sub)):
    sub[i] = sub[i].strip().split("#")

n = int(input())
for i in range(n):
    tiempo = input()
    aviso = False
    for k in sub:
        if (comparar_tiempos(tiempo, k[0]) == 0) or (comparar_tiempos(tiempo, k[0]) == 2):
            if (comparar_tiempos(tiempo, k[1]) == 1) or (comparar_tiempos(tiempo, k[1]) == 2):
                print(f"{tiempo} - {k[2]}")
                aviso = True
    if aviso == False:
        print(f"No existe un dialogo para el tiempo {tiempo}")