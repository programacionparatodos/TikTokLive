// * ------------------------
// * ENTRADA DE DATOS EN JAVA
// * ------------------------

// * Importamos la clase Scanner
import java.util.Scanner;

public class Entrada {
    public static void main(String[] args) {
        // * Instanciamos el objeto teclado
        Scanner teclado = new Scanner(System.in);


        // TODO: ENTRADA INDIVIDUAL
        // ? Permite ingresar un dato desde teclado

        int numero;
        numero = teclado.nextInt();


        // TODO: ENTRADA MÚLTIPLE (LÍNEAS SEPARADAS)
        // ? Cada dato se ingresa por separado

        String animal; 
        int peso;
        double altura;

        animal = teclado.next();
        peso = teclado.nextInt();
        altura = teclado.nextDouble();


        // TODO: ENTRADA MÚLTIPLE (UNA SOLA LÍNEA)
        // ? Permite ingresar varios datos 
        // ? separados por espacios

        int dia, mes, anio;
        dia = teclado.nextInt();
        mes = teclado.nextInt();
        anio = teclado.nextInt();


        // TODO: ENTRADA CON MENSAJE
        // ? Muestra un mensaje antes de 
        // ? ingresar el dato

        String profesion;
        System.out.print("Ingrese su profesión: ");
        profesion = teclado.next();

        // TODO: ENTRADA DE TEXTO CON ESPACIOS
        // ? nextLine() permite leer una línea completa

        String direccion;

        teclado.nextLine();
        System.out.print("Ingrese su dirección: ");
        direccion = teclado.nextLine();

        // TODO: ENTRADA DE UN CARACTER
        // ? Java no tiene nextChar() en Scanner

        char respuesta;
        respuesta = teclado.next().charAt(0);

        // TODO: ENTRADA DE UN DATO LÓGICO
        // ? Permite ingresar true o false

        boolean disponible;
        disponible = teclado.nextBoolean();

        teclado.close();

    }
}