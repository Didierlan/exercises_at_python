#seguir la siguiente serire numerica 4, 56, 92, 144,180, 232
#el ultimo numero no debe tener coma
#Empesemos 56-4 = 52, 92-56 = 36, 144-92 = 52, 
#Solucion 54 + 4 = 56 +36 = 92 + 52 = 144 + 36 = (180) + 52 = (232)

numSerie = 4 
cambio = 0
bandera = 0
lis = [] #lista o array 


while numSerie <= 232:
    lis.append(numSerie)

    if(cambio == 0):
        numSerie += 52
        cambio = 1
    else:
        numSerie += 36
        cambio = 0

    bandera += 1

print(lis)
