# listas de numeros
"""
las listas tambien pueden almacenar numeros. python
pfrece varias herramientas que ayudan a trabajar 
eficientemente con listas de numeros
"""

# Python ofrece varias herraminetas que ayudan a 
# trabajaar eficientemente con listas de numeros.

# Metdodo build-in range() - Construye una lista de numeros
"""
     El metodo range() nos ayuda a crear facilmente
     series de numeros.
"""
print("\nImprimir numeros del 1 al 5 (FOR):")
for value in range(1, 6):
    print(value)

print("\nImprimir numeros del 1 al 5 (LIST):")

# Crear una lista de numeros utilizando range
numbers = list(range(0,10))
print(numbers)

print("\nImprimir numeros Pares del 0 - 10 (LIST):")

# Lista de numeros pares
even_numbers = list(range(0,11,2))
print(even_numbers)

print("\nImprimir numeros Impares del 1 - 10 (LIST):")

# Lista de numeros impares
odd_numbers = list(range(1,10,2))
print(odd_numbers)