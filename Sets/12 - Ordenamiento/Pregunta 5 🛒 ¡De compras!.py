# Aqui puedes empezar a programar 😀
def criterio1(item):
    return item[1]
def criterio2(item):
    return item[0]
def criterio3(item):
    return item[2],item[0]

compras = []
producto = input()
while producto != "FIN":
    producto = producto.split(",")
    producto[1] = int(producto[1])
    compras.append(producto)
    producto = input()

print(f"Lista ordenada por precio:\n{sorted(compras,key = criterio1)}")
print(f"Lista ordenada por orden alfabetico:\n{sorted(compras,key = criterio2)}")
print(f"Lista ordenada por categoria:\n{sorted(compras,key = criterio3)}")