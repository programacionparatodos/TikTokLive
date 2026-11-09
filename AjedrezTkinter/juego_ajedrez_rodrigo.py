import tkinter as tk
from dataclasses import dataclass
from enum import Enum    # ? Para tener en uno solo lugar todos los colores.

# TODO: DEFINIMOS LOS COLORES QUE UTILIZAREMOS Y LOS CARACTERES DE LAS PIEZAS.
# (Color debe definirse ANTES de Pieza, porque Pieza lo usa como anotación de tipo)
class Color( Enum ):
    BLANCO = "white"     # ? Color de las piezas blancas.
    NEGRO  = "black"     # ? Color de las piezas negras.
    CLARO  = '#efd2b3'   # ? Color del fondo claro del tablero de ajedrez
    OSCURO = '#cb6f3a'   # ? Color del fondo oscuro del tablero de ajedrez

# TODO: Para crear una estructura que almacene a cada pieza.
@dataclass
class Pieza:
    tipo  : int         # 1: Rey, 2: Reina, 3: Alfil, 4: Caballo, 5: Torre, 6: Peón
    icono : str         # "\u265A" "\u265B"  "\u265D"    "\u265E"  "\u265C" "\u265F"
    color : Color
    activa: bool = True # cuando es capturada la pieza, cambia su estado a false. Ej: torre.activa = False

# Constantes para los tipos de pieza (más legible que usar números sueltos)
REY, REINA, ALFIL, CABALLO, TORRE, PEON = 1, 2, 3, 4, 5, 6

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


# =====================================================================
# TODO: ESTADO DEL JUEGO
# =====================================================================
turno                = Color.BLANCO   # Empiezan las blancas
seleccion            = None           # (fila, columna) de la pieza seleccionada
movimientos_validos  = []             # Lista de (fila, columna) a donde puede ir la pieza seleccionada
piezas_capturadas    = []             # Historial de piezas capturadas
juego_terminado      = False


# =====================================================================
# TODO: FUNCIONES DE MOVIMIENTO DE CADA PIEZA
# Cada función devuelve una lista de casillas (fila, columna) a las que
# la pieza PODRÍA ir (sin considerar todavía si deja al propio rey en jaque).
# =====================================================================
def en_tablero( fila, columna ):
    """True si la casilla está dentro del tablero."""
    return 0 <= fila < FIL and 0 <= columna < COL


def color_contrario( color ):
    return Color.NEGRO if color == Color.BLANCO else Color.BLANCO


def _movimientos_deslizantes( fila, columna, pieza, direcciones ):
    """Movimientos de piezas que avanzan en línea recta hasta chocar (alfil, torre, reina)."""
    movimientos = []
    for df, dc in direcciones:
        f, c = fila + df, columna + dc
        while en_tablero( f, c ):
            destino = piezas_tablero[f][c]
            if destino is None:
                movimientos.append( ( f, c ) )          # casilla libre: seguimos avanzando
            else:
                if destino.color != pieza.color:
                    movimientos.append( ( f, c ) )      # captura de pieza enemiga
                break                                   # cualquier pieza bloquea el camino
            f += df
            c += dc
    return movimientos


def _movimientos_saltos( fila, columna, pieza, saltos ):
    """Movimientos de piezas que dan un paso fijo (caballo y rey)."""
    movimientos = []
    for df, dc in saltos:
        f, c = fila + df, columna + dc
        if not en_tablero( f, c ):
            continue
        destino = piezas_tablero[f][c]
        if destino is None or destino.color != pieza.color:
            movimientos.append( ( f, c ) )
    return movimientos


def movimientos_rey( fila, columna, pieza ):
    saltos = [ ( -1, -1 ), ( -1, 0 ), ( -1, 1 ),
               (  0, -1 ),            (  0, 1 ),
               (  1, -1 ), (  1, 0 ), (  1, 1 ) ]
    return _movimientos_saltos( fila, columna, pieza, saltos )


def movimientos_reina( fila, columna, pieza ):
    direcciones = [ ( -1, -1 ), ( -1, 0 ), ( -1, 1 ), ( 0, -1 ),
                    (  0,  1 ), (  1, -1 ), (  1, 0 ), ( 1,  1 ) ]
    return _movimientos_deslizantes( fila, columna, pieza, direcciones )


def movimientos_alfil( fila, columna, pieza ):
    direcciones = [ ( -1, -1 ), ( -1, 1 ), ( 1, -1 ), ( 1, 1 ) ]
    return _movimientos_deslizantes( fila, columna, pieza, direcciones )


def movimientos_caballo( fila, columna, pieza ):
    saltos = [ ( -2, -1 ), ( -2, 1 ), ( -1, -2 ), ( -1, 2 ),
               (  1, -2 ), (  1, 2 ), (  2, -1 ), (  2, 1 ) ]
    return _movimientos_saltos( fila, columna, pieza, saltos )


def movimientos_torre( fila, columna, pieza ):
    direcciones = [ ( -1, 0 ), ( 1, 0 ), ( 0, -1 ), ( 0, 1 ) ]
    return _movimientos_deslizantes( fila, columna, pieza, direcciones )


def movimientos_peon( fila, columna, pieza ):
    movimientos = []
    # Las blancas suben (fila disminuye), las negras bajan (fila aumenta)
    if pieza.color == Color.BLANCO:
        direccion, fila_inicial = -1, 6
    else:
        direccion, fila_inicial = 1, 1

    # Avance de una casilla (solo si está libre)
    f = fila + direccion
    if en_tablero( f, columna ) and piezas_tablero[f][columna] is None:
        movimientos.append( ( f, columna ) )

        # Avance de dos casillas desde la fila inicial (ambas casillas libres)
        f2 = fila + 2 * direccion
        if fila == fila_inicial and piezas_tablero[f2][columna] is None:
            movimientos.append( ( f2, columna ) )

    # Capturas en diagonal (solo si hay una pieza enemiga)
    for dc in ( -1, 1 ):
        c = columna + dc
        if en_tablero( f, c ):
            destino = piezas_tablero[f][c]
            if destino is not None and destino.color != pieza.color:
                movimientos.append( ( f, c ) )

    return movimientos


# Diccionario que relaciona el tipo de pieza con su función de movimiento
MOVIMIENTOS = {
    REY    : movimientos_rey,
    REINA  : movimientos_reina,
    ALFIL  : movimientos_alfil,
    CABALLO: movimientos_caballo,
    TORRE  : movimientos_torre,
    PEON   : movimientos_peon,
}


def movimientos_posibles( fila, columna ):
    """Movimientos de la pieza en (fila, columna) sin considerar jaques."""
    pieza = piezas_tablero[fila][columna]
    if pieza is None:
        return []
    return MOVIMIENTOS[ pieza.tipo ]( fila, columna, pieza )


# =====================================================================
# TODO: JAQUE Y MOVIMIENTOS LEGALES
# =====================================================================
def rey_en_jaque( color ):
    """True si el rey de ese color está siendo atacado."""
    pos_rey = None
    for f in range( FIL ):
        for c in range( COL ):
            p = piezas_tablero[f][c]
            if p is not None and p.tipo == REY and p.color == color:
                pos_rey = ( f, c )

    if pos_rey is None:
        return False

    # ¿Alguna pieza enemiga puede llegar a la casilla del rey?
    for f in range( FIL ):
        for c in range( COL ):
            p = piezas_tablero[f][c]
            if p is not None and p.color != color:
                if pos_rey in movimientos_posibles( f, c ):
                    return True
    return False


def movimientos_legales( fila, columna ):
    """Movimientos posibles que NO dejan al propio rey en jaque."""
    pieza = piezas_tablero[fila][columna]
    legales = []

    for ( nf, nc ) in movimientos_posibles( fila, columna ):
        # Simulamos el movimiento
        capturada = piezas_tablero[nf][nc]
        piezas_tablero[nf][nc]       = pieza
        piezas_tablero[fila][columna] = None

        if not rey_en_jaque( pieza.color ):
            legales.append( ( nf, nc ) )

        # Deshacemos el movimiento
        piezas_tablero[fila][columna] = pieza
        piezas_tablero[nf][nc]        = capturada

    return legales


def tiene_movimientos( color ):
    """True si el jugador de ese color tiene al menos un movimiento legal."""
    for f in range( FIL ):
        for c in range( COL ):
            p = piezas_tablero[f][c]
            if p is not None and p.color == color and movimientos_legales( f, c ):
                return True
    return False


# =====================================================================
# TODO: MOVER UNA PIEZA
# =====================================================================
def mover_pieza( origen, destino ):
    """Mueve la pieza de 'origen' a 'destino', capturando si es necesario."""
    fo, co = origen
    fd, cd = destino
    pieza = piezas_tablero[fo][co]

    # Captura
    capturada = piezas_tablero[fd][cd]
    if capturada is not None:
        capturada.activa = False            # la pieza capturada queda inactiva
        piezas_capturadas.append( capturada )

    piezas_tablero[fd][cd] = pieza
    piezas_tablero[fo][co] = None

    # Promoción: el peón que llega al final se convierte en reina
    if pieza.tipo == PEON and ( fd == 0 or fd == FIL - 1 ):
        pieza.tipo  = REINA
        pieza.icono = reina[1]


def cambiar_turno():
    """Alterna el turno y revisa jaque, jaque mate o tablas."""
    global turno, juego_terminado
    turno = color_contrario( turno )
    nombre = "Blancas" if turno == Color.BLANCO else "Negras"

    en_jaque = rey_en_jaque( turno )
    if not tiene_movimientos( turno ):
        juego_terminado = True
        if en_jaque:
            ganador = "Negras" if turno == Color.BLANCO else "Blancas"
            etiqueta.config( text = f"¡Jaque mate! Ganan las {ganador}" )
        else:
            etiqueta.config( text = "Tablas por rey ahogado" )
    elif en_jaque:
        etiqueta.config( text = f"Turno de las {nombre} - ¡JAQUE!" )
    else:
        etiqueta.config( text = f"Turno de las {nombre}" )


# =====================================================================
# TODO: MANEJO DEL CLIC DEL MOUSE
# =====================================================================
def al_hacer_clic( evento ):
    global seleccion, movimientos_validos

    if juego_terminado or tamanio == 0:
        return

    # Convertimos la posición del clic (píxeles) en fila y columna
    columna = int( ( evento.x - inicio_x ) // tamanio )
    fila    = int( ( evento.y - inicio_y ) // tamanio )
    if not en_tablero( fila, columna ):
        return

    pieza = piezas_tablero[fila][columna]

    # 1) Si ya hay una pieza seleccionada y se hizo clic en un destino válido: mover
    if seleccion is not None and ( fila, columna ) in movimientos_validos:
        mover_pieza( seleccion, ( fila, columna ) )
        seleccion           = None
        movimientos_validos = []
        cambiar_turno()

    # 2) Si se hizo clic en una pieza propia: seleccionarla
    elif pieza is not None and pieza.color == turno:
        seleccion           = ( fila, columna )
        movimientos_validos = movimientos_legales( fila, columna )

    # 3) Cualquier otro clic: quitar la selección
    else:
        seleccion           = None
        movimientos_validos = []

    dibujar_tablero()


# TODO: CREACIÓN DE LA VENTANA
ventana = tk.Tk()
ventana.title( "Juego del Ajedrez - Programación Para Todos" )
ventana.geometry( "480x510" ) # ! El cálculo solo se realiza para la cuadro inicial, despues depende del rezise.

etiqueta = tk.Label( ventana, text = "Turno de las Blancas", font = ( "Arial", 12 ) )
etiqueta.pack( side = 'top', pady = 4 )

# TODO: CREACIÓN DEL LIENZO
tablero = tk.Canvas(
    ventana,
    bg = Color.CLARO.value,
    highlightthickness = 0
)

tablero.pack( fill='both', expand=True )    # * PARA PODER REDIMENCIONAR EL TAMAÑO DEL LIENZO

tamanio = inicio_x = inicio_y = 0           # * Definimos las variables para utilizarlas como globales.

# TODO: FUNCIÓN PARA DIBUJAR EL TABLERO
def dibujar_tablero( evento = None ):
    global tamanio, inicio_x, inicio_y
    tablero.delete( "all" )

    # Si viene del evento <Configure> usamos su tamaño; si no, el tamaño actual del lienzo
    if evento is not None:
        ancho = evento.width
        alto  = evento.height
    else:
        ancho = tablero.winfo_width()
        alto  = tablero.winfo_height()

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

            pieza = piezas_tablero[fila][columna]

            # Resaltados: casilla seleccionada y capturas posibles
            if seleccion == ( fila, columna ):
                color = "#f6f669"          # amarillo: pieza seleccionada
            elif ( fila, columna ) in movimientos_validos and pieza is not None:
                color = "#e8725a"          # rojo: se puede capturar aquí

            tablero.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill    = color,
                outline = color
            )

            # Punto en las casillas vacías a las que se puede mover
            if ( fila, columna ) in movimientos_validos and pieza is None:
                r  = tamanio * 0.15
                cx = x1 + tamanio / 2
                cy = y1 + tamanio / 2
                tablero.create_oval(
                    cx - r, cy - r, cx + r, cy + r,
                    fill = "#6b8e4e", outline = ""
                )

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
tablero.bind( "<Button-1>",  al_hacer_clic )   # Clic izquierdo del mouse

ventana.mainloop()