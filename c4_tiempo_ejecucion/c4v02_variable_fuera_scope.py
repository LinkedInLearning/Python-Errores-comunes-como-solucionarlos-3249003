def desactivar_sensor(sensor):
    print(sensor)
    if sensor:
        sensor = False
    return sensor

sensor = True
print(desactivar_sensor(sensor))
