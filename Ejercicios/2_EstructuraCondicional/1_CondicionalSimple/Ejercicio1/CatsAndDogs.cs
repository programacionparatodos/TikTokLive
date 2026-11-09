
// TODO: AtCoder ABC094 A
// * Declaración de variables
int a, b, x;

// * Entrada de datos
string[] datos = Console.ReadLine()!.Split();

a = int.Parse(datos[0]);
b = int.Parse(datos[1]);
x = int.Parse(datos[2]);

// * Proceso
if (x >= a && x <= a + b) {
    // * Salida de datos
    Console.WriteLine("YES");
}

if (x < a || x > a + b) {
    // * Salida de datos
    Console.WriteLine("NO");
}