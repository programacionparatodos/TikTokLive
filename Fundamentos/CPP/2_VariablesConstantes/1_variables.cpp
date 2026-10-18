#include "iostream"
#include "string"

using namespace std;

int main() {

    // *-----------------
    // * VARIABLES EN C++
    // *-----------------

    // ? Una variable es un espacio de memoria
    // ? identificado mediante un nombre
    // ? utilizado para almacenar un dato

    // ? Su valor puede cambiar durante
    // ? la ejecución del programa

    // *-------------------------
    // * DECLARACIÓN DE VARIABLES
    // *-------------------------

    // ? Antes de utilizar una variable en C++
    // ? debemos DECLARARLA

    int nivel;

    // * int:       Tipo de Dato
    // * nivel      Nombre de la variable

    // *------------------------
    // * ASIGNACIÓN EN VARIABLES
    // *------------------------

    // ? Despúes de declarar una variable
    // ? podemos asignarle un valor

    nivel = 5;

    // ? El símbolo = representa una ASIGNACIÓN
    
    // ? El valor de la derecha se asigna a la
    // ? variable de la izquierda

    // *--------------------------------
    // * MODIFICAR VALOR DE UNA VARIABLE
    // *--------------------------------

    nivel = 8;

    // ? Inicialmente   nivel -> 5
    // * Posteriormente nivel -> 8

    // *-------------------------------
    // * INICIALIZACIÓN DE UNA VARIABLE
    // *-------------------------------

    // ? Podemos declar una variable y asignarle
    // ? su primer valor al mismo tiempo

    int vueltas = 12;  

    // * A esto lo llamamos INICIALIZACIÓN

    // *---------------------------------------
    // * VARIABLES EN DIFERENTES TIPOS DE DATOS
    // *---------------------------------------

    int suma = 10;
    double promedio = 67.50;
    char sexo = 'F';
    string nombre = "Adán";
    bool esPar = true;

    // *------------------------------
    // * REGLAS PARA NOMBRAR VARIABLES
    // *------------------------------

    // * 1. Puede comenzar con una letra o guión bajo
    // ? velocidad      destino     _contador

    // * 2. Puede contener números después
    // ?    jugador2    nivel_3     area51

    // ! 3. NO puede comenzar con un número
    // ? 2jugador       5nivel

    // ! 4. NO puede contener espacios
    // ?    velocidad maxima

    // ! 5. NO podemos utilizar simboles especiales
    // ? total$     usuari@     nivel-final

    // * 6. Diferencia entre MAYÚSCULAS y minúsculas
    int puntos = 100;
    int Puntos = 200;
    int PUNTOS = 300;

    // ? Son variables DIFERENTES

    // ! 7. NO podemos utilizar palabras reservadas
    // ? int        while       return
    
    // *---------------------
    // * NOMBRES DESCRIPTIVOS
    // *---------------------

    // ! Evitar:
    int x = 30;

    // * Preferir:
    int distancia_recorrida = 30;

    // *----------------------
    // * CONVENCIÓN snake_case
    // *----------------------

    int cantidad_ruedas = 4;
    double velocidad_promedio = 72.5;
    string placa_automovil = "XR200";

    // ? Las palabras se escriben en minúsculas
    // ? y se separan mediante guiones bajos

    return 0;
}