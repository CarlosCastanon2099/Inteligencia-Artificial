import matplotlib.pyplot as plt
import networkx as nx

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
    
"""
    Realiza una búsqueda en profundidad (backtracking) para encontrar la salida en un laberinto.

    Parámetros:
    - agente (Agente): El agente que se mueve por el laberinto.
    - laberinto (list): El laberinto representado como una matriz.
    - visitados (set): Conjunto de celdas visitadas. Por defecto, es None.
    - instrucciones (list): Lista de instrucciones para llegar a la salida. Por defecto, es una lista vacía.

    Retorna:
    - bool: True si se encuentra la salida, False si no se encuentra.

"""


# Como tenemos laberintos de la forma 
'''
# Representación del laberinto
laberinto = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]
'''
# Vamos a trasladar esta matriz a una grafica de cuadricula 
# Entrada: Una matriz de mxn 
# Salida: Una grafica de cuadricula de mxn

# La grafica de cuadricula se puede hacer con la libreria matplotlib}
# pip install matplotlib
# pip install networkx
# import matplotlib.pyplot as plt


'''
Primero implementamos una funcion que dibuje el grafo de la matriz para trabajar sobre ella e implementar BFS o DFS
'''

def matrixToGraph(laberinto):
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

# Representación del laberinto
laberinto = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]

xAGENTE = 0
yAGENTE = 0

agente = Agente([xAGENTE,yAGENTE])

# Funcion que recibe la version matricial del laberinto y regresa la posicion (x,y) de la primera "S" que
# encuentre en el laberinto

def doxeaLaS(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == "S":
                return (i,j)


############################################
dibujar_grafo_laberinto(laberinto)
############################################

'''
Implementacion de BFS

Usando matrixToGraph tomaremos el laberinto y lo convertiremos en una grafica
a la cual le aplicaremos el algoritmo de BFS para encontrar la salida "S" desde un vertice
inicial "E" (o donde inicie el agente)

'''


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

    # Obtener la ruta más corta
    ruta_mas_corta = obtener_ruta_mas_corta(inicioVertice, finVertice, camino)
    print("Ruta más corta:", ruta_mas_corta)

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
    
    






laberintoGrafica = matrixToGraph(laberinto)
laberintoBSF = BFS(laberinto)
#dibujaBFS(laberintoBSF)



'''
Codigo que no se debe modificar
'''



#algoritmoBRUTAL = backtrack(agente, laberinto)


print("Representacion grafica de los pasos seguidos por el agente para la solucion final: \n")
print("■ = Obstaculos (los 1's)")
print("O = Celda Libre")
print("S = Salida\n")

for lab in laberinto:
    print('[', end='')
    for path in lab:
        if path == 1:
            path = '■'
        if path == 0:
            path = 'O'
        print(f" {path}", end='')
    print(" ]")