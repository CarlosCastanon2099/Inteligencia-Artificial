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
        # self.gen_ataque = True
        self.poder = 1
        
    def esCelulaMuerta(self):
        return self.color == NEGRO
    
    def esCelulaViva(self):
        return self.color == ROJOFUERTE or self.color == AZULCLARITO or self.color == AZULFUERTE
    
    def esCelulaRoja(self):
        return self.color == ROJOFUERTE
    
    def esCelulaAzul(self):
        return self.color == AZULCLARITO or self.color == AZULFUERTE

    def getGenes(self):
        return self.poder

    def mutarGen(self, generacion):
       self.poder = random.randrange(0, generacion+1)

    def print(self):
        print(f"Celula color: {self.color}, gen ataque: {self.gen_ataque}")

# Funcion para encontrar celulas
def encontrar_celulas(tablero, color_celula):
    celulas: set = set()
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j].color == color_celula:
                celulas.add((i,j))
    return celulas

# Funcion para encontrar celulas vecinas
# busca quienes tienen mejores genes los selecciona los usa como padres
def encontrar_celulas_vecinas(tablero, x, y, color_celula) -> set:
    vecinos = set()
    for i in range(-1,2):
        for j in range(-1,2):
            if i+x >= len(tablero) or i+x <= 0: continue
            if i == 0 and j == 0: continue
            if j+y >= len(tablero) or j+y <= 0: continue
            if tablero[i+x,j+y].color == color_celula: vecinos.add((i+x,j+y))
    return vecinos

# Funcion para encontrar el número de vecinos
def encontrar_vecinos(tablero, x, y, color_celula) -> int:
    return len(encontrar_celulas_vecinas(tablero, x, y, color_celula))
    
"""    
👾 Tablero
"""
# Funcion para dibujar la cuadricula y las celulas (las celdas de la cuadricula)
def dibujar(juego):
    pantalla.fill(NEGRO)  # Definimos el color que queremos para el fondo de la pantalla
    for y in range(n_celdas_y):
        for x in range(n_celdas_x):
            if juego.tablero[x, y]:
                pygame.draw.rect(pantalla, juego.tablero[x, y].color, 
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
    texto = font.render("Generaciones: " + str(juego.generaciones), True, BLANCO)
    pantalla.blit(texto, (pantalla_tam[0] - 200, pantalla_tam[1] - 40))

    #texto = font.render("Celulas vivas: " + str(celulas_vivas), True, NEGRO)
    texto = font.render("Celulas vivas: " + str(juego.celulas_vivas), True, BLANCO)
    pantalla.blit(texto, (pantalla_tam[0] - 200, pantalla_tam[1] - 20))

###########################################################################

# Celula = |color|inmunidad      |ataque     |
#          |     |mayor o igual  | numero par|
# Ya lo hace el boton de generar tablero aleatorio
# def iniciar_poblacion(self, ):

###########################################################################################

"""    
🕹️ Clase Juego
Atributos: 
    - Numero de generaciones 
    - Tablero de juego
    - Numero de celulas vivas
    - Ejecutando (En ejecucion o no)
    - Jugando (Realizando reglas de Conway o no)
    - Celulas muertas
    - Celulas azules
    - Celulas rojas
"""
class Juego:
    def __init__(self):
        # Iniciamos las generaciones en 0
        self.generaciones = 0
        # Inicializamos el tablero y sus variables
        self.tablero = np.full((n_celdas_x, n_celdas_y), Celula(NEGRO), dtype=object)
        # Iniciamos las celulas vivas en 0
        self.celulas_vivas = 0
        # Iniciamos a ejecutando y jugando en sus valores por defecto
        self.ejecutando = True
        self.jugando = False
        # Iniciamos los conjuntos de celulas
        self.celulas_muertas = encontrar_celulas(self.tablero, NEGRO)
        self.celulas_azules = set()
        self.celulas_rojas = set()

    #########################################################################################
    # Implementacion operadores geneticos

    def fitness(self, x, y):
        calificacion = self.tablero[x][y].poder - self.generaciones
        if (calificacion < 0 ): return 0
        return calificacion

    def seleccion(self, cantidad_padres):
        padres = []
        candidatos = list(self.celulas_azules)  # Convertir el conjunto en una lista
        for _ in range(cantidad_padres):         
            mejor_candidato = min(candidatos, key=lambda celula: self.fitness(*celula))
            padres.append(mejor_candidato)
            candidatos.remove(mejor_candidato)  # Remover el candidato seleccionado para no repetirlo
        return padres

    def combinacion_de_genes(self, gen_padre, gen_madre):
        hijo = Celula(AZULCLARITO)
        probabilidad = random.random()
        probabilidad_mutacion = 0.10  # Probabilidad de mutación del 10%
        if probabilidad < probabilidad_mutacion:
            hijo.mutarGen(self.generaciones+5)
        elif probabilidad < 0.45:
            hijo.poder = gen_padre
        else:
            hijo.poder = gen_madre
        return hijo
            
    def cruce(self, padre: Celula, madre: Celula):
        
        cantidad_hijos_totales = 10
        # Crear el hijo con los genes combinados de padre y vecino de la madre
        gen_padre = self.tablero[padre[0], padre[1]].getGenes()        
        gen_madre = self.tablero[madre[0], madre[1]].getGenes()
        hijos: list[Celula] = []
        for _ in range(cantidad_hijos_totales):
            hijos.append(self.combinacion_de_genes(gen_padre, gen_madre))
        hijo_elegido = Celula(AZULCLARITO)
        for hijo in hijos:
            if (hijo_elegido.poder < hijo.poder):
                hijo_elegido = hijo
        if (hijo.poder - self.generaciones <= 0): hijo.color = AZULFUERTE
        return hijo

    
    #Función para ejecutar el algoritmo genético
    def ejecuta_genetico(self):
        # Queremos que el número de padres sea 2
        num_padres = 2
        # Seleccionamos a los más aptos del conjunto de células azules
        celulas_padres = self.seleccion(num_padres)
        # Obtenemos la célula hija resultado del cruce de los padres
        # y posiblemente mutada
        celula_hijo = self.cruce(celulas_padres[0], celulas_padres[1])        
        return celula_hijo
        
    
    #########################################################################################
    
    # Actualiza el numero de celulas vivas en el tablero actual
    def actualiza_celulas_vivas(self):
        self.celulas_vivas = len(self.celulas_azules) + len(self.celulas_rojas)
    
    # Actualiza los conjuntos de celulas tras una modificacion en el tablero
    def actualiza_celulas(self):
        self.celulas_muertas = encontrar_celulas(self.tablero, NEGRO)
        celulas_azules_clarito = encontrar_celulas(self.tablero, AZULCLARITO)
        celulas_azules_fuerte = encontrar_celulas(self.tablero, AZULFUERTE)
        self.celulas_azules = celulas_azules_clarito | celulas_azules_fuerte
        self.celulas_rojas = encontrar_celulas(self.tablero, ROJOFUERTE)
    
    # Comienza la ejecucion del juego de la vida con la primer generacion
    def generar_generacion(self):
        self.generaciones += 1
        tablero_siguiente = np.copy(self.tablero)

        for x in range(n_celdas_x):
            for y in range(n_celdas_y):
                celula_actual = self.tablero[x, y]
                self._aplicar_reglas(celula_actual, tablero_siguiente, x, y)

        self.tablero = tablero_siguiente
        self.celulas_vivas = len(self.celulas_azules)
        reloj.tick(5)

    # Funcion de la regla (a) para las celulas azules.
    # (a) Si una celula esta viva y tiene dos o tres vecinas vivas, sobrevive.
    def regla_a_azul(self, tablero_siguiente, x, y):
        vecinos = encontrar_vecinos(self.tablero, x, y, AZULCLARITO) + encontrar_vecinos(self.tablero, x, y, AZULFUERTE)
        if vecinos < 2 or vecinos > 3:
            tablero_siguiente[x, y] = Celula(NEGRO)
            self.celulas_muertas.add((x, y))
            self.celulas_azules.remove((x, y))
    
    # Funcion de la regla (a) para las celulas rojas.
    # (a) Si una celula esta viva y tiene dos o tres vecinas vivas, sobrevive.
    def regla_a_roja(self, tablero_siguiente, x, y):
        # Obtenemos los datos de los vecinos azules
        vecinos_azules_fuertes = encontrar_vecinos(self.tablero, x, y, AZULFUERTE) 
        vecinos_azules = encontrar_vecinos(self.tablero, x, y, AZULCLARITO) + vecinos_azules_fuertes 
        
        # Si es posible el nacimiento de una celula azul
        # La posición tiene 3 vecinos azules y además alguna de las celulas vecinas
        # tiene el gen de ataque
        if (vecinos_azules == 3 and vecinos_azules_fuertes > 0):
            # Creamos una nueva celula y se posiciona en el lugar del tablero
            nueva_celula_azul = self.ejecuta_genetico()
            tablero_siguiente[x, y] = nueva_celula_azul
            self.celulas_azules.add((x, y))
            self.celulas_rojas.remove((x, y))
            return
        # En caso contrario se posiciona una celula de color rojo
        vecinos = encontrar_vecinos(self.tablero, x, y, ROJOFUERTE)
        if vecinos < 2 or vecinos > 3:
            tablero_siguiente[x, y] = Celula(NEGRO)
            self.celulas_muertas.add((x, y))
            self.celulas_rojas.remove((x, y))

    # Funcion de la regla (c)
    # (c) Si una celula esta viva y tiene mas de tres vecinas vivas, muere.
    def regla_c(self, tablero_siguiente, x, y):
        vecinos_azules = encontrar_vecinos(self.tablero, x, y, AZULCLARITO) + encontrar_vecinos(self.tablero, x, y, AZULFUERTE)
        vecinos_rojos = encontrar_vecinos(self.tablero, x, y, ROJOFUERTE)
        if vecinos_azules == 3:
            # Al nacer una nueva célula azul ejecutamos el algoritmo genético
            # para esta nueva célula
            nueva_celula_azul = self.ejecuta_genetico()
            tablero_siguiente[x, y] = nueva_celula_azul
            self.celulas_azules.add((x, y))
            self.celulas_muertas.remove((x, y))
        elif vecinos_rojos == 3:
            tablero_siguiente[x, y] = Celula(ROJOFUERTE)
            self.celulas_rojas.add((x, y))
            self.celulas_muertas.remove((x, y))
    
    # Funcion para aplicar las reglas a,b y c
    # (a) Si una celula esta viva y tiene dos o tres vecinas vivas, sobrevive.
    # (b) Si una celula esta muerta y tiene tres vecinas vivas, nace.
    # (c) Si una celula esta viva y tiene mas de tres vecinas vivas, muere.
    # IMPORTANTE: Este es el nucleo de el juego de la vida de Conway, aqui implementamos las reglas del juego
    def _aplicar_reglas(self, celula_actual: Celula, tablero_siguiente, x, y):
        if celula_actual.esCelulaRoja():
            self.regla_a_roja(tablero_siguiente, x, y)
            #self.regla_b_roja(celula_actual, tablero_siguiente, x, y)
        elif celula_actual.esCelulaAzul():
            self.regla_a_azul(tablero_siguiente, x, y)
            #self.regla_b_azul(celula_actual, tablero_siguiente, x, y)        
        else:
            self.regla_c(tablero_siguiente, x, y)

    # Metodo para aplicar las reglas del juego si el juego esta en curso
    def jugar(self):
        if juego.jugando:
            self.generaciones += 1  # Aumentamos el contador de generaciones
            tablero_siguiente = np.copy(self.tablero)  # Creamos una copia del tablero actual
            # Aplicamos las reglas a cada celda del tablero
            for x in range(n_celdas_x):
                for y in range(n_celdas_y):
                    celula_actual = self.tablero[x, y]
                    self._aplicar_reglas(celula_actual, tablero_siguiente, x, y)
            self.tablero = tablero_siguiente  # Actualizamos el tablero con el siguiente estado
            self.celulas_vivas = len(self.celulas_azules)  # Actualizamos el numero de celulas vivas azules
            reloj.tick(5)  # Velocidad con la que se van a generar las generaciones

#Creamos un juego nuevo
juego = Juego()

"""
🎮 Bucle principal
"""
while juego.ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El evento QUIT es para cerrar la ejecucion, en este caso, darle clic al boton de cerrar ventana            
            juego.ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:  # MOUSEBUTTONDOWN es el evento de pygame de hacer un "clic"
            pos = pygame.mouse.get_pos()
            # Boton de Pausa
            if 10 <= pos[0] <= 40 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                juego.jugando = False
            # Boton de Play
            elif 50 <= pos[0] <= 80 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                juego.jugando = True
            # Boton para borrar toda la cuadricula y ponerla en pausa
            elif 90 <= pos[0] <= 120 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10:
                juego.tablero.fill(Celula(NEGRO))
                juego.generaciones = 0
                juego.actualiza_celulas()
                juego.actualiza_celulas_vivas()
                juego.jugando = False
            # Boton para generar un tablero aleatorio
            elif 130 <= pos[0] <= 160 and pantalla_tam[1] - 40 <= pos[1] <= pantalla_tam[1] - 10: # BV
                juego.tablero = np.random.choice([Celula(NEGRO), Celula(ROJOFUERTE), Celula(AZULCLARITO)], (n_celdas_x, n_celdas_y), p=[0.5, 0.3, 0.2])
                juego.generaciones = 0
                juego.actualiza_celulas()
                juego.actualiza_celulas_vivas()
                juego.jugando = False
            else:  # Si no se hizo clic en un boton, verificar si se hizo clic en una celda del tablero
                if not juego.jugando:  # Con este poderoso if evitamos que se modifique el tablero por el usuario mientras se genera alguna generacion
                    cel_x, cel_y = pos[0] // celda_tam, pos[1] // celda_tam
                    if 0 <= cel_x < n_celdas_x and 0 <= cel_y < n_celdas_y:
                        if juego.tablero[cel_x, cel_y].esCelulaMuerta():
                            juego.tablero[cel_x, cel_y] = Celula(AZULCLARITO)
                            juego.celulas_azules.add((cel_x,cel_y)) 
                            juego.celulas_muertas.remove((cel_x,cel_y))
                        
                        elif juego.tablero[cel_x, cel_y].esCelulaAzul():
                            juego.tablero[cel_x, cel_y] = Celula(ROJOFUERTE)
                            juego.celulas_rojas.add((cel_x,cel_y))
                            juego.celulas_azules.remove((cel_x,cel_y))
                        
                        else:
                            juego.tablero[cel_x, cel_y] = Celula(NEGRO)
                            juego.celulas_muertas.add((cel_x,cel_y))
                            juego.celulas_rojas.remove((cel_x,cel_y))
                juego.actualiza_celulas_vivas()
    """
    ⬛ Dibujamos el tablero
    """
    dibujar(juego)
    pygame.display.flip()
    
    """
    🕹️ Iniciamos el juego
    """
    juego.jugar()

# Comando poderoso para salir de Pygame 
pygame.quit()