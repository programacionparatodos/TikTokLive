#include "iostream"
#include "string"

using namespace std;

int main() {

    // * ----------------------
    // * OPERADORES RELACIONALES
    // * ----------------------

    // ? Nos permiten comparar valores
    // ? En C++ el resultado de una comparación
    // ? es de tipo bool

    // * true
    // * false

    // ? boolalpha permite mostrar true y false
    // ? en lugar de 1 y 0

    cout << boolalpha;

    // * OPERADOR IGUAL QUE     ==

    // ? Comprueba si dos valores son iguales

    // * int == int         =   bool
    // * int == double      =   bool
    // * double == double   =   bool
    // * char == char       =   bool
    // * string == string   =   bool
    // * bool == bool       =   bool

    cout << "Operador Igual que: " << endl;
    cout << (3 == 3) << endl;               // true   
    cout << (2 == 5.0) << endl;             // false 
    cout << (3.5 == 8.3) << endl;           // false
    cout << ('M' == 'J') << endl;           // false
    cout << ("Roxana" == "Soani") << endl;  // false
    cout << (true == false) << endl;        // false

    // * OPERADOR DIFERENTE DE     !=

    // ? Comprueba si dos valores son diferentes

    // * int != int         =   bool
    // * int != double      =   bool
    // * double != double   =   bool
    // * char != char       =   bool
    // * string != string   =   bool
    // * bool != bool       =   bool

    cout << "\nOperador Diferente de: " << endl;
    cout << (3 != 3) << endl;               // false   
    cout << (2 != 5.0) << endl;             // true 
    cout << (3.5 != 8.3) << endl;           // true
    cout << ('M' != 'J') << endl;           // true
    cout << ("Roxana" != "Soani") << endl;  // true
    cout << (true != false) << endl;        // true

    // * OPERADOR MAYOR QUE     >

    // ? Comprueba si el valor de la izquierda
    // ? es mayor que el de la derecha

    // * int > int         =   bool
    // * int > double      =   bool
    // * double > double   =   bool
    // * char > char       =   bool
    // * string > string   =   bool
    // * bool > bool       =   bool

    cout << "\nOperador Mayor que: " << endl;
    cout << (3 > 3) << endl;               // false   
    cout << (2 > 5.0) << endl;             // false
    cout << (3.5 > 8.3) << endl;           // false
    cout << ('M' > 'J') << endl;           // true
    // * minusculas > MAYÚSCULAS
    cout << (string("roxana") > "Soani") << endl;  // true
    cout << (true > false) << endl;        // true
    //         1  >  0

    // * OPERADOR MENOR QUE     <

    // ? Comprueba si el valor de la izquierda
    // ? es menor que el de la derecha

    // * int < int         =   bool
    // * int < double      =   bool
    // * double < double   =   bool
    // * char < char       =   bool
    // * string < string   =   bool
    // * bool < bool       =   bool

    cout << "\nOperador Menor que: " << endl;
    cout << (3 < 3) << endl;               // false   
    cout << (2 < 5.0) << endl;             // true
    cout << (3.5 < 8.3) << endl;           // true
    cout << ('M' < 'J') << endl;           // false
    // * minusculas > MAYÚSCULAS
    cout << (string("Roxana") < "soani") << endl;  // true
    cout << (true < false) << endl;        // false
    //         1  <  0

    // * OPERADOR MAYOR O IGUAL QUE     >=

    // ? Comprueba si un valor es mayor
    // ? o igual que otro

    // * int >= int         =   bool
    // * int >= double      =   bool
    // * double >= double   =   bool
    // * char >= char       =   bool
    // * string >= string   =   bool
    // * bool >= bool       =   bool

    cout << "\nOperador Mayor o igual que: " << endl;
    cout << (3 >= 3) << endl;               // true   
    cout << (2 >= 5.0) << endl;             // false
    cout << (3.5 >= 8.3) << endl;           // false
    cout << ('M' >= 'J') << endl;           // true
    // * minusculas > MAYÚSCULAS
    cout << (string("roxana") >= "Soani") << endl;  // true
    cout << (true >= false) << endl;        // true
    //         1  >=  0

    // * OPERADOR MENOR O IGUAL QUE     <=

    // ? Comprueba si un valor es menor
    // ? o igual que otro

    // * int >= int         =   bool
    // * int >= double      =   bool
    // * double >= double   =   bool
    // * char >= char       =   bool
    // * string >= string   =   bool
    // * bool >= bool       =   bool

    cout << "\nOperador Menor o igual que: " << endl;
    cout << (3 <= 3) << endl;               // true   
    cout << (2 <= 5.0) << endl;             // true
    cout << (3.5 <= 8.3) << endl;           // true
    cout << ('M' <= 'J') << endl;           // false
    // * minusculas > MAYÚSCULAS
    cout << (string("roxana") <= "Soani") << endl;  // false
    cout << (true <= false) << endl;        // false
    //         1  <=  0

    // * COMPARACIÓN DE CADENAS

    // ? Los objetos string también
    // ? permiten comparaciones

    // * string == string       =   bool
    // * string != string       =   bool
    // * string < string        =   bool
    // * string > string        =   bool

    string nombre1 = "Asa";
    string nombre2 = "Liz";

    cout << "\nComparación de cadenas: " << endl;
    cout << (nombre1 == nombre2) << endl;   // false
    cout << (nombre1 != nombre2) << endl;   // true
    cout << (nombre1 > nombre2) << endl;    // false
    cout << (nombre1 < nombre2) << endl;    // true

    // * VERIFICAR EL VALOR ASCII DE UN CARACTER

    char letra = 't';

    cout << "ASCII: " << static_cast<int>(letra) << endl;

    return 0;
}