// * -----------------------
// * SALIDA DE DATOS EN JAVA
// * -----------------------

public class Salida {

    public static void main(String[] args) {
        
        // TODO: SALIDA DE TEXTO
        // ? Permite mostrar mensajes por consola

        System.out.println("Aprendiendo Java desde cero");


        // TODO: SALIDA DEL VALOR DE UNA VARIABLE

        int visitantes = 231;
        System.out.println(visitantes);


        // TODO: CONCATENACIÓN DE TEXTO Y VARIABLE
        // ? Combina texto con el valor de una variable

        String pais = "Bolivia";
        System.out.println("País: " + pais);

        
        // TODO: SALIDA DE VARIOS ELEMENTOS
        // ? Muestra varios valores en una misma línea

        int filas = 6;
        int columnas = 9;

        System.out.println(filas + " " + columnas);

        
        // TODO: USO DE SALTOS DE LÍNEA
        // ? Permite mostrar mensajes en líneas diferentes
        System.out.println("Inicio del programa");
        System.out.print("Fin del programa\n");
        System.out.print("Otra línea\n");


        // TODO: SALIDA DE UNA OPERACIÓN
        // ? Muestra directamente el resultado de
        // ? una operación

        int base = 8;
        int altura = 5;

        System.out.println((base * altura) / 2);
    }
    
}
