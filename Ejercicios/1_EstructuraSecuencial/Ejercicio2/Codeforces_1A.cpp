#include <iostream>

using namespace std;

int main() {

    // * Declaración de variables
    long long n, m, a, fil, col, total;

    // * Entrada de datos
    cin >> n >> m >> a;

    // * Proceso
    col = (n + a - 1) / a;
    fil = (m + a - 1) / a;
    total = col * fil;

    // * Salida de datos
    cout << total << endl;

    return 0;
}