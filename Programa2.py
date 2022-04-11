#Calculadora final 

opcion = 1

while opcion != 0:
    print("Que operacion desea realizar")
    operacion = int(input(" 1 Suma: \n 2 Resta: \n 3 Multiplicacion: \n 4 Divicion: "))
    if operacion > 0 and operacion <5:
        num1 = int(input("escribe el '1' numero "))
        num2 = int(input("escribe el '2' numero "))


        if(operacion == 1):
            resul = num1 + num2
            print(f"la suma de {num1} y {num2} es igual a {resul}")


        elif(operacion == 2):
            resul = num1 - num2
            print(f"la resta de {num1} y {num2} es igual a {resul}")


        elif(operacion == 3):
            resul = num1 * num2
            print(f"la multiplicacion de {num1} y {num2} es igual a {resul}")


        elif(operacion == 4):
            resul = num1 / num2
            print(f"la divicion de {num1} y {num2} es igual a {resul}")


    else:
        print("No se encuentra esa opcion")


    opcion = int(input("Desea continuar '1. yes'  '0.no': "))

print("Fin del programa")

        