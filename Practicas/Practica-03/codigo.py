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
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_weight='bold')
    plt.show()

# Representación del laberinto
laberinto = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S" ]
]


dibujar_grafo_laberinto(laberinto)




agente = Agente([0,0])


algoritmoBRUTAL = backtrack(agente, laberinto)


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