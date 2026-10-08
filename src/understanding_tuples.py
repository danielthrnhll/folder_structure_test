"""
    tuplas

    las tuplas son listas de elementos que no cambian de tamaño,
    es decir. las tuplas son listas inmutables

    se utilizan () para definir una tupla

    elemplo:
        si tenemos un rectamgulo (largo, ancho) que siempre va 
        a tener cierto tamaño, podemos asegurar que sus dimensiones
        no va a cambiar si colocamos sus valores en una tupla. 

"""

dimensions = (200,50) # 200 de largo x 50 de ancho
print("tupla original:", dimensions)

# vamos a imprimir elementos de una tupla
# ( se realiza de la misma forma que una lista)
print(dimensions[0])

# vamos a modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
print(names)
names[0] = "mercury"
print(names)

# dimensions[0] = 500    esta operacion no esta permitida

# looping through a tuple
for dimension in dimensions:
    print(dimension)

"""
    no podemos modificar una tupla, 
    lo que si podemos hacer es cambiar
    la asignacion de una variable que
    almacena en una tupla

"""
dimensions = (500,1000)
print("tupla re-definida:", dimensions)


# dimensions_2 = [200,50]
# print(dir(dimensions_2))