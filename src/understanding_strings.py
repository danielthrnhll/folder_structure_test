"""
Un string es de manera sencilla una serie de caracteres.

En python todo lo que se encuentre dentro dee comillas simples o dobles comillas es considerado un String.

    "Esto es un String."
    'Esto tambien es un String.'

Ejepmplo:

    'Le dije a un amigo, "Python es mi lenguaje de programacion favorito".'
    "El lenguaje 'Phyton' lleva el nombre por Monty Phython, no por la serpiente 'Python'."

Incorrecto:

    " '
    ' "

"""

name = "Clase de ProGramacion."
print(name)

print(name.title())
print(name)
name = name.title()
print(name)

"""
    Un mnetodo es una accion que Python puede realizar en un fragmento de datos o sobre una variable
    El punto . despues de una variable, seguido del metodo title() dice que tiene que ejecutar title()
    de la variable name.

    Todos los metodos van seguidos de parentesis porque en ocasiones necesitan informacion adicional para funcionar,
    lo cual iria dentro de los parentesis. En esta ocasion title() no necesita informacion adicional, para funcionar.
"""

# OTROS METODOS
print(name.upper())
print(name.lower())