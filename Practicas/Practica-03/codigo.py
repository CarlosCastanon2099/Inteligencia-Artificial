# -*- coding: utf-8 -*-
"""practica03.ipynb

# 🔴 Práctica 03: Exploradores de laberinto 🏟️

----

<b>Team:</b> <font color='red'>S</font><b>ocios</b> <font color='blue'>I</font><b>nteligentemente</b> <font color='green'>A</font><b>rtificiales</b> (<font color='red'>S</font>.<font color='blue'>I</font>.<font color='green'>A</font>)


<font color='red'>✪</font> Bonilla Reyes Dafne

<font color='red'>✪</font> Castañón Maldonado Carlos Emilio

<font color='red'>✪</font> Mares Cruz Tlacaelel Horacio

<font color='red'>✪</font> Maya Castrejón Luis Manuel

<font color='red'>✪</font> Navarro Santana Pablo César



----

### 📌 **Definimos la clase agente**

<div style="text-align: justify">

El agente tiene que explorar el laberinto y encontrar la salida. Al crearlo, solo le damos su posición inicial en el 
laberinto, como si estuviera parado en la entrada, mirando hacia adentro, preguntándose qué le depara el destino.

Tiene que moverse pero no puede simplemente moverse como sea debe evitar obstáculos. Le decimos en qué dirección ir 
("arriba", "abajo", "izquierda", "derecha"), y él verifica si el camino está libre. Si encuentra un muro 
(un obstáculo representado por un 1), sabe que debe detenerse y pensar en otro camino.

</div>
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
import networkx as nx
from IPython import display
from IPython.display import HTML
import numpy as np
import seaborn as sns

class Agente:
    def __init__(self, posicion):
        """
        Inicializa un objeto Agente con una posición dada.

        Args:
            posicion (list): La posición inicial del agente en forma de lista [x, y].
        """
        self.posicion = posicion

    def mover(self, direccion, laberinto):
        """
        Mueve el agente en la dirección especificada si es un movimiento válido.

        Args:
            direccion (str): La dirección en la que se desea mover el agente ("arriba", "abajo", "izquierda", "derecha").
            laberinto (list): El laberinto en forma de matriz.

        Returns:
            list or None: La nueva posición del agente si el movimiento es válido, None en caso contrario.
        """
        x, y = self.posicion
        # Mueve el agente arriba si no es límite superior, y donde la celda destino no es un obstáculo.
        if direccion == "arriba" and x > 0 and laberinto[x-1][y] != 1:
            self.posicion = [x-1, y]
        # Mueve el agente abajo si no es límite inferior, y donde la celda destino no es un obstáculo.
        elif direccion == "abajo" and x < len(laberinto) - 1 and laberinto[x+1][y] != 1:
            self.posicion = [x+1, y]
        # Mueve el agente izquierda si no es límite izquierdo, y donde la celda destino no es un obstáculo.
        elif direccion == "izquierda" and y > 0 and laberinto[x][y-1] != 1:
            self.posicion = [x, y-1]
        # Mueve el agente derecha si no es límite derecho, y donde la celda destino no es un obstáculo.
        elif direccion == "derecha" and y < len(laberinto[0]) - 1 and laberinto[x][y+1] != 1:
            self.posicion = [x, y+1]
        else:
            return None

        return self.posicion

"""#### ➡️ **Flechas**
Mientras nuestro agente explora, vamos a dejar un rastro de su viaje. Para eso utilizamos la función flechas. Cada vez que el Agente 
toma una decisión sobre hacia dónde moverse, convertimos esa dirección en una flecha visual ("↑", "↓", "←", "→").
"""

'''
Funcion que recibe una dirección y retorna la flecha correspondiente a la dirección.
'''
def flechas(direccion):
    """
    Devuelve una flecha correspondiente a la dirección dada.

    Parámetros:
    direccion (str): La dirección de la flecha. Puede ser "arriba", "abajo", "izquierda" o "derecha".

    Retorna:
    str: La flecha correspondiente a la dirección dada.
    """
    if direccion == "arriba":
        return  "↑"
    elif direccion == "abajo":
        return  "↓"
    elif direccion == "izquierda":
        return  "←"
    elif direccion == "derecha":
        return  "→"

"""### 📌 **Backtracking**
Funcion en la que definimos el backtracking que usará el agente para encontrar (o no) la salida del laberinto. Esta funcion regresa solo la solucion final, es decir, el camino que el agente debe seguir para llegar a la salida del laberinto y
por ende no regresa todos los posibles caminos usados por el agente.

Iniciamos marcando el comienzo de la exploración con el registro del primer movimiento. Para evitar recorrer los mismos caminos, empleamos un conjunto de visitados, y evaluamos cada movimiento en función de su viabilidad y su capacidad para acercarnos a la meta. Al hacer esto el agente encuentra la salida y aprende de cada paso.

</div>
"""

"""
    Realiza una búsqueda en profundidad (backtracking) para encontrar la salida en un laberinto.

    Parámetros:
    - agente (agente): El agente que se mueve por el laberinto.
    - laberinto (list): El laberinto representado como una matriz.
    - visitados (set): Conjunto de celdas visitadas. Por defecto, es None.
    - instrucciones (list): Lista de instrucciones para llegar a la salida. Por defecto, es una lista vacía.

    Retorna:
    - bool: True si se encuentra la salida, False si no se encuentra.

"""
def backtrack(agente, laberinto, visitados = None, instrucciones = []):
    if not instrucciones :
        instrucciones.append(f"Primer movimiento!\t Posición: [{agente.posicion[0]}, {agente.posicion[1]}]")
    if visitados is None:
        visitados = set()

    x, y = agente.posicion

    if laberinto[x][y] == "S":  # Si el agente encuentra la salida, imprime el camino y retorna True
        for i in instrucciones:
            print(i)
        print("Encontré la salida :D\n")
        return True
    else:
        visitados.add((x, y))  # Marcar la celda actual como visitada
        movimientos = ["arriba", "abajo", "izquierda", "derecha"]

        for movimiento in movimientos:
            agente_temp = Agente(agente.posicion[:])  # Crear una copia del agente para simular movimientos
            nueva_posicion = agente_temp.mover(movimiento, laberinto)

            if nueva_posicion and tuple(nueva_posicion) not in visitados:  # Verificar si el movimiento es válido y Si la nueva posición no ha sido visitada

                instrucciones.append(f"Movimiento: {movimiento}\t Posición: {nueva_posicion}")
                if backtrack(Agente(nueva_posicion), laberinto, visitados):
                    laberinto[agente.posicion[0]][agente.posicion[1]] = flechas(movimiento)
                    return True
                else:
                    laberinto[agente.posicion[0]][agente.posicion[1]] = 0
                    instrucciones.pop()

        return False

"""
### 📌 **Implementacion de DFS y BFS**

"""



# Funcion auxiliar para localizar la primera "S" que se encuentre en un laberinto
# Esta es usada en las funciones de DFS y BFS.
def doxeaLaS(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == "S":
                return (i,j)

# Funcion que en base a un laberinto matricial, dibuja a este ultimo como una grafica.
def dibujar_grafo_laberinto(laberinto):
    G = nx.Graph()

    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Crear nodos
    for fila in range(filas):
        for columna in range(columnas):
            # Agregar nodo con su posición como atributo
            G.add_node((fila, columna))

    # Crear aristas
    for fila in range(filas):
        for columna in range(columnas):
            # Verificar si la celda actual es un pasillo (0 o "E" o "S")
            if laberinto[fila][columna] == 0 or laberinto[fila][columna] == "E" or laberinto[fila][columna] == "S":
                # Agregar aristas a las celdas vecinas que también son pasillos
                if fila > 0 and laberinto[fila - 1][columna] == 0:
                    G.add_edge((fila, columna), (fila - 1, columna))
                if fila < filas - 1 and laberinto[fila + 1][columna] == 0:
                    G.add_edge((fila, columna), (fila + 1, columna))
                if columna > 0 and laberinto[fila][columna - 1] == 0:
                    G.add_edge((fila, columna), (fila, columna - 1))
                if columna < columnas - 1 and laberinto[fila][columna + 1] == 0:
                    G.add_edge((fila, columna), (fila, columna + 1))

    # Dibujar el grafo
    pos = {(fila, columna): (columna, -fila) for fila in range(filas) for columna in range(columnas)}
    #print(pos)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_weight='bold')
    plt.show()

"""#### 📌 **Implementación de DFS**"""

xAGENTE = 0
yAGENTE = 0

laberinto = [[]]


def obtener_ruta_mas_corta(inicio, fin, camino):
    ruta = [fin]
    while ruta[-1] != inicio:
        ruta.append(camino[ruta[-1]])
    return ruta[::-1]


def DFS(Laberinto):
    G = nx.Graph()

    # Vertice Inicial (E)
    inicio = (xAGENTE, yAGENTE)

    # Vertice Final (S)
    fin = doxeaLaS(Laberinto)

    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Crear nodos
    for fila in range(filas):
        for columna in range(columnas):
            if laberinto[fila][columna] == "E":
                inicio = (fila, columna)  # Establecer el vértice inicial
            elif laberinto[fila][columna] == "S":
                fin = (fila, columna)  # Establecer el vértice final
            # Agregar nodo con su posición como atributo
            G.add_node((fila, columna))

    # Crear aristas
    for fila in range(filas):
        for columna in range(columnas):
            # Verificar si la celda actual es un pasillo (0 o "E" o "S")
            if laberinto[fila][columna] == 0 or laberinto[fila][columna] == "E" or laberinto[fila][columna] == "S":
                # Agregar aristas a las celdas vecinas que también son pasillos
                if fila > 0 and laberinto[fila - 1][columna] == 0:
                    G.add_edge((fila, columna), (fila - 1, columna))
                if fila < filas - 1 and laberinto[fila + 1][columna] == 0:
                    G.add_edge((fila, columna), (fila + 1, columna))
                if columna > 0 and laberinto[fila][columna - 1] == 0:
                    G.add_edge((fila, columna), (fila, columna - 1))
                if columna < columnas - 1 and laberinto[fila][columna + 1] == 0:
                    G.add_edge((fila, columna), (fila, columna + 1))

    # Algoritmo DFS
    visitados = set()
    camino = {inicio: None}
    pila = [inicio]

    while pila:
        nodo = pila.pop()
        if nodo == fin:
            break
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in G.neighbors(nodo):
                if vecino not in visitados:
                    pila.append(vecino)
                    camino[vecino] = nodo



    # Construir la nueva gráfica con los nodos y aristas alcanzables por DFS
    G_bfs = nx.Graph()
    for nodo, padre in camino.items():
        if padre is not None:
            G_bfs.add_edge(nodo, padre)


    # Dibujar el grafo resultante del DFS
    pos = {(fila, columna): (columna, -fila) for fila in range(filas) for columna in range(columnas)}
    # node_shapes = ["E" if nodo == inicioVertice else "S" if nodo == finVertice else "0" for nodo in G_bfs.nodes()]
    nx.draw(G_bfs, pos, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_weight='bold') # node_shape=node_shapes
    plt.show()

    # Dibujamos el camino de la solución
    pos = {(fila, columna): (columna, -fila) for fila in range(filas) for columna in range(columnas)}

    caminitoDFS = obtener_ruta_mas_corta(inicio, fin, camino)

    nx.draw(G_bfs, pos, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_weight='bold')
    nx.draw_networkx_nodes(G_bfs, pos, nodelist=caminitoDFS, node_color='red', node_size=700)
    nx.draw_networkx_edges(G_bfs, pos, edgelist=[(caminitoDFS[i], caminitoDFS[i+1]) for i in range(len(caminitoDFS)-1)], edge_color='red', width=2)
    plt.show()

"""#### 📌 **Implementación de BFS**

"""

xAGENTE = 0
yAGENTE = 0

laberinto = [[]]


def obtener_ruta_mas_corta(inicio, fin, camino):
    ruta = [fin]
    while ruta[-1] != inicio:
        ruta.append(camino[ruta[-1]])
    return ruta[::-1]


def BFS(Laberinto):
    G = nx.Graph()

    # Vertice Inicial (E)
    inicio = (xAGENTE, yAGENTE)

    # Vertice Final (S)
    fin = doxeaLaS(Laberinto)

    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Crear nodos
    for fila in range(filas):
        for columna in range(columnas):
            if laberinto[fila][columna] == "E":
                inicio = (fila, columna)  # Establecer el vértice inicial
            elif laberinto[fila][columna] == "S":
                fin = (fila, columna)  # Establecer el vértice final
            # Agregar nodo con su posición como atributo
            G.add_node((fila, columna))

    # Crear aristas
    for fila in range(filas):
        for columna in range(columnas):
            # Verificar si la celda actual es un pasillo (0 o "E" o "S")
            if laberinto[fila][columna] == 0 or laberinto[fila][columna] == "E" or laberinto[fila][columna] == "S":
                # Agregar aristas a las celdas vecinas que también son pasillos
                if fila > 0 and laberinto[fila - 1][columna] == 0:
                    G.add_edge((fila, columna), (fila - 1, columna))
                if fila < filas - 1 and laberinto[fila + 1][columna] == 0:
                    G.add_edge((fila, columna), (fila + 1, columna))
                if columna > 0 and laberinto[fila][columna - 1] == 0:
                    G.add_edge((fila, columna), (fila, columna - 1))
                if columna < columnas - 1 and laberinto[fila][columna + 1] == 0:
                    G.add_edge((fila, columna), (fila, columna + 1))

    # Algoritmo BFS
    inicioVertice = inicio
    finVertice = fin

    # Cola para almacenar los nodos que se van a visitar
    cola = [inicioVertice]
    # Conjunto para almacenar los nodos que ya se visitaron
    visitados = set()
    # Diccionario para almacenar el camino que se ha seguido para llegar a cada nodo
    camino = {inicioVertice: None}

    # Mientras la cola no está vacía
    while cola:
        # Sacar el primer nodo de la cola
        actual = cola.pop(0)
        # Si el nodo actual es el nodo final, terminar
        if actual == finVertice:
            break
        # Si el nodo actual no ha sido visitado
        if actual not in visitados:
            # Marcar el nodo actual como visitado
            visitados.add(actual)
            # Agregar los vecinos del nodo actual a la cola
            for vecino in G.neighbors(actual):
                if vecino not in visitados:
                    cola.append(vecino)
                    # Almacenar el camino que se ha seguido para llegar al vecino
                    camino[vecino] = actual

    # Obtener la ruta del camino desde el nodo inicial hasta el nodo final
    ruta_mas_corta = obtener_ruta_mas_corta(inicioVertice, finVertice, camino)

    #print("Ruta más corta:", ruta_mas_corta)

    # Construir la nueva gráfica con los nodos y aristas alcanzables por BFS
    G_bfs = nx.Graph()
    for nodo, padre in camino.items():
        if padre is not None:
            G_bfs.add_edge(nodo, padre)


    # Dibujar el grafo resultante del BFS
    pos = {(fila, columna): (columna, -fila) for fila in range(filas) for columna in range(columnas)}
    # node_shapes = ["E" if nodo == inicioVertice else "S" if nodo == finVertice else "0" for nodo in G_bfs.nodes()]
    nx.draw(G_bfs, pos, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_weight='bold') # node_shape=node_shapes
    plt.show()

    # Dibujamos la ruta mas corta
    pos = {(fila, columna): (columna, -fila) for fila in range(filas) for columna in range(columnas)}

    nx.draw(G_bfs, pos, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_weight='bold')
    nx.draw_networkx_nodes(G_bfs, pos, nodelist=ruta_mas_corta, node_color='red', node_size=700)
    nx.draw_networkx_edges(G_bfs, pos, edgelist=[(ruta_mas_corta[i], ruta_mas_corta[i+1]) for i in range(len(ruta_mas_corta)-1)], edge_color='red', width=2)
    plt.show()

"""### 📌 **Laberinto**
Aquí definimos el laberinto que usaremos para nuestro algoritmo.
"""

# Representación del laberinto
laberinto = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]

laberintoBacktrack = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]

laberintoBFS = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]

laberintoDFS = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]

"""### El Agente
Creamos una instancia del agente en la entrada del laberinto (que es la (0,0), pero puede cambiar)
"""

xAGENTE = 0
yAGENTE = 0

agente = Agente([xAGENTE,yAGENTE])

"""### Llamada a nuestro algoritmo

Finalmente, llamamos a nuestro algoritmo para que se ejecute y nos muestre si encontró la salida o no.
"""

# algoritmoBRUTAL = backtrack(agente, laberintoBacktrack)

print("Representacion grafica de los pasos seguidos por el agente para la solucion final: \n")
print("■ = Obstaculos (los 1's)")
print("O = Celda Libre")
print("S = Salida\n")

for lab in laberintoBacktrack:
    print('[', end='')
    for path in lab:
        if path == 1:
            path = '■'
        if path == 0:
            path = 'O'
        print(f" {path}", end='')
    print(" ]")

"""## BFS

Representacion de la grafica asociada al laberinto, notese como es que todos los vertices asociados a los **1's** quedan desconectados de la grafica
ya que no es posible moverse a traves de ellos.
"""

# laberintoGrafica = dibujar_grafo_laberinto(laberintoBFS)

"""Procedemos a realizar la busqueda en anchura para encontrar la salida del laberinto.

Esto partiendo desde nuestro vertice inicial (E o la posicion del agente) y buscando el vertice final S (la salida del laberinto).

Una vez realizada la busqueda, regresamos una nueva grafica en la que se muestre en rojo el camino mas corto entre el agente y la salida.
"""

# laberintoBSF = BFS(laberintoBFS)

"""### Imprimimos el laberinto en su forma matricial original"""

# Imprimimos el laberinto original en su forma de matriz
print("\nLaberinto Original: ")
for lab in laberinto:
    print(lab)

"""### Gif de la busqueda en anchura."""

# import seaborn as sns

def BFS_animation(laberinto):
    G = nx.Graph()

    # Vertice Inicial (E)
    inicio = (xAGENTE, yAGENTE)

    # Vertice Final (S)
    fin = doxeaLaS(laberinto)

    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Crear nodos
    for fila in range(filas):
        for columna in range(columnas):
            if laberinto[fila][columna] == "E":
                inicio = (fila, columna)  # Establecer el vértice inicial
            elif laberinto[fila][columna] == "S":
                fin = (fila, columna)  # Establecer el vértice final
            # Agregar nodo con su posición como atributo
            G.add_node((fila, columna))

    # Crear aristas
    for fila in range(filas):
        for columna in range(columnas):
            # Verificar si la celda actual es un pasillo (0 o "E" o "S")
            if laberinto[fila][columna] == 0 or laberinto[fila][columna] == "E" or laberinto[fila][columna] == "S":
                # Agregar aristas a las celdas vecinas que también son pasillos
                if fila > 0 and laberinto[fila - 1][columna] == 0:
                    G.add_edge((fila, columna), (fila - 1, columna))
                if fila < filas - 1 and laberinto[fila + 1][columna] == 0:
                    G.add_edge((fila, columna), (fila + 1, columna))
                if columna > 0 and laberinto[fila][columna - 1] == 0:
                    G.add_edge((fila, columna), (fila, columna - 1))
                if columna < columnas - 1 and laberinto[fila][columna + 1] == 0:
                    G.add_edge((fila, columna), (fila, columna + 1))

    # Algoritmo BFS
    inicioVertice = inicio
    finVertice = fin

    # Cola para almacenar los nodos que se van a visitar
    cola = [inicioVertice]
    # Conjunto para almacenar los nodos que ya se visitaron
    visitados = set()
    # Diccionario para almacenar el camino que se ha seguido para llegar a cada nodo
    camino = {inicioVertice: None}

    # Lista para almacenar los grafos en cada iteración
    grafos = []

    # Mientras la cola no está vacía
    while cola:
        # Construir el grafo actual
        G_bfs = nx.Graph()
        for nodo, padre in camino.items():
            if padre is not None:
                G_bfs.add_edge(nodo, padre)
        grafos.append(G_bfs.copy())

        # Sacar el primer nodo de la cola
        actual = cola.pop(0)
        # Si el nodo actual es el nodo final, terminar
        if actual == finVertice:
            break
        # Si el nodo actual no ha sido visitado
        if actual not in visitados:
            # Marcar el nodo actual como visitado
            visitados.add(actual)
            # Agregar los vecinos del nodo actual a la cola
            for vecino in G.neighbors(actual):
                if vecino not in visitados:
                    cola.append(vecino)
                    # Almacenar el camino que se ha seguido para llegar al vecino
                    camino[vecino] = actual

    # Obtener la ruta más corta
    ruta_mas_corta = obtener_ruta_mas_corta(inicioVertice, finVertice, camino)
    #print("Ruta más corta:", ruta_mas_corta)

    return grafos, ruta_mas_corta

def update(frame):
    ax.clear()
    nx.draw(grafos[frame], pos, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_weight='bold')
    plt.title(f'Iteración {frame+1}')



laberintoBSF = BFS(laberintoBFS)


# Generar grafos y posición de nodos
grafos, ruta_mas_corta = BFS_animation(laberintoBFS)
pos = {(fila, columna): (columna, -fila) for fila in range(len(laberintoBFS)) for columna in range(len(laberintoBFS[0]))}

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(grafos), interval=1000, repeat=True)

# Configurar el formato de renderizado predeterminado como HTML5
plt.rcParams['animation.html'] = 'html5'

# Visualizar la animación en el notebook
HTML(ani.to_jshtml())

"""## DFS

Representacion de la grafica asociada al laberinto, notese como es que todos los vertices asociados a los **1's** quedan desconectados de la grafica
ya que no es posible moverse a traves de ellos.
"""

# laberintoGrafica = dibujar_grafo_laberinto(laberintoDFS)

"""Procedemos a realizar la busqueda por profundidad para encontrar la salida del laberinto.

Esto partiendo desde nuestro vertice inicial (E o la posicion del agente) y buscando el vertice final S (la salida del laberinto).

Una vez realizada la busqueda, regresamos una nueva grafica en la que se muestre en rojo el camino mas corto entre el agente y la salida.
"""

laberintoDSF = DFS(laberintoDFS)

"""### Gif de la busqueda por profundidad."""

# To be Continued...

"""### Generador aleatorio de laberintos

---

Modificar los parametros de filas y columnas para generar laberintos de diferentes tamaños.
"""

# Dimensiones del laberinto
filas = 25
columnas = 25

import random

# Crear el laberinto con todos los valores aleatorios
laberintoA = [[random.choice([0,1]) for _ in range(columnas)] for _ in range(filas)]

# Elegir una posición aleatoria para la entrada (E) y la salida (S)
entrada_fila, entrada_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
salida_fila, salida_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)

# Asegurarse que la entrada y la salida no estén en la misma posición
while entrada_fila == salida_fila and entrada_columna == salida_columna:
    salida_fila, salida_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)

# Establecer la entrada (E) y la salida (S)
laberintoA[entrada_fila][entrada_columna] = 'E'
laberintoA[salida_fila][salida_columna] = 'S'

"""
# Imprimir el laberinto
for fila in laberintoA:
    print(fila)


# agenteA = Agente( [entrada_fila, entrada_columna] )

En caso de que al ejecutar no se muestren los pasos, es un alto indicativo de que no existe solucion para el laberinto generado.

# algoritmoBRUTALISIMO = backtrack(agenteA, laberintoA)

# Imprimir trayecto y eventos en el laberinto
print("Representacion grafica de los pasos seguidos por el agente para la solucion final: \n")
print("■ = Obstaculos (los 1's)")
print("O = Celda Libre")
print("S = Salida\n")

for lab in laberintoA:
    print('[', end='')
    for path in lab:
        if path == 1:
            path = '■'
        if path == 0:
            path = 'O'
        print(f" {path}", end='')
    print(" ]")

"""