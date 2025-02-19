# ejercicio_12
def calcular_sueldo_trabajador():
    # Definir variables
    nombre = ""
    horas_normales = 0.0
    horas_extras = 0.0
    pago_hora = 0.0
    sueldo_base = 0.0
    pago_horas_extras = 0.0
    sueldo_bruto = 0.0
    deduccion_pago_forzoso = 0.0
    deduccion_politica_habitacional = 0.0
    deduccion_caja_ahorro = 0.0
    total_deducciones = 0.0
    hijos = 0
    asignacion_hijos = 0.0
    asignacion_academica = 250000
    asignacion_hogar = 180000
    total_asignaciones = 0.0
    sueldo_neto = 0.0

    # Entrada de datos
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_normales = float(input("Ingrese el número de horas normales trabajadas: "))
    pago_hora = float(input("Ingrese el pago por una hora normal: "))
    horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
    hijos = int(input("Ingrese el número de hijos del trabajador: "))

    # Cálculo del sueldo base y horas extras
    sueldo_base = horas_normales * pago_hora
    pago_horas_extras = horas_extras * (pago_hora * 1.25)
    sueldo_bruto = sueldo_base + pago_horas_extras

    # Cálculo de deducciones
    deduccion_pago_forzoso = sueldo_base * 0.05
    deduccion_politica_habitacional = sueldo_base * 0.02
    deduccion_caja_ahorro = sueldo_base * 0.07
    total_deducciones = deduccion_pago_forzoso + deduccion_politica_habitacional + deduccion_caja_ahorro

    # Cálculo de asignaciones
    asignacion_hijos = hijos * 173000
    total_asignaciones = asignacion_academica + asignacion_hijos + asignacion_hogar

    # Cálculo del sueldo neto
    sueldo_neto = sueldo_bruto - total_deducciones + total_asignaciones

    # Mostrar resultados
    print("--------------------------------------------------")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo base: {sueldo_base:.2f}")
    print(f"Pago por horas extras: {pago_horas_extras:.2f}")
    print(f"Sueldo bruto: {sueldo_bruto:.2f}")
    print("--------------------------------------------------")
    print("Deducciones:")
    print(f" - Pago forzoso (5%): {deduccion_pago_forzoso:.2f}")
    print(f" - Política habitacional (2%): {deduccion_politica_habitacional:.2f}")
    print(f" - Caja de ahorro (7%): {deduccion_caja_ahorro:.2f}")
    print(f"Total de deducciones: {total_deducciones:.2f}")
    print("--------------------------------------------------")
    print("Asignaciones:")
    print(f" - Actualización académica: {asignacion_academica:.2f}")
    print(f" - Asignación por hijos: {asignacion_hijos:.2f}")
    print(f" - Prima por hogar: {asignacion_hogar:.2f}")
    print(f"Total de asignaciones: {total_asignaciones:.2f}")
    print("--------------------------------------------------")
    print(f"Sueldo neto a recibir: {sueldo_neto:.2f}")
    print("--------------------------------------------------")


calcular_sueldo_trabajador()