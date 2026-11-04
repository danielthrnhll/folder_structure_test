"""
    realizar una funcion que genere
    el nombre completo de una persona.
    dando su: primer nombre. segundo nombre
    y apellidos

"""

def create_fullname(firstname: str, lastname: str, middlename: str = "") -> str:
    """
    esta funcion genera el nombre completo de una persona
    dada los parametros
    """
    if middlename == "":
        fullname = f"{firstname} {lastname}".title()
    else:
        fullname = f"{firstname} {middlename} {lastname}".title() 
    print(fullname)
    return fullname

# argumentos posicionales
create_fullname("daniell", "limon", "garcia")

# argumentos clave
create_fullname(lastname="limon", middlename= "martin", firstname= "daniell")

# posicion y argumentos clave ( ver como combinarlos)
create_fullname("daniell", lastname="limon", middlename="martin") 

#rgumentos opcionales
create_fullname("daniell" , "limon" )