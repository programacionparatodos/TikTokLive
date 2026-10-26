import tkinter as tk

# TODO: CONFIGURACIÓN DEL TABLERO

TAM_CAS = 60
FIL = 8
COL= 8

COLOR_CLARO = '#efd2b3'
COLOR_OSCURO = '#cb6f3a'

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

# TODO: FUNCIÓN PARA DIBUJAR EL TABLERO

def dibujar_tablero(evento):
    tablero.delete("all")

    ancho = evento.width
    alto = evento.height

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


    # TODO: DIBUJAMOS LOS PEONES BLANCOS
    fila = 6

    for columna in range(COL):
        x = inicio_x + columna * tamanio + tamanio / 2
        y = inicio_y + fila * tamanio + tamanio / 2
        tam_fuente = max(1, int(tamanio * 0.65))
        
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0 ,1, 2]:
                tablero.create_text(
                        x + dx,
                        y + dy,
                        text="\u265F",
                        font=(
                            "DejaVu Sans",
                            tam_fuente
                        ),
                        fill="black"
                    )
                    
        tablero.create_text(
                x,
                y,
                text="\u265F",
                font=(
                    "DejaVu Sans",
                    tam_fuente
                ),
                fill="white"
            )

    # TODO: DIBUJAMOS LOS PEONES NEGROS
    fila = 1
    
    for columna in range(COL):
        x = inicio_x + columna * tamanio + tamanio / 2
        y = inicio_y + fila * tamanio + tamanio / 2
        tam_fuente = max(1, int(tamanio * 0.65))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0 ,1]:
                tablero.create_text(
                    x + dx,
                    y + dy,
                    text="\u265F",
                    font=(
                        "DejaVu Sans",
                        tam_fuente
                    ),
                    fill="black"
                )
                                    
        tablero.create_text(
                x,
                y,
                text="\u265F",
                font=(
                    "DejaVu Sans",
                    tam_fuente
                ),
                fill="black"
            )

    



tablero.bind("<Configure>", dibujar_tablero)

ventana.mainloop()