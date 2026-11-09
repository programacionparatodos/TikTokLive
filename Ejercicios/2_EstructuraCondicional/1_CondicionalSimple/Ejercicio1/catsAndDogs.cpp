
// TODO: AtCoder ABC094 A
#include <iostream>

using namespace std;

int main() {

    // * Declaración de variables
    int a, b, x;

    // * Entrada de datos
    cin >> a >> b >> x;

    // * Proceso
    if (x >= a && x <= a + b) {
        // * Salida de datos
        cout << "YES" << endl;
    }

    if (x < a || x > a + b) {
        // * Salida de datos
        cout << "NO" << endl;
    }

    return 0;
}