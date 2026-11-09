import tkinter as tk

# TODO: Para crear una estructura que almacene a cada pieza.
from dataclasses import dataclass
@dataclass
class Pieza:
    tipo  : int         # 1: Rey, 2: Reina, 3: Alfil, 4: Caballo, 5: Torre, 6: Peón
    icono : str         # "\u265A" "\u265B"  "\u265D"    "\u265E"  "\u265C" "\u265F"
    color : Color
    activa: bool = True # cuando es capturada la pieza, cambia su estado a false. Ej: torre.activa = False

# TODO: DEFINIMOS LOS COLORES QUE UTILIZAREMOS Y LOS CARACTERES DE LAS PIESAS.
from enum import Enum    # ? Para tener en uno solo lugar todos los colores.
class Color( Enum ):
    BLANCO = "white"     # ? Color de las piezas blancas.
    NEGRO  = "black"     # ? Color de las piezas negras.
    CLARO  = '#efd2b3' # ? Color del fondo claro del tablero de ajedrez
    OSCURO = '#cb6f3a' # ? Color del fondo oscuro del tablero de ajedrez

rey       = [1, "\u265A"]
reina     = [2, "\u265B"]
alfil     = [3, "\u265D"]
caballo   = [4, "\u265E"]
torre     = [5, "\u265C"]
peon      = [6, "\u265F"]

piezas_inicio = [ torre, caballo, alfil, reina, rey, alfil, caballo, torre ]

# TODO: TAMAÑO DEL TABLERO
FIL = 8
COL = 8

def crear_matriz( color, fila_piezas, fila_peones ):
    peones      = [ Pieza( peon[0], peon[1], color ) for _ in range( COL ) ]
    Jerarquicos = [ Pieza(    t[0],    t[1], color ) for t in piezas_inicio ]
    if fila_piezas < fila_peones:
        return [ Jerarquicos, peones ]
    else:
        return [ peones, Jerarquicos ]

piezas_negras  = crear_matriz( Color.NEGRO,  0, 1 )   # ? fila 0: las piezas jerarquicas y fila 1: los peones.
piezas_blancas = crear_matriz( Color.BLANCO, 7, 6 )   # ? fila 7: las piezas jerarquicas y fila 6: los peones.
vacias = [ [ None ] * COL for _ in range( FIL - 4 ) ] # ? Filas de la 2 a la 5 están vacias.
piezas_tablero = piezas_negras + vacias + piezas_blancas

# TODO: CREACIÓN DE LA VENTANA
ventana = tk.Tk()
ventana.title( "Juego del Ajedrez - Programación Para Todos" )
ventana.geometry( "480x480" ) # ! El cálculo solo se realiza para la cuadro inicial, despues depende del rezise.

# TODO: CREACIÓN DEL LIENZO
tablero = tk.Canvas(
    ventana,
    bg = Color.CLARO.value,
    highlightthickness = 0
)

tablero.pack( fill='both', expand=True )    # * PARA PODER REDIMENCIONAR EL TAMAÑO DEL LIENZO

tamanio = inicio_x = inicio_y = 0           # * Definimos las variables para utilizarlas como globales.

# TODO: FUNCIÓN PARA DIBUJAR EL TABLERO
def dibujar_tablero( evento ):
    global tamanio, inicio_x, inicio_y
    tablero.delete( "all" )

    ancho = evento.width
    alto  = evento.height

    tamanio    = min( ancho / COL, alto / FIL )
    tam_fuente = max( 1, int( tamanio * 0.65 ) )

    ancho_tablero = COL * tamanio
    alto_tablero  = FIL * tamanio

    inicio_x = ( ancho - ancho_tablero ) / 2
    inicio_y = y1 = ( alto - alto_tablero ) / 2

    # RECORREMOS TODAS LAS FILAS DEL TABLERO
    for fila in range( FIL ):
        y2 = y1 + tamanio
        x1 = inicio_x

        # RECORREMOS TODAS LAS COLUMNAS DEL TABLERO
        for columna in range( COL ):
            x2 = x1 + tamanio

            color = Color.OSCURO.value
            if ( fila + columna ) % 2 == 0:
                color = Color.CLARO.value

            tablero.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill    = color,
                outline = color
            )

            pieza = piezas_tablero[fila][columna]
            if pieza is not None:
                dibujarPieza( pieza, columna, fila, tam_fuente, "black" )

            x1 = x2

        y1 = y2

    # * Crearle un marco al tablero
    tablero.create_rectangle(
        inicio_x,
        inicio_y,
        inicio_x + COL * tamanio,
        inicio_y + FIL * tamanio,
        fill    = "",
        outline = "black",
        width   = 3
    )


def dibujarPieza( pieza, pos_x, pos_y, tam_fuente, color_borde ):
    fila    = inicio_y + pos_y * tamanio + tamanio / 2
    columna = inicio_x + pos_x * tamanio + tamanio / 2

    maximo  = 1
    if pieza.color.value == "white" :
        maximo = 2

    # TODO: DIBIJAMOS EL FONDO, GENERANDO LA IMPRESIÓN DE BORDE
    for dx in range( -maximo, maximo, 1 ):
        for dy in range( -maximo, maximo, 1 ):
            if ( dx == 0 and dy == 0 ):
                continue    # ! EL CENTRO SE DIBUJARÁ DESPUÉS DE TERMINAR EL FOR ANIDADO

            tablero.create_text (
                columna + dx,
                fila + dy,
                text = pieza.icono,
                font = (
                    "DejaVu Sans",
                    tam_fuente
                ),
                fill = color_borde
            )

    # DIBUJA EL CENTRO
    tablero.create_text(
            columna,
            fila,
            text=pieza.icono,
            font = (
                "DejaVu Sans",
                tam_fuente
            ),
            fill = pieza.color.value
        )

tablero.bind( "<Configure>", dibujar_tablero )

ventana.mainloop()