# Aqui puedes empezar a programar 😀
cantidad = int(input())
archivo = open("libros.txt","r")
lineas = archivo.readlines()
archivo.close()
for i in range(len(lineas)):
    lineas[i] = lineas[i].strip()
    lineas[i] = lineas[i].split(",")
    lineas[i][2] = int(lineas[i][2])
for i in range(cantidad):
    nuevo_or = input()
    nuevo = nuevo_or.split(",")
    repetido = False
    for j in range(len(lineas)):
        if lineas[j][0] == nuevo[0]:
            lineas[j][2] += 1
            repetido = True
    if repetido == False:
        nuevo.append(1)
        lineas.append(nuevo)
archivo = open("libros.txt","w")
for k in range(len(lineas)):
    if type(lineas[k])  == list:
        lineas[k][2] = str(lineas[k][2])
        print(",".join(lineas[k]),file=archivo)
    else:
        print(lineas[k],file=archivo)
archivo.close()