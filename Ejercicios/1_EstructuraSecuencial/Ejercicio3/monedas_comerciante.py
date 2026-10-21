
# TODO: Monedas Comerciante

# * Entrada
N, C, B = map(int, input("Ingresa valores de N, C, B").split())

# * Proceso
cofres = N // C
resto = N % C
bolsas = resto // B
sobrantes = resto % B

# * Salida
print(cofres, bolsas, sobrantes)