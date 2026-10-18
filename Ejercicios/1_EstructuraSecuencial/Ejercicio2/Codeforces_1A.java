package Ejercicio2;

// * Entrada de datos
import java.util.Scanner;

public class Codeforces_1A {
    public static void main(String[] args) {
        
        // * Declaración de variables
        long n, m, a, fil, col, total; 

        // * Entrada de datos
        Scanner teclado = new Scanner(System.in);
        n = teclado.nextLong();
        m = teclado.nextLong();
        a = teclado.nextLong();

        // * Proceso
        col = (n + a - 1) / a;
        fil = (m + a - 1) / a;
        total = col * fil;

        // * Salida de datos
        System.out.println(total);

        teclado.close();
    }
}
