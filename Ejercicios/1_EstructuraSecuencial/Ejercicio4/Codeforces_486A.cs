
// TODO: 486A - Calculating Function | Codeforces

// * Declaración de variables
long n, fn;

// * Entrada
n = long.Parse(Console.ReadLine()!);

// * Proceso
fn = (n / 2) - (n % 2) * n;

// * Salida
Console.WriteLine(fn);