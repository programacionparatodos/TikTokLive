
// * ----------------------
// * OPERADORES ARITMÉTICOS
// * ----------------------

// ? Permiten realizar operaciones
// ? matemáticas con valores numéricos


// * OPERADOR SUMA  +

// ? Permite sumar dos valores numéricos

// * int + int          = int
// * int + float        = float
// * float + int        = float
// * float + float      = float
// * int + double       = double
// * double + int       = double
// * double + double    = double

Console.WriteLine("Operador Suma: ");
Console.WriteLine(14 + 27);         // 41
Console.WriteLine(12 + 3.5f);       // 15.5 
Console.WriteLine(6.25f + 8);       // 14.25
Console.WriteLine(4.5f + 2.25f);    // 6.75
Console.WriteLine(18 + 7.75);       // 25.75
Console.WriteLine(9.5 + 12);        // 21.5
Console.WriteLine(6.75 + 3.25);     // 10

// * CONCATENACIÓN DE CADENAS   +

// ? Permite unir cadenas de texto
// ? También puede concatenar una cadena
// ? con valores de otros tipos

// * string + string = string
// * string + int = string

Console.WriteLine("\nConcatenación: string + string");
Console.WriteLine("Curso de " + "C#");
// Curso de C#

Console.WriteLine("\nConcatenación: string + int");
Console.WriteLine("Grupo: " + 1);
// Grupo: 1


// * OPERADOR RESTA  -

// ? Permite calcular la diferencia
// ? entre dos valores numéricos

// * int - int          = int
// * int - float        = float
// * float - int        = float
// * float - float      = float
// * int - double       = double
// * double - int       = double
// * double - double    = double

Console.WriteLine("\nOperador Resta: ");
Console.WriteLine(48 - 19);         // 29
Console.WriteLine(35 - 6.5f);       // 28.5 
Console.WriteLine(22.75f - 11);     // 11.75
Console.WriteLine(16.5f - 4.25f);   // 12.25
Console.WriteLine(50 - 12.75);      // 37.25
Console.WriteLine(28.5 - 14);       // 14.5
Console.WriteLine(19.75 - 6.25);    // 13.5


// * OPERADOR MULTIPLICACIÓN  *

// ? Permite calcular el producto
// ? de dos valores numéricos

// * int * int          = int
// * int * float        = float
// * float * int        = float
// * float * float      = float
// * int * double       = double
// * double * int       = double
// * double * double    = double

Console.WriteLine("\nOperador Multiplicación: ");
Console.WriteLine(7 * 9);         // 63
Console.WriteLine(6 * 1.5f);      // 9 
Console.WriteLine(3.25f * 4);     // 13
Console.WriteLine(2.5f * 1.5f);   // 3.75
Console.WriteLine(8 * 2.75);      // 22
Console.WriteLine(4.5 * 6);       // 27
Console.WriteLine(1.25 * 3.5);    // 4.375


// * OPERADOR DIVISIÓN  /

// ? Permite dividir un valor entre otro

// ? Si ambos operadores son enteros,
// ? se descarta la parte decimal

// ? Si uno es float o double, el resultado
// ? es del tipo decimal correspondiente

// * int / int          = int
// * int / float        = float
// * float / int        = float
// * float / float      = float
// * int / double       = double
// * double / int       = double
// * double / double    = double

Console.WriteLine("\nOperador División: ");
Console.WriteLine(84 / 7);          // 12
Console.WriteLine(45 / 2.0f);       // 22.5
Console.WriteLine(37.5f / 3);       // 12.5
Console.WriteLine(18.0f / 4.0f);    // 4.5
Console.WriteLine(63 / 2.0);        // 31.5
Console.WriteLine(52.5 / 7);        // 7.5
Console.WriteLine(22.5 / 2.5);      // 9


// * OPERADOR MÓDULO  %

// ? Permite obtener el residuo
// ? de una división

// * int % int          = int
// * int % float        = float
// * float % int        = float
// * float % float      = float
// * int % double       = double
// * double % int       = double
// * double % double    = double

Console.WriteLine("\nOperador Módulo: ");
Console.WriteLine(23 % 6);      // 5
Console.WriteLine(37 % 8);      // 5 
Console.WriteLine(42 % 7);      // 0
Console.WriteLine(17.5f % 4);   // 1.5
Console.WriteLine(29 % 4.0f);   // 1
Console.WriteLine(18.5 % 6.0);  // 0.5
Console.WriteLine(27 % 4.5);    // 0


// * POTENCIA CON Math.Pow()

// ? Permite delevar una base a un exponente

// ? C# no tiene un operador ** como Python
// ? Utilizamos el método Math.Pow()

// ? El resultado de Math.Pow()
// ? siempre es double

// * Math.Pow(double, double) = double

Console.WriteLine("\nPotencia con Math.Pow(): ");
Console.WriteLine(Math.Pow(3, 4));      // 81
Console.WriteLine(Math.Pow(6, 2));      // 36
Console.WriteLine(Math.Pow(4, 3));      // 64
Console.WriteLine(Math.Pow(9, 0.5));    // 3
Console.WriteLine(Math.Pow(16, 1.5));   // 64