package C2_VariablesConstantes;

public class T1_Variables {
    public static void main(String[] args) {
        
        // * -----------------
        // * VARIABLES EN JAVA
        // * -----------------

        // ? Una variable es un espacio de
        // ? memoria identificado mediante
        // ? un nombre utilizado para
        // ? almacenar un dato

        // * Su valor puede cambiar durante
        // * la ejecución del programa

        // * ------------------------
        // * DECLARACIÓN DE VARIABLES
        // * ------------------------

        // ? En Java debemos indicar el 
        // ? TIPO DE DATO de la variable

        int monedas;

        // * int        Tipo de dato
        // * monedas    Nombre de la variable

        // * ---------------------------
        // * ASIGNACIÓN DE UNA VARIABLES
        // * ---------------------------

        monedas = 150;

        // * El símbolo = representa una
        // * ASIGNACIÓN

        System.out.println(monedas);

        // * -------------------------------
        // * MODIFICAR EL VALOR DE VARIABLES
        // * -------------------------------

        monedas = 275;

        System.out.println(monedas);

        // * Inicialmente:      monedas -> 150
        // * Posteriormente:    monedas -> 275

        // * ---------------------------
        // * INICIALIZACIÓN DE VARIABLES
        // * ---------------------------

        // ? Podemos declarar una variable y
        // ? darle su primer valor inmediatamente

        int bateria = 85;

        // * --------------------------
        // * INICIALIZACIÓN TIPOS DATOS
        // * --------------------------

        byte vidas = 3;
        short altitud = 3700;
        int experiencia = 125000;
        long estrellas = 8000000000L;
        float velocidad = 35.5F;
        double coordenada = 125.7589;
        char rango = 'S';
        String planeta = "Marte";
        boolean nave_activa = true;

        // * -----------------------------
        // * REGLAS PARA NOMBRAR VARIABLES
        // * -----------------------------

        // * 1. Puede comenzar con una letra,
        // *    quión bajo _ o signo $   

        // ? energia    _energia    $energia

        // ! IMPORTANTE
        // * Aunque $ esta permitido,
        // * NO se lo recomienda

        // * 2. Después puede contener letras,
        // * números, _ y $

        // ? jugador2   energia_01

        // ! 3. NO puede comenzar con un número
        // ? 2jugador       10nivel

        // ! 4. NO puede contener espacios
        // ? puntos jugador

        // ! 5. NO podemos utilizar otros
        // ! símbolos arbitrarios
        // ? usuari@    nivel-final

        // * 6. Diferencia MAYÚSCULAS/minúsculas

        int puntos = 10;
        int Puntos = 20;
        int PUNTOS = 30;

        // ? Son variables diferentes

        // ! 7. No podemos utilizar palabras
        // ! reservadas

        // ? int    class   while    return

        // * --------------------
        // * CONVENSIÓN camelCase
        // * --------------------

        // ? En Java utilizaremos normalmente
        // ? camelCase para las variables

        int cantidadEnemigos = 12;
        double distanciaRecorrida = 456.789;
        boolean escudoActivado = true;

        // ? La primera palabra comienza en
        // ? minúsculas

        // ? Las siguientes palabras comienzan
        // ? la primera letra en MAYÚSCULAS

        // ! IMPORTANTE
        // * camelCase es una convención,
        // * no una obligación

        // * ---------------
        // * TIPADO ESTÁTICO
        // * ---------------

        int temperaturaMotor = 90;
        temperaturaMotor = 105;

        // * seguimos trabajando con int

        // temperaturaMotor = "caliente";

        // ! No podemos cambiar libremente
        // ! el tipo de la variable

        // * El tipo de dato se establece
        // * al declarar la variable
        // ! NO puede cambiar después

    }
}
