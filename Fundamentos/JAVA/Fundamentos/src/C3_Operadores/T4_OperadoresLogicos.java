public class T4_OperadoresLogicos {
    public static void main(String[] args) {
    
        // * ------------------
        // * OPERADORES LÓGICOS
        // * ------------------

        // * &&     Y lógico
        // * ||     O lógico
        // * !      Negación

        // * OPERADOR LÓGICO    &&

        // ? Devuelve true solamente cuando
        // ? AMBAS condiciones son VERDADERAS

        // * boolean && boolean = boolean

        System.out.println("Operador Lógico Y: ");
        System.out.println(true && true);       // true
        System.out.println(true && false);      // false
        System.out.println(false && true);      // false      
        System.out.println(false && false);     // false

        System.out.println("\nOperador Lógico Y en Expresiones: ");
        System.out.println(10 > 5 && 8 > 3); // true
        //                   true && true       

        System.out.println(10 > 5 && 8 < 3); // false
        //                   true && false

        // * OPERADOR LÓGICO    ||

        // ? Devuelve true cuando AL MENOS
        // ? una de las condiciones es VERDADERA

        // * boolean || boolean = boolean

        System.out.println("\nOperador Lógico O: ");
        System.out.println(true || true);       // true
        System.out.println(true || false);      // true
        System.out.println(false || true);      // true  
        System.out.println(false || false);     // false

        System.out.println("\nOperador Lógico O en Expresiones: ");
        System.out.println(10 > 5 || 8 > 3); // true
        //                   true || true       

        System.out.println(10 > 5 || 8 < 3); // true
        //                   true || false

        // * OPERADOR LÓGICO    !

        // ? Invierte el valor lógico
        // ? de una expresión

        // * !boolean = boolean

        System.out.println("\nOperador Lógico NO: ");
        System.out.println(!true);      // false
        System.out.println(!false);     // true

        System.out.println("\nOperador Lógico NO en Expresiones: ");
        System.out.println(!(10 > 5));  // false
        // *               !true
        System.out.println(!(10 < 5));  // true
        // *               !false

    }
}
