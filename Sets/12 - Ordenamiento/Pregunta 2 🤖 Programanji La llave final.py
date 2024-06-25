# Aqui puedes empezar a programar 😀
def criterio1(item):
    return item[0]
def criterio2(item):
    return item[1]

cantidad = int(input())
posiciones = []
for i in range(cantidad):
    linea = input().split(",")
    linea[0] = int(linea[0])
    posiciones.append(linea)
print(sorted(posiciones,key=criterio1))
print(sorted(posiciones,key=criterio2))