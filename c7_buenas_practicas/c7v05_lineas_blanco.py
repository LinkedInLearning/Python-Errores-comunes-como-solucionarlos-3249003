import os
import sys
from datetime import datetime
def funcion():
    pass
class ClasePersona:
    def __init__(self, name):
        self.name = name
    def caminar(self):
        print("Caminando")

def funcion_2(valor, lista):
    print("Primer bloque de lógica")
    if valor:
        print(valor)
    print("Segundo bloque de lógica")
    for elemento in lista:
        print(elemento)