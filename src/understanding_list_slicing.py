players = ["charly", "juan", "iancarlo", "lizandro"]

#slicing
print(players[0:2])

# el slicing me permite trabajar con un grupo
# especifico de una lista: al resultado se le conoc3 como
# un "slice"

print(players[1:4]) # "juan", "iancarlo", "lizandro"
print(players[:3]) # "charly", "juan", "iancarlo"
print(players[2:]) # "iancarlo", "lizandro"
print(players[-3:]) # "juan", "iancarlo", "lizandro"

# casos especiales
print(players[1:6]) # rellena con espacios blancos
print(players[6:1]) # da lista vacia
print(players[:0]) # da lista vacia

# looping through a slice
students = ["charly", "juan", "iancarlo", "lizandro"]
for student in students [2:4]:
    print(f"el estudiante {student}, va a pasar la materia")

#slicing [::]

# como podemos copiar una lista?
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food #manera erronea de copiar una lista

# 3 maneras de copiar una lista
# metodo 1, utilizando slicing
my_friend_food_2 = my food[:]

# metodo 2: utilizando el metodo copy
my my_friend_food_3 = my_food.copy

#metodo 3: utilizando el metodo build-in list()
my_friend_food_4 = list(my_food)
