
# TODO: Count Balls - AtCoder

# * Entrada
n, a, b = map(int, input().split())

# * Proceso
t = a + b
g = n // t
z = g * a
r = n % t
e = (r + a - abs(r - a)) // 2
azules = z + e

# * Salida
print(azules)