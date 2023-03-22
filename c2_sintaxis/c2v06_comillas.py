import random


def escribir_mensaje():
    "Retorna un mensaje de cumpleaños con el nombre y la edad de la persona"

    frases = [
        "Yo solo se que ya tu sabes",
        "La vida es eso que pasa cuando pasa la vida",
        "Ante la duda, comer hamburguesa"
    ]

    frase_aleatoria = random.choice(frases)
    mensaje = f"Paco dijo \"{frase_aleatoria}\""
    return mensaje


print(escribir_mensaje())
