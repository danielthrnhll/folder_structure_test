#agregando elementos a una lista

motorcycles = ["honda", "mortalica", "yamaha"]
print(motorcycles) #["honda", "mortalica", "yamaha"]

#metodo append - agrega elementos a la lista
motorcycles.append("kawasaki")
print(motorcycles) #["honda", "mortalica", "yamaha", "kawasaki"]

"""
el metodo append ayuda a crear
facilmente de manera dinamica
"""
motorcycles_2 = [] #lista vacia
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle)
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")
print(motorcycles_2)
motorcycle = "charly"
motorcycles_2.append(motorcycle)
print(motorcycles_2)

# el metodo insert nos ayuda a agregar elementos
# a una lista en un indice especifico

motorcycle_3 = ["honda", "yamaha", "suzuki"]
print("\n lista original" )
print(motorcycle_3)
motorcycle_3.insert(0, "ducati")
print("\n lista despues del metodo insert")
print(motorcycle_3)

# metodo .pop()