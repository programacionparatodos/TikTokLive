
// * ----------------------
// * ENTRADA DE DATOS EN C#
// * ----------------------

// ? En C# utilizamos principalmente:
// * Console.ReadLine()     Leer
// ? para recibir información por teclado

// TODO: ENTRADA INDIVIDUAL
// ? Permite ingresar un dato desde teclado
string nombre;
nombre = Console.ReadLine()!;

// ? También podemos declarar y leer directamente
// string nombre = Console.ReadLine();


// TODO: ENTRADA MÚLTIPLE (Líneas Separadas)
// ? Cada dato se ingresa en una línea diferente

string usuario;
int edad;
double salario;

// ! Console.ReadLine() recibe texto

usuario = Console.ReadLine()!;

// ? int.Parse() convierte texto a entero
edad = int.Parse(Console.ReadLine()!);

// ? double.Parse() convierte texto a real
salario = double.Parse(Console.ReadLine()!);


// TODO: ENTRADA MÚLTIPLE (Una sola línea)
// ? Permite ingresar varios valores separados
// ? por espacios

string[] datos = Console.ReadLine()!.Split();
// * 5 10 30
//  5 posicion 0
// 10 posicion 1
// 30 posicion 2
int a = int.Parse(datos[0]);
int b = int.Parse(datos[1]);
int c = int.Parse(datos[2]); 


// TODO: ENTRADA CON MENSAJE
// ? Muestra un mensaje antes de ingresar
// ? un dato

Console.Write("Ingrese su país de nacimiento: ");
string pais = Console.ReadLine()!;