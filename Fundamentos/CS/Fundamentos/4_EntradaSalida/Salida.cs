
// * ---------------------
// * SALIDA DE DATOS EN C#
// * ---------------------

// ? En C# utilizamos principalmente:
// * Console.WriteLine()     Escribir
// ? para mostrar información por consola

// TODO: SALIDA DE TEXTO
// ? Permite mostrar un mensaje por consola
// ! El mensaje debe ir entre comillas dobles

Console.WriteLine("Hello baby!");


// TODO: SALIDA DEL VALOR DE UNA VARIABLE
// ? Muestra el contenido de una variable

string nombre = "Yasmin Gonzalez";
Console.WriteLine(nombre);


// TODO: CONCATENACIÓN DE TEXTO Y VARIABLE
string usuario = "Daniel_P";
Console.WriteLine("Muchas gracias " + usuario);

// * Otra forma: Interpolación de cadenas
Console.WriteLine($"Te agradecemos {usuario}");

// * Otra forma: String index params
Console.WriteLine("{0} Como estas?", usuario);


// TODO: SALIDA DE VARIOS ELEMENTOS
// ? Muestra varios valores separados
// ? por espacios

int valor1 = 10;
int valor2 = 20;

// * Otra forma: concatenación
Console.WriteLine(valor1 + " " + valor2);

// * Otra forma: interpolación
Console.WriteLine($"{valor1} {valor2}");

// * Otra forma: String index params
Console.WriteLine("{0} {1}", valor1, valor2);


// TODO: USO DE SALTOS DE LÍNEA
// ? Muestra mensajes en líneas diferentes

Console.WriteLine("Primera línea");
Console.WriteLine("Segunda línea");

Console.Write("Primera línea");
Console.Write("\nSegunda línea\n");


// TODO: SALIDA DE UN RESULTADO
// ? Muestra el resultado de una operación

double num1 = 2.5;
double num2 = 5.0;
double num3 = -2.7;

Console.WriteLine((num1 - num3) * num2);