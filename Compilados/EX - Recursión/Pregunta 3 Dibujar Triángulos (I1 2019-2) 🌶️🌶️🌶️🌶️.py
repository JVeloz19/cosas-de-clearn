# Recuerda que puedes agregar más parámetros si lo crees necesario
def dibujar(n,f=0):
    print("_"*f+"*",end = "")
    if n != 1:
        print("_*"*(n-1))
        dibujar(n-1,f+1)
base = int(input())
dibujar(base)