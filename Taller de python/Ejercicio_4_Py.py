#ejercicio_4
try:

    total_compra = float(input("Ingrese el total de la compra: "))


    descuento = total_compra * 0.15
    total_pagar = total_compra - descuento


    print(f"El descuento aplicado es: {descuento:.2f}")
    print(f"El total a pagar después del descuento es: {total_pagar:.2f}")

except ValueError:
    print("Error: ingrsar valor valido.")