############################
# IMPLEMENTA AQUÍ TU CLASE
############################

class Pelicula:

    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año

    def posterior(self,año):
        if self.año >= año:
            return True
        return False