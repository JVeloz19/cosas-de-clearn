# Aqui puedes empezar a programar 😀
class Famoso:
    
    def __init__(self,nombre,identificador,altura,fecha_nacimiento):
        self.nombre = nombre
        self.identificador = identificador
        self.altura = altura
        self.fecha_nacimiento = fecha_nacimiento

class PUCWood:

    def __init__(self):
        self.famosos = []

    def agregar_famoso(self,instancia_famoso):
        self.famosos.append(instancia_famoso)

    def filtrar_por_altura(self,simbolo,altura):
        lista = []
        for famoso in self.famosos:
            if simbolo == "<=":
                if famoso.altura <= altura:
                    lista.append(famoso.nombre)
            elif simbolo == ">=":
                if famoso.altura >= altura:
                    lista.append(famoso.nombre)
            elif simbolo == "=":
                if famoso.altura == altura:
                    lista.append(famoso.nombre)
        return lista

    def filtrar_por_nombre(self, string): 
        lista = []
        for famoso in self.famosos:
            if string in famoso.nombre:
                lista.append(famoso.nombre)
        return lista