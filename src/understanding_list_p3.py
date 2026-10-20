# Trabajndo en listas
print("\n\t Hoy toca trabajar con listas \n".upper())

# Vamos a crear una lista de puros strings con nombres 
magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])
# print(magicians[0], magicians[1], magicians[2], magicians[3])

#CICLO FOR
print("\n\t Ciclo For \n".upper())

for magician in magicians: 
    print(magician)

# A esto se le llama looping

# Ahora vamos a imprimri un mensaje para cada mago
print("\n")
for magician in magicians: 
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}")
    print("\n")
print("Gracias a todos. Fue un gran espectaculo.")

print("\n\t Identacion - Indentation \n".upper())

# identacion
"""
    python utiliza la identacion para determinar
    cuando una linea de codigo esta conectada a 
    la linea de codigo anterior

    basicamente, se utilizan 4 espacios en blanco para
    obligarnos a escribir codigo ordenado y estructurado
"""
# no olvidemos identar - traceback error
magicians = ["alice", "david", "calorine"]
#for magician in magicians:
#print(magician) #identacion error

# error de logica - logic error - identacionError
for magician in magicians:
    print(magician)
print(f"no puedo a esperar a ver el siguiente truco, {magician}")

# IndentationError: unexpected indent
message = "hello python world"
#    print(message)

# no olvidar los 2 puntos (:) - syntax error
#for magician in magicians
#    print(magician)