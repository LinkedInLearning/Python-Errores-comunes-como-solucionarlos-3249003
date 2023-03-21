def calcular_total(dinero, interes, anios):
    x = dinero * ((1 + intres/100) ** anios)
    return round(x, 2)


dinero = 1000
interes = 4.5
anios = 3

resultado = calcular_total(dinero, interes, anios)
print(resultado)
