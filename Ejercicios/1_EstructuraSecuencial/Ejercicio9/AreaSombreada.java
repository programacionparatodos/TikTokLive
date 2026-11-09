package Ejercicio9;

// TODO: Área Sombreada

// * Entrada de datos
import java.util.Scanner;

public class AreaSombreada {
    public static void main(String[] args) {

        // * Entrada de datos
        Scanner teclado = new Scanner(System.in);
        double n = teclado.nextDouble();

        // * Proceso
        double area = n * n / 2;

        // * Salida
        System.out.println(area);

        teclado.close();

    }
}
