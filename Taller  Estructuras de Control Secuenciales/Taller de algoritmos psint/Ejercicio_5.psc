Algoritmo Ejercicio_5
	Proceso Calcular_CalificacionFinal
	Definir parcial1, parcial2, parcial3, examenFinal, trabajoFinal Como Real
	Definir promedioParciales, calificacionFinal Como Real
	//Entradas
	Escribir "Ingrese la primera calificaci�n parcial: "
	Leer parcial1
	
	Escribir "Ingrese la segunda calificaci�n parcial: "
	Leer parcial2
	
	Escribir "Ingrese la tercera calificaci�n parcial: "
	Leer parcial3
	
	Escribir "Ingrese la calificaci�n del examen final: "
	Leer examenFinal
	
	Escribir "Ingrese la calificaci�n del trabajo final: "
	Leer trabajoFinal
	//Caja negra
	promedioParciales <- (parcial1 + parcial2 + parcial3) / 3
	calificacionFinal <- (promedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)
	//Salidas
	Escribir "La calificaci�n final en computaci�n es: ", calificacionFinal
	
	
FinAlgoritmo
