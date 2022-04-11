#dado un numero imprimir sus antesesores


num = 100
lista = []
cantidad = range(num)
neW = min(cantidad)



while num > neW:

    num += -1
    lista.append(num)


print(lista)