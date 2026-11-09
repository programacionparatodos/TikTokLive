package Ejercicio8;

//TODO: Three Dice | AtCoder

// * Entrada de datos
import java.util.Scanner;

public class ThreeDice_AtCoder {
    public static void main(String[] args) {
        
        // * Declaración de variables
        byte a, b, c, suma;

        // * Entrada de datos
        Scanner teclado = new Scanner(System.in);
        a = teclado.nextByte();
        b = teclado.nextByte();
        c = teclado.nextByte();

        // * Proceso
        suma = (byte)(21 - (a + b + c));

        // * Salida de datos
        System.out.println(suma);

        teclado.close();

    }
}