#include "iostream"

using namespace std;

int main() {

    // *-------------------
    // * TIPO ENTERO EN C++
    // *-------------------

    // ? Los enteros representan números
    // ? SIN PARTE DECIMAL
    // ? Pueden ser positivos, negativos o cero

    // ? Ej:    67      -59       9       0
    
    cout << 67 << endl;
    cout << -59 << endl;
    cout << 9 << endl;
    cout << 0 << endl;

    // *-----------------
    // * TIPOS DE ENTEROS
    // *-----------------

    // ? A diferencia de otros lenguajes, C++ posee
    // ? varios tipos para trabajar con enteros

    // * short
    // * int
    // * long
    // * long long

    // ? La diferencia principal está en el rango
    // ? de números que pueden representar

    // *------------------
    // * TIPO ENTERO short
    // *------------------

    // ? Se utiliza para números enteros
    // ? relativamente pequeños

    // ? Rango: -32768 hasta 32767

    // ? Ej:    850     -120        15000

    // *----------------
    // * TIPO ENTERO int
    // *----------------

    // ? Es el tipo entero de uso general
    // ? más utilizado en c++

    // ? Rango: -2417483648 hasta 2147483647
    // ? Ej:    12500000    -45000      980000

    // ! IMPORANTE:
    // * Usaremos int para los números enteros

    // *-----------------
    // * TIPO ENTERO long
    // *-----------------

    // ! IMPORTANTE
    // * El rango depende de la plataforma

    // ? Puede encontrarse comúnmente como:

    // * 32 bits:
    // ? -2147483648 hasta 2147483647

    // * 64 bits:
    // * aproximadamente -9.22 trillones de millones
    // * hastsa 9.22 trillones de millones
     
    // *----------------------
    // * TIPO ENTERO long long
    // *----------------------

    // ? Se utiliza para trabajar con números
    // ? enteros de gran magnitud

    // * Tiene como mínimo 64 bits

    // * Rango -9.22 hasta 9.22 trillones de millones

    // *-------------------------------------
    // * FORMA DE REPRESENTAR NÚMEROS ENTEROS
    // *-------------------------------------

    // *-------------------
    // * signed (con signo)
    // *-------------------

    // ? negativos, cero, positivos
    // ? Ej:    -500        0       500

    // ? int
    // ? signed int
    // * representan el mismo tipo

    // *---------------------
    // * unsigned (sin signo)
    // *---------------------
    
    // ? Solamente representa valores
    // ? enteros NO NEGATIVOS

    // ? 0 hasta 4294967295

    // *-------------------------------
    // * RESUMEN TIPOS DE DATOS ENTEROS
    // *-------------------------------

    // ? short
    // * Enteros de rango pequeño

    // ? int
    // * entero de uso general

    // ? long
    // * rango al menos tan amplio como int

    // ? long long
    // * enteros de gran magnitud

    // ? signed
    // * negativos, cero, positivos

    // ? unsigned
    // * cero y positivos

    return 0;
}