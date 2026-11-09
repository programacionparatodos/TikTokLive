# * Biblioteca para crear interfaces gráficas
# ? Verificar si ya esta instalado
# TODO: python -m tkinter
import tkinter as tk

# * Biblioteca para abrir y redimensionar imágenes
# ? Instalar Pillow
from PIL import Image, ImageTk, ImageFilter, ImageOps

# * Biblioteca para construir rutas de archivos
from pathlib import Path

# TODO: CONFIGURACIÓN DEL TABLERO

TAM_CAS = 60
FIL = 8
COL= 8

COLOR_CLARO = '#EEEED2'
COLOR_OSCURO = '#769656'

# TODO: CARGAR LAS IMÁGENES
CARPETA = Path(__file__).resolve().parent

RUTA_IMAGENES = CARPETA / "imagenes"


# TODO: Función para contorno de piezas blancas

def agregar_contorno(imagen):
    mascara = imagen.getchannel("A")
    contorno = mascara.filter(
        ImageFilter.MaxFilter(61)
    )

    fondo = Image.new(
        "RGBA",
        imagen.size,
        (0,0,0,0)
    )

    fondo.putalpha(contorno)
    fondo.alpha_composite(imagen)

    return fondo


# TODO: CLASE PIEZA
class Pieza:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

        ruta = RUTA_IMAGENES / f"{nombre}_{color}.png"

        self.imagen = Image.open(ruta).convert("RGBA")

        if self.color == "blanco":
            self.imagen = agregar_contorno(self.imagen)

    # * METODO PARA MOVIMIENTOS DEL PEÓN
    def movimientos_peon(self, estado_tablero, 
                         fila, columna):

        movimientos = []

        if self.nombre != "peon":
            return movimientos

        if self.color == "blanco":
            direccion = -1
            fila_inicial = 6
        else:
            direccion = 1
            fila_inicial = 1

        nueva_fila = fila + direccion

        # * Avanzar una casilla
        if 0 <= nueva_fila < FIL:
            if estado_tablero[nueva_fila][columna] is None:
                movimientos.append((nueva_fila, columna))

                # * Avanzar dos casillas desde la posición inicial
                if fila == fila_inicial:
                    segunda_fila = fila + 2 * direccion

                    if estado_tablero[segunda_fila][columna] is None:
                        movimientos.append((segunda_fila, columna))

        return movimientos

    # * MÉTODO PARA MOVIMIENTOS DE LA TORRE
    def movimientos_torre(self, estado_tablero, 
                         fila, columna):
        
        movimientos = []

        if self.nombre != "torre":
            return movimientos

        direcciones = [
            (-1, 0), # Arriba
            (1, 0),  # Abajo
            (0, -1), # Izquierda
            (0, 1)   # Derecha
        ]

        for cambio_fila, cambio_columna in direcciones:

            nueva_fila = fila + cambio_fila
            nueva_columna = columna + cambio_columna

            while (0 <= nueva_fila < FIL and
                   0 <= nueva_columna < COL):

                if estado_tablero[nueva_fila][nueva_columna] is not None:
                    break

                movimientos.append((nueva_fila, nueva_columna))
                nueva_fila += cambio_fila
                nueva_columna += cambio_columna
        
        return movimientos

    # * MÉTODO PARA MOVIMIENTOS DEL ALFIL
    def movimientos_alfil(self, estado_tablero, 
                         fila, columna):

        movimientos = []

        if self.nombre != "alfil":
            return movimientos

        direcciones = [
            (-1, -1), # Arriba izquierda
            (-1, 1),  # Arriba derecha
            (1, -1),  # Abajo izquierda
            (1, 1)    # Abajo derecha
        ]

        for cambio_fila, cambio_columna in direcciones:

            nueva_fila = fila + cambio_fila
            nueva_columna = columna + cambio_columna

            while (0 <= nueva_fila < FIL and
                   0 <= nueva_columna < COL):
                if estado_tablero[nueva_fila][nueva_columna] is not None:
                    break

                movimientos.append((nueva_fila, nueva_columna))

                nueva_fila += cambio_fila
                nueva_columna += cambio_columna

        return movimientos

    # * MÉTODO PARA MOVIMIENTOS DEL REY
    def movimientos_rey(self, estado_tablero, 
                         fila, columna):

        movimientos = []

        if self.nombre != "rey":
            return movimientos

        direcciones = [
            (-1, 0), # Arriba
            (1, 0),  # Abajo
            (0, -1), # Izquierda
            (0, 1),   # Derecha
            (-1, -1), # Arriba izquierda
            (-1, 1),  # Arriba derecha
            (1, -1),  # Abajo izquierda
            (1, 1)    # Abajo derecha
        ]

        for cambio_fila, cambio_columna in direcciones:

            nueva_fila = fila + cambio_fila
            nueva_columna = columna + cambio_columna

            if (0 <= nueva_fila < FIL and
                   0 <= nueva_columna < COL):
                
                if estado_tablero[nueva_fila][nueva_columna] is None:
                    movimientos.append((nueva_fila, nueva_columna))

        return movimientos

    # * MÉTODO PARA MOVIMIENTOS DE LA DAMA
    def movimientos_dama(self, estado_tablero, 
                         fila, columna):

        movimientos = []

        if self.nombre != "dama":
            return movimientos

        direcciones = [
            (-1, 0), # Arriba
            (1, 0),  # Abajo
            (0, -1), # Izquierda
            (0, 1),   # Derecha
            (-1, -1), # Arriba izquierda
            (-1, 1),  # Arriba derecha
            (1, -1),  # Abajo izquierda
            (1, 1)    # Abajo derecha
        ]

        for cambio_fila, cambio_columna in direcciones:

            nueva_fila = fila + cambio_fila
            nueva_columna = columna + cambio_columna

            while (0 <= nueva_fila < FIL and
                   0 <= nueva_columna < COL):
                
                if estado_tablero[nueva_fila][nueva_columna] is not None:
                    break

                movimientos.append((nueva_fila, nueva_columna))

                nueva_fila += cambio_fila
                nueva_columna += cambio_columna

        return movimientos

    # * MÉTODO PARA MOVIMIENTOS DEL CABALLO
    def movimientos_caballo(self, estado_tablero, 
                         fila, columna):

        movimientos = []

        if self.nombre != "caballo":
            return movimientos

        direcciones = [
            (-2, -1), # Arriba izquierda
            (-2, 1),  # Arriba derecha
            (2, -1), # Abajo izquierda
            (2, 1),   # Abajo derecha
            (-1, -2), # Izquierda arriba
            (1, -2),  # Izquierda abajo
            (-1, 2),  # Derecha arriba
            (1, 2)    # Derecha abajo
        ]

        for cambio_fila, cambio_columna in direcciones:

            nueva_fila = fila + cambio_fila
            nueva_columna = columna + cambio_columna

            if (0 <= nueva_fila < FIL and
                   0 <= nueva_columna < COL):
                
                if estado_tablero[nueva_fila][nueva_columna] is None:
                    movimientos.append((nueva_fila, nueva_columna))

        return movimientos

    # * MÉTODO PARA DIBUJAR UNA PIEZA
    def dibujar(self, tablero, fila, columna,
                inicio_x, inicio_y, tamanio):

        # * Calculamos el centro de la casilla
        x = inicio_x + columna * tamanio + tamanio / 2
        y = inicio_y + fila * tamanio + tamanio / 2

        # * Calculamos el tamaño de la imagen
        tam_imagen = max(1, int(tamanio * 0.85))

        # * Redimensionamos la imagen
        imagen = self.imagen.resize(
            (tam_imagen, tam_imagen),
            Image.Resampling.LANCZOS
        )

        # * Volteamos los caballos
        if self.nombre == "caballo" and columna == 1:
            imagen = ImageOps.mirror(imagen)

        # * Convertimos la imagen para Tkinter
        foto = ImageTk.PhotoImage(imagen)

        # * Conservamos la referencia
        tablero.imagenes.append(foto)

        # * Dibujamos la pieza
        tablero.create_image(
            x,
            y,
            image=foto
        )

# TODO: CREACIÓN DE LAS PIEZAS
piezas = {}

for color in ["blanco", "negro"]:
    for nombre in ["peon", "torre", "caballo", 
                   "alfil", "dama", "rey"]:
        piezas[f"{nombre}_{color}"] = Pieza(nombre, color)


# TODO: MATRIZ PARA REPRESENTAR EL TABLERO
estado_tablero = [
    [None for columna in range(COL)]
    for fila in range(FIL)
]

# TODO: POSICIONES INICIALES DE LAS PIEZAS
orden = [
    "torre", "caballo", "alfil", "dama",
    "rey", "alfil", "caballo", "torre"
]

for columna in range(COL):
    # * Colocamos los peones blancos y negros
    estado_tablero[6][columna] = piezas["peon_blanco"]
    estado_tablero[1][columna] = piezas["peon_negro"]

    # * Colocamos las piezas principales
    nombre = orden[columna]
    estado_tablero[7][columna] = piezas[f"{nombre}_blanco"]
    estado_tablero[0][columna] = piezas[f"{nombre}_negro"]

# TODO: CREACIÓN DE LA VENTANA
ventana = tk.Tk()
ventana.title("Juego del Ajedrez - Programación Para Todos")

ventana.geometry(
    f"{COL * TAM_CAS}x{FIL * TAM_CAS}"
)

# TODO: CREACIÓN DEL LIENZO
tablero = tk.Canvas(
    ventana,
    bg=COLOR_CLARO,
    highlightthickness=0
)

tablero.pack(fill='both', expand=True)

# TODO: CONTROL DE SELECCIÓN DE PIEZAS
pieza_seleccionada = None
movimientos_disponibles = []

# TODO: FUNCIÓN PARA DIBUJAR EL TABLERO

def dibujar_tablero(evento):
    tablero.delete("all")
    tablero.imagenes = []

    ancho = tablero.winfo_width()
    alto = tablero.winfo_height()

    tamanio = min(ancho / COL, alto / FIL)

    ancho_tablero = COL * tamanio
    alto_tablero = FIL * tamanio

    inicio_x = (ancho - ancho_tablero) / 2
    inicio_y = (alto - alto_tablero) / 2

    for fila in range(FIL):
        for columna in range(COL):
            x1 = inicio_x + columna * tamanio
            y1 = inicio_y + fila * tamanio

            x2 = x1 + tamanio
            y2 = y1 + tamanio

            if (fila + columna) % 2 == 0:
                color = COLOR_CLARO
            else:
                color = COLOR_OSCURO

            tablero.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                outline=color
            )

    # TODO: DIBUJAMOS TODAS LAS PIEZAS
    # TODO: DESDE LA MATRIZ

    for fila in range(FIL):
        for columna in range(COL):
            
            pieza = estado_tablero[fila][columna]

            if pieza is not None:
                pieza.dibujar(
                    tablero, fila, columna,
                    inicio_x, inicio_y, tamanio
                )

    # TODO: RESALTAR EL PÉON SELECCIONADO

    if pieza_seleccionada is not None:
        fila, columna = pieza_seleccionada

        x1 = inicio_x + columna * tamanio
        y1 = inicio_y + fila * tamanio

        tablero.create_rectangle(
            x1 + 2, y1 + 2,
            x1 + tamanio - 2, y1 + tamanio - 2,
            outline="#1B97D5",
            width=3
        )

    # TODO: RESALTAR MOVIMIENTOS DISPONIBLES

    for fila, columna in movimientos_disponibles:

        x1 = inicio_x + columna * tamanio
        y1 = inicio_y + fila * tamanio

        tablero.create_rectangle(
            x1 + 2, y1 + 2,
            x1 + tamanio - 2, y1 + tamanio - 2,
            outline="#DA4117",
            width=3
        )

# TODO: SELECCIONAR Y MOVER PIEZA
def seleccionar_casilla(evento):
    global pieza_seleccionada, movimientos_disponibles

    ancho = tablero.winfo_width()
    alto = tablero.winfo_height()

    tamanio = min(ancho / COL, alto / FIL)

    inicio_x = (ancho - COL * tamanio) / 2
    inicio_y = (alto - FIL * tamanio) / 2

    columna = int((evento.x - inicio_x) // tamanio)
    fila = int((evento.y - inicio_y) // tamanio)

    if not (0 <= fila < FIL and 0 <= columna < COL):
        return

    if (fila, columna) in movimientos_disponibles:
        fila_origen, columna_origen = pieza_seleccionada

        estado_tablero[fila][columna] = estado_tablero[fila_origen][columna_origen]
        estado_tablero[fila_origen][columna_origen] = None

        pieza_seleccionada = None
        movimientos_disponibles = []
    else:
        pieza = estado_tablero[fila][columna]
        if pieza is not None and pieza.nombre in ["peon", 
                                                  "torre", 
                                                  "alfil",
                                                  "rey",
                                                  "dama",
                                                  "caballo"]:
            pieza_seleccionada = (fila, columna)

            if pieza.nombre == "peon":
                movimientos_disponibles = pieza.movimientos_peon(
                    estado_tablero, fila, columna
                )

            elif pieza.nombre == "torre":
                movimientos_disponibles = pieza.movimientos_torre(
                    estado_tablero, fila, columna
                )        

            elif pieza.nombre == "alfil":
                movimientos_disponibles = pieza.movimientos_alfil(
                    estado_tablero, fila, columna
                )

            elif pieza.nombre == "rey":
                movimientos_disponibles = pieza.movimientos_rey(
                    estado_tablero, fila, columna
                )   

            elif pieza.nombre == "dama":
                movimientos_disponibles = pieza.movimientos_dama(
                    estado_tablero, fila, columna
                )

            elif pieza.nombre == "caballo":
                movimientos_disponibles = pieza.movimientos_caballo(
                    estado_tablero, fila, columna
                )
            
        else: 
            pieza_seleccionada = None
            movimientos_disponibles = []

    dibujar_tablero(tablero)

tablero.bind("<Configure>", dibujar_tablero)
tablero.bind("<Button-1>", seleccionar_casilla)

ventana.mainloop()