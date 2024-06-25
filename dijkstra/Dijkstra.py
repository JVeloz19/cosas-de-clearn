def dijkstra(Grafo, salida):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    return result, dist, prev


grafo = {
    "1": {"3": 2, "2": 14,"4": 5},
    "2": {"6":3 , "5":18, "1":14 },
    "3": {"7":6 , "8":9, "1":2},
    "4": {"9":2, "10":8 , "1":5},
    "5": {"10":2, "11":5, "2":18},
    "6": {"12":8 , "7":5, "2":3},
    "7": {"13":12, "3":6, "6":5},
    "8": {"14":4 ,"9":12,"3":9},
    "9": {"15":9 , "4":2, "8":12},
    "10": {"16":11 , "5":2 , "4":8},
    "11": {"17":2 , "12":13 , "5":5},
    "12": {"18":7 , "6": 8 , "11":13},
    "13": {"18":11 , "14":9 , "7":12},
    "14": {"19":15 , "8":4 , "13":9},
    "15": {"19":21 , "16":3 , "9":9 },
    "16": {"17":10 , "10":11 , "15":3},
    "17": {"20":8 , "16":10 , "11":2},
    "18": {"20":4 , "12":7 , "13":11},
    "19": {"20":15, "12":21 , "14":15},
    "20": {"17":8 , "18":4, "19":15}
}

s, distancia, previos = dijkstra(grafo, "7")
print("Distancias")
for i in str(distancia)[1:-1].split(","):
    print(f"\t{i}")
print("Previos")
for i in str(previos)[1:-1].split(","):
    print(f"\t{i}")