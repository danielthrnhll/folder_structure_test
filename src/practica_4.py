"""
    realizar un programa que calcule
    el total de un ticket, tomando
    en cuenta el iva y la propina
"""

subtotal_txt = input("subtotal (mnx): ")
iva_txt = input("iva (%) ejemplo: 16: ")
tip_txt = input("propina (%) ej: (10): (negativo para doña tota)")

try:
    subtotal = float(subtotal_txt)
    iva = float(iva_txt)/100
    tip = float(tip_txt)/100
except:
    print("entrada no valida, ej: 150.0, 16, 10")
    raise SystemExit(1)

iva_account = subtotal*iva
tip_account = subtotal*tip
total = subtotal + tip_account + iva_account

print(f"subtotal: {subtotal}")
print(f"iva: {iva}")
print(f"tip: {tip}")
print(f"total: {total}")