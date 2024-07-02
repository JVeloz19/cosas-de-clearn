# Escribe tu código aquí!
from dccine import *
arch = open("subtitulos.txt")
subtitulos = arch.readlines()
arch.close()
arch = open("postcreditos.txt")
postcreditos = arch.readlines()
arch.close()
pos_or = []

for i in range(len(subtitulos)):
    subtitulos[i] = subtitulos[i].strip().split("#")
for i in range(len(postcreditos)):
    postcreditos[i] = postcreditos[i].strip().split("#")
    rever_pos = revertir(postcreditos[i][0],postcreditos[i][1])
    if  rever_pos != ["",""]:
        for k in range(len(subtitulos)):
            if subtitulos[k][0] == rever_pos[0] and subtitulos[k][1] == rever_pos[1]:
                pos_or.append([postcreditos[i][0],postcreditos[i][1],subtitulos[k][2]])
                subtitulos[k] = [subtitulos[k][0],subtitulos[k][1],postcreditos[i][2]]
    else:
        pos_or.append(postcreditos[i])

arch = open("subtitulos_originales.txt","w")
for k in subtitulos:
    print("#".join(k),file=arch)
arch.close()

arch = open("postcreditos_originales.txt","w")
for i in pos_or:
    print("#".join(i),file=arch)
arch.close()