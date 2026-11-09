// * Declaración de variables
byte a, b, c, suma;

// * Entrada de datos
string [] datos = Console.ReadLine()!.Split();
a = byte.Parse(datos[0]);
b = byte.Parse(datos[1]);
c = byte.Parse(datos[2]);

// * Proceso
suma = (byte)(21 - (a + b + c));

// * Salida de datos
Console.WriteLine(suma);