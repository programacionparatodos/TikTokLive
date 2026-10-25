
// TODO: 486A - Calculating Function | Codeforces

Algoritmo CalculatingFunction
	
	// * Declaración de variables
	Definir n, fn Como Entero;
	
	// * Entrada de datos
	Leer n;
	
	// * Proceso
	fn <- trunc(n / 2) - (n % 2) * n;
	
	// * Salida de datos
	Escribir fn;
	
FinAlgoritmo
