# Escribe tu código aquí!
class Planta:
    
    def __init__(self,nombre,resistencia):
        self.nombre = nombre
        self.agua = 0
        self.resistencia = resistencia

    def __str__(self):
        return f"{self.nombre} - {self.agua}/{self.resistencia}"

    def regar(self,agua):
        if self.agua + agua < self.resistencia:
            self.agua += agua
        else:
            self.agua = self.resistencia
    
class Huerto:

    def __init__(self):
        self.plantas = []

    def regar_planta(self,nombre_planta,agua):
        for i in self.plantas:
            if i.nombre == nombre_planta:
                i.regar(agua)
        
    def plantar(self,planta):
        if planta not in self.plantas:
            self.plantas.append(planta)
            planta.agua += 5