# Aqui puedes empezar a programar 😀
def es_primo(num):
    if num ==1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def factores_primos(n):
    if es_primo(n)== True:
        print(n)
    else:
        for i in range(2,n):
            if es_primo(i)==True and n%i==0:
                print(i)
                return factores_primos(n//i)