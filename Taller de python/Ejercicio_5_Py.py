# ejercicio_5
def calcular_calificacion_final():
    # Solicitar
    parcial1 = float(input("Ingrese la primera calificación parcial: "))
    parcial2 = float(input("Ingrese la segunda calificación parcial: "))
    parcial3 = float(input("Ingrese la tercera calificación parcial: "))
    examen_final = float(input("Ingrese la calificación del examen final: "))
    trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

    # Calcular el promedio de los parciales
    promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

    # Calcular la calificación final
    calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

    # Mostrar la calificación final
    print(f"calificacion final: {calificacion_final}")

# Llamar a la función para ejecutar el proceso
calcular_calificacion_final()