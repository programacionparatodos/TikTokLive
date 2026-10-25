
// TODO: Count Balls - AtCoder

#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    // * Declaración de variables
    long long n, a, b; 

    // * Entrada
    cin >> n >> a >> b;

    // * Proceso
    long long t = a + b;
    long long g = n / t;
    long long z = g * a;
    long long r = n % t;
    long long e = (r + a - abs(r - a)) / 2;
    long long azules = z + e;

    // * Salida
    cout << azules << endl;

    return 0;
}