
# TODO: Billiards | AtCoder

# * Entrada de datos
Sx, Sy, Gx, Gy = map(int, input().split())

# * Proceso
x = (Sx*Gy + Sy*Gx) / (Gy + Sy)

# * Salida de datos
print(f"{x:.10f}")