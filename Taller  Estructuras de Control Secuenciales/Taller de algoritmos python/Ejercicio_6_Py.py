# ejrcicio_6
def calcular_porcentaje_genero():
    # Definir variables
    total_estudiantes = 0
    hombres = 0
    mujeres = 0
    porcentaje_hombres = 0.0
    porcentaje_mujeres = 0.0

    # Solicitar entrada al usuario
    hombres = int(input("Ingrese el número de hombres en el grupo: "))
    mujeres = int(input("Ingrese el número de mujeres en el grupo: "))

    # Calcular el total de estudiantes
    total_estudiantes = hombres + mujeres

    # Calcular los porcentajes
    porcentaje_hombres = (hombres / total_estudiantes) * 100
    porcentaje_mujeres = (mujeres / total_estudiantes) * 100

    # Mostrar los resultados
    print(f"El porcentaje de hombres en el grupo es: {porcentaje_hombres:.2f}%")
    print(f"El porcentaje de mujeres en el grupo es: {porcentaje_mujeres:.2f}%")

# Llamar a la función
calcular_porcentaje_genero()