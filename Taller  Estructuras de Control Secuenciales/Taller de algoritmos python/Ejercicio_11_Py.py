# ejercicio_11
def calcular_promedios():
    # Definir variables
    examen_mat = 0.0
    tarea_mat1 = 0.0
    tarea_mat2 = 0.0
    tarea_mat3 = 0.0
    prom_tareas_mat = 0.0
    promedio_mat = 0.0

    examen_fis = 0.0
    tarea_fis1 = 0.0
    tarea_fis2 = 0.0
    prom_tareas_fis = 0.0
    promedio_fis = 0.0

    examen_quim = 0.0
    tarea_quim1 = 0.0
    tarea_quim2 = 0.0
    tarea_quim3 = 0.0
    prom_tareas_quim = 0.0
    promedio_quim = 0.0

    promedio_general = 0.0

    # Entrada de datos para Matemática
    examen_mat = float(input("Ingrese la nota del examen de Matemática: "))
    tarea_mat1 = float(input("Ingrese la nota de la primera tarea de Matemática: "))
    tarea_mat2 = float(input("Ingrese la nota de la segunda tarea de Matemática: "))
    tarea_mat3 = float(input("Ingrese la nota de la tercera tarea de Matemática: "))

    # Cálculo del promedio de Matemática
    prom_tareas_mat = (tarea_mat1 + tarea_mat2 + tarea_mat3) / 3
    promedio_mat = (examen_mat * 0.90) + (prom_tareas_mat * 0.10)

    # Entrada de datos para Física
    examen_fis = float(input("Ingrese la nota del examen de Física: "))
    tarea_fis1 = float(input("Ingrese la nota de la primera tarea de Física: "))
    tarea_fis2 = float(input("Ingrese la nota de la segunda tarea de Física: "))

    # Cálculo del promedio de Física
    prom_tareas_fis = (tarea_fis1 + tarea_fis2) / 2
    promedio_fis = (examen_fis * 0.80) + (prom_tareas_fis * 0.20)

    # Entrada de datos para Química
    examen_quim = float(input("Ingrese la nota del examen de Química: "))
    tarea_quim1 = float(input("Ingrese la nota de la primera tarea de Química: "))
    tarea_quim2 = float(input("Ingrese la nota de la segunda tarea de Química: "))
    tarea_quim3 = float(input("Ingrese la nota de la tercera tarea de Química: "))

    # Cálculo del promedio de Química
    prom_tareas_quim = (tarea_quim1 + tarea_quim2 + tarea_quim3) / 3
    promedio_quim = (examen_quim * 0.85) + (prom_tareas_quim * 0.15)

    # Cálculo del promedio general
    promedio_general = (promedio_mat + promedio_fis + promedio_quim) / 3

    # Mostrar resultados
    print("--------------------------------------------------")
    print(f"Promedio en Matemática: {promedio_mat:.2f}")
    print(f"Promedio en Física: {promedio_fis:.2f}")
    print(f"Promedio en Química: {promedio_quim:.2f}")
    print("--------------------------------------------------")
    print(f"Promedio general en las tres materias: {promedio_general:.2f}")
    print("--------------------------------------------------")

# Llamar a la función
calcular_promedios()