
// TODO: Monedas Comerciante

package Ejercicio3;

import java.util.Scanner;

public class MonedasComerciante {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        // * Declaración de variables
        int N, C, B;   
        int cofres, resto, bolsas, sobrantes;

        // * Entrada
        N = teclado.nextInt();
        C = teclado.nextInt();
        B = teclado.nextInt();

        // * Proceso
        cofres = N / C;
        resto = N % C;
        bolsas = resto / B;
        sobrantes = resto % B;

        // * Salida
        System.out.println(cofres);
        System.out.println(bolsas);
        System.out.println(sobrantes);

        teclado.close();

    }
}
