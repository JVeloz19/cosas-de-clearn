def criterio(item):
    return item[1]
nombres = input().split(",")
for i in range(len(nombres)):
    nivel = int(input())
    nombres[i] = [nombres[i],nivel]
print(sorted(nombres,key=criterio,reverse=True))