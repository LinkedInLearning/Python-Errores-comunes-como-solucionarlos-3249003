import itertools


lista_marcas = ["Mazda", "Chevrolet", "Jeep"]
lista_anios = ["2020", "2021", "2022"]

marcas_anios = []
for marca in lista_marcas:
    for anio in lista_anios:
        marcas_anios.append((marca, anio))

print(marcas_anios)


marcas_anios = list(itertools.product(lista_marcas, lista_anios))
print(marcas_anios)
