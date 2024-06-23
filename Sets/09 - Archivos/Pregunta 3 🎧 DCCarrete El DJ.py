# Aqui puedes empezar a programar 😀
artista = input()
archivo = open("mejores_canciones.txt","r")
lineas = archivo.readlines()
archivo.close()
for linea in lineas:
    linea = linea.strip()
    linea = linea.split(",")
    if linea[1] == artista:
        print(f"Cancion: {linea[0]} - {linea[2]}")