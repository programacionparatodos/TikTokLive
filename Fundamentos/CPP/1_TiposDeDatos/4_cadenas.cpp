#include "iostream"
// * nos permite usar y manipular cadenas
#include "string"

using namespace std;

int main() {

    // *-------------------
    // * TIPO CADENA EN C++
    // *-------------------

    // ? Secuencia de caracteres
    // ? letras, numeros, símbolos, espacios
    // ? Ej:    "Programación Para Todos"
    // ? "65"       "b"     "Bolivia"

    cout << "Programación Para Todos" << endl;
    cout << "65" << endl;
    cout << "b" << endl;
    cout << "Bolivia" << endl;

    // *-------------------
    // * TIPO CADENA string
    // *-------------------

    // ! IMPORTANTE
    // * string pertenece a la biblioteca
    // * estándar de C++, por eso utilizamos
    // * #include "string"/<string>

    // *----------------
    // * COMILLAS DOBLES
    // *----------------

    // ! IMPORTANTE
    // * El contenido entre comillas dobles
    // * será tratado como texto

    // ? "2026"         cadena (string)
    // ? 2026           entero (int)

    // *----------------------
    // * POSICIONES EN CADENAS
    // *----------------------

    // ? Cada caracter ocupa una posición
    // ? dentro de la cadena

    //      0   1   2   3   4   5   6   7
    // ?    Q   u   i   r   C   o   d   e

    // ! Las posiciones comienzan desde 0

    // ? posición 0 -> Q
    // ? posición 1 -> u
    // ? posición 4 -> C

    // *-------------
    // * CADENA VACÍA
    // *-------------

    // ? Una cadena también puede no contener
    // ? ningún caracter

    // ? Ej:        ""
    // * A esto lo llamamos cadena vacía

    // *----------------------------
    // * RESUMEN TIPO DE DATO CADENA
    // *----------------------------

    // ? string
    // * Secuencia de caracteres

    // ? Utiliza comillas dobles

    // ? Se puede accedeer a sus caracteres
    // ? de manera independiente por su posición
    return 0;
}