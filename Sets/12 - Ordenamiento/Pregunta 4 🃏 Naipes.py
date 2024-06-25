# Aqui puedes empezar a programar 😀
def criterio(item):
    return item[0]
cartas = input().split(",")
for i in range(len(cartas)):
    numero = int(input())
    cartas[i] = [numero,cartas[i]]
ordenadas = []
for pinta in ("CPDT"):
    temporal = []
    for carta in cartas:
        if carta[1] == pinta:
            temporal.append(carta)
    for i in sorted(temporal,key = criterio):
        ordenadas.append(i)
print(ordenadas)