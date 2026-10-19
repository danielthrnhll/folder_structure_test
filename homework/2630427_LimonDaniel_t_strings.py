"""
Daniel Martin Limon Garcia
2630427
IM 1-2
"""

"""
Resumen Ejecutivo:

Los strings son un tipo de datos compuestos por secuencias de caracteres que representan texto. 
Se delimitan mediante el uso de comillas simples o dobles. LOs strins son inmutables pero estos se
pueden volver a definir.
Los strings tienen varias operaciones basicas, como lo son la concatenacion sencillas que usan el + 
o las f strings con la cual puedes introducir variables adentro de las comillas. para obtener longitud
se usa el len(). extraer una sola parte del string(una subcadena), esto con corchetes y indices indicando
el comienzo y el final. para remplazar texto se usa el metodo replace y se pone en commillas lo que se va
a remplazar y luego por lo que se va a remplazar
la validacion y normalizacion del texto es fundamental para garantizar la seguridad del sistema, evitar 
errores inesperados y asegurar la consistencia de los datos

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
"""
se definira una variable con un string adentro,
la cual luego con el metodo split se convertira en una lista 
y se imprimiran solo las iniciales en mayuscula seguidas de
un punto
"""

#inputs:
full_name = "   daniel limon garcia  ".strip().lower()

#Outputs:
"""
Daniel Limon Garcia
D.L.M
"""

# validations
"""
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.
"""

#test cases
print("test cases problem 1 \n".title())

#normal
full_name = "   daniel limon garcia  ".strip().lower()
names = full_name.split()
print(full_name.title())
print(f"{names[0][0].upper()}.{names[1][0].upper()}.{names[2][0].upper()}.")

#border

full_name = "   daniel limon garcia  ".strip().lower()
names = full_name.split()
print(full_name.title())
print(f"{names[0][0].upper()}.{names[1][0].upper()}.{names[2][0].upper()}.")

# error
"""
full_name = "   daniel limon  ".strip().lower()
names = full_name.split()
print(full_name.title())
print(f"{names[0][0].upper()}.{names[1][0].upper()}.{names[2][0].upper()}.")

tiene menos elementos de los necesarios por lo cual marcara:
IndexError: list index out of range
"""

# problem 2
# description:
"""
se define una variable la cual
debemos verificar si es una direccion 
de correo valida, esto viendo si tiene 
un @ y un . despues de este
"""

#inputs

email_text = "2630427@upv.edu.mx".strip().lower()

#outputs
"""
True o False
Si es válido: "Domain: <domain_part>"
"""

# validations:
# Valid email: True or False
# Si es válido: "Domain: email.com"

#test cases
print("\n test cases problem 2 \n".title())

#normal
where_is_the_at = email_text.find("@")
at_symbols = email_text.count("@")
valid_email = "@" in email_text and "." in email_text[where_is_the_at:]
print(f"valid email: {valid_email}")
print(f"la cantidad de @ es {at_symbols}")
if valid_email == True:
    print(f"domain: {email_text[where_is_the_at + 1:]} \n")

# Border
email_text = "2630427upv.edu.mx".strip().lower()
where_is_the_at = email_text.find("@")
at_symbols = email_text.count("@")
valid_email = "@" in email_text and "." in email_text[where_is_the_at:]
print(f"valid email: {valid_email}")
print(f"la cantidad de @ es {at_symbols}")
if valid_email == True:
    print(f"domain: {email_text[where_is_the_at + 1:]}")

# Error
"""

email_text = 2630427
where_is_the_at = email_text.find("@")
at_symbols = email_text.count("@")
valid_email = "@" in email_text and "." in email_text[where_is_the_at:]
print(f"valid email: {valid_email}")
print(f"la cantidad de @ es {at_symbols}")
if valid_email == True:
    print(f"domain: {email_text[where_is_the_at + 1:]}")

la variable es un int por lo tanto marca
AttributeError: 'int' object has no attribute 'find' 
ya que te marca el primer error 

"""

# Problem 3
# description:
"""
dada una frase, se tiene que averiguar si esta
es un palidromo, esto revomiendo los espacios y
invirtiendo el orden y compararla con la frase original
"""

#inputs
# phrase = string

# Outputs
#Is palindrome: true" o "Is palindrome: false"

#validations:
# phrase no vacía tras strip().
# Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres)

#test cases
print("\n test cases problem 3 \n".title())

#normal
phrase = "roma ni se conoce sin oro ni se conoce sin amor".strip().lower()
normalized_phrase = phrase.replace(" ","")
sliced_phrase = normalized_phrase[::-1]
if normalized_phrase == "":
    print("error")
elif normalized_phrase == sliced_phrase:
    is_palindrome = True
else:
     is_palindrome = False
print(f"Is palindrome: {is_palindrome}")
print(f"{phrase} \n")

# border

phrase = "el profe charly es el mejor profe".strip().lower()
normalized_phrase = phrase.replace(" ","")
sliced_phrase = normalized_phrase[::-1]
if normalized_phrase == "":
    print("error")
elif normalized_phrase == sliced_phrase:
    is_palindrome = True
else:
     is_palindrome = False
print(f"Is palindrome: {is_palindrome}")
print(f"{phrase} \n")

# error

phrase = " ".strip().lower()
normalized_phrase = phrase.replace(" ","")
sliced_phrase = normalized_phrase[::-1]
if normalized_phrase == "":
    print("error")
elif normalized_phrase == sliced_phrase:
    is_palindrome = True
else:
     is_palindrome = False
print(f"Is palindrome: {is_palindrome}")
print(f"{phrase} \n")
"""
nuestra frase no tiene ningun elemento
adentro por lo tanto no podria ser un palindromo
"""

#problem 4
# description:
"""
dada una oracion, se tiene que contar las palabras
que tiene, cual es la primera y la ultima y cual 
es la mas larga y la mas corta
"""


# inputs
# sentence = oracion 

# Salidas:
"""
Word count: n
First word: word
Last word: word
Shortest word: wor
Longest worrrrrrrrd
"""

# Validaciones:
# Oración no vacía tras strip().
# Debe contener al menos una palabra válida después de split().


#test cases
print("\n test cases problem 4 \n".title())

# normal
sentence = "ayer tuve cita con el otorrinolaringologo y me fue muy bien".strip().lower()
words = sentence.split()
shortest_word = min(words, key=len)
largest_word = max(words, key=len)
print(f"word count: {len(words)}")
print(f"first word: {words[0]}")
print(f"last word: {words[-1]}")
print(f"shortest word: {shortest_word}")
print(f"largest word: {largest_word} \n")

# border
sentence = "hola dos tres sam".strip().lower()
words = sentence.split()
shortest_word = min(words, key=len)
largest_word = max(words, key=len)
print(f"word count: {len(words)}")
print(f"first word: {words[0]}")
print(f"last word: {words[-1]}")
print(f"shortest word: {shortest_word}")
print(f"largest word: {largest_word} \n")

#al haber varias palabras de misma logngitud, se toma la primera

# error
"""
sentence = " ".strip().lower()
words = sentence.split()
shortest_word = min(words, key=len)
largest_word = max(words, key=len)
print(f"word count: {len(words)}")
print(f"first word: {words[0]}")
print(f"last word: {words[-1]}")
print(f"shortest word: {shortest_word}")
print(f"largest word: {largest_word} \n")

sentence queda vacia tras el strip() por lo tanto da:
ValueError: min() iterable argument is empty 
"""

# problem 5
# description:
"""
determinar si una contraseña es segura o no
esto en base a ciertos criterios que nosotros 
podemos definir
"""


# inputs:
# password = string

# outpust
# Password strength: weak, medium or strong

# Validations:
# No aceptar contraseña vacía.
# Verificar longitud con len().

#test cases
print("\n test cases problem 5 \n".title())

# si la contraseña tiene 12 o mas caracteres, al menos un numero, al menos 1 letra tanto
# mayuscula como minuscula y un caracter no alfanumerico, la cotraseña es: strong

# si la contraseña tiene 8 o mas caracteres, tiene minusculas y/o numeros y tiene una 
# mayuscula y/o un caracter alfanumerico, la cotraseña es: Medium 

# si la contraseña tiene 8 o mas caracteres pero solo tiene letras minusculas y/o numeros
# la contraseña es: fair

# si la contraseña tiene menos de 8 caracteres es: weak

#normal
password = "Muerto_en_vida_67".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

# border
print(" casos border \n")

print("caso border 1: 7 caracteres")
password = "67_A_67".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")
    
print("caso border 2: 8 caracteres, solo numeros ")
password = "99999999".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

print("caso border 3: 8 caracteres, solo letras minusculas ")
password = "aaaaaaaa".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

print("caso border 4: 8 caracteres, letras minusculas y numeros")
password = "aaaa6767".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

print("caso border 5: 8 caracteres, letras minusculas y mayusculas")
password = "aaaaAAAA".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

print("caso border 6: 8 caracteres, numeros y caracteres especiales ")
password = "67__67__".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

print("caso border 7: 8 caracteres, letra minuscula y mayuscula, numeros y caracteres especiales ")
password = "MIma69__".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

print("caso border 8: 12 caracteres, letra minuscula y mayuscula, numeros y caracteres especiales ")
password = "Marialabuena_9".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")


# error
print(" caso de erro (contraseña vacia) \n")
password = "".strip()
password_lenght = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_number = any(c.isdigit() for c in password)
has_special_caracter = any(not c.isalnum() for c in password)
if password == "":
    print("error")
elif password_lenght >= 12 and has_lower == True and has_upper == True and has_number == True and has_special_caracter == True:
    print("Password strength: strong \n")
elif password_lenght >= 8 and (has_upper == True or has_special_caracter == True) and (has_lower == True or has_number == True):
    print("Password strength: medium \n")
elif password_lenght >= 8 and (has_lower == True or has_number == True):
    print("Password strength: fair \n")
else:
    print("Password strength: weak \n")

#problem 6
# description:

#inputs
# product_name = string
# price_value = int o float o str, en caso de int o float luego se pasa a str

# outpust
# Label: <exactly 30 characters>

# validations
# product_name no vacío tras strip().
# price_value debe poder convertirse a un número positivo

# test cases 
print("\n test cases problem 6 \n".title())

# normal
product_name = "pera".strip()
product_lenght = len(product_name)
price_value = "33".strip()
price_lenght = len(price_value)
lenght_price_n_product = product_lenght + price_lenght
if lenght_price_n_product >= 13:
    rest = product_lenght - price_lenght
    product_name = product_name[0:rest]
    concatenation_price_and_product = f"Product: {product_name} Price: ${price_value}"
    label = concatenation_price_and_product[:32].ljust(30, " ")
    print(f'Label: "{label}"')
else: 
    concatenation_price_and_product = f"Product: {product_name} Price: ${price_value}"
    label = concatenation_price_and_product[:32].ljust(30, " ")
    print(f'Label: "{label}"')

# border
print("\n la suma de product_lenght y price_lenght da 13")
product_name = "television".strip()
product_lenght = len(product_name)
price_value = "999".strip()
price_lenght = len(price_value)
lenght_price_n_product = product_lenght + price_lenght
if lenght_price_n_product > 13:
    rest = product_lenght - price_lenght
    product_name = product_name[0:rest]
    concatenation_price_and_product = f"Product: {product_name} Price: ${price_value}"
    label = concatenation_price_and_product[:32].ljust(30, " ")
    print(f'Label: "{label}"')
else: 
    concatenation_price_and_product = f"Product: {product_name} Price: ${price_value}"
    label = concatenation_price_and_product[:32].ljust(30, " ")
    print(f'Label: "{label}"')

# error
"""
print("\n la suma de product_lenght y price_lenght da 13")
product_name = 67
product_lenght = len(product_name)
price_value = "-17".strip()
price_lenght = len(price_value)
lenght_price_n_product = product_lenght + price_lenght
if lenght_price_n_product > 13:
    rest = product_lenght - price_lenght
    product_name = product_name[0:rest]
    concatenation_price_and_product = f"Product: {product_name} Price: ${price_value}"
    label = concatenation_price_and_product[:32].ljust(30, " ")
    print(f'Label: "{label}"')
else: 
    concatenation_price_and_product = f"Product: {product_name} Price: ${price_value}"
    label = concatenation_price_and_product[:32].ljust(30, " ")
    print(f'Label: "{label}"')

el product_name no puede ser un int y por eso da:
TypeError: object of type 'int' has no len()
"""

# conclusiones
"""
el manejo de strings es de gran importancia ya que esto
nos podria ayudar a la hora de querer manejar grandes cantidades de datos
cosasa conmo el lower() y el strip() son de gran ayuda a la hora de querer 
normalizar las bariables de tipo str y el split es util cuanfdo queremos trabajar
los elementos de un str por separado
la normalizacion es muy importante para que todos nuestros datos sean constantes
los strings son inmutables, a la hora de modificar un lo que se hace en realidazd es
crear uno nuevo y esto es muy importante de saber ya que puede ser de gran utilidad
"""

"""
referencias:
- https://www.programaenpython.com/fundamentos/strings-en-python/
- https://www.datacamp.com/es/tutorial/python-len
- https://medium.com/@mystiquelord123/the-lower-upper-islower-and-isupper-methods-in-python-f6877886b890
- https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/
- https://www.luisllamas.es/python-slices/
"""