##AQUI PUEDES ESCRIBIR TU CODIGO
class Nerdflix:

    def __init__(self):
        self.peliculas = []
        self.usuarios = []
        self.visualizaciones = []

    def agregar_usuario(self, u ):
        self.usuarios.append(u)

    def agregar_pelicula(self, p):
        self.peliculas.append(p)

    def peli_disponible(self, n): 
        for peli in self.peliculas:
            if peli.nombre == n:
                return True
        return False

    def users_fragiles(self):
        lista = []
        for user in self.usuarios:
            if user.pass_fragil():
                lista.append(user.nombre)
        return lista

    def nuevo_visionado(self, u, p):
        self.visualizaciones.append([u,p])

    def max_visionador(self, n):
        viewers = []
        for visu in self.visualizaciones:
            if visu[1].nombre == n:
                viewers.append(visu[0])
        mas_vicio = None
        contador_mas_vicio = 0
        for viewer in viewers:
            if viewers.count(viewer) > contador_mas_vicio:
                contador_mas_vicio = viewers.count(viewer)
                mas_vicio = viewer
            elif viewers.count(viewer) == contador_mas_vicio:
                if len(viewer.nombre) < len(mas_vicio.nombre):
                    contador_mas_vicio = viewers.count(viewer)
                    mas_vicio = viewer
        if mas_vicio == None:
            return ""
        else:
            return mas_vicio.nombre