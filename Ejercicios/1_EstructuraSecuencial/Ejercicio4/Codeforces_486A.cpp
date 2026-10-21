
// TODO: 486A - Calculating Function | Codeforces

#include <iostream> 

using namespace std;

int main() {

    // * Declaración de variables
    long long n, fn;  

    // * Entrada
    cin >> n;

    // * Proceso
    fn = (n / 2) - (n % 2) * n;

    // * Salida
    cout << fn << endl;

    return 0;
}