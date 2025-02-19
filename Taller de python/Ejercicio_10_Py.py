# ejrcicio_10
def cambio_divisas():
    # Entrasdas
    chelines = 0.0
    dracmas = 0.0
    pesetas = 0.0
    pesetas_desde_chelines = 0.0
    francos_desde_dracmas = 0.0
    dolares_desde_pesetas = 0.0
    liras_desde_pesetas = 0.0

    # Conversión de chelines austríacos a pesetas
    chelines = float(input("Ingrese la cantidad en chelines austríacos: "))
    pesetas_desde_chelines = (chelines * 956.871) / 100
    print(f"{chelines} chelines austríacos equivalen a {pesetas_desde_chelines:.2f} pesetas.")

    # Conversión de dracmas griegos a francos franceses
    dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
    francos_desde_dracmas = (dracmas * 88.607) / 100 / 20.110
    print(f"{dracmas} dracmas griegos equivalen a {francos_desde_dracmas:.2f} francos franceses.")

    # Conversión de pesetas a dólares estadounidenses y liras italianas
    pesetas = float(input("Ingrese la cantidad en pesetas: "))
    dolares_desde_pesetas = pesetas / 122.499
    liras_desde_pesetas = (pesetas * 100) / 9.289
    print(f"{pesetas} pesetas equivalen a {dolares_desde_pesetas:.2f} dólares estadounidenses.")
    print(f"{pesetas} pesetas equivalen a {liras_desde_pesetas:.2f} liras italianas.")

cambio_divisas()