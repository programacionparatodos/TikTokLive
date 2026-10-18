
# * ------------------
# * OPERADORES LÓGICOS
# * ------------------

# ? Los operadores lógicos permiten
# ? combiar o negar condiciones

# ? Los principales son:

# * and
# * or
# * not

# * OPERADOR LÓGICO AND

# ? Devuelve True cuando AMBAS
# ? condiciones son VERDADERAS.

# * bool and bool = bool

print(True and True)        # True
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False

# * Ejemplo con comparaciones

print(10 > 5 and 8 > 3)     # True
#       True and True
print(10 > 5 and 8 < 3)     # False
#       True and False

# * OPERADOR LÓGICO OR

# ? Devuelve True cuando AL MENOS
# ? una condición es VERDADERA

# * bool or bool = bool

print(True or True)        # True 
print(True or False)       # True
print(False or True)       # True
print(False or False)      # False

# * Ejemplo con comparaciones

print(10 > 5 or 3 > 8)      # True
#       True or False
print(10 < 5 or 3 > 8)      # False 
#      False or False

# * OPERADOR LÓGICO NOT

# ? Invierte el valor lógico
# ? de una condición

# * not bool = bool

print(not True)     # False 
print(not False)    # True

# * Ejemplo con comparaciones

print(not(10 > 5))      # False
#     not  True      
print(not(10 < 5))      # True      
#     not  False