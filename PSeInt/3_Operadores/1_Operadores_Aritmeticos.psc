Algoritmo OperadoresAritmeticos
	
	// OPERADORES ARITMÉTICOS
	
	// Suma: +
	Escribir "Operador Suma (+)";
	Definir a, b, sumaEntero Como Entero;
	a <- 10;
	b <- 4;
	// Entero + Entero = Entero
	sumaEntero <- a + b;
	//    10 + 4 = 14
	// sumaEntero = 14 (Entero)
	Escribir sumaEntero;
	
	Definir c, d, sumaReal Como Real;
	c <- 4.5;
	d <- 3.5;
	
	// Real + Real = Real
	sumaReal = c + d;
	//    4.5 + 3.5 = 8.0
	// sumaReal = 8.0 (Real)
	Escribir sumaReal;
	
	// Entero + Real = Real
	sumaReal <- a + c;
	//     10 + 4.5 = 14.5
	// sumaReal = 14.5
	Escribir sumaReal;
	
	Escribir "Operador Resta (-)";
	// Resta: - 
	
	Definir restaEntera Como Entero;
	
	// Entero - Entero = Entero
	restaEntera = a - b;
	//           10 - 4 = 6
	// restaEntera = 6
	Escribir restaEntera;
	
	Definir restaReal Como Real;
	
	// Real - Real = Real
	restaReal = c - d;
	//        4.5 - 3.5 = 1.0
	// restaReal = 1.0
	Escribir restaReal;
	
	// Real - Entero = Real
	restaReal = d - a;
	//        3.5 - 10 = -6.5
	// restaReal = -6.5
	Escribir restaReal;
	
	Escribir "Operador Multiplicación (*)";
	// Multiplicación: * 
	
	Definir multiplicacionEntera Como Entero;
	
	// Entero * Entero = Entero
	multiplicacionEntera = a * b;
	//           10 * 4 = 40
	// multiplicacionEntera = 40
	Escribir multiplicacionEntera;
	
	Definir multiplicacionReal Como Real;
	
	// Real * Real = Real
	multiplicacionReal = c * d;
	//        4.5 * 3.5 = 15.75
	// multiplicacionReal = 15.75
	Escribir multiplicacionReal;
	
	// Real * Entero = Real
	multiplicacionReal = d * a;
	//        3.5 * 10 = 35
	// multiplicacionReal = 35
	Escribir multiplicacionReal;
	
	Escribir "Operador División Real (/)";
	// División Real: / 
	
	Definir divisionReal Como Real;
	
	// Entero / Entero = Real
	divisionReal = a / b;
	//           10 / 4 = 2.5
	// divisionReal = 2.5
	Escribir divisionReal;

	// Real / Real = Real
	divisionReal = c / d;
	//        4.5 / 3.5 = 1.2857
	// divisionReal = 1.2857
	Escribir divisionReal;
	
	// Real / Entero = Real
	divisionReal = d / a;
	//        3.5 / 10 = 0.35
	// divisionReal = 0.35
	Escribir divisionReal;
	
	Escribir "División Entera (trunc)";
	// División Entera: trunc() 
	
	Definir divisionEntera Como Entero;
	
	// Entero / Entero = Real
	divisionEntera = trunc(a / b);
	//           10 / 4 = 2
	// divisionEntera = 2
	Escribir divisionEntera;
	
	// Real / Real = Real
	divisionEntera = trunc(c / d);
	//        4.5 / 3.5 = 1
	// divisionEntera = 1
	Escribir divisionEntera;
	
	// Real / Entero = Real
	divisionEntera = trunc(d / a);
	//        3.5 / 10 = 0
	// divisionReal = 0
	Escribir divisionEntera;
	
	Escribir "Operador Módulo (%)";
	// Módulo Entero: 
	
	Definir modulo Como Entero;
	
	// Entero % Entero = Entero
	modulo <- a % b;
	Escribir modulo;
	
	// Entero % Entero = Entero
	modulo <- a MOD b;
	Escribir modulo;
	
	Escribir "Operador Potencia (^)";
	
	Definir potenciaEntera Como Entero;
	
	// Entero ^ Entero = Entero
	potenciaEntera <- a ^ b;
	//              10 ^ 4 = 10000
	// potenciaEntera = 10000
	Escribir potenciaEntera;
	
	Definir  potenciaReal Como Real;
	// Real ^ Real = Real
	potenciaReal <- c ^ d;
	//             4.5 ^ 3.5 = 193.305316
	// potenciaReal = 193.305316
	Escribir potenciaReal;
	
	// Entero ^ Real = Real
	potenciaReal <- a ^ d;
	//            10 ^ 3.5 = 3162.27766
	// potenciaReal = 3162.27766
	Escribir potenciaReal;
	
	// Entero ^ Entero Negativo = Real
	potenciaReal = 5 ^ (-2);
	// potenciaReal = 0.04
	Escribir potenciaReal;	
	
FinAlgoritmo
