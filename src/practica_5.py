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
    print(f"tu indice de masa corporal es {imc}")
except ValueError:
    print("datos no validos (ej: 10, 67, 11)")
except:
    print("la altura debe ser diferente a cero")
except Exception:
    print(Exception)

print("procesos posteriores")