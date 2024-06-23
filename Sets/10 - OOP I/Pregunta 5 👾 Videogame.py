class Jugador:

    def __init__(self, nombre, vida, exp):
        self.nombre =  nombre
        self.vida = int(vida)
        self.exp = int(exp)
        self.monedas = 0

    def tomar_pocion_exp(self, tamano):
        if self.monedas < 5:
            return False
        else:
            self.monedas -= 5
            if tamano == "grande":
                self.exp += 5
            elif tamano == "chica":
                self.exp += 3
            return True

    def tomar_pocion_vida(self, tamano):
        if self.exp < 5:
            return False
        else:
            self.exp -= 5
            if tamano == "grande":
                self.vida += 5
            elif tamano == "chica":
                self.vida += 3
            return True

    def luchar(self, oponente):
        fuerza = self.vida + self.exp
        if fuerza >= oponente:
            return True
        else:
            self.vida = 0
            return False

    def __str__(self):
        return f"------ RESUMEN RONDA ------\nNombre: {self.nombre}\nVida: {self.vida}\nExperiencia: {self.exp}\nMonedas: {self.monedas}"


def comenzar_aventura(jugador, eventos):
    turno = 0
    while turno < len(eventos) and jugador.vida > 0:
        evento = eventos[turno]
        if "chica" in evento:
            tamano = "chica"
        elif "grande" in evento:
            tamano = "grande"

        if "pocion exp" in evento:
            resultado = jugador.tomar_pocion_exp(tamano)
            if resultado == True:
                print('>> He tomado la pocion de experiencia')
            else:
                print('>> No me alcanzan las monedas para tomar la pocion')
        
        elif "pocion vida" in evento:
            resultado = jugador.tomar_pocion_vida(tamano)
            if resultado == True:
                print('>> He tomado la pocion de vida')
            else:
                print('>> No me alcanza la experiencia para tomar la pocion')

        elif evento == "bolsa de monedas":
            jugador.monedas += 4
            print(">> Encontre monedas")

        elif evento.isdecimal():
            fuerza_oponente = int(evento)
            resultado = jugador.luchar(fuerza_oponente)
            if resultado == True:
                print('>> Gane el combate')
            else:
                print('>> Fui derrotado')
        print(jugador)
        turno +=1