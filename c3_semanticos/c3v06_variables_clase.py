class Vehiculo:

    cantidad_llantas = 4


class Carro(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


print(Vehiculo.cantidad_llantas, Carro.cantidad_llantas, Camion.cantidad_llantas)

Camion.cantidad_llantas = 6
print(Vehiculo.cantidad_llantas, Carro.cantidad_llantas, Camion.cantidad_llantas)

Vehiculo.cantidad_llantas = 8
print(Vehiculo.cantidad_llantas, Carro.cantidad_llantas, Camion.cantidad_llantas)
