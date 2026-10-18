public class T2_OperadoresAritmeticos {
    public static void main(String[] args) {
        
        // * ----------------------
        // * OPERADORES ARITMÉTICOS
        // * ----------------------

        // ? Los operadores aritméticos permiten
        // ? realizar operaciones matemáticas

        // * suma:              +
        // * resta:             -
        // * multiplicación:    *
        // * división:          /
        // ! divisón entera     / int / int
        // * módulo:            %
        // ! potencia           Math.pow()

        // * OPERADOR SUMA  +

        // ? Permite sumar dos valores numéricos

        // * int + int          =   int
        // * int + double       =   double
        // * double + int       =   double
        // * double + double    =   double

        System.out.println("Operador Suma: ");
        System.out.println(2 + 7);      // 9
        System.out.println(6 + 2.5);    // 8.5
        System.out.println(5.2 + 3);    // 8.2
        System.out.println(6.3 + 8.2);  // 14.5

        // ? El operador + también permite
        // ? concatenar cadenas

        // * String + String = String
        System.out.println("\nConcatenación: String + String: ");
        System.out.println("Hola " + "Mundo");
        // Hola Mundo

        // * String + int = String
        System.out.println("\nConcatenación: String + int: ");
        System.out.println("Edad: " + 21);
        // Edad: 21

        // * OPERADOR RESTA  -

        // ? Permite restar un valor de otro

        // * int - int          =   int
        // * int - double       =   double
        // * double - int       =   double
        // * double - double    =   double

        System.out.println("\nOperador Resta: ");
        System.out.println(2 - 7);      // -5
        System.out.println(6 - 2.5);    // 3.5
        System.out.println(5.2 - 3);    // 2.2
        System.out.println(6.3 - 8.2);  // -1.9

        // * OPERADOR MULTIPLICACIÓN  *

        // ? Permite multiplicar dos valores

        // * int * int          =   int
        // * int * double       =   double
        // * double * int       =   double
        // * double * double    =   double

        System.out.println("\nOperador Multiplicación: ");
        System.out.println(2 * 7);      // 14
        System.out.println(6 * 2.5);    // 15
        System.out.println(5.2 * 3);    // 15.6
        System.out.println(6.3 * 8.2);  // 51.66

        // * OPERADOR DIVISIÓN  /

        // ? Permite dividir un valor entre otro

        // ! Si ambos operandos son enteros.
        // ! JAVA realiza DIVISIÓN ENTERA

        // * int / int          =   int
        // * int / double       =   double
        // * double / int       =   double
        // * double / double    =   double

        System.out.println("\nOperador División: ");
        System.err.println(10 / 2);         // 5
        System.out.println(10 / 4.0);       // 2.5
        System.err.println(10.0 / 4);       // 2.5
        System.out.println(10.0 / 4.0);     // 2.5

        // * OPERADOR MÓDULO  %

        // ? Devuelve el residuo de una división

        // * int % int          =   int
        // * int % double       =   double
        // * double % int       =   double
        // * double % double    =   double

        System.out.println("\nOperador Módulo: ");
        System.err.println(10 % 3);         // 1
        System.out.println(10 % 4.0);       // 2.0
        System.err.println(10.0 % 4);       // 2.0
        System.out.println(10.0 % 4.0);     // 2.0

        // * POTENCIA  Math.pow(base, exponente)

        // * No existe un operador para Potencia
        // ! System.out.println(2 ** 3);    ERROR

        // ! System.out.println(2 ^ 3);     XOR

        // ? Math.pow() permite elevar un número
        // ? a una determinada potencia

        // * Math.pow(int, int)         =   double
        // * Math.pow(int, double)      =   double
        // * Math.pow(double, int)      =   double
        // * Math.pow(double, double)   =   double

        System.out.println("\nPotencia con Math.pow(): ");
        System.out.println(Math.pow(2, 3));       // 8.0
        System.out.println(Math.pow(10.0, 3.0));  // 1000.0
    }

}
