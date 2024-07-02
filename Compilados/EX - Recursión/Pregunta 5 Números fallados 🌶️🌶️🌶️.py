# No cambiar el nombre de la función
def fallado(n,ultimo):
    n = str(n)
    ultimo=str(ultimo)
    if len(n) == 1:
        return -1
    if n[-2] == ultimo:
        return ultimo
    if len(n)>=2:
        return fallado(n[:-1],n[-2])