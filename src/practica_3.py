"""
    vamos a realizar un programa que pregunte
    el nombre de una persona y su edad
"""
name = input("como te llamas?:")
age_txt = input("cuantos años tienes?:")

try:
    age = int(age_txt)
    print(f"hola {name}, tienes {age_txt} años.")
    print(f"en corea tendrias {age+1} años")
except:
    print("la edad que introduciste no es un numero entero")

print("procesos posteriores")


if age_txt == "67":
    print(676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767)
else:
    print("pendejo")


