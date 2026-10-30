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


sum = 0.0
count_inputs = 0
minimun_value = None
maximun_value = None 
message = """
    suma de valores

    para salir del programa tipea exit

"""

while True:
    value_txt = input(message)
    if value_txt.lower() == "exit":
        break
    
    try:
        value = float(value_txt)
    except ValueError:
        print("el valor que ingresaste no es valido")
        continue 
    sum += value
    count_inputs += 1

    if minimun_value == None and maximun_value == None :
        minimun_value = value
        maximun_value = value
    else:
        if value < minimun_value:
            minimun_value = value
        elif value > maximun_maximun:  
            maximun_maximun = value


average = sum / count_inputs
print(f"tu total acumulado es: {sum}")
print(f"tus inputs fueron {count_inputs}")
print(f"tu promedio fue {average}")
print(f"tu valor mas pequeño fue {min}")
print(f"tu valor mas grande fue {max}")