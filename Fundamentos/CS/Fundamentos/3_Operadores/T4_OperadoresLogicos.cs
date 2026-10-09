

 // * ---------------------------------
 // * OPERADORES LÓGICOS
 // * ---------------------------------

 // ? Permiten combinar o negar
 // ? expresiones lógicas.

 // * &&    AND
 // * ||    OR
 // * !     NOT


 // * OPERADOR LÓGICO AND &&

 // ? Devuelve true únicamente cuando
 // ? ambas condiciones son verdaderas.

 // * bool && bool = bool

 Console.WriteLine(true && true);     // True
 Console.WriteLine(true && false);    // False
 Console.WriteLine(false && true);    // False
 Console.WriteLine(false && false);   // False


 // * EJEMPLOS CON COMPARACIONES

 Console.WriteLine(25 >= 18 && 40 < 60);  // True
 Console.WriteLine(72 > 50 && 15 > 30);   // False
 Console.WriteLine(12 < 5 && 80 >= 40);   // False
 Console.WriteLine(34 != 34 && 7 > 20);   // False


 // * OPERADOR LÓGICO OR ||

 // ? Devuelve true cuando al menos
 // ? una condición es verdadera.

 // * bool || bool = bool

 Console.WriteLine(true || true);     // True
 Console.WriteLine(true || false);    // True
 Console.WriteLine(false || true);    // True
 Console.WriteLine(false || false);   // False


 // * EJEMPLOS CON COMPARACIONES

 Console.WriteLine(45 > 30 || 12 > 50);   // True
 Console.WriteLine(18 < 9 || 64 == 64);   // True
 Console.WriteLine(23 > 70 || 15 < 8);    // False
 Console.WriteLine(90 <= 90 || 7 == 2);   // True


 // * OPERADOR LÓGICO NOT !

 // ? Invierte el valor lógico
 // ? de una condición.

 // * !bool = bool

 Console.WriteLine(!true);     // False
 Console.WriteLine(!false);    // True


 // * EJEMPLOS CON COMPARACIONES

 Console.WriteLine(!(45 >= 20));    // False
 Console.WriteLine(!(17 == 28));    // True
 Console.WriteLine(!(63 < 40));     // True
 Console.WriteLine(!(12 != 12));    // True
