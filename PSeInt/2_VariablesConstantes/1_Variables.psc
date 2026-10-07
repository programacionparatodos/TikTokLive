Algoritmo Variables
	
	// -------------------
    // VARIABLES EN PSeInt
    // -------------------
	
    // Una variable es un espacio de
    // memoria identificado mediante
    // un nombre utilizado para
    // almacenar un dato
	
    // Su valor puede cambiar durante
    // la ejecución del algoritmo
	
	
    // ------------------------
    // DECLARACIÓN DE VARIABLES
    // ------------------------
	
    // En PSeInt utilizamos la palabra
    // reservada Definir
	
    Definir monedas Como Entero;
	
    // Definir     Palabra reservada
    // monedas     Nombre de la variable
    // Como        Palabra reservada
    // Entero      Tipo de dato
	
	
    // --------------------------
    // ASIGNACIÓN DE UNA VARIABLE
    // --------------------------
	
    monedas <- 150;
	
    // El símbolo <- representa
    // una ASIGNACIÓN
	
    Escribir monedas;
	
	
    // -------------------------------
    // MODIFICAR EL VALOR DE VARIABLES
    // -------------------------------
	
    monedas <- 275;
	
    Escribir monedas;
	
    // Inicialmente:      monedas -> 150
    // Posteriormente:    monedas -> 275
	
	
    // -----------------------
    // VARIABLES SEGÚN SU TIPO
    // -----------------------
	
    Definir vidas Como Entero;
    Definir temperatura Como Real;
    Definir rango Como Caracter;
    Definir planeta Como Cadena;
    Definir nave_activa Como Logico;
	
	
    // ---------------------
    // ASIGNACIÓN DE VALORES
    // ---------------------
	
    vidas <- 3;
    temperatura <- 25.5;
    rango <- 'S';
    planeta <- "Marte";
    nave_activa <- Verdadero;
	
	
    // -------------------
    // MOSTRAR LOS VALORES
    // -------------------
	
    Escribir vidas;
    Escribir temperatura;
    Escribir rango;
    Escribir planeta;
    Escribir nave_activa;
	
	
    // -----------------------------
    // REGLAS PARA NOMBRAR VARIABLES
    // -----------------------------
	
    // 1. Utilizar nombres claros
    // y descriptivos
	
    // edad
    // promedio
    // cantidad_estudiantes
	
	
    // Evitar nombres poco descriptivos
	
    // x
    // a
    // dato1
	
	
    // 2. NO utilizar espacios
	
    // cantidad estudiantes
	
    // cantidad_estudiantes
	
	
    // 3. NO comenzar con números
	
    // 2jugador
	
    // jugador2
	
	
    // 4. Evitar caracteres especiales
	
    // preci@final
    // nota-final
	
    // precio_final
    // nota_final
	
	
    // 5. Evitar palabras reservadas
	
    // Proceso
    // Si
    // Mientras
    // Definir
	
	
    // -----------------------
    // CONVENCIÓN DE ESCRITURA
    // -----------------------
	
    // PSeInt no nos obliga a utilizar
    // una convención específica
	
    // En nuestro curso utilizaremos
    // snake_case
	
    Definir cantidad_enemigos Como Entero;
    Definir distancia_recorrida Como Real;
    Definir escudo_activado Como Logico;
	
    // Las palabras se escriben
    // normalmente en minúsculas
	
    // Si tenemos varias palabras,
    // las separamos utilizando _
	
    // cantidad_enemigos
    // distancia_recorrida
    // escudo_activado
	
    // IMPORTANTE
    // snake_case será una convención
    // utilizada en nuestro curso
	
	
    // -------------------
    // TIPADO DE VARIABLES
    // -------------------
	
    // Cuando definimos una variable
    // indicamos el tipo de dato
    // que almacenará
	
    Definir puntos Como Entero;
	
    puntos <- 100;
    puntos <- 250;
	
    // Podemos cambiar su valor
    // manteniendo el tipo establecido

FinAlgoritmo
