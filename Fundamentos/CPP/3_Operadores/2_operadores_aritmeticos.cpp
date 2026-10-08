#include "iostream"
#include "string"
// * Importante para usar pow()
#include "cmath"

using namespace std;

int main() {

    // * ----------------------
    // * OPERADORES ARITMÉTICOS
    // * ----------------------
    
    // ? Permiten realizar operaciones
    // ? matemáticas con valores numéricos

    // * OPERADOR SUMA +

    // ? Permite sumar dos valores numéricos

    // * int + int          = int
    // * int + float        = float
    // * float + int        = float
    // * float + float      = float
    // * int + double       = double
    // * double + int       = double
    // * double + double    = double

    cout << "Operador Suma: " << endl;
    cout << 5 + 3 << endl;
    cout << 5 + 2.5f << endl;
    cout << 2.5f + 5 << endl;
    cout << 2.5f + 1.5f << endl;
    cout << 5 + 2.5 << endl;
    cout << 2.5 + 5 << endl;
    cout << 2.5 + 1.5 << endl;

    // * OPERADOR RESTA -

    // ? Permite restar un valor de otro

    // * int - int          = int
    // * int - float        = float
    // * float - int        = float
    // * float - float      = float
    // * int - double       = double
    // * double - int       = double
    // * double - double    = double

    cout << "\nOperador Resta: " << endl;
    cout << 10 -4 << endl;
    cout << 10 - 2.5f << endl;
    cout << 8.5f - 3 << endl;
    cout << 8.5f - 2.5f << endl;
    cout << 10.0 - 2.5 << endl;

    // * OPERADOR MULTIPLICACIÓN *

    // ? Permite multiplicar dos valores

    // * int * int          = int
    // * int * float        = float
    // * float * int        = float
    // * float * float      = float
    // * int * double       = double
    // * double * int       = double
    // * double * double    = double

    cout << "\nOperador Multiplicación: " << endl;
    cout << 5 * 3 <<endl;
    cout << 5 * 2.5f << endl;
    cout << 2.5f * 4 << endl;
    cout << 2.5 * 2.0f << endl;
    cout << 5 * 2.5 << endl;

    // * OPERADOR DIVISIÓN /

    // ? Permite dividir un valor entre otro

    // ? Si ambos operandos son enteros,
    // ? el resultado es una DIVISIÓN ENTERA

    // ? Si alguno es decimal, el resultado
    // ? conserva la parte decimal

    // * int / int          = int
    // * int / float        = float
    // * float / int        = float
    // * float / float      = float
    // * int / double       = double
    // * double / int       = double
    // * double / double    = double

    cout << "\nOperador División: " << endl;
    cout << 10 / 2 << endl;
    cout << 10 / 4 << endl;
    cout << 10 / 4.0f << endl;
    cout << 10.0f / 4 << endl;
    cout << 10.00 / 4.0 << endl;

    // * OPERADOR MÓDULO %

    // ? Devuelve el residuo de una
    // ? división entre números enteros

    // * int % int = int

    cout << "\nOperador Módulo: " << endl;
    cout << 10 % 3 << endl;
    cout << 10 % 4 << endl;
    cout << 7 % 2 << endl;

    // ? No admite float ni double

    // ! cout << 10.5 % 3;    ERROR

    // * POTENCIA con pow()

    // ? C++ no posee un operador aritmético
    // ? específico para calcular potencias.
    // ? Utilizamos pow() de <cmath>

    // * pow(base, exponente)

    // * pow(int, int)          = double
    // * pow(int, double)       = double
    // * pow(double, int)       = double
    // * pow(double, double)    = double

    cout << "\nPotencia con pow(): " << endl;
    cout << pow(2, 3) << endl;
    cout << pow(5, 2.0) << endl;
    cout << pow(10.0, 3) << endl;
    cout << pow(2.0, 0.5) << endl;

    // ? Aunque cout muestre 8, pow(2, 3)
    // ? devuelve un resultado double

    return 0;
}