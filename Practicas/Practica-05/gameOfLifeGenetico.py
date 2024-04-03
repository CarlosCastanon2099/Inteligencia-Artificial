import pygame
import numpy as np
import random 
  
### Algotimos genetico para el juego de la vida de Conway

"""    
🕹️ Pygame
"""
pygame.init()
# Obtenemos la informacion de la pantalla
pantalla_info = pygame.display.Info()
# Nombre de la aplicacion 🐎
pygame.display.set_caption("Juego de la Vida de Conway")
# Reloj para controlar la velocidad de las generaciones. Esta variable claramente existe 
# porque sabiamos que si no existia podiamos llegar a la generacion 1000 en muy poco tiem-
# po y no porque al probar este programa llegamos al millon a la velocidad de la luz XD
reloj = pygame.time.Clock()

"""    
⬛ Dimensiones de la cuadricula y celdas
"""
n_celdas_x = 50
n_celdas_y = 50
# Tamaño de las celdas de la cuadricula, al modificar este valor se modifica el tamaño de 
# las celdas de la cuadricula y por ende, tambien el de toda la pantalla.
celda_tam = 0
# Calculamos dinamicamente el tamaño de las celdas de acuerdo a la altura de la pantalla 
# donde se despliega la aplicacion, para ello multiplicamos el tamaño y numero de celdas 
# y verificamos que no exceda la altura.
while celda_tam * n_celdas_y < pantalla_info.current_h - 150: # -150 que utilizan los botones inferiores
    celda_tam += 1
# Configuramos la pantalla en la que desplegaremos la cuadricula
pantalla_tam = (n_celdas_x * celda_tam, n_celdas_y * celda_tam + 50)
pantalla = pygame.display.set_mode(pantalla_tam)

"""    
🖍️ Colores 
"""
# Colores colorful 😈😈😈
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0) #(255, 128, 128) rojo segun mas clarito 
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
GRIS = (128, 128, 128)
MORADO = (128, 0, 128)
CELESTE = (152, 245, 255)

# Colores mas colorful 😈😈😈
ROJOFUERTE = (89, 2, 2)
ROJOBONITO = (191, 4, 4)
AZULFUERTE = (4, 104, 191)
AZULCLARITO = (5, 175, 242)

"""    
🦠 Clase Celula
Atributos: 
    - Color 
    - Estado (viva o muerta)
"""
class Celula:
    def __init__(self, color):
        self.color = color
        #self.estado = estado 
        
    def esCelulaMuerta(self):
        return self.color == NEGRO
    
    def esCelulaViva(self):
        return self.color == ROJOFUERTE or self.color == AZULCLARITO
    
    def esCelulaRoja(self):
        return self.color == ROJOFUERTE
    
    def esCelulaAzul(self):
        return self.color == AZULCLARITO

"""    
🦠 Clase Celula Azul 🔵
Atributos: 
    - Ataque
    - Defensa
"""
class CelulaAzul(Celula):
    def __init__(self):
        super().__init__(AZULCLARITO)
        self.gen_ataque = False
        self.gen_defensa = False

    def adquirirGenAtaque(self):
        self.gen_ataque = True

    def adquirirGenDefensa(self):
        self.gen_defensa = True

"""    
🦠 Funciones de Celulas 👾
"""
# Funcion para contar las celulas vivas de todo el tablero
def contar_celulas_vivas(tablero):
    return np.sum(tablero)

# Funcion para encontrar celulas
def encontrar_celulas(tablero, color_celula):
    celulas: set = set()
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j].color == color_celula:
                celulas.add((i,j))
    return celulas

# Funcion para encontrar vecinos
def encontrar_vecinos(tablero, x, y, color_celula) -> int:
    total = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i+x >= len(tablero) or i+x <= 0: continue
            if i == 0 and j == 0: continue
            if j+y >= len(tablero) or j+y <= 0: continue
            if tablero[i+x,j+y].color == color_celula: total += 1
    return total
    
"""    
👾 Tablero
"""
# Funcion para dibujar la cuadricula y las celulas (las celdas de la cuadricula)
def dibujar(tablero):
    pantalla.fill(NEGRO)  # Definimos el color que queremos para el fondo de la pantalla
    for y in range(n_celdas_y):
        for x in range(n_celdas_x):
            if tablero[x, y]:
                pygame.draw.rect(pantalla, tablero[x, y].color, 
                                 (x * celda_tam, y * celda_tam, celda_tam, celda_tam))  # Dibujamos las celulas vivas
            pygame.draw.rect(pantalla, GRIS, (x * celda_tam, y * celda_tam, celda_tam, celda_tam),1)  # Dibujamos la cuadricula
        
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
###########################################################################

# Celula = |color|inmunidad      |ataque     |
#          |     |mayor o igual  | numero par|


# def iniciar_poblacion(self, ):



# def fitness(self, ): 



# def seleccion(self, ):



# def cruce(self, ):



# def mutacion(self, ):



###########################################################################################

# Iniciamos las generaciones en 0
global generaciones 
generaciones = 0

# Iniciamos las celulas vivas en 0
global celulas_vivas
celulas_vivas = 0

# Iniciamos a ejecutando y jugando en sus valores por defecto

global ejecutando
ejecutando = True

global jugando
jugando = False


# celulaDefault = Celula(NEGRO, False, 0, 0)
# celulaRoja    = Celula(ROJOFUERTE, False, 0, 0)
# celulaAzul    = Celula(AZULCLARITO, False, 0, 0)
global celulas_muertas
celulas_muertas: set = encontrar_celulas(tablero, NEGRO)

global celulas_azules
celulas_azules: set = set()

global celulas_rojas
celulas_rojas: set = set()

class Juego(tablero):
    def __init__(self):
        self.generaciones = 0
        self.celulas_muertas = set()
        self.celulas_azules = set()
        self.celulas_rojas = set()

    def generar_generacion(self, tablero):
        self.generaciones += 1
        tablero_siguiente = np.copy(tablero)

        for x in range(n_celdas_x):
            for y in range(n_celdas_y):
                celula_actual = tablero[x, y]
                self._aplicar_reglas(celula_actual, tablero_siguiente, x, y)

        tablero = tablero_siguiente
        self.celulas_vivas = len(self.celulas_azules)
        reloj.tick(5)
    
    # Funcion de la regla (a)
    # (a) Si una celula esta viva y tiene dos o tres vecinas vivas, sobrevive.
    def regla_a_azul(self, celula_actual, tablero_siguiente, x, y):
        if celula_actual.esCelulaRoja():
            vecinos = encontrar_vecinos(tablero, x, y, AZULCLARITO)
            if vecinos < 2 or vecinos > 3:
                tablero_siguiente[x, y] = Celula(NEGRO)
                self.celulas_muertas.add((x, y))
                self.celulas_rojas.remove((x, y))
    
    # Funcion de la regla (a)
    # (a) Si una celula esta viva y tiene dos o tres vecinas vivas, sobrevive.
    def regla_a_roja(self, celula_actual, tablero_siguiente, x, y):
        if celula_actual.esCelulaRoja():
            vecinos = encontrar_vecinos(tablero, x, y, ROJOFUERTE)
            if vecinos < 2 or vecinos > 3:
                tablero_siguiente[x, y] = Celula(NEGRO)
                self.celulas_muertas.add((x, y))
                self.celulas_rojas.remove((x, y))
                
    # Funcion de la regla (b)
    # (b) Si una celula esta muerta y tiene tres vecinas vivas, nace.
    def regla_b_azul(self, celula_actual, tablero_siguiente, x, y):
        vecinos_azules = 0  # Inicializar contador de vecinos azules
        if celula_actual.esCelulaMuerta():
            vecinos = encontrar_vecinos(tablero, x, y, celula_actual.color)
            for vecino in vecinos:
                if tablero[vecino[0]][vecino[1]].color == AZULCLARITO:  # Comprobar si el vecino es azul
                    vecinos_azules += 1  # Incrementar el contador de vecinos azules
            # Comprobar regla de vida para la celula actual basada en el numero de vecinos azules
            if vecinos_azules == 3:
                tablero_siguiente[x][y] = Celula(NEGRO)
                self.celulas_muertas.add((x, y))
                self.celulas_azules.remove((x, y))
    
    # Funcion de la regla (b)
    # (b) Si una celula esta muerta y tiene tres vecinas vivas, nace.
    def regla_b_roja(self, celula_actual, tablero_siguiente, x, y):
        vecinos_azules = 0  # Inicializar contador de vecinos azules
        if celula_actual.esCelulaMuerta():
            vecinos = encontrar_vecinos(tablero, x, y, celula_actual.color)
            for vecino in vecinos:
                if tablero[vecino[0]][vecino[1]].color == ROJOFUERTE:  # Comprobar si el vecino es azul
                    vecinos_azules += 1  # Incrementar el contador de vecinos azules
            # Comprobar regla de vida para la celula actual basada en el numero de vecinos azules
            if vecinos_azules == 3:
                tablero_siguiente[x][y] = Celula(NEGRO)
                self.celulas_muertas.add((x, y))
                self.celulas_azules.remove((x, y))
        
    # Funcion de la regla (c)
    # (c) Si una celula esta viva y tiene mas de tres vecinas vivas, muere.
    def regla_c(self, celula_actual, tablero_siguiente, x, y):
        if celula_actual.esCelulaMuerta():
            vecinos_azules = encontrar_vecinos(tablero, x, y, AZULCLARITO)
            vecinos_rojos = encontrar_vecinos(tablero, x, y, ROJOFUERTE)
            if vecinos_azules == 3:
                tablero_siguiente[x, y] = Celula(AZULCLARITO)
                self.celulas_azules.add((x, y))
                self.celulas_muertas.remove((x, y))
            elif vecinos_rojos == 3:
                tablero_siguiente[x, y] = Celula(ROJOFUERTE)
                self.celulas_rojas.add((x, y))
                self.celulas_muertas.remove((x, y))
            elif vecinos_rojos == 3 and vecinos_azules == 3:
                tablero_siguiente[x, y] = Celula(ROJOFUERTE)
                self.celulas_rojas.add((x, y))
                self.celulas_muertas.remove((x, y))
    
    # Funcion para aplicar las reglas a,b y c
    def _aplicar_reglas(self, celula_actual, tablero_siguiente, x, y):
        self.regla_a_azul(celula_actual, tablero_siguiente, x, y)
        self.regla_a_roja(celula_actual, tablero_siguiente, x, y)
        self.regla_b_azul(celula_actual, tablero_siguiente, x, y)
        self.regla_b_roja(celula_actual, tablero_siguiente, x, y)
        self.regla_c(celula_actual, tablero_siguiente, x, y)

    # Metodo para aplicar las reglas del juego si el juego esta en curso
    def jugandoo(self, tablero):
        if jugando:
            generaciones += 1  # Aumentamos el contador de generaciones
            tablero_siguiente = np.copy(tablero)  # Creamos una copia del tablero actual
            # Aplicamos las reglas a cada celda del tablero
            for x in range(n_celdas_x):
                for y in range(n_celdas_y):
                    celula_actual = tablero[x, y]
                    self._aplicar_reglas(celula_actual, tablero_siguiente, x, y)
            tablero = tablero_siguiente  # Actualizamos el tablero con el siguiente estado
            self.celulas_vivas = len(self.celulas_azules)  # Actualizamos el numero de celulas vivas azules
            reloj.tick(5)  # Velocidad con la que se van a generar las generaciones

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
                celulas_azules = encontrar_celulas(tablero, AZULCLARITO)
                celulas_rojas = encontrar_celulas(tablero, ROJOFUERTE)
                celulas_vivas = len(celulas_azules) + len(celulas_rojas)
                jugando = False
            # Boton para generar un tablero aleatorio
            elif 130 <= pos[0] <= 160 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10: # BV
                tablero = np.random.choice([Celula(NEGRO), Celula(ROJOFUERTE), Celula(AZULCLARITO)], (n_celdas_x, n_celdas_y), p=[0.5, 0.3, 0.2])
                generaciones = 0
                celulas_muertas = encontrar_celulas(tablero, NEGRO)
                celulas_azules = encontrar_celulas(tablero, AZULCLARITO)
                celulas_rojas = encontrar_celulas(tablero, ROJOFUERTE)
                celulas_vivas = len(celulas_azules) + len(celulas_rojas)
                jugando = False
            else:  # Si no se hizo clic en un boton, verificar si se hizo clic en una celda del tablero
                if not jugando:  # Con este poderoso if evitamos que se modifique el tablero por el usuario mientras se genera alguna generacion
                    cel_x, cel_y = pos[0] // celda_tam, pos[1] // celda_tam
                    if 0 <= cel_x < n_celdas_x and 0 <= cel_y < n_celdas_y:
                        if tablero[cel_x, cel_y].esCelulaMuerta():
                            tablero[cel_x, cel_y] = Celula(AZULCLARITO)
                            celulas_azules.add((cel_x,cel_y)) 
                            celulas_muertas.remove((cel_x,cel_y))

                        elif tablero[cel_x, cel_y].esCelulaAzul():
                            tablero[cel_x, cel_y] = Celula(ROJOFUERTE)
                            celulas_rojas.add((cel_x,cel_y))
                            celulas_azules.remove((cel_x,cel_y))
                            
                        else:
                            tablero[cel_x, cel_y] = Celula(NEGRO)
                            celulas_muertas.add((cel_x,cel_y))
                            celulas_rojas.remove((cel_x,cel_y))
                celulas_vivas = len(celulas_azules) + len(celulas_rojas)
                        

    # Dibujamos el tablero
    dibujar(tablero)
    pygame.display.flip()

    # (a) Si una celula esta viva y tiene dos o tres vecinas vivas, sobrevive.
    # (b) Si una celula esta muerta y tiene tres vecinas vivas, nace.
    # (c) Si una celula esta viva y tiene mas de tres vecinas vivas, muere.
    # IMPORTANTE: Este es el nucleo de el juego de la vida de Conway, aqui implementamos las reglas del juego

    # Juego(tablero)
    
    if jugando:
        generaciones += 1  # Aumentamos el contador de generaciones
    #     tablero_siguiente = np.copy(tablero)    # Creamos una copia del tablero actual para poder modificarlo sin afectar el tablero original
    #     # (esta copia solo se guarda en codigo y no se dibuja o se muestra en pantalla)
        
        '''
        for x in range(n_celdas_x):
            for y in range(n_celdas_y):
                celula_actual = tablero[x,y]
                if celula_actual.esCelulaRoja():
                    vecinos = encontrar_vecinos(tablero, x, y, ROJOFUERTE)
                    if vecinos < 2 or vecinos > 3: # En caso de que la celula este viva y tenga menos de 2 o mas de 3
                    # vecinos vivos, la celula muere brutalmente 😢
                        tablero_siguiente[x, y] = Celula(NEGRO)
                        celulas_muertas.add((x,y))
                        celulas_rojas.remove((x,y))
                elif celula_actual.esCelulaAzul():
                    vecinos = encontrar_vecinos(tablero, x, y, AZULCLARITO)
                    if vecinos < 2 or vecinos > 3: # En caso de que la celula este viva y tenga menos de 2 o mas de 3
                    # vecinos vivos, la celula muere brutalmente 😢
                        tablero_siguiente[x, y] = Celula(NEGRO)
                        celulas_muertas.add((x,y))
                        celulas_azules.remove((x,y))
                elif celula_actual.esCelulaMuerta():
                    vecinos_azules = encontrar_vecinos(tablero, x, y, AZULCLARITO)
                    vecinos_rojos = encontrar_vecinos(tablero, x, y, ROJOFUERTE)
                    if vecinos_azules == 3: # En caso de que la celula este muerta y tenga exactamente 3 vecinos vivos
                    # La celula revive y ahora esta viva 😎
                        tablero_siguiente[x, y] = Celula(AZULCLARITO)
                        celulas_azules.add((x,y))
                        celulas_muertas.remove((x,y))                        
                    elif vecinos_rojos == 3: # En caso de que la celula este muerta y tenga exactamente 3 vecinos vivos
                    # La celula revive y ahora esta viva 😎
                        tablero_siguiente[x, y] = Celula(ROJOFUERTE)
                        celulas_rojas.add((x,y))
                        celulas_muertas.remove((x,y))
                    elif vecinos_rojos == 3 and vecinos_azules == 3: # Si existe algun empate priorizamos el crecimiento de celulas rojas
                        tablero_siguiente[x, y] = Celula(ROJOFUERTE)
                        celulas_rojas.add((x,y))
                        celulas_muertas.remove((x,y))
        tablero = tablero_siguiente
        celulas_vivas = len(celulas_azules)
        reloj.tick(5)  # Velocidad con la que se van a generar las generaciones
        '''

# Comando poderoso para salir de Pygame 
pygame.quit()
