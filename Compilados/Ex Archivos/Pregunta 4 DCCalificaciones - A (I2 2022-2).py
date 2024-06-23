def leer_archivos():
    ruts_validos = []
    aretornar = []
    archivo = open("ramos.csv")
    ramos = archivo.readlines()
    archivo.close()
    for i in range(len(ramos)):
        ramos[i] = ramos[i].strip().split(",")
        if "IIC1103" in ramos[i]:
            ruts_validos.append(ramos[i][0])

    archivo = open("estudiantes.csv")
    datos = archivo.readlines()
    archivo.close()
    for i in range(len(datos)):
        datos[i] = datos[i].strip().split(",")
        if datos[i][0] in ruts_validos:
            aretornar.append(datos[i])
    return aretornar