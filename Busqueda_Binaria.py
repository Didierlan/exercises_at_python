#Algoritmo burbuja para oordenar el array ya un requerimiento del algoritmo busqueda binaria dice que el arreglo o lista debe estar ordenada.

def busqueda(lista,nBus):


    ba = len(lista)
    i = 0
    while i < ba :
        if type(lista[i]) == int or type(lista[i]) == float:
            i= i+1
        else:
            return print("La lista solo debe tener numeros")
            break;

        
            
    aux = 0

    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
              aux = lista[j]
              lista[j] = lista[j+1]
              lista[j+1] = aux 

    ap1 = 0
    ap2 = len(lista) -1 
    pm = 0
    bandera = False

    while ap1 <= ap2:
        pm = (ap1 + ap2)//2

        if nBus == lista[pm]:
            print("numero encontrado en la pocicion # " , pm)
            bandera = True
            break
        if nBus > lista[pm]:
            ap1 = ap1 +1
        if nBus < lista[pm]:
            ap2 = ap2 -1


    if(bandera == True):
        pass
    else:
        print("no se encontro nada")

    return pm



busqueda([3,8.2,1,9.7,2,6.45,7,0], 6.45)
#busqueda([0, 1, 2, 3, 6, 7, 8, 9], 6)



    

    
