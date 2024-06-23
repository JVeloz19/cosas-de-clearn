############################

# IMPLEMENTA AQUÍ TU CLASE

class Usuario:

    def __init__(self,nombre,contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def pass_fragil(self):
        if len(self.contraseña) < 8 or self.contraseña.isalpha():
            return True
        return False