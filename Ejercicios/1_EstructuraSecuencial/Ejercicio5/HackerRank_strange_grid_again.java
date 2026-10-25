
// TODO: Strange Grid Again - HackerRank

package Ejercicio5;

// * Entrada
import java.util.Scanner;

public class HackerRank_strange_grid_again {
    public static void main(String[] args) {
        
        // * Declaración de variables
        long r, c, grupo, posicion, desplazamiento;

        // * Entrada
        Scanner teclado = new Scanner(System.in);
        r = teclado.nextLong();
        c = teclado.nextLong();

        // * Proceso
        grupo = (r - 1) / 2;
        long inicio = grupo * 10;
        posicion = (r - 1) % 2;
        desplazamiento = 2 * (c - 1);
        long resultado = inicio + posicion + desplazamiento;

        // * Salida
        System.out.println(resultado);

        teclado.close();
    }
}
