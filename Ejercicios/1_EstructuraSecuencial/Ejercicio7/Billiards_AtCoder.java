
// TODO: Billiards | AtCoder

package Ejercicio7;

// * Entrada de datos
import java.util.Scanner;

public class Billiards_AtCoder {
    public static void main(String[] args) {
        
        // * Declaración de variables
        int Sx, Sy, Gx, Gy;
        double x;

        // * Entrada de datos
        Scanner teclado = new Scanner(System.in);

        Sx = teclado.nextInt();
        Sy = teclado.nextInt();
        Gx = teclado.nextInt();
        Gy = teclado.nextInt();

        // * Proceso
        x = (Sx * Gy + Sy * Gx) / (double)(Gy + Sy);
        
        // * Salida de datos
        System.out.printf("%.10f%n", x);

        teclado.close();
    }
}