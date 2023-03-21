def verificar_estudiante(nombre, lista_estudiantes):

    if type(nombre) != str:
        raise Exception("El nombre debe ser un texto")

    if nombre not in lista_estudiantes:
        raise Exception("El estudiante no está en la lista")

    return True


lista_estudiantes = ["Paco", "Javier", "Emilio"]
verificar_estudiante(1, lista_estudiantes)
verificar_estudiante("Ana", lista_estudiantes)
verificar_estudiante("Paco", lista_estudiantes)
