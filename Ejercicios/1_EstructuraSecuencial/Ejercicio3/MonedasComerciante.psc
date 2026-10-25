
// TODO: Monedas Comerciante - Programación Para Todos

Algoritmo MonedasComerciante

	// * Declaración de variables
	Definir N, C, B, resto Como Entero;
	Definir cofres, bolsas, sobrantes Como Entero;

	// * Entrada de datos
	Leer N, C, B;

	// * Proceso
	cofres <- trunc(N / C);
	resto <- N % C;
	bolsas <- trunc(resto / B);
	sobrantes <- resto % B;

	// * Salida de datos
	Escribir cofres, bolsas, sobrantes;
	
FinAlgoritmo
