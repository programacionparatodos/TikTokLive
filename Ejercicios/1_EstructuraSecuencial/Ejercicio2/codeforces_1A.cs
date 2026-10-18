
// * Declaración de variables
long n, m, a, fil, col, total;

// * Entrada de datos
string [] datos = Console.ReadLine()!.Split();
n = long.Parse(datos[0]);
m = long.Parse(datos[1]);
a = long.Parse(datos[2]);

// * Proceso
col = (n + a - 1) / a;
fil = (m + a - 1) / a;
total = col * fil;

// * Salida de datos
Console.WriteLine(total);