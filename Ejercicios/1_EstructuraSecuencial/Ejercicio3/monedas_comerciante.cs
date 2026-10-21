
// TODO: Monedas Comerciante

// * Declaración de variables
int N, C, B;   
int cofres, resto, bolsas, sobrantes;

// * Entrada
string[] datos = Console.ReadLine()!.Split();
N = int.Parse(datos[0]);
C = int.Parse(datos[1]);
B = int.Parse(datos[2]);

// * Proceso
cofres = N / C;
resto = N % C;
bolsas = resto / B;
sobrantes = resto % B;

// * Salida
Console.WriteLine(cofres);
Console.WriteLine(bolsas);
Console.WriteLine(sobrantes);