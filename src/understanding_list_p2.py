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

# metodo .pop() elimina el ultimo elemento de una lista,
#pero nos permite utilizar el elemento despues de eliminarlo

motorcycles_4 = ["honda", "suzuki", "hd", "italika"]
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(motorcycles_4)
print(f"tu moto borrada es {deleted_motorcycle}")

# se pueden utilizar tambien para eliminar un elemento especifico
motorcycles_5 = ["honda", "suzuki", "hd", "italika"]
print(motorcycles_5)
motorcycles_5.pop(0)
print(motorcycles_5) #lista sin honda

# metodo .remove()
# permite eliminar elementos por su valor
print(67)
motorcycles_6 = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles_6)
motorcycles_6.remove("yamaha")
print(motorcycles_6)

"""
    Función built-in sorted
    
    Ordena la lista de manera temporal 
    en orden alfabetico

"""
cars = ['bmw', 'audi', 'toyotta']
print("Lista Original")
print(cars)
print("Lista Ordenada")
print(sorted(cars))
print("Lista Original")
print(cars)

"""
    Método reverse
    
    El método reverse de las listas
    invierte la lista de manera permanente

"""
cars.reverse()
print(cars)

"""

    Función built-in len

    Longitud de las listas
    
    El método len nos dice la cantidad
    de elementos que hay en una lista
    
"""

print(len(cars))