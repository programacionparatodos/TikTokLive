
// TODO: 486A - Calculating Function | Codeforces

package Ejercicio4;

// * Entrada
import java.util.Scanner;

public class Codeforces_486A {
    
    public static void main(String[] args) {
        
        // * Declaración de variables
        long n, fn;

        // * Entrada
        Scanner teclado = new Scanner(System.in);
        n = teclado.nextLong();

        // * Proceso
        fn = (n / 2) - (n % 2) * n; 

        // * Salida
        System.out.println(fn);

        teclado.close();

    }
}
