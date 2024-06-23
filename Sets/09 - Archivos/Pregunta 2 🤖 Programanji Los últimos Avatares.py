# Aqui puedes empezar a programar 😀
def escribir_archivo(nombre_archivo, lineas):
    archivo = open(nombre_archivo,"w")
    for i in lineas:
        print(i,file=archivo)
    archivo.close()

nombre_archivo = input()
cantidad = int(input())
lista_str = []
for i in range(cantidad):
    lista_str.append(input())
escribir_archivo(nombre_archivo,lista_str)