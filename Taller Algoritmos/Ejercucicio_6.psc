Algoritmo Ejercicio_6
	Escribir " Calcular_Porcentaje_Genero"
	Definir totalEstudiantes, hombres, mujeres Como Entero
	Definir porcentajeHombres, porcentajeMujeres Como Real
	
	Escribir "Ingrese el n�mero de hombres en el grupo: "
	Leer hombres
	
	Escribir "Ingrese el n�mero de mujeres en el grupo: "
	Leer mujeres
	
	totalEstudiantes <- hombres + mujeres
	
	porcentajeHombres <- (hombres / totalEstudiantes) * 100
	porcentajeMujeres <- (mujeres / totalEstudiantes) * 100
	
	Escribir "El porcentaje de hombres en el grupo es: ", porcentajeHombres, "%"
	Escribir "El porcentaje de mujeres en el grupo es: ", porcentajeMujeres, "%"

FinAlgoritmo
