

 // * ---------------------------------
 // * OPERADORES RELACIONALES
 // * ---------------------------------

 // ? Permiten comparar dos valores.
 // ? El resultado siempre es bool.

 // * true
 // * false


 // * OPERADOR IGUAL QUE ==

 // ? Comprueba si dos valores son iguales.

 // * int == int       = bool
 // * int == double    = bool
 // * double == double = bool
 // * char == char     = bool
 // * bool == bool     = bool
 // * string == string = bool

 Console.WriteLine(17 == 17);           // True
 Console.WriteLine(24 == 31);           // False
 Console.WriteLine(12 == 12.0);         // True
 Console.WriteLine('M' == 'M');         // True
 Console.WriteLine(false == true);      // False
 Console.WriteLine("C#" == "C#");       // True


 // * OPERADOR DIFERENTE DE !=

 // ? Comprueba si dos valores
 // ? son diferentes.

 // * int != int       = bool
 // * int != double    = bool
 // * double != double = bool
 // * char != char     = bool
 // * bool != bool     = bool
 // * string != string = bool

 Console.WriteLine(26 != 18);           // True
 Console.WriteLine(42 != 42);           // False
 Console.WriteLine(7.5 != 9);           // True
 Console.WriteLine('X' != 'Z');         // True
 Console.WriteLine("Sol" != "Luna");    // True


 // * OPERADOR MAYOR QUE >

 // ? Comprueba si el valor de la izquierda
 // ? es mayor que el de la derecha.

 // * int > int       = bool
 // * int > double    = bool
 // * double > int    = bool
 // * double > double = bool
 // * char > char     = bool

 Console.WriteLine(56 > 23);            // True
 Console.WriteLine(14 > 39);            // False
 Console.WriteLine(18.75 > 12);         // True
 Console.WriteLine('Z' > 'K');          // True


 // * OPERADOR MENOR QUE <

 // ? Comprueba si el valor de la izquierda
 // ? es menor que el de la derecha.

 // * int < int       = bool
 // * int < double    = bool
 // * double < int    = bool
 // * double < double = bool
 // * char < char     = bool

 Console.WriteLine(16 < 47);            // True
 Console.WriteLine(63 < 28);            // False
 Console.WriteLine(14.25 < 19);         // True
 Console.WriteLine('C' < 'H');          // True


 // * OPERADOR MAYOR O IGUAL QUE >=

 // ? Comprueba si un valor es mayor
 // ? o igual que otro.

 // * int >= int       = bool
 // * int >= double    = bool
 // * double >= double = bool
 // * char >= char     = bool

 Console.WriteLine(75 >= 42);           // True
 Console.WriteLine(36 >= 36);           // True
 Console.WriteLine(21 >= 49);           // False
 Console.WriteLine(18.5 >= 18.5);       // True


 // * OPERADOR MENOR O IGUAL QUE <=

 // ? Comprueba si un valor es menor
 // ? o igual que otro.

 // * int <= int       = bool
 // * int <= double    = bool
 // * double <= double = bool
 // * char <= char     = bool

 Console.WriteLine(27 <= 58);           // True
 Console.WriteLine(44 <= 44);           // True
 Console.WriteLine(82 <= 35);           // False
 Console.WriteLine(12.75 <= 15.5);      // True