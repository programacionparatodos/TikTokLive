
# TODO: AtCoder ABC094 A

# * Entrada de datos
a, b, x = map(int, input().split())

# * Proceso
if x >= a and x <= a + b:
    # * Salida de datos
    print("YES")

if x < a or x > a + b:
    # * Salida de datos
    print("NO")