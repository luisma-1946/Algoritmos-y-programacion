# Ejercicio_3
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))


comisiones = (venta1 + venta2 + venta3) * 0.10
sueldo_total = sueldo_base + comisiones

#Salida
print(f"El total de comisiones es: {comisiones}")
print(f"El sueldo total del vendedor es: {sueldo_total}")