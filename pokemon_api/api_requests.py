# vamois a realizar nuestra primera peticion a una api

import requests

# la api
api_url = "https://pokeapi.co/api/v2/pokemon/25"

# esta es la primer peticion que estamos haciendo
response = requests.get(api_url, timeout = 10)

# para revisar si hubo errores en la peticion
response.raise_for_status() 

# vamos a imprimir el codigo de estado
print(response.status_code)
pokemon = response.json()

#vamos a imprimir el tipo de variable de pokemon
print(type(pokemon))

#vamos a imprimir el pokemon
# print(pokemon)

# vamos a imprimir el id
print(pokemon["id"])
print(pokemon["name"])
print(pokemon["height"]/10)
print(pokemon["weight"]/10)

for element in pokemon["types"]:
    print(element["type"]["name"])