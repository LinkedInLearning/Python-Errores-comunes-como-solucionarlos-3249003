import requests


def procesar_repuesta(endpoint, num_vehiculo):

    try:
        request = requests.get(endpoint)
        status_code = request.status_code
        print(f"La API respondió con el código {status_code}")

        response = request.json()
        print(f"Cantidad de vehículos: {len(response)}")

        print(f"Características del vehículo seleccionado {response[num_vehiculo]}")

    except Exception as e:
        print("Se levantó una excepción")
        print(e)


endpoint_ok = "https://run.mocky.io/v3/6d585571-664c-46e1-8289-769ad70c119a"
endpoint_not_found = "https://run.mocky.io/v3/a94518cb-ba70-4abc-8793-e4d7ee50a914"
procesar_repuesta(endpoint=endpoint_not_found, num_vehiculo=3)
