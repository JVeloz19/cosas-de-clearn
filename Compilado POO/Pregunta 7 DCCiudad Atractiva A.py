### No modificar ###

class Atraccion:
    def __init__(self,n,x,y,p):
        self.nombre = n
        self.x = x
        self.y = y
        self.principal = p

    def distancia(self, otra_atraccion):
        # A continuación de calcula la distancia entre las atracciones
        return ((self.x - otra_atraccion.x) ** 2 + (self.y - otra_atraccion.y) ** 2) ** (1/2)

    def __str__(self):
        return "Atraccion " + self.nombre + " - (" + str(self.x) + ", " +str(self.y)+")"

class Clasificador:

    def __init__(self):
        self.principales = []
        self.secundarias = []

    def agregar_atraccion(self, atraccion):
        if atraccion.principal == True:
            self.principales.append(atraccion)
        else:
            self.secundarias.append(atraccion)