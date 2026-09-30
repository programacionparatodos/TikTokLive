
// TODO: Nuestro primer Hello World en C#
// Console.WriteLine("Hello, World!");
// Console.WriteLine("Desde Arch Linux!");
// Console.WriteLine("Con C# =)");

using System.Linq;

int[] vector = {34, 5, 15, 37, 7, 19, 57, 23};

int mayor = vector.Max();
int menor = vector.Min();

Console.WriteLine($"Mayor: {mayor}");
Console.WriteLine($"Menor: {menor}");