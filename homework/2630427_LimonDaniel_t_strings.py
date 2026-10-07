"""
Daniel Martin Limon Garcia
2630427
IM 1-2
"""

"""
Resumen Ejecutivo:

"""

# los strings son inmutables: cualquier cambio genera una nueva cadena
# es buena practica normalizar entrada con strip() y lower() antes de compararla
# evitar "numeros magicos" en indices; documentar que extrae cada slice
# usar metodos de string en lugar de reescribir logica basica
# diseñar validaciones clara: primero que no este vacio, luego el formato
# escribir codigo legible: nombres de variables claros y mensajes de error entendibles


#PROBLEMS 

#problem 1: full name format (name + initials)
# description:

#inputs:
full_name = "   daniel limon garcia  ".strip().lower()
names = full_name.split()
print(full_name.title())
print(f"{names[0][0].upper()}.{names[1][0].upper()}.{names[2][0].upper()}.")

#Outputs:
"""
Daniel Limon Garcia
D.L.M
"""
