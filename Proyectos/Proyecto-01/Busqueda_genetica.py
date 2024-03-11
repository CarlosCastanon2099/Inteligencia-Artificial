import random 
# Genes validos para el algoritmo genetico
ALF = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'])

# Clase para la creación de individuos de una población
class Individual(object): 

    # Inicialización de un objeto tipo individuo
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.calificar_ajuste()

    # Crear genes aleatorios para la mutación
    @classmethod
    def mutated_genes(self): 
        gene = random.choice(GENES) 
        return gene 
  
    # Crear cromosomas de los genes
    @classmethod
    def create_gnome(self):
        gnome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(gnome_len)] 
  
    # La unión de individuos para la creación de uno nuevo
    def emparejar(self, par2): 
  
        # Creamos una lista de cromosomas del emparejamiento
        cromosoma_hijos = [] 
        counter = -1
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
            counter += 1
            
            if TARGET[counter] != '_':
                cromosoma_hijos.append(TARGET[counter])
                continue
            prob = random.random() 

            # Si la probabilidad es menor de 0.45, insertamos al primer gen
            if prob < 0.35: 
                cromosoma_hijos.append(gp1) 
  
            # Sino, y la probabilidad es menor de 0.90, lo insertamos al segundo gen
            elif prob < 0.60: 
                cromosoma_hijos.append(gp2) 
  
            # Sino, insertamos un gen aleatorio
            else:
                cromosoma_hijos.append(self.mutated_genes()) 
  
        # Creamos un nuevo individuo y lo regresamos
        return Individual(''.join(cromosoma_hijos)) 
  

    # Funcion para regresar la calificación a que tan
    # cercana esta la palabra de la original
    def calificar_ajuste(self): 
        calculo = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if   gt == '_' and gs in LETRAS_USADAS: calculo += 1
            elif gt != '_' and gt != gs: calculo += 1

        if self.chromosome not in palabras: calculo += 1
        return calculo


def create_population(POPULATION_SIZE):
    population = []
    for _ in range(POPULATION_SIZE): 
        palabra_aleatoria = list(TARGET)
        for ind_letra in range(len(palabra_aleatoria)):
            if palabra_aleatoria[ind_letra] == '_':
                palabra_aleatoria[ind_letra] = random.choice(GENES) 
        population.append(Individual(''.join(palabra_aleatoria)))
    return population

def get_palabras():
    palabras = []
    # Cargamos el Diccionario.txt
    with open("Diccionario.txt", "r", encoding="utf8") as diccionarioPalabras:
        for palabra in diccionarioPalabras:
            if len(palabra) - 1 == len(TARGET):
                palabras.append(palabra[:-1])
    return palabras

def create_dict_poblacion(palabras_poblacion):
    dict_poblacion = dict()
    # Iteramos por todas las palabras de la población y por las letras
    # que son necesarias revisar (Las que estan como '_' en la palabra original)
    for palabra in palabras_poblacion:
        for indice in range(len(palabra)):
            if TARGET[indice] == '_':
                if palabra[indice] in dict_poblacion:
                    dict_poblacion[palabra[indice]] += 1
                else:
                    dict_poblacion[palabra[indice]] = 1
    return dict_poblacion

def genetica(palabra, usadas):
    
    # Hacemos que las variables sean globales para que funcionen con la clase
    global TARGET
    TARGET = palabra
    global LETRAS_USADAS
    LETRAS_USADAS = usadas

    # Genes validos para el algoritmo genetico
    global GENES
    GENES = list(ALF - set(LETRAS_USADAS))

    # El numero de generaciones necesarias
    MAX_GENERATIONS = 20
    
    # Definimos a nuestra poblacion como todas las palabras que tienen la misma longitud que la palabra a buscar
    POPULATION_SIZE = 1000

    # Creamos una lista con las palabras que tienen la misma longitud que la palabra a buscar
    global palabras
    palabras = get_palabras()

    # Definimos la poblacion
    population = create_population(POPULATION_SIZE)

    # Contador de la generacion actual
    generation = 0

    # Algoritmo de busqueda genetica para el juego del ahorcado
    while MAX_GENERATIONS - generation > 0: 
        # Ordenar la población de acuerdo a su calificación en el ajuste
        population = sorted(population, key = lambda x:x.fitness)
    
        # Si el individuo tiene una calificación de 0, esto significa
        # que el individuo cumple con los parametros que pedimos
        # Sino, creamos una nueva generación
        new_generation = [] 

        # Nos quedamos nomas con el 10% de la población mas cercana al 
        # resultado esperado
        s = int((10*POPULATION_SIZE)/100) 
        new_generation.extend(population[:s]) 

        # Procedemos a cruzar la mitad mas cercana al resultado de nuestra
        # población original y agregarla a nuestra generación deseada
        s = int((90*POPULATION_SIZE)/100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.emparejar(parent2) 
            new_generation.append(child) 

        # Nuestra nueva generación se convierte en nuestra futura poblaciónd deseada
        population = new_generation 

        # Aumentamos nuestro contado de generación
        generation += 1

        # print("Generation: {}\tString: {}\tFitness: {}". 
        #         format(generation, 
        #         "".join(population[0].chromosome), 
        #         population[0].fitness)) 


        # Si el fitness del primer individuo de la población es 0, salimos porque
        # encontramos una palabra con los aspectos deseados
        if population[0].fitness <= 0:
            break

    # Ordenar la población de acuerdo a su calificación en el ajuste
    population = sorted(population, key = lambda x:x.fitness)

    # Procedemos a obtener las palabras con fitness == 0
    palabras_poblacion = [i.chromosome for i in population if i.fitness == 0]
    
    # Procedemos a tener el diccionario de la población
    dict_poblacion = create_dict_poblacion(palabras_poblacion)
    # Creamos las variables de la letra mas repetida y del numero de la letra
    letra_elegida = ""
    repet_letra = 0

    # Vamos llenando el diccionario con la cantidad de repeticiones de las letras
    for key in dict_poblacion.keys():
        if dict_poblacion[key] > repet_letra:
            letra_elegida = key
            repet_letra = dict_poblacion[key]

    # print(palabras_poblacion)
    # print(letra_elegida)
    # print(repet_letra)

    # Regresamos la letra mas repetida entre las palabras elegidas
    if letra_elegida == '':
        letra_elegida = random.choice(GENES)
    # print(letra_elegida)
    return letra_elegida


if __name__ == '__main__':
    
    palabra = "_r_o_"
    letras = ['a','o','n','r','b']
    genetica(palabra, letras)