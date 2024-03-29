import pygame
import numpy as np
import random 

# Dimensiones de la cuadrícula y de las celulas (las celdas de la cuadricula)
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
# celulaDefault = Celula(NEGRO, False, 0, 0)
# celulaRoja = Celula(ROJOFUERTE, False, 0, 0)
# celulaAzul = Celula(AZULCLARITO, False, 0, 0)
ROJOFUERTE = (89, 2, 2)
ROJOBONITO = (191, 4, 4)
AZULFUERTE = (4, 104, 191)
AZULCLARITO = (5, 175, 242)

# Inicializamos a Pygame
pygame.init()

# Tamaño de las celdas de la cuadrícula, al modificar este valor se modifica el tamaño de las celdas de la cuadricula
# Y por ende, también el de toda la pantalla
celda_tam = 0

# Obtenemos la información de la pantalla
pantalla_info = pygame.display.Info()

# Calculamos dinámicamente el tamaño de las celdas de acuerdo a la altura de la pantalla donde se 
# despliega la aplicación, para ello multiplicamos el tamaño y número de celdas y verificamos
# que no exceda la altura.
while celda_tam * n_celdas_y < pantalla_info.current_h - 150: #-150 que utilizan los botones inferiores
    celda_tam += 1

# Configuramos la pantalla en la que desplegaremos la cuadrícula
pantalla_tam = (n_celdas_x * celda_tam, n_celdas_y * celda_tam + 50)
pantalla = pygame.display.set_mode(pantalla_tam)

# Nombre de la aplicación 🐎
pygame.display.set_caption("Juego de la Vida de Conway")

# Reloj para controlar la velocidad de las generaciones
# esta variable claramente existe porque sabíamos que si no existía podíamos llegar a la generación 1000
# en muy poco tiempo y no porque al probar este programa llegamos al millón a la velocidad de la luz XD
reloj = pygame.time.Clock()

# Clase Celula
#   Atributos: Color de la celula, estado (viva o muerta)
class Celula:
    def __init__(self, color):
        self.color = color
        #self.estado = estado 
        #self.x = x
        #self.y = y
    
    # Metodo para saber si es una celula muerta
    def esCelulaMuerta(self):
        return self.color == NEGRO
    
    def esCelulaRoja(self):
        return self.color == ROJOFUERTE
    
    def esCelulaAzul(self):
        return self.color == AZULCLARITO
    
    # Metodo para saber si es una celula viva (roja o azul)
    def esCelulaViva(self):
        return self.color == ROJOFUERTE or self.color == AZULCLARITO
    



# Función para contar las celulas vivas de todo el tablero
def contar_celulas_vivas(tablero):
    return np.sum(tablero)

def encontrar_celulas(tablero, color_celula):
    celulas: set = set()
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j].color == color_celula:
                celulas.add((i,j))
    return celulas

def encontrar_vecinos(tablero, x, y, color_celula) -> int:
    total = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i+x >= len(tablero) or i+x <= 0: continue
            if i == 0 and j == 0: continue
            if j+y >= len(tablero) or j+y <= 0: continue
            if tablero[i+x,j+y].color == color_celula: total += 1
    return total
    

# Función para dibujar la cuadricula y las celulas (las celdas de la cuadrícula)
def dibujar(tablero):
    pantalla.fill(NEGRO)  # Definimos el color que queremos para el fondo de la pantalla
    for y in range(n_celdas_y):
        for x in range(n_celdas_x):
            if tablero[x, y]:
                pygame.draw.rect(pantalla, tablero[x, y].color, 
                                 (x * celda_tam, y * celda_tam, celda_tam, celda_tam))  # Dibujamos las celulas vivas
            pygame.draw.rect(pantalla, GRIS, (x * celda_tam, y * celda_tam, celda_tam, celda_tam),1)  # Dibujamos la cuadricula

    # Dibujar botones
    #pygame.draw.rect(pantalla, MORADO, (10, pantalla_tam[1] - 40, 30, 30))  # Botón de Pausa
    #pygame.draw.rect(pantalla, AZUL, (50, pantalla_tam[1] - 40, 30, 30))    # Botón de Play
    #pygame.draw.rect(pantalla, ROJO, (90, pantalla_tam[1] - 40, 30, 30))    # Botón para borrar toda la cuadricula

    #pygame.draw.rect(pantalla, NEGRO, (10, pantalla_tam[1] - 40, 30, 30),2)  # Color para el contorno del botón de Pausa
    #pygame.draw.rect(pantalla, NEGRO, (50, pantalla_tam[1] - 40, 30, 30),2)  # Color para el contorno del boton de Play
    #pygame.draw.rect(pantalla, NEGRO, (90, pantalla_tam[1] - 40, 30, 30),2)  # Color para el contorno del botón de borrado
        
    # Cargar imágenes
    imagen_pausa = pygame.image.load("Imagenes/Pausa.png")
    imagen_play = pygame.image.load("Imagenes/PlayDefinitivo.png")
    imagen_limpiar = pygame.image.load("Imagenes/Borrado-Stop.png")
    imagen_aleatorio = pygame.image.load("Imagenes/Aleatorio.png")

    # Escalar imágenes al tamaño deseado
    imagen_pausa = pygame.transform.scale(imagen_pausa, (30, 30))
    imagen_play = pygame.transform.scale(imagen_play, (30, 30))
    imagen_limpiar = pygame.transform.scale(imagen_limpiar, (30, 30))
    imagen_aleatorio = pygame.transform.scale(imagen_aleatorio, (30, 30))

    # Dibujar imágenes en lugar de botones
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
#tablero = np.zeros((n_celdas_x, n_celdas_y), dtype=object(Celula(NEGRO, False)))
    
#tablero = np.full((n_celdas_x, n_celdas_y), Celula(NEGRO), dtype=object)
    
tablero = np.empty((n_celdas_x, n_celdas_y), dtype=object)
tablero.fill(Celula(NEGRO))

# tablero = np.empty((n_celdas_x, n_celdas_y), dtype=object)
# for i in range(n_celdas_x):
#     for j in range(n_celdas_y):
#         tablero[i,j] = Celula(NEGRO)


# Iniciamos las generaciones en 0
generaciones = 0

# Iniciamos las celulas vivas en 0
celulas_vivas = 0

# Iniciamos a ejecutando y jugando en sus valores por defecto
ejecutando = True
jugando = False


# celulaDefault = Celula(NEGRO, False, 0, 0)
# celulaRoja    = Celula(ROJOFUERTE, False, 0, 0)
# celulaAzul    = Celula(AZULCLARITO, False, 0, 0)
celulas_muertas: set = encontrar_celulas(tablero, NEGRO)
celulas_azules: set = set()
celulas_rojas: set = set()

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
                tablero.fill(Celula(NEGRO))
                celulas_muertas = encontrar_celulas(tablero, NEGRO)
                celulas_azules = encontrar_celulas(tablero, ROJOFUERTE)
                celulas_rojas = encontrar_celulas(tablero, AZULCLARITO)
                celulas_vivas = len(celulas_azules) + len(celulas_rojas)
                jugando = False
            # Boton para generar un tablero aleatorio
            elif 130 <= pos[0] <= 160 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10: # BV
                tablero = np.random.choice([Celula(NEGRO), Celula(ROJOFUERTE), Celula(AZULCLARITO)], (n_celdas_x, n_celdas_y), p=[0.5, 0.3, 0.2])
                generaciones = 0
                celulas_muertas = encontrar_celulas(tablero, NEGRO)
                celulas_azules = encontrar_celulas(tablero, ROJOFUERTE)
                celulas_rojas = encontrar_celulas(tablero, AZULCLARITO)
                celulas_vivas = len(celulas_azules) + len(celulas_rojas)
                jugando = False
            else:  # Si no se hizo clic en un boton, verificar si se hizo clic en una celda del tablero
                if not jugando:  # Con este poderoso if evitamos que se modifique el tablero por el usuario mientras se genera alguna generacion
                    cel_x, cel_y = pos[0] // celda_tam, pos[1] // celda_tam
                    if 0 <= cel_x < n_celdas_x and 0 <= cel_y < n_celdas_y:
                        tablero[cel_x, cel_y] = Celula(AZULCLARITO)
                        celulas_azules.add((cel_x,cel_y))
                        celulas_muertas.remove((cel_x,cel_y))
                        celulas_vivas = len(celulas_azules) + len(celulas_rojas)

    # Dibujamos el tablero
    dibujar(tablero)
    pygame.display.flip()

    # (a) Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.
    # (b) Si una célula está muerta y tiene tres vecinas vivas, nace.
    # (c) Si una célula está viva y tiene más de tres vecinas vivas, muere.
    # IMPORTANTE: Este es el nucleo de el juego de la vida de Conway, aqui implementamos las reglas del juego
    if jugando:
        generaciones += 1  # Aumentamos el contador de generaciones
        tablero_siguiente = np.copy(tablero)    # Creamos una copia del tablero actual para poder modificarlo sin afectar el tablero original
        # (esta copia solo se guarda en código y no se dibuja o se muestra en pantalla)
        for x in range(n_celdas_x):
            for y in range(n_celdas_y):
                vecinos = encontrar_vecinos(tablero, x, y, AZULCLARITO)
                if tablero[x, y].esCelulaAzul() and (vecinos < 2 or vecinos > 3):  # En caso de que la célula este viva y tenga menos de 2 o mas de 3
                    # vecinos vivos, la célula muere brutalmente 😢
                    tablero_siguiente[x, y] = Celula(NEGRO)
                    celulas_muertas.add((x,y))
                    celulas_azules.remove((x,y))
                elif tablero[x, y].esCelulaMuerta() and vecinos == 3:  # En caso de que la celula este muerta y tenga exactamente 3 vecinos vivos
                    # La célula revive y ahora esta viva 😎
                    tablero_siguiente[x, y] = Celula(AZULCLARITO)
                    celulas_azules.add((x,y))
                    celulas_muertas.remove((x,y))
        tablero = tablero_siguiente
        celulas_vivas = len(celulas_azules)
        reloj.tick(5)  # Velocidad con la que se van a generar las generaciones

# Comando poderoso para salir de Pygame 
pygame.quit()
