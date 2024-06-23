# Aqui puedes empezar a programar 😀
def cargar_archivo(nombre_archivo):
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        print(linea.strip())
cargar_archivo(input())