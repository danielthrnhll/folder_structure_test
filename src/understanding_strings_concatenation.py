#combinacion o concatenacion de strings

first_name = "daniel"
last_name = "limon"
full_name = first_name + " " + last_name
print(full_name)

print("hola".upper(),"daniel" + " " "limon", first_name.title() + " " + last_name.title())


message = "hola, " + full_name.title() + "!"
print(message)

#whitespaces

"""

se refiere a cualquier string (caracter)
que no se imprime, es decir, un espacio
(" "), tabuladores (\t) y finales de 
linea (\n)

""" 

print("python")
print("\t\tPython")
print("lenguajes: \npython \nC \njava")


#concatenacion de strings utilizando f strings

famous_person = "elpepe"
message = f"{famous_person} una vez dijo que python es amor"
print(message)
quote = "hola"
message_2 = f"{famous_person} una vez dijo {quote}"

# ELIMINACIÓN DE ESPACIOS EN BLANCO


programming_language = " Pyth on "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())

#investigar que hace el metodo join delos strings