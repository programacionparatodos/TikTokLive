
// TODO: 617A - Elephant | Codeforces

package Ejercicio1;

// * Entrada
import java.util.Scanner;

public class Codeforces_617A {
    public static void main(String[] args) {
        
        // * Declaración de variables
        int x, pasos = 0;

        // * Entrada
        Scanner teclado = new Scanner(System.in);

        x = teclado.nextInt();

        // * Proceso
        pasos = (x + 4) / 5;

        // * Salida
        System.out.println(pasos);

        teclado.close();

    }
}