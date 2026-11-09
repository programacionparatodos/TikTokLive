
// TODO: Billiards | AtCoder

#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    // * Declaración de variables
    int Sx, Sy, Gx, Gy;
    double x;

    // * Entrada de datos
    cin >> Sx >> Sy >> Gx >> Gy;

    // * Proceso
    x = (Sx * Gy + Sy * Gx) / static_cast<double>(Gy + Sy);

    // * Salida de datos
    cout << fixed << setprecision(10) << x << endl;

    return 0;
}