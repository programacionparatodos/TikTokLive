#include "iostream"
#include "string"

using namespace std;

int main() {

    // * ----------------------
    // * SALIDA DE DATOS EN C++
    // * ----------------------

    // ? En C++ utilizamos el comando
    // * cout <<        Escribir
    // ? c    = character
    // ? out  = output
    // * cout = salida de caracteres

    // TODO: SALIDA DE TEXTO
    // ? Permite mostrar mensajes por consola

    cout << "Bienvenidos al curso de c++" << endl;

    // TODO: SALIDA DEL VALOR DE UNA VARIABLE
    // ? Muestra el contenido de una variable
    
    int asistentes = 278;
    cout << asistentes << endl;

    // TODO: CONCATENACIÓN DE TEXTO Y VARIABLE
    // ? Combina texto con el valor de una variable

    string lenguaje = "C++";
    cout << "Estamos aprendiendo " << lenguaje << endl;

    // TODO: SALIDA DE VARIOS ELEMENTOS
    // ? Muestra varios valores en una misma línea

    int ancho = 12;
    int alto = 9;

    cout << ancho << " " << alto << endl;

    // TODO: USO DE SALTOS DE LÍNEA
    // ? Permite mostrar mensajes en diferentes líneas
    
    cout << "Primera actividad\n";
    cout << "Segunda actividad\n";

    // * Otra forma: endl
    cout << "Tercera actividad" << endl;
    cout << "Cuarta actividad" << endl;

    
    // TODO: SALIDA DE UNA OPERACIÓN
    // ? Muestra directamente el resultado de una
    // ? operación

    int largo = 7;
    int profundidad = 4;

    cout << largo * profundidad << endl;

    return 0;
}