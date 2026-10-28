"""
    programa para calcular el indice de
    masa corporal de una persona
"""
weight_txt = input("peso (en kg):")
height_txt = input("altura (en m):")

try:
    weight = float(weight_txt)
    height = float(height_txt)
    imc = weight / (height ** 2)
except:
    print("datos no validos (ej: 10, 67, 11)")