// * ---------------
// * VARIABLES EN C#
// * ---------------

// ? Una variable es un espacio de memoria
// ? identificado mediante un nombre 
// ? utilizado para almacenar un dato

// * Su valor puede cambiar durante
// * la ejecución del programa

// * ------------------------
// * DECLARACIÓN DE VARIABLES
// * ------------------------

// ? Podemos indicar explicitamente
// ? el TIPO DE DATO de la variable

// * int:       Tipo de Dato

int numero;
// * numero     Nombre de la variable

int edad;
// * edad       Nombre de la variable

// * --------------------------
// * ASIGNACIÓN DE UNA VARIABLE
// * --------------------------

numero = 20;
edad = 25;

// * El simbolo = representa una
// * ASIGNACIÓN

Console.WriteLine(numero);
Console.WriteLine(edad);

// * -------------------------------
// * MODIFICAR EL VALOR DE VARIABLES
// * -------------------------------

edad = 30;
Console.WriteLine(edad);

// * Inicialmente:      edad -> 25
// * Posteriormente:    edad -> 30

// * ---------------------------
// * INICIALIZACIÓN DE VARIABLES
// * ---------------------------

// ? Podemos declarar una variable y
// ? darle su primer valor inmediatamente

double precio = 199.99;

sbyte temperatura = -15;
byte vidas = 3;

short altitud = 3700;
ushort energia = 60000;

float velocidad = 35.5F;
decimal saldo = 1250.75M;

char rango = 'M';
string planeta = "Jupiter";

bool estaConHambre = true;

// * -----------------------------
// * REGLAS PARA NOMBRAR VARIABLES
// * -----------------------------

// * 1. Puede comenzar con una letra
// * o guión bajo _

// ?    energia     _energia

// * 2. Depués puede contener letras, 
// * números y guión bajo _

// ?    jugador2     energia_01

// ! 3. NO puede comenzar con un número

// ?    2jugador    10nivel

// ! 4. NO puede contener espacios

// ?    puntos jugador

// ! 5. NO podemos utilizar símbolos
// ! arbitrarios

// ?    usuari@     nivel-final

// * 6. Diferencia MAYÚSCULAS/minúsculas

int puntos = 3;
int Puntos = 2;
int PUNTOS = 6;

// ? Son variables diferentes

// ! 7. NO podemos utilizar palabras
// ! reservadas directamente

// ?    int   class   while   return

// * --------------------
// * CONVENCIÓN camelCase
// * --------------------

// ? En C# utilizaremos normalmente
// ? camelCase para variables locales

int cantidadEnemigos = 10;
double distanciaRecorrida = 456.789;
bool escudoActivado = false;

// ? La primera palabra comienza
// ? completamente en minúsculas

// ? Las siguientes palabras comienzan
// ? con la primera letra en MAYÚSCULA

// ! IMPORTANTE
// * camelCase es una convención,
// * no una OBLIGACIÓN

// * ---------------
// * TIPADO ESTÁTICO
// * ---------------

int temperaturaMotor = 90;
temperaturaMotor = 150;

// * Seguimos trabajando con int

// temperaturaMotor = "caliente";

// ! No podemos cambiar libremente
// ! el tipo de la variable

// * ------------------------
// * INFERENCIA DE TIPO - var
// * ------------------------

// ? C# puede determinar automáticamente
// ? el tipo a partir del valor inicial

var combustible = 75;
var piloto = "Don Mauro";

// ? combustible -> int
// ? piloto      -> stringM

// ! var NO significa que la variable
// ! pueda cambiar libremente de tipo

combustible = 50;
// ! continua siendo int

// combustible = "lleno";