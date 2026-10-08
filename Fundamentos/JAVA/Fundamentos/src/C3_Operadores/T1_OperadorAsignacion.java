public class T1_OperadorAsignacion {
    public static void main(String[] args) {
        
        // * ------------------------
        // * OPERADOR DE ASIGNACIÓN =
        // * ------------------------

        // ? El operador de asignación (=)
        // ? permite guardar un valor dentro
        // ? de una variable

        // * variable = valor;

        int cantidad = 5;
        double peso = 65.4;
        char vocal = 'e';
        String ciudad = "Lima";
        boolean esPrimavera = true;

        System.out.println("Valores de las variables: ");
        System.out.println(cantidad);
        System.out.println(peso);
        System.out.println(vocal);
        System.out.println(ciudad);
        System.out.println(esPrimavera);

        // ? También podemos asignar el resultado
        // ? de una expresión a una variable

        System.out.println("\nAsignación del resultado de una expresión: ");
        int resultado = 8 + 4; // 12
        System.out.println(resultado);

    }   
}