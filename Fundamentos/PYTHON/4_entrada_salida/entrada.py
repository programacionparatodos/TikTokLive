
# *---------------------------
# * ENTRADA DE DATOS EN PYTHON
# *---------------------------

# ? En Python utilizamos principalmente la función:
# * input()         Leer
# ? para recibir información desde el teclado
# * input() lee una cadena de texto


# TODO: ENTRADA INDIVIDUAL
# ? Permite ingresar un fato desde el teclado

color = input()
print(color)


# TODO: ENTRADA MÚLTIPLE (LÍNEAS SEPARADAS)
# ? Cada dato se ingresa por separado

pelicula = input()              # str
duracion = int(input())         # int
calificacion = float(input())   # float

# TODO: ENTRADA MÚLTIPLE (UNA SOLA LÍNEA)
# ? Permite ingresar varios datos separados por espacios

x, y, z = map(int, input().split())

# * Otra forma: usando listas
datos = input().split()

# ? 12 24 36
# ? 12 posición 0
# ? 24 posición 1
# ? 36 posición 2
 
a = int(datos[0])
b = int(datos[1])
c = int(datos[2])


# TODO: ENTRADA CON MENSAJE
# ? Muestra un mensaje antes de ingresar un dato

pasatiempo = input("Ingrese su pasatiempo favorito: ")


# TODO: ENTRADA DE UN CARACTER
# ? Python no tiene un tipo char independiente
inicial = input()[0]