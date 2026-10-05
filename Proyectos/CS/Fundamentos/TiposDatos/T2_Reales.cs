// * ---------------------------
// * TIPOS DE DATOS REALES EN C#
// * ---------------------------

// ? Representan números que pueden
// ? contener una PARTE DECIMAL

// * float, double, decimal

// * -------------------------
// * TIPOS DE DATOS REAL float
// * -------------------------

// ? Precisión aproximada
// ? 6 a 9 dígitos

Console.WriteLine("\nfloat");
Console.WriteLine(35.5F);
Console.WriteLine(-12.75F);

// * --------------------------
// * TIPOS DE DATOS REAL double
// * --------------------------

// ? Precisión aproximada
// ? 15 a 17 dígitos

Console.WriteLine("\ndouble");
Console.WriteLine(125.7589);
Console.WriteLine(-987.123456);

// * ---------------------------
// * TIPOS DE DATOS REAL decimal
// * ---------------------------

// ? Ofrece una mayor precisión
// ? decimal que float y double

Console.WriteLine("\ndecimal");
Console.WriteLine(1250.75M);
Console.WriteLine(99.99M);

// * -------------------------
// * VERIFICAR EL TIPO DE DATO
// * -------------------------

Console.WriteLine(35.5F.GetType());
Console.WriteLine(35.5.GetType());
Console.WriteLine(35.5M.GetType());