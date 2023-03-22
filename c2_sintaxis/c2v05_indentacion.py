class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz Cumpleaños")

    def es_mayor_edad(self):
        es_mayor_edad = False
        if self.edad >= 18:
            es_mayor_edad = True
        return es_mayor_edad


paco = Persona(nombre="Paco", edad=27)
paco_es_mayor = paco.es_mayor_edad()
print(paco_es_mayor)
