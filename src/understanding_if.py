print("\nTRABAJO CON IF STATEMENT")
# IF STATEMENT
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)

# EL CONDICIONAL O CONDITION
# EL CONDICIONAL ES EL CORAZON DEL IF

print("\nTRABAJO CON LA CONDICIONAL VERDADERA")
# CONDICIONAL VERDADERO
# CONDICIONAL = True

truck = "ford"
print(truck == "ford")  # True

print("\nTRABAJO CON LA CONDICIONAL FALSO")
# CONDICIONAL FALSO
# CONDICIONAL = False

print(truck == "audi")  # False

print(truck == "Ford".lower())  # Verdadero

print("\nTRABAJO CON LA CONDICIONAL DE DESIGUALDAD")
# CONDICIONAL DE DESIGUALDAD !

print(truck != "audi")  # True
print(truck != "ford")  # False

print("\nTRABAJO CON LA COMPARACIONES NUMERICAS")
# COMPARACIONES NUMERICAS
age = 34
print(age == 34)  # True

answer = 17
if answer != 42:
    print("Respuesta Incorrecta")

print("\nTRABAJO CON MENOR QUE")
# CONECTOR MENOR QUE <
age = 19
print(age < 21)  # True
print(age <= 21)  # True
print(age > 21)  # False
print(age >= 21)  # False

print("\n Multiple Conditions")

# multiple conditions
age_0 = 22
age_1 = 18
print("operacion AND")
print(age_0>=21 and age_1>=21) #False
print(age_0>=21 and age_1>=18) 

print("operacion or")
print(age_0>=21 or age_1>=21)
print(age_0>=23 or age_1>=21)

# como saber si un elemnto esta en una lista
food = ["chilaquiles", "flautas", "gorditas", "tamales"]
print("nopales esta en la lista?")
print("nopales" in food)
print("gorditas esta en la lista?")
print("gorditas" in food)

# Como saber si un elemto NO esta en la lista?
banned_user = ["andrew", "carolina", "david"]
user = "marie"
print(user not in banned_user) #True
