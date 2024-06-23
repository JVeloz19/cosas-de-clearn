# Aqui puedes empezar a programar 😀
for i in range(4):
    nombre = input()
    numero = nombre.strip(".txt")
    numero = numero.split("_")
    numero = numero[1]
    archivo = open(nombre,"w")
    archivo.close()
for i in range(int(input())):
    linea = input()
    linea = linea.split(",")
    archivo = open(linea[0]+"s_"+numero+".txt","a")
    linea.pop(0)
    print(",".join(linea),file=archivo)
    archivo.close()