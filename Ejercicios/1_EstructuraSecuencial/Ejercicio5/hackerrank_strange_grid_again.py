
# TODO: Strange Grid Again - HackerRank

# * Entrada
r, c = map(int, input().split())

# * Proceso
grupo = (r - 1) // 2
inicio = grupo * 10
posicion = (r - 1) % 2
desplazamiento = 2 * (c - 1)
resultado = inicio + posicion + desplazamiento

# * Salida
print(resultado)