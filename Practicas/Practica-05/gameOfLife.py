import pygame
import numpy as np

# Dimensiones de la cuadricula y de las celulas (las celdas de la cuadricula)
n_celdas_x = 50
n_celdas_y = 50

# Colores 😈
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
GRIS = (128, 128, 128)
MORADO = (128, 0, 128)
CELESTE = (152, 245, 255)

# Colores mas Colorful 😈😈😈
ROJOFUERTE = (89, 2, 2)
ROJOBONITO = (191, 4, 4)
AZULFUERTE = (4, 104, 191)
AZULCLARITO = (5, 175, 242)

# Inicializamos a Pygame
pygame.init()

# Tamaño de las celdas de la cuadricula, al modificar este valor se modifica el tamaño de las celdas de la cuadricula
# Y por ende, tambien el de toda la pantalla
celda_tam = 0

# Obtenemos la informacion de la pantalla
pantalla_info = pygame.display.Info()

# Calculamos dinamicamente el tamaño de las celdas de acuerdo a la altura de la pantalla donde se 
# despliega la aplicacion, para ello multiplicamos el tamaño y numero de celdas y verificamos
# que no exceda la altura.
while celda_tam * n_celdas_y < pantalla_info.current_h - 150: #-150 que utilizan los botones inferiores
    celda_tam += 1

# Configuramos la pantalla en la que desplegaremos la cuadricula
pantalla_tam = (n_celdas_x * celda_tam, n_celdas_y * celda_tam + 50)
pantalla = pygame.display.set_mode(pantalla_tam)

# Nombre de la aplicacion 🐎
pygame.display.set_caption("Juego de la Vida de Conway")

# Reloj para controlar la velocidad de las generaciones
# esta variable claramente existe porque sabiamos que si no existia podiamos llegar a la generacion 1000
# en muy poco tiempo y no porque al probar este programa llegamos al millon a la velocidad de la luz XD
reloj = pygame.time.Clock()

# Funcion para contar las celulas vivas de todo el tablero
def contar_celulas_vivas(tablero):
    return np.sum(tablero)

# Funcion para dibujar la cuadricula y las celulas (las celdas de la cuadricula)
def dibujar(tablero):
    pantalla.fill(NEGRO)  # Definimos el color que queremos para el fondo de la pantalla
    for y in range(n_celdas_y):
        for x in range(n_celdas_x):
            if tablero[x, y]:
                pygame.draw.rect(pantalla, CELESTE,
                                 (x * celda_tam, y * celda_tam, celda_tam, celda_tam))  # Dibujamos las celulas vivas
            pygame.draw.rect(pantalla, GRIS, (x * celda_tam, y * celda_tam, celda_tam, celda_tam),
                             1)  # Dibujamos la cuadricula

    # Dibujar botones
    #pygame.draw.rect(pantalla, MORADO, (10, pantalla_tam[1] - 40, 30, 30))  # Boton de Pausa
    #pygame.draw.rect(pantalla, AZUL, (50, pantalla_tam[1] - 40, 30, 30))    # Boton de Play
    #pygame.draw.rect(pantalla, ROJO, (90, pantalla_tam[1] - 40, 30, 30))    # Boton para borrar toda la cuadricula

    #pygame.draw.rect(pantalla, NEGRO, (10, pantalla_tam[1] - 40, 30, 30),2)  # Color para el contorno del boton de Pausa
    #pygame.draw.rect(pantalla, NEGRO, (50, pantalla_tam[1] - 40, 30, 30),2)  # Color para el contorno del boton de Play
    #pygame.draw.rect(pantalla, NEGRO, (90, pantalla_tam[1] - 40, 30, 30),2)  # Color para el contorno del boton de borrado
        
    # Cargar imagenes
    imagen_pausa = pygame.image.load("Imagenes/Pausa.png")
    imagen_play = pygame.image.load("Imagenes/PlayDefinitivo.png")
    imagen_limpiar = pygame.image.load("Imagenes/Borrado-Stop.png")
    imagen_aleatorio = pygame.image.load("Imagenes/Aleatorio.png")

    # Escalar imagenes al tamaño deseado
    imagen_pausa = pygame.transform.scale(imagen_pausa, (30, 30))
    imagen_play = pygame.transform.scale(imagen_play, (30, 30))
    imagen_limpiar = pygame.transform.scale(imagen_limpiar, (30, 30))
    imagen_aleatorio = pygame.transform.scale(imagen_aleatorio, (30, 30))

    # Dibujar imagenes en lugar de botones
    pantalla.blit(imagen_pausa, (10, pantalla_tam[1] - 40))
    pantalla.blit(imagen_play, (50, pantalla_tam[1] - 40))
    pantalla.blit(imagen_limpiar, (90, pantalla_tam[1] - 40))
    pantalla.blit(imagen_aleatorio, (130, pantalla_tam[1] - 40))

    # Posiciones de los botones
    posicion_pausa = (10, pantalla_tam[1] - 40)
    posicion_play = (50, pantalla_tam[1] - 40)
    posicion_borrar = (90, pantalla_tam[1] - 40)
    posicion_aleatorio = (130, pantalla_tam[1] - 40)

    # # Texto con el numero de generaciones y celulas vivas
    font = pygame.font.Font(None, 24)
    
    #texto = font.render("Generaciones: " + str(generaciones), True, NEGRO)
    texto = font.render("Generaciones: " + str(generaciones), True, BLANCO)
    pantalla.blit(texto, (pantalla_tam[0] - 200, pantalla_tam[1] - 40))

    #texto = font.render("Celulas vivas: " + str(celulas_vivas), True, NEGRO)
    texto = font.render("Celulas vivas: " + str(celulas_vivas), True, BLANCO)
    pantalla.blit(texto, (pantalla_tam[0] - 200, pantalla_tam[1] - 20))



# Inicializamos el tablero y sus variables
tablero = np.zeros((n_celdas_x, n_celdas_y), dtype=bool)

# Iniciamos las generaciones en 0
generaciones = 0

# Iniciamos las celulas vivas en 0
celulas_vivas = 0

# Iniciamos a ejecutando y jugando en sus valores por defecto
ejecutando = True
jugando = False

# Bucle principal
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El evento QUIT es para cerrar la ejecucion, en este caso, darle clic al boton de cerrar ventana
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:  # MOUSEBUTTONDOWN es el evento de pygame de hacer un "clic"
            pos = pygame.mouse.get_pos()
            # Boton de Pausa
            if 10 <= pos[0] <= 40 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                jugando = False
            # Boton de Play
            elif 50 <= pos[0] <= 80 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                jugando = True
            # Boton para borrar toda la cuadricula y ponerla en pausa
            elif 90 <= pos[0] <= 120 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                tablero = np.zeros((n_celdas_x, n_celdas_y), dtype=bool)
                generaciones = 0
                celulas_vivas = 0
                jugando = False
            # Boton para generar un tablero aleatorio
            elif 130 <= pos[0] <= 160 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                tablero = np.random.choice([False, True], (n_celdas_x, n_celdas_y), p=[0.7, 0.3])
                generaciones = 0
                celulas_vivas = contar_celulas_vivas(tablero)
                jugando = False
            else:  # Si no se hizo clic en un boton, verificar si se hizo clic en una celda del tablero
                if not jugando:  # Con este poderoso if evitamos que se modifique el tablero por el usuario mientras se genera alguna generacion
                    cel_x, cel_y = pos[0] // celda_tam, pos[1] // celda_tam
                    if 0 <= cel_x < n_celdas_x and 0 <= cel_y < n_celdas_y:
                        tablero[cel_x, cel_y] = not tablero[cel_x, cel_y]
                        celulas_vivas = contar_celulas_vivas(tablero)

    # Dibujamos el tablero
    dibujar(tablero)
    pygame.display.flip()

    # IMPORTANTE: Este es el nucleo de el juego de la vida de Conway, aqui implementamos las reglas del juego
    if jugando:
        generaciones += 1  # Aumentamos el contador de generaciones
        tablero_siguiente = np.copy(
            tablero)    # Creamos una copia del tablero actual para poder modificarlo sin afectar el tablero original
        # (esta copia solo se guarda en codigo y no se dibuja o se muestra en pantalla)
        for x in range(n_celdas_x):
            for y in range(n_celdas_y):
                vecinos = np.sum(tablero[(x - 1):(x + 2), (y - 1):(y + 2)]) - tablero[x, y]  # Contamos los vecinos vivos de cada celula (celda)
                if tablero[x, y] and (vecinos < 2 or vecinos > 3):  # En caso de que la celula este viva y tenga menos de 2 o mas de 3
                    # vecinos vivos, la celula muere brutalmente 😢
                    tablero_siguiente[x, y] = False
                elif not tablero[x, y] and vecinos == 3:  # En caso de que la celula este muerta y tenga exactamente 3 vecinos vivos
                    # La celula revive y ahora esta viva 😎
                    tablero_siguiente[x, y] = True
        tablero = tablero_siguiente
        celulas_vivas = contar_celulas_vivas(tablero)
        reloj.tick(5)  # Velocidad con la que se van a generar las generaciones

# Comando poderoso para salir de Pygame 
pygame.quit()
