# Aqui puedes empezar a programar 😀
country = input() 
stars = float(input() )
year = int(input() )

archivo_bots = open("bots.txt")
id_bots = archivo_bots.readlines()
archivo_bots.close()
for i in range(len(id_bots)):
    id_bots[i] = id_bots[i].strip()
    id_bots[i] = int(id_bots[i])

archivo_reviews = open("reviews.txt")
lines_reviews = archivo_reviews.readlines()
archivo_reviews.close()
for j in range(len(lines_reviews)):
    lines_reviews[j]= lines_reviews[j].strip()
    lines_reviews[j]= lines_reviews[j].split(",")
    lines_reviews[j][0]= int((lines_reviews[j][0]))
    lines_reviews[j][1]= int((lines_reviews[j][1]))
    lines_reviews[j][3]= int((lines_reviews[j][3]))
    lines_reviews[j][4]= float((lines_reviews[j][4]))

archivo_hotels = open("hotels.txt")
lines_hotels = archivo_hotels.readlines()
archivo_hotels.close()
for k in range(len(lines_hotels)):
    lines_hotels[k] = lines_hotels[k].strip()
    lines_hotels[k] = lines_hotels[k].split(",")
    lines_hotels[k][0] = int(lines_hotels[k][0])

reviews_validas = []
hoteles_posibles = []
for i in lines_reviews:
    if i[0] not in id_bots and i[4]>=stars and i[3]>=year:
        reviews_validas.append(i)
        for j in lines_hotels :
            if country in j[2] and j[0] == i[1]:
                hoteles_posibles.append(j[0])
print(f"Numero de reviews: {len(lines_reviews)}\nNumero de reviews validas: {len(reviews_validas)}")

maxim = 0
revi = 0
for i in range(len(hoteles_posibles)):
    contador = hoteles_posibles.count(hoteles_posibles[i])
    if contador>maxim:
        maxim = contador
        mejor_id = hoteles_posibles[i]
        revi= contador
    hoteles_posibles[i] = [hoteles_posibles[i],contador]
for z in lines_hotels:
    if z[0] == mejor_id:
        nombre = z[1]
        direccion = z[2]
print(f"ID: {mejor_id}\nNombre: {nombre}\nDireccion: {direccion}\nReviews validas del hotel: {revi}")