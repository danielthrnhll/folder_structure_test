"""
Crear una lista con los primeros
10 numeros cuadraticos.
"""

print("\nImprimir los primeros 10 numeros cuadraticos (LIST - FOR):")
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)