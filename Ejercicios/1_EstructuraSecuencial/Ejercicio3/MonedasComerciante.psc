Algoritmo MonedasComerciante
	Definir N, C, B, resto Como Entero;
	Definir cofres, bolsas, sobrantes Como Entero;
	Leer N, C, B;
	cofres <- trunc(N / C);
	resto <- N % C;
	bolsas <- trunc(resto / B);
	sobrantes <- resto % B;
	Escribir cofres, bolsas, sobrantes;
FinAlgoritmo
