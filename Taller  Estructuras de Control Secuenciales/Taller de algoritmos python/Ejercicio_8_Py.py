# ejercicio_8
import math

def calcular_area_triangulo():
    # Entradas
    a = 0.0
    b = 0.0
    c = 0.0
    s = 0.0
    area = 0.0

    # Solicitar entrada al usuario
    a = float(input("Ingrese la longitud del lado a: "))
    b = float(input("Ingrese la longitud del lado b: "))
    c = float(input("Ingrese la longitud del lado c: "))

    # Calcular el semiperímetro
    s = (a + b + c) / 2

    # Calcular el área usando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Mostrar el resultado
    print(f"El área del triángulo es: {area:.2f}")

# Llamar a la función
calcular_area_triangulo()