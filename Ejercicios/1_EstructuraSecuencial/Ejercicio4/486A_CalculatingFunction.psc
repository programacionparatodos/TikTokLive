
// TODO: 486A - Calculating Function | Codeforces
Algoritmo CalculatingFunction
	
	// * Declaraci�n de variables
	Definir n, fn Como Entero;
	
	// * Entrada
	Leer n;
	
	// * Proceso
	fn <- trunc(n / 2) - (n % 2) * n;
	
	// * Salida
	Escribir fn;
	
FinAlgoritmo
