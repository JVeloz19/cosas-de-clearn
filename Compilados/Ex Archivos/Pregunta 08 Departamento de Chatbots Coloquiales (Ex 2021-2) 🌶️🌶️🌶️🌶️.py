# Escribe tu código aquí!       
n = int(input())
estadisticas = []
for i in range(n):
    arch = open(f"chatbot_{i}.txt")
    chat = arch.readlines()
    arch.close()
    errores = []
    contador = 0
    totales = 0
    for k in chat:
        if k == "CHATBOT: Eso no esta dentro de mis protocolos.\n":
            contador += 1
        if k[:8] == "CHATBOT:":
            totales += 1
        if k == "----FIN DE LA CONVERSACION----\n" or k == "----FIN DE LA CONVERSACION----":
            errores.append([contador,totales])
            contador = 0
            totales = 0 
    estadisticas.append(errores)

arch  = open("resultados.txt","w")
for n in range(len(estadisticas)):
    print(f"CHATBOT {n}",file=arch)
    errores = 0
    totales = 0
    
    for m in range(len(estadisticas[n])):
        print(f"Conversacion {m+1} -> {estadisticas[n][m][0]}/{estadisticas[n][m][1]}",file=arch)    
        errores += estadisticas[n][m][0]
    print(f"Errores por conversacion: {round(errores/len(estadisticas[n]),2)}",file=arch)
arch.close()