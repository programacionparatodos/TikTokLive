
// TODO: Strange Grid Again - HackerRank

Algoritmo StrangeGridAgain
	
	// * Declaración de variables
	Definir r, c, grupo, inicio, posicion Como Entero;
	Definir desplezamiento, resultado Como Entero;
	
	// * Entrada de datos
	Leer r, c;
	
	// * Proceso 
	grupo <- trunc((r - 1) / 2);
	inicio <- grupo * 10;
	posicion <- (r - 1) % 2;
	desplezamiento <- 2 * (c - 1);
	resultado <- inicio + posicion + desplezamiento;
	
	// * Salida de datos
	Escribir resultado;
	
FinAlgoritmo