#include "iostream"
#include "string"

using namespace std;

int main() {

    // *------------------
    // * CONSTANTES EN C++
    // *------------------

    // ? Una constante es un espacio de memoria
    // ? identificado mediante un nombre, utilizado
    // ? para almacenar un dato, el cual no puede
    // ? cambiar su valor durante la ejecución

    // *-----------------
    // * CONSTANTES const
    // *-----------------

    const int MAXIMO_JUGADORES = 11;

    // ? const + tipo + nombre + valor

    // ! No sería correcto declarar una const
    // ! sin proporcionale un valor

    // *----------------------------
    // * CONVENCIÓN UPPER_SNAKE_CASE
    // *----------------------------

    const int TIEMPO_LIMITE = 60;
    const double ALTURA_MAXIMA = 2500.8;
    const char SEXO_MUJERES = 'F';
    const string NOMBRE_SISTEMA_OPERATIVO = "Arch Linux";
    const bool MODO_SEGURO = true;

    // ? Todas las letras en MAYÚSCULAS
    // ? y las palabras separadas mediante _

    return 0;
}