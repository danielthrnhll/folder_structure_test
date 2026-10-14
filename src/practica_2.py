"""
    
    Ejercicio

    realizar un programa que determine el costo de un boleto
    a partir de las siguientes condiciones

    -costo para una persona menor o iguala 4 años: gratis
    - costo para una persona cuya edad es mayor a 4
    años pero menor o igual a 18: 200
    -costo para una persona cuya edad es mayor a 18: 500

"""
print("esto se realiza con el if normal")
age = input("ingresa tu edad: ")
age = int(age)

if age <= 4:
    cost = 0
if age > 4 and age <= 18:
    cost = 200
if age > 18:
    cost = 500
print(f"el costo de tu boleto es de {cost}")

# if elif else
print("esto se realiza con el if elif else")
if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
else:
    cost = 0
# cuando el if elif cubre TODOS los casos el else esta de mas
print(f"el costo de tu boleto es de {cost}")