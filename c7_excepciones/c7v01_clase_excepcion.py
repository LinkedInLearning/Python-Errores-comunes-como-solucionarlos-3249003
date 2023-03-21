import requests


class UnableToDecodeResponse(Exception):
    """No se pudo decodificar el contenido de la respuesta"""
    pass


def procesar_repuesta(endpoint):

    try:
        request = requests.get(endpoint)
        status_code = request.status_code
        print(f"La API respondió con el código {status_code}")

        response = request.json()
        print(response)

    except requests.JSONDecodeError:
        raise UnableToDecodeResponse


endpoint_ok = "https://run.mocky.io/v3/6d585571-664c-46e1-8289-769ad70c119a"
endpoint_not_found = "https://run.mocky.io/v3/a94518cb-ba70-4abc-8793-e4d7ee50a914"
procesar_repuesta(endpoint=endpoint_not_found)
