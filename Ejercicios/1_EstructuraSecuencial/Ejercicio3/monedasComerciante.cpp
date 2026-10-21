
// TODO: Monedas Comerciante

#include <iostream>

using namespace std;

int main() {

    // * Declaración de variables
    int N, C, B;   
    int cofres, resto, bolsas, sobrantes;

    // * Entrada
    cin >> N >> C >> B;

    // * Proceso
    cofres = N / C;
    resto = N % C;
    bolsas = resto / B;
    sobrantes = resto % B;

    // * Salida
    cout << cofres << endl;
    cout << bolsas << endl;
    cout << sobrantes << endl;

    return 0;
}