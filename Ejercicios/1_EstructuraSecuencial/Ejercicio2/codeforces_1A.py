
# TODO: 1A - Theatre Square | Codeforces

# * Entrada de datos
n, m, a = map(int, input().split())

# * Proceso
col = (n + a - 1) // a 
fil = (m + a - 1) // a
total = col * fil

# * Salida de datos
print(total)