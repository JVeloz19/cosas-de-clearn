def impariestos_rec(a, dias):
    if a %5 == 0 or a%7 == 0: #390 dias
        if dias < 390:
            return a
        return impariestos_rec(a+1,dias-390)
    else:
        if dias < 360:
            return a
        return impariestos_rec(a+1,dias-360)