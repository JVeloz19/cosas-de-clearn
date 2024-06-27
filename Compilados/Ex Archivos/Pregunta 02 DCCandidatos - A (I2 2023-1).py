archivo = open("postulaciones.txt")
postulaciones = archivo.readlines()
for postulacion in postulaciones:
    postulacion = postulacion.strip().split(";")
    estudiante = postulacion.pop(0)
    if len(postulacion) != 3:
        print(f"INVALIDO {estudiante}")
    elif postulacion[0] ==postulacion[1] or postulacion[0] ==postulacion[2] or postulacion[1] ==postulacion[2]:
            print(f"INVALIDO {estudiante}")
    else:
        print(f"VALIDO {estudiante}") 