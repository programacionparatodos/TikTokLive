
// TODO: Count Balls - AtCoder

package Ejercicio6;

// * Entrada
import java.util.Scanner;

public class CountBalls_AtCoder {
    public static void main(String[] args) {
        
        // * Declaración de variables
        long n, a, b, t, g, z, r, e, azules;
        
        // * Entrada
        Scanner teclado = new Scanner(System.in);

        n = teclado.nextLong();
        a = teclado.nextLong();
        b = teclado.nextLong();

        // * Proceso
        t = a + b;
        g = n / t;
        z = g * a;
        r = n % t;
        e = (r + a - Math.abs(r - a)) / 2;
        azules = z + e;

        // * Salida
        System.out.println(azules);

        teclado.close();

    }
}
