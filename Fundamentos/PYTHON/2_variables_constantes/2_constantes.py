
# *---------------------
# * CONSTANTES EN PYTHON
# *---------------------

# ? Es un nombre asociado a un valor que NO debería
# ? cambiar durante la ejecución del programa

PI = 3.14159
GRAVEDAD = 9.81
DIAS_SEMANA = 7

# ! IMPORTANTE
# * Python NO posee constantes estrictas
# * como otros lenguajes de programación

# ? Una constante en Python se establece
# ? principalmente mediante una CONVENCIÓN

# *------------------
# * FORMA DE ESCRIBIR
# *------------------

# ? Para las constantes utilizamos la convención
# ? UPPER_SNAKE_CASE

# ? Se escriben las palabras en MAYÚSCULAS
# ? y se separan utilizando guiones bajos _

PI = 3.14159

IVA = 0.13

VELOCIDAD_MAXIMA = 120

DIAS_DE_LA_SEMANA = 7

# *-----------------------
# * VARIABLE VS CONSTANTE
# *-----------------------

# ? Una VARIABLE puede cambiar su valor

edad = 23
edad = 24

# ? Una CONSTANTE no debería cambiar su valor

PI = 3.14159

# *-----------------------------
# * ¿SE PUEDE CAMBIAR SU VALOR?
# *-----------------------------

# ! Python SÍ permite reasignar una constante

PI = 3.14159
PI = 3.1416

# ! PERO NO DEBERÍAMOS HACERLO

# ? Python no genera un error por cambiarla
# ? porque el lenguaje no impide la reasignación

# * Las MAYÚSCULAS indican a otros programadores:
# * "Este valor debe tratarse como una constante"

# *------------------
# * BUENA PRÁCTICA
# *------------------

# * VARIABLE
precio_producto = 150

# * CONSTANTE
IVA = 0.13

# ? Las variables utilizan normalmente snake_case
# ? Las constantes utilizan normalmente UPPER_SNAKE_CASE