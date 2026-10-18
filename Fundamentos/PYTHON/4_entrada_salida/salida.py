
# *--------------------------
# * SALIDA DE DATOS EN PYTHON
# *--------------------------

# ? En Python utilizamos principalmente la función:
# * print()         Escribir
# ? para mostrar información por consola

# TODO: SALIDA DE TEXTO
# ? Permite mostrar mensajes por consola

print("Programación Para Todos, aprendiendo Python")


# TODO: SALIDA DEL VALOR DE UNA VARIABLE
# ? Muestra el contenido de una variable

participantes = 150
print(participantes)


# TODO: CONCATENACIÓN DE TEXTO Y VARIABLE
# ? Combina texto con el valor de una variable

deporte = "Fútbol"

print("Deporte favorito: " + deporte)

# * Otra forma: f-string
print(f"Deporte favorito: {deporte}")


# TODO: SALIDA DE VARIOS ELEMENTOS
# ? Muestra varios valores en una misma línea

puntos_local = 4
puntos_visita = 6
print(puntos_local, puntos_visita)

# * Otra forma: separador personalizado
print(puntos_local, puntos_visita, sep="")


# TODO: USO DE SALTOS DE LÍNEA
# ? Permite mostrar mensajes en diferentes líneas

print("Capítulo uno")
print("Capítulo dos")

# * Otra forma: utilizando \n
print("Introducción\nDesarrollo\nConclusión")


# TODO: SALIDA DE UNA OPERACIÓN
# ? Muestra el resultado de una operación

horas = 4
minutos = 30

print(horas * 60 + minutos)