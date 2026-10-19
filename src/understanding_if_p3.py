guisos = ["salsa verde", "deshebrada", "nopales"]

if "salsa verde" in guisos:
    print(f"hay salsa verde")
elif "deshebrada" in guisos:
    print("hay deshebrada")
elif "guiso especial":
    print("hay guiso especial")

# lista vacia

guisos_2 = []

if guisos_2:     # aqui pregunta si hay algo en la lista
    for guiso in guisos_2:
        print(guiso)
else:
    print("no hay guisos")

#
guisos_disponibles = ["salsas verde", "deshebrada", "picadillo", "asado"]
guisos_a_ordenar = ["baebacoa", "deshebrada", "cabrito"]
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print("si hay de ese guiso")
    else:
        print("una disculpa, no tenemos de ese guiso")
print("final")