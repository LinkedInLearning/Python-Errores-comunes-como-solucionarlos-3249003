# Iteración y modificación de una lista
lista_numeros = [2, 5, 8, 12, 14, 35]

for numero in lista_numeros:
    print(numero)
    if numero % 2 == 0:
        lista_numeros.remove(numero)

print(lista_numeros)


# Iteración correcta de una lista
lista_numeros = [2, 5, 8, 12, 14, 35]

impares = []
for numero in lista_numeros:
    if numero % 2 != 0:
        impares.append(numero)

print(lista_numeros)
