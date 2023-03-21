import csv

with open("archivos/datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    columnas = next(reader)
    for fila in reader:
        print(fila[0])
