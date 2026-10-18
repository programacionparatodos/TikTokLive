public class T3_OperadoesRelacionales {
    public static void main(String[] args) {

        // * -----------------------
        // * OPERADORES RELACIONALES
        // * -----------------------

        // ? Permiten comparar dos valores

        // ? El resultado de una comparación
        // ? siempre es boolean (lógico)

        // * true       verdadero
        // * false      falso

        // * ==         Igual que
        // * !=         Diferente de
        // * >          Mayor que
        // * <          Menor que
        // * >=         Mayor o igual que
        // * <=         Menor o igual que

        // * OPERADOR IGUAL QUE ==

        // ? Conprueba si dos valores son iguales

        // * comparacion = boolean

        System.out.println("\nOperador Igual que: ");
        System.out.println(5 == 5);         // true
        System.out.println(5.0 == 8);       // fasle 
        System.out.println(5 == 5.0);       // true
        System.out.println(true == true);   // true
        System.out.println('a' == 'b');     // false

        // ! System.out.println("auto" == "auto");

        System.out.println("\nComparar si 2 String son iguales con equals: ");
        String nombre = "Nallely";
        System.out.println(nombre.equals("tapia")); // false

        // * OPERADOR DIFERENTE DE  !=

        // ? Comprueba si dos valores son diferentes

        // * comparacion = boolean (lógico)

        System.out.println("\nOperador Diferente de: ");
        System.out.println(5 != 5);         // false
        System.out.println(5.0 != 8);       // true 
        System.out.println(5 != 5.0);       // false
        System.out.println(true != true);   // false
        System.out.println('a' != 'b');     // true


        // ! System.out.println("auto" != "auto");

        System.out.println("\nComparar si 2 Strings son diferentes con equals: ");
        nombre = "Nallely";
        System.out.println(!nombre.equals("tapia")); // true

        // * OPERADOR MAYOR QUE >

        // ? Comprueba si el valor de la izquierda
        // ? es mayor que el de la derecha

        // * comparacion = boolean (lógico)

        System.out.println("\nOperador Mayor que: ");
        System.out.println(10 > 5);     // true
        System.out.println(3 > 8.5);    // false
        System.out.println(3.5 > 8.5);  // false

        // * OPERADOR MENOR QUE <

        // ? Comprueba si el valor de la izquierda
        // ? es menor que el de la derecha

        // * comparacion = boolean (lógico)

        System.out.println("\nOperador Menor que: ");
        System.out.println(10 < 5);     // false
        System.out.println(3 < 8.5);    // true
        System.out.println(3.5 < 8.5);  // true

        // * OPERADOR MAYOR O IGUAL QUE >=

        // ? Comprueba si un valor es mayor
        // ? o igual que otro

        // * comparacion = boolean (lógico)

        System.out.println("\nOperador Mayor o igual que: ");
        System.out.println(10 >= 5);     // true
        System.out.println(3 >= 8.5);    // false
        System.out.println(3.5 >= 8.5);  // false

        // * OPERADOR MENOR O IGUAL QUE <=

        // ? Comprueba si un valor es menor
        // ? o igual que otro

        // * comparacion = boolean (lógico)

        System.out.println("\nOperador Menor o igual que: ");
        System.out.println(10 <= 5);     // false
        System.out.println(3 <= 3);    // true
        System.out.println(3.5 <= 8.5);  // true

        // * int     con     int/double -> boolean
        // * double  con     int/double -> boolean
        // * char    con     char       -> boolean

        // * boolean == bool  ->  boolean
        // * boolean != bool  ->  boolean
        // ! INCORRECTO: true > false  
               
    }
}

