def calcular_factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_factorial_recursivo(numero-1)


print(calcular_factorial_recursivo(5))
