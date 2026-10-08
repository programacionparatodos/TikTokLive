
# * -----------------------
# * OPERADORES RELACIONALES
# * -----------------------

# ? Los operadores relacionales permiten
# ? comparar dos valores

# ? El resultado de una comparación
# ? siempre es un valor booleano

# * True
# * False

# * OPERADOR IGUAL QUE ==

# ? Comprueba si dos valores son iguales

# * comparacion = bool

print("OPERADOR IGUAL QUE ==")
print(5 == 5)               # True               
print(5.5 == 5)             # False
print(5.0 == 5)             # True
print("Hola" == "Hola")     # True
print(True == False)        # False

# * OPERADOR DIFERENTE DE !=

# ? Comprueba si dos valores son diferentes

# * comparacion = bool

print("\nOPERADOR DIFERENTE DE !=")
print(5 != 3)           # True
print(5 != 5)           # False
print("A" != "B")       # True

# * OPERADOR MAYOR QUE >

# ? Comprueba si el valor de la izquierda
# ? es mayor que el de la derecha

# * comparacion = bool

print("\nOPERADOR MAYOR QUE >")
print(10 > 5.3)         # True
print(-3.5 > -7.2)      # True      
print(True > False)     # True
#       1  >  0

# * OPERADOR MENOR QUE <

# ? Comprueba si el valor de la izquierda
# ? es mejor que el de la derecha

# * comparacion = bool
print("\nOPERADOR MENOR QUE <")
print(3 < 10)           # True
print(True < True)      # False
print(-4.2 < 1.3)       # True

# * OPERADOR MAYOR O IGUAL QUE >=

# ? Comprueba si un valor es mayor
# ? o igual que otro

# * comparacion = bool

print("\nOPERADOR MAYOR O IGUAL QUE >=")
print(5 >= 5.1)         # False
print(10 >= 10.0)       # True 
print(True >= False)    # True
#      1   >=   0
#   1 > 0   OR   1 == 0       

# * OPERADOR MENOR O IGUAL QUE <=

# ? Comprueba si un valor es menor
# ? o igual que otro

# * comparacion = bool

print("\nOPERADOR MENOR O IGUAL QUE <=")
print(5 <= 5.1)         # True
print(10 <= 10.0)       # True 
print(True <= False)    # False
#      1   <=   0
#   1 < 0   OR   1 == 0

# * -------
# * RESUMEN
# * -------
# 
# * int   con   int/float   ->  bool
# * float con   int/float   ->  bool 
# * str   con   str         ->  bool
# * bool  con   bool        ->  bool