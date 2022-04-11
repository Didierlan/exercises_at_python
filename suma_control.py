#Realizar la suma de dos numero y mostrar el resulatado,"condicion" 
# el usuario decide cuando dejar de sumar

num1 = 0
num2 = 0
resultado = 0
continuar = 0

while continuar == 0:
    num1 = int(input("Ingrese el primer numero "))
    num2 = int(input("Ingrese el segundo numero "))

    resultado = num1 + num2
    print(resultado)
    continuar = num1 = int(input("Desea continuar\n 1.Salir\n 0.continuar"))

print("fin del bucle")