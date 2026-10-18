
# * ------------------------
# * TIPOS DE DATOS EN PYTHON
# * ------------------------

# * Entero      ->  int
# * Real        ->  float
# * Carácter    ->  str
# * Cadena      ->  str
# * Lógico      ->  bool

# ! IMPORTANTE
# * Python no tiene un tipo de dato char
# * Un carácter se representa mediante un str
# * cuya longitud es exactamente 1

# * ----------------
# * TIPO ENTERO: int
# * ----------------

# ? Los números enteros representan números
# ? SIN PARTE DECIMAL
# ? Pueden ser positivos, negativos o cero
# ? Ej:  7      -3      4       -9      0

# * CURIOSIDAD:
# ? 12500000        12_500_000
# * Los guiones bajos no modifican el valor
# * Hacen que los números grandes sean más fáciles de leer

# type(): permite conocer el tipo de dato
# de un valor. <class 'int'>

print(type(7))
print(type(-3))
print(type(4))
print(type(-9))
print(type(0))

# * ----------------
# * TIPO REAL: float
# * ----------------

# ? Los números reales representan números
# ? CON PARTE DECIMAL
# ? Pueden ser positivos, negativos o cero
# ? Ej:     15.6    -8.5    10.0    0.0

# * CURIOSIDAD:
# ? Python utiliza punto decimal . NO coma ,
# * Correcto como decimal:       10.5
# ! 10,5 NO representa el número decimal 10.5

# type(): permite conocer el tipo de dato
# de un valor. <class 'float'>

print(type(15.6))
print(type(-8.5))
print(type(10.0))
print(type(0.0))

# * ------------------
# * TIPO CARÁCTER: str
# * ------------------

# ? Representa un solo carácter
# ? Se escribe entre comillas simples o dobles
# ? Ej:     "A"     '7'     '@'

# ! IMPORTANTE
# * Python no posee un tipo char independiente
# * Un carácter es un str cuya longitud es 1
# * "7" y 7 son diferentes
# ? "7"     -> str
# ?  7      -> int

# type(): permite conocer el tipo de dato
# de un valor. <class 'str'>

print(type("A"))
print(type('7'))
print(type('@'))

# * ----------------
# * TIPO CADENA: str
# * ----------------

# ? Almacena una secuencia de caracteres
# ? Se escribe entre comillas simples o dobles
# ? Ej:     "Samuel"    'Ing. Villalba'
# ?         "345"       "correo@gmail.com"

# * CURIOSIDAD:
#       0   1   2   3   4   5
# ?     P   y   t   h   o   n
#      -6  -5  -4  -3  -2  -1

# * [0]     ->      P
# * [1]     ->      y
# * [2]     ->      t

# ! IMPORTANTE:
# * Las posiciones empiezan desde 0

# ? También podemos utilizar índices negativos
# * [-1]    ->      n
# * [-2]    ->      o

# type(): permite conocer el tipo de dato
# de un valor. <class 'str'>

print(type("Samuel"))
print(type('Ing. Villalba'))
print(type("345"))

# * -----------------
# * TIPO LÓGICO: bool
# * -----------------

# ? Un dato lógico solo puede tener 2 valores:
# ?     - Verdadero:    True
# ?     - Falso:        False

# ! IMPORTANTE:
# * True y False deben comenzar con mayúscula

# type(): permite conocer el tipo de dato
# de un valor. <class 'bool'>

print(type(True))
print(type(False))