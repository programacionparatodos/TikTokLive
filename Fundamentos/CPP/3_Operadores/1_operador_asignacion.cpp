#include "iostream"
#include "string"

using namespace std;

int main() {

    // * ------------------------
    // * OPERADOR DE ASIGNACIÓN =
    // * ------------------------

    // ? Permite asignar un valor a una
    // ? variable. La variable debe tener
    // ? un tipo compatible con el valor
    // ? que recibe

    // * variable = valor;

    int edad = 29;
    double estatura = 1.75;
    char inicial = 's';
    string nombre = "Lety";
    bool estaAprendiendo = true;

    cout << "Operador de Asignación: " << endl;
    cout << edad << endl;
    cout << estatura << endl;
    cout << inicial << endl;
    cout << nombre << endl;
    cout << estaAprendiendo << endl;

    // * ASIGNACIÓN DE UNA EXPRESIÓN

    // ? Permite almacenar el resultado
    // ? de una operación

    // * int + int = int

    int resultado = 8 + 2;  // 10

    cout << "\nAsignación de una expresión: " << endl;
    cout << resultado << endl;
    
    return 0;
}