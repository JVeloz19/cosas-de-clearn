def seccion_alumno(alumnos,num_al):
    for i in alumnos:
        if i[0] == num_al:
            return i[1]

votos_validos = [[],[],[]]
resumen = [] #Nombre de cada voto valido
archivo = open("alumnos.txt")
alumnos = archivo.readlines()
for i in range(len(alumnos)):
    alumnos[i] = alumnos[i].strip().split(",")
archivo.close()

for i in ["votaciones_s1.txt","votaciones_s2.txt","votaciones_s3.txt"]:
    votos_invalidos = []
    seccion = int(i[-5])
    votaciones = open(i)
    votos = votaciones.readlines()
    votaciones.close()
    for i in range(len(votos)):
    
        voto = votos[i].strip().split(",")
        sec_correcta = False
        if seccion_alumno(alumnos, voto[0]) == str(seccion):
            sec_correcta = True
        if sec_correcta and voto not in votos_validos[seccion-1]:
            votos_validos[seccion-1].append(voto)
            resumen.append(voto[1])
            
for seccion in range(3):
    print(f"Votos s{seccion+1}:")
    for i in votos_validos[seccion]:
        print(",".join(i))
archivo = open("resultados.txt","a")
print(f"Marquinez,{resumen.count('Marquinez')}\nSepulveda,{resumen.count('Sepulveda')}\nLopez,{resumen.count('Lopez')}",file=archivo)
archivo.close()