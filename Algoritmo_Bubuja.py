#Dada una lista de numero desordenados entregarla ordenada utilizar una fincion


def ordenar(listaa): 
    auxiliar = 0

    for i in range(len(listaa) -1):
        for j in range(len(listaa)-1):

            if listaa[j] > listaa[j + 1]: 
                auxiliar = listaa[j + 1]
                listaa[j + 1] = listaa[j]
                listaa[j] = auxiliar

    return listaa

        


 
print(ordenar([40,7,3,56,0,1,9,10,34,5]))









