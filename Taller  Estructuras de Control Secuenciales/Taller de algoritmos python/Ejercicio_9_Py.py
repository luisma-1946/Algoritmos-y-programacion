# ejercicio_9
def calcular_salario_neto():
    # Definir variables
    horas_trabajadas = 0.0
    precio_hora = 0.0
    salario_bruto = 0.0
    descuento = 0.0
    salario_neto = 0.0

    # Solicitar entrada al usuario
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
    precio_hora = float(input("Ingrese el precio por hora trabajada: "))

    # Calcular el salario bruto, descuento y salario neto
    salario_bruto = horas_trabajadas * precio_hora
    descuento = salario_bruto * 0.20
    salario_neto = salario_bruto - descuento

    # Mostrar los resultados
    print(f"El salario bruto es: {salario_bruto:.2f}")
    print(f"El descuento por impuestos es: {descuento:.2f}")
    print(f"El salario neto a recibir es: {salario_neto:.2f}")


calcular_salario_neto()