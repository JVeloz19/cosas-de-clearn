archivo = open("diccionario.txt")
diccionario = archivo.readlines()
archivo.close()

for i in range(len(diccionario)):
    diccionario[i] = diccionario[i].strip().split("-")
    diccionario[i] = [diccionario[i][0],diccionario[i][1]]

archivo = open("catalan.txt")
palabras = archivo.readlines()
archivo.close()
for palabra in palabras:
    palabra = palabra.strip()
    for dic in diccionario:
        if palabra == dic[0]:
            with open("castellano.txt", "a") as castellano:
                print(dic[1],file=castellano)