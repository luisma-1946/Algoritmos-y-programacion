Algoritmo Ejercicio_12
	Escribir  CalcularPromedios
	Definir examenMat, tareaMat1, tareaMat2, tareaMat3, promTareasMat, promedioMat Como Real
	Definir examenFis, tareaFis1, tareaFis2, promTareasFis, promedioFis Como Real
	Definir examenQuim, tareaQuim1, tareaQuim2, tareaQuim3, promTareasQuim, promedioQuim Como Real
	Definir promedioGeneral Como Real
	
	// Entradas
	Escribir "Ingrese la nota del examen de Matem�tica: "
	Leer examenMat
	Escribir "Ingrese la nota de la primera tarea de Matem�tica: "
	Leer tareaMat1
	Escribir "Ingrese la nota de la segunda tarea de Matem�tica: "
	Leer tareaMat2
	Escribir "Ingrese la nota de la tercera tarea de Matem�tica: "
	Leer tareaMat3
	
	// Caja negra
	promTareasMat <- (tareaMat1 + tareaMat2 + tareaMat3) / 3
	promedioMat <- (examenMat * 0.90) + (promTareasMat * 0.10)
	
	// Entradas
	Escribir "Ingrese la nota del examen de F�sica: "
	Leer examenFis
	Escribir "Ingrese la nota de la primera tarea de F�sica: "
	Leer tareaFis1
	Escribir "Ingrese la nota de la segunda tarea de F�sica: "
	Leer tareaFis2
	
	// Caja negra
	promTareasFis <- (tareaFis1 + tareaFis2) / 2
	promedioFis <- (examenFis * 0.80) + (promTareasFis * 0.20)
	
	// Entrada
	Escribir "Ingrese la nota del examen de Qu�mica: "
	Leer examenQuim
	Escribir "Ingrese la nota de la primera tarea de Qu�mica: "
	Leer tareaQuim1
	Escribir "Ingrese la nota de la segunda tarea de Qu�mica: "
	Leer tareaQuim2
	Escribir "Ingrese la nota de la tercera tarea de Qu�mica: "
	Leer tareaQuim3
	
	// Caja negra
	promTareasQuim <- (tareaQuim1 + tareaQuim2 + tareaQuim3) / 3
	promedioQuim <- (examenQuim * 0.85) + (promTareasQuim * 0.15)
	
	// Caja negra
	promedioGeneral <- (promedioMat + promedioFis + promedioQuim) / 3
	
	// Salidas
	Escribir "--------------------------------------------------"
FinAlgoritmo
