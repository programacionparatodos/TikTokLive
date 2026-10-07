Algoritmo OperadoresLogicos
	
	// Operador Lógico: Y
	// V  Y  V  Y  V  Y  V -> V
	// V  Y  V  Y  V  Y  F -> F
	
	Definir comparacion Como Logico;
	
	Escribir "Operador Lógico Y";
	Escribir "";
	// Lógico Y Lógico
	comparacion = Verdadero Y Verdadero;
	// comparacion = Verdadero
	Escribir comparacion;
	comparacion = Verdadero Y Falso;
	// comparacion = Falso
	Escribir comparacion;
	comparacion = Falso Y Verdadero;
	// comparacion = Falso
	Escribir comparacion;
	comparacion = Falso Y Falso;
	// comparacion = Falso
	Escribir comparacion;
	Escribir "";
	
	// Operador Lógico: O
	// F  O  F  O  F  O  V -> V
	// F  O  F  O  F  O  F -> F
	
	Escribir "Operador Lógico O";
	Escribir "";
	// Lógico O Lógico
	comparacion = Verdadero O Verdadero;
	// comparacion = Verdadero 
	Escribir comparacion;
	comparacion = Verdadero O Falso;
	// comparacion = Verdadero
	Escribir comparacion;
	comparacion = Falso O Verdadero;
	// comparacion = Verdadero
	Escribir comparacion;
	comparacion = Falso O Falso;
	// comparacion = Falso
	Escribir comparacion;
	Escribir "";
	
	// Operador Lógico: NO
	Escribir "Operador Lógico NO";
	Escribir "";
	
	comparacion = NO Verdadero;
	// comparacion = Falso
	Escribir comparacion;
	
	comparacion = NO Falso;
	// comparacion = Verdadero
	Escribir comparacion;
	
	
FinAlgoritmo
