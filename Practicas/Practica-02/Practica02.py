

class Agente:
    def __init__(self, posicion):
        self.posicion = posicion  # La posición inicial del agente

    def mover(self, direccion, laberinto):
        x, y = self.posicion
        if direccion == "arriba" and x > 0 and laberinto[x-1][y] != 1: # Mueve el agente arriba si no es límite superior y la celda destino no es un obstáculo.       
            self.posicion = [x-1, y]

        elif direccion == "abajo" and x < len(laberinto) - 1 and laberinto[x+1][y] != 1: # Mueve el agente abajo si no es límite inferior y la celda destino no es un obstáculo.     
            self.posicion = [x+1, y]

        elif direccion == "izquierda" and y > 0 and laberinto[x][y-1] != 1:# Mueve el agente izquierda si no es límite izquierdo y la celda destino no es un obstáculo.   
            self.posicion = [x, y-1]

        elif direccion == "derecha" and y < len(laberinto[0]) - 1 and laberinto[x][y+1] != 1:# Mueve el agente derecha si no es límite derecho y la celda destino no es un obstáculo. 
            self.posicion = [x, y+1]
            
        else:
            return None  # Devolver None si el movimiento no es válido
        
        return self.posicion


def flechas(direccion):
    if direccion == "arriba":
        return  "↑"
    elif direccion == "abajo":
        return  "↓"
    elif direccion == "izquierda":
        return  "←"
    elif direccion == "derecha":
        return  "→"
    



'''
Ejemplo:
Movimiento: derecha, Posición: [0, 1]
Movimiento: abajo, Posición: [1, 1]
Movimiento: abajo, Posición: [2, 1]
Movimiento: derecha, Posición: [2, 2]
Movimiento: abajo, Posición: [3, 2]
Movimiento: derecha, Posición: [3, 3]
Encontré la salida :D
'''
def backtrack_tremaux(agente, laberinto, visitados = None, instrucciones = []):
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
                if backtrack_tremaux(Agente(nueva_posicion), laberinto, visitados):
                    laberinto[agente.posicion[0]][agente.posicion[1]] = flechas(movimiento)
                    return True
                else:
                    laberinto[agente.posicion[0]][agente.posicion[1]] = 0
                    instrucciones.pop()
                    
        if movimiento == "derecha" and len(instrucciones) == 1:
            print("No hay ruta hacia la salida :c\n")
        return False


# El laberinto
# Aqui definimos el laberinto que usarémos para nuestro algoritmo.
    
laberinto = [
    ["E",  0,  0,    0,    0  ],
    [ 1,   0,  1,    1,    0  ],
    [ 0,   0,  0,    0,    0  ],
    [ 0,   1,  0,    1,    0  ],
    [ 0,   0,  0,    1,   "S"]
]


### El Agente
# Creamos una instancia del agente en la entrada del laberinto (que es la (0,0), pero puede cambiar)

agente = Agente([0,0])

### Llamada a nuestro algoritmo

# Finalmente, llamamos a nuestro algoritmo para que se ejecute y nos muestre si encontró la salida o no.

algoritmoBRUTAL = backtrack_tremaux(agente, laberinto)

# Representacion grafica:

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


### Generador aleatorio de laberintos



#Modificar los parametros de filas y columnas para generar laberintos de diferentes tamaños.
    
# Dimensiones del laberinto
filas = 25
columnas = 25

import random

# Crear el laberinto con todos los valores aleatorios
laberintoA = [[random.choice([0,1]) for _ in range(columnas)] for _ in range(filas)]

# Elegir una posición aleatoria para la entrada (E) y la salida (S)
entrada_fila, entrada_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
salida_fila, salida_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)

# Asegurarse de que la entrada y la salida no estén en la misma posición
while entrada_fila == salida_fila and entrada_columna == salida_columna:
    salida_fila, salida_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)

# Establecer la entrada (E) y la salida (S)
laberintoA[entrada_fila][entrada_columna] = 'E'
laberintoA[salida_fila][salida_columna] = 'S'

# Imprimir el laberinto
for fila in laberintoA:
    print(fila)

# laberintoA[entrada_fila][entrada_columna] = 'E'
agenteA = Agente( [entrada_fila, entrada_columna] )

algoritmoBRUTALISIMO = backtrack_tremaux(agenteA, laberintoA)


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