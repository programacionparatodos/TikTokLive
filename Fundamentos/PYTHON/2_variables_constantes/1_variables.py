
# *--------------------
# * VARIABLES EN PYTHON
# *--------------------

# ? Es un nombre que hace referencia a un valor
# ? y puede asociarse posteriormente a otro valor

edad = 23
edad = 30

# *------------------------------
# * REGLAS PARA NOMBRAR VARIABLES
# *------------------------------

# * 1. Pueden comenzar con una letra (a-z, A-Z)
# *    o con un guión bajo _
# ? nombre      edad        _precio

# * 2. Pueden contener letras, números y guiones bajos
# ? contador1       edad4       peso_5

# * 3. Para separar palabras usamos guión bajo _
# ? nombre_completo
# ? precio_producto

# ! 4. NO pueden comenzar con un número
# ? 1nota       5edad

# ! 5. NO pueden contener espacios
# ? nombre completo

# ! 6. NO podemos utilizar símbolos especiales
# ? precio$     nota-final      edad@persona

# * 7. Diferencia MAYÚSCULAS y minúsculas
# ? edad        Edad        EDAD
# ? Son variables diferentes (case-sensitive)

# ! 8. NO podemos utilizar palabras reservadas
# ? if      while      class      True
# * Estas palabras poseen un significado
# * especial en Python

# *----------------------
# * CONVENCIÓN snake_case
# *----------------------

# ? Se escribe todo en minúsculas y para separar
# ? palabras usamos guiones bajos _
# ? edad_usuario        precio_producto
# ? nombre_completo     promedio_final

# ! IMPORTANTE:
# * snake_case es una convención, no una obligación
# * del lenguaje Python

# *---------------------
# * NOMBRES DESCRIPTIVOS
# *---------------------

# ! Evitar nombres que no indiquen qué representan
x = 150

# * Preferir nombres claros y descriptivos
precio_producto = 150

# *-----------------------------
# * PYTHON TIENE TIPADO DINÁMICO
# *-----------------------------

edad = 22               # int

edad = "veintidos"      # str

edad = 25.4             # float

# ? El tipo pertenece al valor, no queda fijado
# ? permanentemente al nombre de la variable

# * Por eso, un mismo nombre puede asociarse
# * posteriormente a valores de diferentes tipos

# *--------------------
# * ASIGNACIÓN MÚLTIPLE
# *--------------------

# * Podemos asignar varios valores a varias
# * variables en una sola línea

nombre, edad, altura = "Andy", 27, 1.78

# * Podemos asignar el mismo valor
# * a varias variables

x = y = z = 7