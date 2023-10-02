import requests
# Obtener los datos de la API de países
response = requests.get("https://restcountries.eu/rest/v2/all")
# Comprobar el código de estado
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()
    # Recorrer la lista de países
    for country in data:
        # Imprimir el nombre del país y sus provincias
        print(country["name"], country["subregion"])
else:
    # Mostrar un mensaje de error
    print("Error al obtener los datos:", response.status_code)
