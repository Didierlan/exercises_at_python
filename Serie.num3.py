#seguir la siguiente serire numerica 99, 90, 83,78,?,?
#el ultimo numero no debe tener coma
#Empesemos 99-9 = 9, 90-83 = 7, 83-78 = 5, 78-3 = 75, 75-1 = 74  
#Solucion solucion 9-2 =,7-2 =,5-2 =,3-2=,1
#debemos restar -2 en cada posicion 

numSerie = 99

resta = 9
lista = []

while resta >= -1: 
    lista.append(numSerie)
    numSerie -= resta
    # + por - = -
    resta += -2


print(lista)

