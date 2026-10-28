# dictionaries

"""

    los diccionarios se componen de elementos
    con una llave y un valor. estos se definen
    con las llaves {}
    
"""

# diccionario simple
alien_0 = {"color": "green", "points": 5}

# diccionario vacio
alien_1 = {}

# diccionario mas simple
alien_2 = {"color": "verde"}

# accesar a los elementos de un diccionario

print(f"tu alien es de color: {alien_0["color"]}")
print(f"si matas al alien_0, se te otorgan: {alien_0["points"]}")

# agregar elementos a un diccionario
print("\n agregar elementos a un dict")
alien_0["x_position"] = 25
alien_0["y_position"] = 0
print(alien_0)

# modificar un valor en un diccionario
print("\n modificando elementos a un dict")
alien_0["y_position"] = 80
print(alien_0)

# eliminando un elemento de un diccionario
print("\n eliminando elementos a un dict")
del alien_0["points"]
print(alien_0)

# diccionarios para objetos (elementos) similares
favorite_languages = {
    "jen": "python", 
    "sarah": "c", 
    "eduard": "ruby", 
    "phill": "python"}

# looping  thought all key-values pairs

user_0 = {
    "username": "daniell_th", 
    "firstname": "daniel",
    "lastname": "limon",
    "age": 19,
    "birthday": "17-sep"}

# looping a traves de llaves y valores

print("looping a traves de llaves y valores \n")
for key, value in user_0.items():
    print("key:", key)
    print("value:", value, "\n")

# looping a traves de llaves

print("looping a traves de llaves \n")
for key in user_0.keys():
    print("key:", key, "\n")

# looping a traves de llaves y valores

print("looping a traves de valores \n")
for value in user_0.values():
    print("value:", value, "\n")