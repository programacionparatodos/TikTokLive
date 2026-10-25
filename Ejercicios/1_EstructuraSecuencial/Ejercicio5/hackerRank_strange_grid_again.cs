
// TODO: Strange Grid Again - HackerRank

// * Declaración de variables
long r, c, grupo, posicion, desplazamiento;
long inicio, resultado;

// * Entrada
string [] datos = Console.ReadLine()!.Split();
// ? Console.ReadLine()!   "7 2"
// ? .Split()   "7 2"   ->   "7" "2"
// *                          0   1  

r = long.Parse(datos[0]); //* "7"  ->  7
c = long.Parse(datos[1]); //* "2"  ->  2

// * Proceso
grupo = (r - 1) / 2;
inicio = grupo * 10;
posicion = (r - 1) % 2;
desplazamiento = 2 * (c - 1);
resultado = inicio + posicion + desplazamiento;

// * Salida
Console.WriteLine(resultado);