#include "iostream"
#include "string"

using namespace std;

int main() {

    // * -----------------------
    // * ENTRADA DE DATOS EN C++
    // * -----------------------

    // ? En C++ utilizamos el comando
    // * cin >>         Leer
    // ? c   = character
    // ? in  = input
    // * cin = entrada de caracteres

    // TODO: ENTRADA INDIVIDUAL
    // ? Permite ingresar un dato desde teclado

    string ciudad;

    cin >> ciudad;
    
    // TODO: ENTRADA MÚLTIPLE (LÍNEAS SEPARADAS)
    // ? Cada dato se ingresa por separado

    string producto;
    int cantidad;
    double precio;

    cin >> producto;
    cin >> cantidad;
    cin >> precio;


    // TODO: ENTRADA MÚLTIPLE (UNA MISMA LÍNEA)
    // ? Permite ingresar varios datos separados
    // ? por espacios
    
    int nota1, nota2, nota3;
    cin >> nota1 >> nota2 >> nota3;


    // TODO: ENTRADA CON MENSAJE
    // ? Muestra un mensaje antes de leer el dato

    int temperatura;

    cout << "Ingrese la temperatura actual: ";
    cin >> temperatura;


    // TODO: ENTRADA DE TEXTO CON ESPACIOS
    // ? getline() permite leer una línea completa
    string nombreCompleto;
    cin >> ws; // ws = whitespace
    getline(cin, nombreCompleto);

    cout << nombreCompleto << endl;

    return 0;
}