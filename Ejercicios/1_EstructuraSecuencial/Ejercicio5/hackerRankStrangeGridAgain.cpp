
// TODO: Strange Grid Again - HackerRank

#include <iostream>

using namespace std;

int main() {

    // * Declaración de variables
    long long r, c, grupo, posicion, desplazamiento;
    long long inicio, resultado;

    // * Entrada
    cin >> r >> c;

    // * Proceso
    grupo = (r - 1) / 2;
    inicio = grupo * 10;
    posicion = (r - 1) % 2;
    desplazamiento = 2 * (c - 1);
    resultado = inicio + posicion + desplazamiento;

    // * Salida
    cout << resultado << endl;
    
    return 0;
}