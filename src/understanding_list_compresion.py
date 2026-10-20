"""
   Una list comprehension
   combina el for loop y la creacion de 
   nuevos elementos en una sola linea
   de codigo y automaticamente agrega
   cada nuevo elemento a la lista, es decir,
   sin utilizar el metodo append().
"""
print("\nList comprehension (Mas facil y Rapido):")
squares = [value**2 for value in range(0, 11)]
print(squares)