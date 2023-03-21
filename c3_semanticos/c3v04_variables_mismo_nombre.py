class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_edad(self):
        es_mayor_edad = False
        if self.edad >= 18:
            es_mayor_edad = True
            return es_mayor_edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz Cumpleaños #{self.edad} {self.nombre}")


persona_1 = Persona(nombre="Paco", edad=27)
print(persona_1.nombre)
persona_2 = Persona(nombre="Javier", edad=25)
print(persona_2.nombre)
