
// TODO: AtCoder ABC094 A

// * Entrada de datos
import java.util.Scanner;

public class CatsAndDogs {
    public static void main(String[] args) {
        
        // * Declaración de variables
        int a, b, x;

        // * Entrada de datos
        Scanner teclado = new Scanner(System.in);

        a = teclado.nextInt();
        b = teclado.nextInt();
        x = teclado.nextInt();

        // * Proceso
        if (x >= a && x <= a + b) {
            // * Salida de datos
            System.out.println("YES");
        }

        if (x < a || x > a + b) {
            // * Salida de datos
            System.out.println("NO");
        }        

        teclado.close();
        
    }
}
