class IntroWallet:

    def __init__(self, propietario, introcoin, bitcoin, valor_bitcoin_a_introcoin):
        self.propietario = propietario
        self.introcoin = float(introcoin)
        self.bitcoin = float(bitcoin)
        self.valor_bitcoin_a_introcoin = float(valor_bitcoin_a_introcoin)

    def depositar(self, cantidad, tipo):
        if tipo == "bitcoin":
            self.bitcoin += cantidad
        elif tipo == "introcoin":
            self.introcoin += cantidad
        else:
            return  "No se ha podido realizar el deposito"
        return f"Se han depositado {cantidad} {tipo} correctamente"

    def bitcoin_a_introcoin(self):
        bc = self.bitcoin
        equivalente = round(((1/self.valor_bitcoin_a_introcoin)*bc),3)
        return [bc,equivalente]

    def introcoin_a_bitcoin(self):
        ic = self.introcoin
        equivalente = round((self.valor_bitcoin_a_introcoin*ic),3) 
        return [ic,equivalente]

    def pagar(self, cantidad, tipo):
        if tipo == "bitcoin" and self.bitcoin >= cantidad:
            self.bitcoin -= cantidad
            return(f"Compra exitosa por {cantidad} {tipo}")
        elif tipo == "introcoin" and self.introcoin >= cantidad:
            self.introcoin -= cantidad
            return(f"Compra exitosa por {cantidad} {tipo}")
        else:
            if tipo == "bitcoin": 
                nuevo = self.introcoin_a_bitcoin()
                if self.bitcoin + nuevo[1] >= cantidad:
                    self.bitcoin = self.bitcoin + nuevo[1] - cantidad
                    self.introcoin = 0
                    return(f"Se han cambiado {nuevo[0]} introcoin a {nuevo[1]} bitcoin y se ha realizado el pago")
            elif tipo == "introcoin":
                nuevo = self.bitcoin_a_introcoin()
                if self.introcoin + nuevo[1] >= cantidad:
                    self.introcoin = self.introcoin + nuevo[1] - cantidad
                    self.bitcoin = 0
                    return(f"Se han cambiado {nuevo[0]} bitcoin a {nuevo[1]} introcoin y se ha realizado el pago")
            return("No hay fondos suficientes para realizar el pago")

    def __str__(self):
        return f"IntroWallet de {self.propietario}\nSaldo de introcoin: {round(self.introcoin,3)}\nSaldo de bitcoin: {round(self.bitcoin,3)}"

def realizar_acciones(introwallet, lista_acciones):
    for accion in lista_acciones:
        if accion[0] == "pagar":
            print(introwallet.pagar(accion[1],accion[2]))
        else:
            print(introwallet.depositar(accion[1],accion[2]))
    print(introwallet)