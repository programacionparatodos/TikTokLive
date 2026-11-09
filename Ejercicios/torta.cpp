
#include <iostream>
#include <string>
#include <thread>
#include <chrono>

using namespace std;

// Tiempo de espera
void esperar(int milisegundos) {
    this_thread::sleep_for(chrono::milliseconds(milisegundos));
}

// Contar caracteres con tildes
int contarCaracteres(string texto) {
    int cantidad = 0;

    for (unsigned char letra : texto) {
        if (letra < 128 || letra >= 192) {
            cantidad++;
        }
    }

    return cantidad;
}

int main() {

    // DATOS PERSONALIZABLES
    string nombre = "QuirCode";
    int edad = 1;

    string mensaje1 = "TE QUEREMOS MUCHO";
    string mensaje2 = "PROGRAMACIÓN PARA TODOS";

    // DISEÑO DE LA TORTA
    int pisos = 3;
    int anchoBase = 55;
    int margenIzq = 5;
    int velocidad = 350;

    // Colores
    string amarillo = "\033[93m";
    string rosa = "\033[95m";
    string celeste = "\033[96m";
    string verde = "\033[92m";
    string blanco = "\033[97m";
    string normal = "\033[0m";

    // Ajustar ancho según los mensajes
    if (contarCaracteres(mensaje1) + 12 > anchoBase) {
        anchoBase = contarCaracteres(mensaje1) + 12;
    }

    if (contarCaracteres(mensaje2) + 6 > anchoBase) {
        anchoBase = contarCaracteres(mensaje2) + 6;
    }

    // Preparar las velas
    string edadTexto = to_string(edad);
    int velas = edadTexto.length();
    int anchoVelas = velas * 4 - 3;

    int espacioVelas = margenIzq +
        (anchoBase - anchoVelas) / 2;

    // Limpiar pantalla
    cout << "\033[2J\033[H";

    // * ESPACIO PARA LAS LLAMAS
    cout << "\n";

    // Números de las velas
    cout << string(espacioVelas, ' ');

    for (int i = 0; i < velas; i++) {
        if (i % 2 == 0) {
            cout << celeste << edadTexto[i] << normal;
        } else {
            cout << rosa << edadTexto[i] << normal;
        }

        if (i < velas - 1) {
            cout << "   ";
        }
    }
    cout << "\n";

    // Soportes de las velas
    cout << string(espacioVelas, ' ');

    for (int i = 0; i < velas; i++) {
        cout << blanco << "|" << normal;

        if (i < velas - 1) {
            cout << "   ";
        }
    }
    cout << "\n";

    // * PISOS DE LA TORTA
    for (int p = 0; p < pisos; p++) {
        int reduccion = (pisos - 1 - p) * 8;
        int anchoActual = anchoBase - reduccion;
        int espaciosIzq = margenIzq + reduccion / 2;

        // Color de cada piso
        string colorPiso = rosa;

        if (p == 1) {
            colorPiso = celeste;
        } else if (p == 2) {
            colorPiso = verde;
        }

        // Texto y color de cada piso
        string textoPiso = "o   o   o   o";
        string colorMensaje = amarillo;

        if (p == 1) {
            textoPiso = mensaje1;
            colorMensaje = rosa;
        } else if (p == 2) {
            textoPiso = mensaje2;
            colorMensaje = celeste;
        }

        // Borde superior
        cout << string(espaciosIzq, ' ');
        cout << colorPiso;
        cout << string(anchoActual, '~');
        cout << normal << "\n";

        // Interior del piso
        int espacios = anchoActual - 2 -
                       contarCaracteres(textoPiso);

        int izquierda = espacios / 2;
        int derecha = espacios - izquierda;

        cout << string(espaciosIzq, ' ');
        cout << colorPiso << "*" << normal;
        cout << string(izquierda, ' ');
        cout << colorMensaje << textoPiso << normal;
        cout << string(derecha, ' ');
        cout << colorPiso << "*" << normal;
        cout << "\n";

        // Borde inferior
        cout << string(espaciosIzq, ' ');
        cout << colorPiso;

        if (p == pisos - 1) {
            cout << "*";
            cout << string(anchoActual - 2, '=');
            cout << "*";
        } else {
            cout << string(anchoActual, '*');
        }

        cout << normal << "\n";
    }

    // * SALUDO DE CUMPLEAÑOS
    string saludo = "¡FELIZ CUMPLEAÑOS! " + nombre;

    int espacioSaludo = margenIzq +
        (anchoBase - contarCaracteres(saludo)) / 2;

    if (espacioSaludo < 0) {
        espacioSaludo = 0;
    }

    cout << "\n";
    cout << string(espacioSaludo, ' ');
    cout << amarillo << saludo << normal;
    cout << flush;

    // * ANIMACIÓN DE LAS LLAMAS
    int ciclo = 0;

    while (true) {
        // Volver a la primera línea
        cout << "\033[1;1H\033[2K";
        cout << string(espacioVelas, ' ');

        for (int i = 0; i < velas; i++) {
            if (ciclo % 2 == 0) {
                cout << amarillo << "*" << normal;
            } else {
                cout << " ";
            }

            if (i < velas - 1) {
                cout << "   ";
            }
        }

        cout << flush;

        ciclo++;
        esperar(velocidad);
    }

    return 0;
}
