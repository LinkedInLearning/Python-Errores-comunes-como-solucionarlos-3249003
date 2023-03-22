lista_numeros = [2, 5, 8, 12, 14, 35]

impares = []
for numero in lista_numeros:
    if numero % 2 != 0:
        impares.append(numero)

print(impares)
