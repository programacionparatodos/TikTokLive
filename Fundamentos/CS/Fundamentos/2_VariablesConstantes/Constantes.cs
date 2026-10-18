// * ----------------
// * CONSTANTES EN C#
// * ----------------

// ? Una constante almacena un valor
// ? que NO puede modificarse después
// ? de haber sido definido

// ? En C# utilizamos la palabra
// ? reservada: const

// * ----------------------
// * DECLARAR UNA CONSTANTE
// * ----------------------

const double PI = 3.141592;

Console.WriteLine(PI);

// * const      Indica que es una constante
// * double     Tipo de dato
// * PI         Nombre de la constante
// * =          Símbolo de asignación
// * 3.14..     Valor asignado

// * -------------------------
// * EL VALOR NO PUEDE CAMBIAR
// * -------------------------

const int DIAS_SEMANA = 7;

Console.WriteLine(DIAS_SEMANA);

// DIAS_SEMANA = 8;

// ! ERROR
// ? Una constante no puede recibir
// ? posteriormente otro valor

// * -----------------------------
// * CONSTANTES DE DISTINTOS TIPOS
// * -----------------------------

const int MesesAnio = 12;
const double Gravedad = 9.81;
const string CiudadNacimiento = "Oruro";

// * ---------------------
// * CONVENCIÓN DE NOMBRES
// * ---------------------

// ? En C# es habitual utilizar
// ? PascalCase para constantes

const MaximoIntentos = 3;

// ? Cada palabra comienza con
// ? una letra MAYÚSCULA

// ! IMPORTANTE
// * PascalCase es una convención
// * de escritura

// * ---------------------
// * VARIABLE VS CONSTANTE
// * ---------------------

int nivel = 1;
nivel = 2;
nivel = 3;

// ? Una variable puede cambiar

const int NivelMaximo = 100;

// NivelMaximo = 200;

// ! Una constante NO puede cambiar