
// TODO: Count Balls AtCoder

Algoritmo CountBalls
	
	// * Declaración de variables
	Definir n, a, b, t, g Como Entero;
	Definir z, r, e, azules Como Entero;
		
	// * Entrada de datos
	Leer n, a, b;	
	
	// * Proceso 
	t <- a + b;
	g <- trunc(n / t);
	z <- g * a;
	r <- n % t;
	e <- trunc((r + a - abs(r - a)) / 2);
	azules <- z + e;
	
	// * Salida de datos
	Escribir azules;
	
FinAlgoritmo