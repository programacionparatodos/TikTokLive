#include "iostream"

using namespace std;

int main() {

    // * ------------------
    // * OPERADORES LÓGICOS
    // * ------------------

    // ? Permiten combinar o negar
    // ? condiciones lógicas

    // * AND (Y lógico)     &&
    // * OR  (O lógico)     ||
    // * NOT (negación)     !

    cout << boolalpha;

    // * OPERADOR LÓGICO AND &&

    // ? Devuelve true únicamente cuando
    // ? ambas condiciones son verdaderas

    // * bool && bool = bool

    cout << "Operador Lógico Y: " << endl;
    cout << (true && true) << endl;      // true
    cout << (true && false) << endl;     // false
    cout << (false && true) << endl;     // false
    cout << (false && false) << endl;    // false

    // * Ejemplos con comparaciones

    cout << "\nEjemplos con comparaciones: " << endl;
    cout << (10 > 5 && 8 > 3) << endl;  // true
    //         true && true 
    cout << (10 > 5 && 8 < 3) << endl;  // false
    //         true && false

    // * OPERADOR LÓGICO OR ||

    // ? Devuelve true cuando al menos
    // ? una condicion es verdadera

    // * bool || bool = bool

    cout << "\nOperador Lógico O: " << endl;
    cout << (true || true) << endl;      // true
    cout << (true || false) << endl;     // true
    cout << (false || true) << endl;     // true
    cout << (false || false) << endl;    // false

    // * Ejemplos con comparaciones

    cout << "\nEjemplos con comparaciones: " << endl;
    cout << (10 > 5 || 8 > 3) << endl;  // true
    //         true || true 
    cout << (10 > 5 || 8 < 3) << endl;  // true
    //         true || false

    // * OPERADOR LÓGICO NOT !
    // ? Invierte el valor lógico
    // ? de una condición

    // * !bool = bool

    cout << "\nOperador lógico negación: " << endl;
    cout << (!true) << endl;    // false
    cout << (!false) << endl;   // true

    cout << "\nEjemplos con comparaciones: " << endl;
    cout << (!(10 > 5)) << endl;    // false
    // *     !true     
    cout << (!(10 < 5)) << endl;    // true
    // *     !false
    
    return 0;
}