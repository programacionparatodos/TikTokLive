#include "iostream"

using namespace std;

int main() {

    // *-----------------
    // * TIPO REAL EN C++
    // *-----------------

    // ? Los números reales permiten representar
    // ? valores CON PARTE DECIMAL

    // ? Pueden ser positivos, negativos o cero

    // ? Ej:    3.42    4.18    -0.123      0.0
    cout << 3.42 << endl;
    cout << 4.18 << endl;
    cout << -0.123 << endl;
    cout << 0.0 << endl;

    // *----------------
    // * TIPOS DE REALES
    // *----------------

    // ? c++ posee principalmente:
    // * float
    // * double
    // * long double

    // *----------------
    // * TIPO REAL float
    // *----------------

    // ? Trabaja con precisión simple
    // ? 6 a 7 dígitos decimales significativos
    // ? Ej:    18.75       245.45178       -12.25

    // *-----------------
    // * TIPO REAL double
    // *-----------------

    // ? Trabaja con mayor precisión que float
    // ? 15 a 16 dígitos decimalaes significativos

    // ? Ej:    12345.6789012345

    // ! IMPORTANTE
    // * double seerá nuestra opción principal

    // *----------------------
    // * TIPO REAL long double
    // *----------------------

    // ? Se utiliza cuando necesitamos trabajar
    // ? con una precisión mayor a la habitual (double)

    // *---------------------
    // * PUNTO DECIMAL EN C++
    // *---------------------

    // ? C++ utiliza el punto . como separador decimal
    // * Correcto:      58.78
    // ! Incorrecto:    58,78

    // *------------------------------
    // * RESUMEN TIPOS DE DATOS REALES
    // *------------------------------
    
    // ? float
    // * Precisión simple

    // ? double
    // * mayor precisión (uso recomendado)

    // ? long double
    // * precisión al menos igual a double
    
    return 0;
}