from datetime import date


def obtener_fecha_hoy():
	return date.today()


fecha_hoy = obtener_fecha_hoy()
print(fecha_hoy)
