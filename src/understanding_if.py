



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
