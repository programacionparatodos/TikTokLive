package C2_VariablesConstantes;

public class T2_Constantes {
    public static void main(String[] args) {
        
        // * ------------------
        // * CONSTANTES EN JAVA
        // * ------------------

        // ? Una constante representa un valor
        // ? que no queremos permitir que sea
        // ? reasignado después de inicializarlo

        // ? En Java utilizamos: final
        // * impide que una constante sea
        // * reasignada posteriormente

        // ? final + tipo + NOMBRE + valor

        final int MAXIMO_INTENTOS = 5;

        System.out.println(MAXIMO_INTENTOS);

        // ! No podemos cambiar su valor
        // MAXIMO_INTENTOS = 10;

        // ! Generará un error de compilación

        // * ---------------------------
        // * CONVENSIÓN UPPER_SNAKE_CASE
        // * ---------------------------

        final double DISTANCIA_MAXIMA = 15000.75;

        // ? Todas las letras en MAYÚSCULAS
        // ? separadas por _ cada palabra
    }
}
