"""
Daniel Martin Limon Garcia
2630427
IM 1-2
"""

"""

resumen ejecutivo:
En Python, los tipos de datos int y float permiten trabajar con números enteros y decimales, respectivamente. 
Los booleanos (True y False) representan valores de verdad que se obtienen mediante comparaciones y permiten 
tomar decisiones en un programa. La validación de rangos es importante para garantizar que los datos ingresados 
sean correctos y estén dentro de los límites establecidos. Asimismo, evitar la división entre cero previene errores 
durante la ejecución del código. Este documento describirá cada problema, el diseño de sus entradas y salidas, y 
las validaciones aplicadas. También explicará cómo se utilizan los enteros, flotantes y booleanos para realizar 
operaciones, evaluar condiciones y obtener resultados confiables.

"""

"""

principios y buenas practicas:
- Usar tipos apropiados: int para contadores, float para cantidades con decimales.
- Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
- Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
- Usar nombres de variables descriptivos y mensajes claros para el usuario.
- Documentar claramente cómo se interpretan los booleanos (qué significa true y qué significa false en cada contexto).

"""

# problems

# problem 1: Problem 1: Temperature converter and range flag
# description:
# se convertira la temperatura introducida, la cual esta en celcius,
# a fahrenheit y kelvin. si celsius rebasa el limite de cero absoluto
# de fahrenheit marcara error


#inputs:
# temp_c = temp

# outputs
# "Fahrenheit:" <temp_f>
# "Kelvin:" <temp_k>
# "High temperature:" true|false

#Validations:
# Verificar que temp_c pueda convertirse a float.
# No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0

#test cases
print("\n test cases problem 1 \n".title())

#normal
temp_c = 20
print(f"celcius: {temp_c}°C")
if temp_c <= -273.15:
    print("error: invalid temperature \n")
else:
    Fahrenheit = (temp_c * 9/5) + 32
    print(f"fahrenheit: {Fahrenheit}°F")
    kelvin = temp_c - 273.15
    print(f"kelvin: {kelvin}°K")
    if temp_c >=30:
        hot = True
    else:
        hot = False
    print(f"high temperature: {hot} \n")
        
# border
temp_c = 30
print(f"celcius: {temp_c}°C")
if temp_c <= -273.15:
    print("error: invalid temperature \n")
else:
    Fahrenheit = (temp_c * 9/5) + 32
    print(f"fahrenheit: {Fahrenheit}°F")
    kelvin = temp_c - 273.15
    print(f"kelvin: {kelvin}°K")
    if temp_c >=30:
        hot = True
    else:
        hot = False
    print(f"high temperature: {hot} \n")

# error
temp_c = -300
print(f"celcius: {temp_c}°C")
if temp_c <= -273.15:
    print("error: invalid temperature \n")
else:
    Fahrenheit = (temp_c * 9/5) + 32
    print(f"fahrenheit: {Fahrenheit}°F")
    kelvin = temp_c - 273.15
    print(f"kelvin: {kelvin}°K")
    if temp_c >=30:
        hot = True
    else:
        hot = False
    print(f"high temperature: {hot} \n")

# Problem 2: Work hours and overtime payment
# description:
# de acuerdo a unas horas dadas y un pago por hora
# dado se saca el pago por hora, si se trabajo mas de
# 40 horas, el pago de horas extra y pago total

#inputs:
# hours_worked = horas en float
# hourly_rate = cuanto se paga por hora en float

#outputs
# Regular pay: 20
# Overtime pay: 30
# Total pay: total_pay
# Has overtime: true|false

# Validations
# hours_worked >= 0
# hourly_rate > 0
# Si alguno no cumple, mostrar "Error: invalid input".

# test cases
print("\n test cases problem 2 \n".title())

# normal
hours_worked = 67
hourly_rate = 350
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input \n")
elif hours_worked <= 40:
    overtime = False
    regular_pay = hours_worked * hourly_rate
    print(f"regular pay: {regular_pay}")
    print("overtime pay: 0")
    print(f"total pay: {regular_pay}")
    print(f"has overtime: {overtime} \n")
else: 
    overtime = True
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    print(f"regular pay: {regular_pay}")
    print(f"overtime pay: {overtime_pay}")
    print(f"total pay: {regular_pay + overtime_pay}")
    print(f"has overtime: {overtime} \n")

#border
hours_worked = 40
hourly_rate = 400
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input \n")
elif hours_worked <= 40:
    overtime = False
    regular_pay = hours_worked * hourly_rate
    print(f"regular pay: {regular_pay}")
    print("overtime pay: 0")
    print(f"total pay: {regular_pay}")
    print(f"has overtime: {overtime} \n")
else: 
    overtime = True
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    print(f"regular pay: {regular_pay}")
    print(f"overtime pay: {overtime_pay}")
    print(f"total pay: {regular_pay + overtime_pay}")
    print(f"has overtime: {overtime} \n")

# Error
hours_worked = -1
hourly_rate = 67
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input \n")
elif hours_worked <= 40:
    overtime = False
    regular_pay = hours_worked * hourly_rate
    print(f"regular pay: {regular_pay}")
    print("overtime pay: 0")
    print(f"total pay: {regular_pay}")
    print(f"has overtime: {overtime} \n")
else: 
    overtime = True
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    print(f"regular pay: {regular_pay}")
    print(f"overtime pay: {overtime_pay}")
    print(f"total pay: {regular_pay + overtime_pay}")
    print(f"has overtime: {overtime} \n")

# problem 3: Discount eligibility with booleans
# description:
# averiguar si una compra es elegible para descuento
# esdto tanto si es estudiante, adulto mayor o cuesta mas
# de 1000

#inputs
# purchase_total = 10000
# is_student_text YEs or NO
# is_senior_text = YEs or NO

# outputs
# Discount eligible: true o false
# Final total: 9000

# validations
# purchase_total >= 0.0
# Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
# Si el texto no es "YES" ni "NO", mostrar "Error: invalid input"

# test cases 
print("\n test cases problem 3 \n".title())

# normal
purchase_total = 6700
is_student = "yes".upper()
is_senior = "no".upper()
if not (is_student == "YES" or is_senior == "YES" or is_student == "NO" or is_senior == "NO"):
    print("Error: invalid input \n")
elif purchase_total < 0:
    print("Error: invalid input \n")
elif (is_student == "YES" or is_senior == "YES" or purchase_total >= 1000) and purchase_total >= 0:
    purchase_with_discount = purchase_total * 0.9
    discount_elegible = True
    print(f"discount elegible: {discount_elegible}")
    print(f"final total: {purchase_with_discount}\n")
elif (is_student == "NO" or is_senior == "NO" or purchase_total <= 1000) and purchase_total >= 0:
    discount_elegible = False
    print(f"discount elegible: {discount_elegible}")
    print(f"final total: {purchase_total} \n")

# border
purchase_total = 0
is_student = "no".upper()
is_senior = "yeS".upper()
if not (is_student == "YES" or is_senior == "YES" or is_student == "NO" or is_senior == "NO"):
    print("Error: invalid input \n")
elif purchase_total < 0:
    print("Error: invalid input \n")
elif (is_student == "YES" or is_senior == "YES" or purchase_total >= 1000) and purchase_total >= 0:
    purchase_with_discount = purchase_total * 0.9
    discount_elegible = True
    print(f"discount elegible: {discount_elegible}")
    print(f"final total: {purchase_with_discount} \n")
elif (is_student == "NO" or is_senior == "NO" or purchase_total <= 1000) and purchase_total >= 0:
    discount_elegible = False
    print(f"discount elegible: {discount_elegible} \n")
    print(f"final total: {purchase_total}")

# error
print("error 1")
purchase_total = -75
is_student = "yes".upper()
is_senior = "yeS".upper()
if not (is_student == "YES" or is_senior == "YES" or is_student == "NO" or is_senior == "NO"):
    print("Error: invalid input \n")
elif purchase_total < 0:
    print("Error: invalid input \n")
elif (is_student == "YES" or is_senior == "YES" or purchase_total >= 1000) and purchase_total >= 0:
    purchase_with_discount = purchase_total * 0.9
    discount_elegible = True
    print(f"discount elegible: {discount_elegible}")
    print(f"final total: {purchase_with_discount} \n")
elif (is_student == "NO" or is_senior == "NO" or purchase_total <= 1000) and purchase_total >= 0:
    discount_elegible = False
    print(f"discount elegible: {discount_elegible} \n")
    print(f"final total: {purchase_total}")

print("error 2")
purchase_total = 67
is_student = "el".upper()
is_senior = "talvez".upper()
if not (is_student == "YES" or is_senior == "YES" or is_student == "NO" or is_senior == "NO"):
    print("Error: invalid input \n")
elif purchase_total < 0:
    print("Error: invalid input \n")
elif (is_student == "YES" or is_senior == "YES" or purchase_total >= 1000) and purchase_total >= 0:
    purchase_with_discount = purchase_total * 0.9
    discount_elegible = True
    print(f"discount elegible: {discount_elegible}")
    print(f"final total: {purchase_with_discount} \n")
elif (is_student == "NO" or is_senior == "NO" or purchase_total <= 1000) and purchase_total >= 0:
    discount_elegible = False
    print(f"discount elegible: {discount_elegible} \n")
    print(f"final total: {purchase_total}")

# problem 4:  Basic statistics of three integers
# description: sumar 3 enteros y sacar un promedio,
# suma, cual es el mas grande y pequeño y si todos son 
# par o no.

#inputs
# n1 = int
# n2 = int
# n3 = int

# outputs
# "Sum:" <sum_value>
# "Average:" <average_value>
# "Max:" <max_value>
# "Min:" <min_value>
# "All even:" true|false

# Validations:
# Verificar que los tres valores se puedan convertir a int.
# No se requieren restricciones adicionales (se permiten negativos).

#test cases
print("\n test cases problem 4 \n".title())

# normal
n1 = int("67")
n2 = int("41")
n3 = int("420")
if not(isinstance(n1, int) and isinstance(n2, int) and isinstance(n3, int)):
    print("error: these are no int values \n")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value/3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
        all_even = True
    else:
       all_even = False
    print(f"sum: {sum_value}")
    print(f"average {average_value}")
    print(f"max: {max_value}")
    print(f"min: {min_value}")
    print(f"all even: {all_even} \n")

# border
n1 = int(float("41.12"))
n2 = int(float("-7.04"))
n3 = int(float("67.99"))
if not(isinstance(n1, int) and isinstance(n2, int) and isinstance(n3, int)):
    print("error: these are no int values \n")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value/3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
        all_even = True
    else:
       all_even = False
    print(f"sum: {sum_value}")
    print(f"average {average_value}")
    print(f"max: {max_value}")
    print(f"min: {min_value}")
    print(f"all even: {all_even} \n")

# error
n1 = "pepe"
n2 = int("1")
n3 = int("2")
if not(isinstance(n1, int) and isinstance(n2, int) and isinstance(n3, int)):
    print("error: these are no int values \n")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value/3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
        all_even = True
    else:
       all_even = False
    print(f"sum: {sum_value}")
    print(f"average {average_value}")
    print(f"max: {max_value}")
    print(f"min: {min_value}")
    print(f"all even: {all_even} \n")

#problem 5: Loan eligibility (income and debt ratio)
# description: determinar si alguien es apto para un
# credito esto calculando su debt ratio y verificando
# su credit score

#inputs:
# monthly_income = float
# monthly_debt = float
# credit_score = float

# outputs:
# debt ratio: 67
# Eligible: true o false

# Validaciones:
# monthly_income > 0.0 (evitar división entre cero).
# monthly_debt >= 0.0
# credit_score >= 0
# Si no se cumple, mostrar "Error: invalid input".

#test cases
print("\n test cases problem 5 \n".title())

# normal
monthly_income = 50067.67
monthly_debt = 20000.79
credit_score = 670
debt_ratio = monthly_debt / monthly_income
if not monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
    print("Error: invalid values \n")
else:
    if monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650:
        eligible = True
    else:
        eligible = False
    print(f"debt ratio: {debt_ratio}")
    print(f"eligible: {eligible } \n")

# border
monthly_income = 8000
monthly_debt = 3200
credit_score = 650
debt_ratio = monthly_debt / monthly_income
if not monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
    print("Error: invalid values \n")
else:
    if monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650:
        eligible = True
    else:
        eligible = False
    print(f"debt ratio: {debt_ratio}")
    print(f"eligible: {eligible} \n")

# error
monthly_income = -8000
monthly_debt = 67777
credit_score = 420
debt_ratio = monthly_debt / monthly_income
if not monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
    print("Error: invalid values \n")
else:
    if monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650:
        eligible = True
    else:
        eligible = False
    print(f"debt ratio: {debt_ratio}")
    print(f"eligible: {eligible} \n")

# problem 6: Body Mass Index (BMI) and category flag
# description:
# determinar el indice de masa corpora de alguien
# en base a peso y altura y señalar si esta por debajo
# en la media o por arriba del peso estandar

# inputs
# weight_kg = float
# height_m = float

#outputs
# "BMI:" <bmi_redondeado>
# "Underweight:" true o false
# "Normal:" true o false
# "Overweight:" true o false

# validation
# weight_kg > 0.0
# height_m > 0.0
# Si no se cumple, mostrar "Error: invalid input

# test cases
print("\n test cases problem 6 \n".title())

# normal
weight_kg = 67.9
height_m = 1.67
bmi = weight_kg / (height_m * height_m)
bmi_round = round(bmi, 1)
is_underweight = (bmi < 18.5)
is_normal = (18.5 <= bmi < 25.0)
is_overweight = (bmi >= 25.0)
if  weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input \n")
else:
    print(f"BMI: {bmi_round}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight} \n")

# border
weight_kg = 59.95
height_m = 1.80
bmi = weight_kg / (height_m * height_m)
bmi_round = round(bmi, 1)
is_underweight = (bmi < 18.5)
is_normal = (18.5 <= bmi < 25.0)
is_overweight = (bmi >= 25.0)
if  weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input \n")
else:
    print(f"BMI: {bmi_round}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight} \n")

# error
weight_kg = 1
height_m = -1.67
bmi = weight_kg / (height_m * height_m)
bmi_round = round(bmi, 1)
is_underweight = (bmi < 18.5)
is_normal = (18.5 <= bmi < 25.0)
is_overweight = (bmi >= 25.0)
if  weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input \n")
else:
    print(f"BMI: {bmi_round}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight} \n")


# conclusiones
"""

los enteros y los flotantes soy muy importantes ya que nois permiten hacer calculos de forma 
muy sencilla y rapida
a la hora de hacer una comparacion, generamos datos booleanos (true y false), que tecnicamente 
tambien son enteros (0 y 1)
es importante evitar las divisiones entre cero ya que es algo que esta indeterminado en las 
matematicas reales y el codigo truena y ahi queda
las condicionales son de gran ayuda ya que nos permiten descartar y categorizar datos facilmente
estos sistemas son usados para calcular sueldos, precios y datos facilmente en la vida real

"""

# fuentes
"""
- https://entrenamiento-python-basico.readthedocs.io/es/2.7/leccion3/tipo_numericos.html
- https://ellibrodepython.com/booleano-python
- https://interactivechaos.com/es/python/function/int
- https://ellibrodepython.com/operadores-logicos
- https://micro.recursospython.com/recursos/como-dividir-un-numero.html

"""