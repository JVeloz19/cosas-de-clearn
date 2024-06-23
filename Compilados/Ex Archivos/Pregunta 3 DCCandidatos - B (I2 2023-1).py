archivo = open("postulaciones.txt")
postulaciones = archivo.readlines()
total = []
nombres = []
final = []
for postulacion in postulaciones:
    postulacion = postulacion.strip().split(";")
    postulacion.pop(0)
    total.append([postulacion[0],5])
    total.append([postulacion[1],3])
    total.append([postulacion[2],1])
for elem in total: #elem = ["UC",5]
    if elem[0] in nombres:
        for i in range(len(final)):
            if final[i][0] == elem[0]:
                final[i][1] += elem[1]
    else:
        nombres.append(elem[0])
        final.append([elem[0],elem[1]])
puntajes = open("puntaje_universidades.txt","w")

for i in final:
    linea = [i[0],str(i[1])]
    print(";".join(linea),file=puntajes)
puntajes.close()