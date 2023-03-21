lista_divisores = [1, 2, 4, 0, 3, 5]

for numero in lista_divisores:
    if numero != 0:
        resultado = 5 / numero
        print(resultado)
    else:
        print("El divisor es cero, no se hará la operación")
