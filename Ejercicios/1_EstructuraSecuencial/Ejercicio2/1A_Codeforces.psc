// 1A - Theatre Square | Codeforces
Algoritmo TheatreSquare1A

	// Declaración de variables
	Definir n, m, a Como Entero;
	Definir col, fil, total Como Entero;

	// Entrada de datos
	Escribir "Ingrese el valor de n: ";
	Leer n;
	Escribir "Ingrese el valor de m: ";
	Leer m;
	Escribir "Ingrese el valor de a: ";
	Leer a;

	// Proceso
	col = TRUNC((n + a - 1) / a);
	fil = TRUNC((m + a - 1) / a);
	total = col * fil;

	// Salida de datos
	Escribir "El total es: ", total;

FinAlgoritmo