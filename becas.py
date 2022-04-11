
def beca(nCasillas):

    lisName = []
    lisNum = []

    for i in range(nCasillas):
        name = (input(f" {i+1 } nombre: "))
        lisName.append(name)
        calif = int((input(f" {i + 1 } calificacion: ")))
        lisNum.append(calif)


    auxNombre = ""
    auxNumero = 0
    for i in range(len(lisNum)-1):
        for j in range(len(lisNum)-1):

            if lisNum[j] < lisNum[j + 1]: 

                auxNumero = lisNum[j]
                lisNum[j]  = lisNum[j + 1]
                lisNum[j + 1] = auxNumero
                auxNombre = lisName[j]
                lisName[j] = lisName[j + 1]
                lisName[j + 1] = auxNombre


        
        
    for k in range(nCasillas):

        if lisNum[k] >= 8:
            print(f"{k + 1} {lisName[k]} {lisNum[k]} Tiene derecho a veca")
        else:
            print(f"{k + 1} {lisName[k]} {lisNum[k]} NOOOO derecho a veca")



nCasillas = int(input("ingrese las casillas que desea: "))
beca(nCasillas)


