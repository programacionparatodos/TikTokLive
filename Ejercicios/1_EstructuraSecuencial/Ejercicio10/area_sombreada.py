
# TODO: Área Sombreada

import math

# * Entrada de Datos
n = float(input("Ingrese el lado del cuadrado: "))

# * Proceso
r = n / 4
areaCua = n * n
areaCir = 2 * (math.pi * r * r)
area = areaCua - areaCir

# * Salida de datos
print(f"Área sombreada: {area:.2f}")