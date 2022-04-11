#seguir la siguiente serire numerica 1,9,25,49,?,?,
#empesemos 
#49 -25 = 24 , 25-9 = 16 , 9-1 = 8 
#la secuencia es que por cada numero se le debe sumar 8
#8+1 =9, 8+8 = 16 + 9 = 25, 16+8 = 24 + 25 = 49, 24 + 8 = 32+ 49 = 81 .......


numSerie = 1
valor_incrementable = 8
contador = 0
list = []
while contador < 7:
    list.append(numSerie) # con una lista pa que se vea mejor
    #print(f"{numSerie} , ")
    numSerie += valor_incrementable
    valor_incrementable += 8
    contador += 1

print(list)
print("Poseso terminado")