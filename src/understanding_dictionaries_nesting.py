# nesting

# listas de diccionarios
covenant_elite = {"name": "elite", "color": "blue", "points": 10, "shield": True}
covenant_jackal = {"name": "jackal", "color": "grey", "points": 6, "shield": True}
covenant_grunts = {"name": "grunt", "color": "orange", "points": 3, "shield": False}

# nesting de lista de diccionario
covenants = []
covenants.append(covenant_elite)
covenants.append(covenant_jackal)
covenants.append(covenant_grunts)
print(covenants)

print("\n looping")
# looping though the list
for covenant in covenants:
    print(covenant)

# vamos a crear una flotilla de enemigos (covenant)
covenant_fleet = []

for _ in range(2):
    covenant_fleet.append(covenant_elite)

for _ in range(5):
    covenant_fleet.append(covenant_jackal)

for _ in range(20):
    covenant_fleet.append(covenant_grunts)

print("\n flotilla")
print(covenant_fleet)

# nesting: una lista en un diccionario

tacos = {
    "tortillas": ["maiz", "harina"],
    "guisos": ["bistek", "tripa", "pastor"]
}

print(f"\n tu has ordenado unos tacos de {tacos["guisos"][0]}")
print(f"en tortillas de {tacos["tortillas"][1]}")