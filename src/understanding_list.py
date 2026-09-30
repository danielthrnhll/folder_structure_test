"""
las listas nos permiten almacenar informacion en un lugar
la cantidad que se desee: ya sean pocos elementos o
millones de elementos

una lista es una coleccion de items (elementos) que tiene
un orden particular. se pueden crear listas que incluyan 
strings, enteros, floats, los nombres de las personas de tu
familia, etc, podemos almacenar (los tipos de datos permitidos
en python) lo que queramos en una lista

son elementos mutables, puede modificarse el tamaño de la lista

se recomienda nombrar una variable del tipo lista en plural

en python, los corchetes [] indican una lista, sus elementos
se separan por comas.

ejemplo: 

"""
bicycles = ["trek","cannondale","redline","specialized", "giant"]

print(bicycles)

# como podemos acceder a los elementos de una lista?

"""

las listas son colecciones ordenaras, se puede acceder
a un elemento de una lista diciendole a python la posicion
o indice del elemento deseado

para obtener el valor deseado, se debe escribir
el nombre de la lista, seguido del indice del elemento
entre corchetes

"""

print(bicycles[2])
print(bicycles[2], bicycles[1], bicycles[3])
print(bicycles[1].upper())

#los indices comienzan en 0, no en 1
# ejemplo

print(bicycles[0]) #trek
print(bicycles[2]) #redline

#accediendo al ultimo elemento de una lista

print(bicycles[-1])
print(bicycles[-2])

#utilizando valores individuales de una lista

message = f"my first bicycle was a {bicycles[-1].title()}"
print(message)

"""

metodo append.()
agregar elementos a la lista
"""