"""
    while condition:
    se va a  repetir siempre que sea True
    

    while True
        print("hola")

    realizar un programa que capture ei
    importe y acumule todos estos importes
    en una variabe
"""
sum = 0.0
message = """
    sistema gestor de acumulacion de valores.
    la creatividad esta en tus manos

    para salir del programa, puedes tipear 
    q, e. quit, exit

"""
while True:
    value_txt = input(message)

    if value_txt == "quit" or \
        value_txt == "exit" or \
        value_txt == "q" or \
        value_txt == "e":
        break

    value = float(value_txt)
    sum += value # estructura acumuladora

print(f"tu total acumulado es: {sum}")

"""
tarea - realizar un programa que
capture los importes introducidos por el usuario

el programa debe:
    - contabilizar cuantos importes ha introducido el usuario
    - acumular los importes que ha introducido el usuario
    - establecer el maximo y minimo de los valores introducidos
    - calcular el promedio de los valores introducidos

despues de que el usuario termine el programa
debe mostrar estos datos

 - el contador de numeros utilixados
 - el acumulado de los numeros ingresados
 - el promedio
 -el minimo y maximo valor ingresados


"""