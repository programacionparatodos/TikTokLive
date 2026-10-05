// * ---------------------------
// * TIPOS DE DATOS ENTERO EN C#
// * ---------------------------

// ? Los números enteros no contienen
// ? PARTE DECIMAL
// ? postivos, negativos o cero

// ? C# dispone de diferentes tipos 
// ? enteros según el rango de valores
// ? que necesitemos almacenar

// * -------------------------------
// * TIPOS DE DATOS ENTERO CON SIGNO
// * -------------------------------

// * sbyte
// ? 8 bits
// ? -128 hasta 127

Console.WriteLine("sbyte");
Console.WriteLine((sbyte)100);
Console.WriteLine((sbyte)-50);

// * short
// ? 16 bits
// ? -32768 hasta 32767

Console.WriteLine("short");
Console.WriteLine((short)25000);
Console.WriteLine((short)-15000);

// * int
// ? 32 bits
// ? -2147483648 hasta 2147483647

Console.WriteLine("int");
Console.WriteLine(150000);
Console.WriteLine(-850000);

// ! int es el tipo entero utilizado
// ! habitualmente en C#

// * long
// ? 64 bits
// ? Permite representar números
// ? enteros muchos más grandes

Console.WriteLine("long");
Console.WriteLine(80000000000L);
Console.WriteLine(-50000000000L);

// * -------------------------------
// * TIPOS DE DATOS ENTERO SIN SIGNO
// * -------------------------------

// ? No representan números negativos y
// ? permiten amplicar el rango positivo

// * byte
// ? 8 bits
// ? 0 hasta 255

Console.WriteLine("byte");
Console.WriteLine((byte)200);

// * ushort
// ? 16 bits
// ? 0 hasta 65535

Console.WriteLine("ushort");
Console.WriteLine((ushort)60000);

// * uint
// ? 32 bits
// ? 0 hasta 4294967295

Console.WriteLine("uint");
Console.WriteLine((uint)3000000000U);

// * ulong
// ? 64 bits
// ? permite representar valores
// ? positivos extremadamente grandes

Console.WriteLine("ulong");
Console.WriteLine(150000000000UL);

// * -------------------------
// * VERIFICAR EL TIPO DE DATO
// * -------------------------

// ? GetType() permite conocer el tipo
// ? de un valor durante la ejecución

Console.WriteLine(25.GetType());
Console.WriteLine(8000000000L.GetType());
Console.WriteLine(3000000000U.GetType());