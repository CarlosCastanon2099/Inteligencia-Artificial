import random 

# Number of individuals in each generation 
# POPULATION_SIZE = 599

# Valid genes 
GENES = '''abcdefghijklmnopqrstuvwxyz'''

# Target string to be generated 
#TARGET = "dafne"

class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 

    @classmethod
    def mutated_genes(self): 
        ''' 
        create random genes for mutation 
        '''
        global GENES 
        gene = random.choice(GENES) 
        return gene 

    @classmethod
    def create_gnome(self): 
        ''' 
        create chromosome or string of genes 
        '''
        global TARGET 
        gnome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(gnome_len)] 

    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''

        # chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     

            # random probability   
            prob = random.random() 

            # if prob is less than 0.45, insert gene 
            # from parent 1  
            if prob < 0.45: 
                child_chromosome.append(gp1) 

            # if prob is between 0.45 and 0.90, insert 
            # gene from parent 2 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 

            # otherwise insert random gene(mutate),  
            # for maintaining diversity 
            else: 
                child_chromosome.append(self.mutated_genes()) 

        # create new Individual(offspring) using  
        # generated chromosome for offspring 
        return Individual(child_chromosome) 

    def cal_fitness(self): 
        ''' 
        Calculate fitness score, it is the number of 
        characters in string which differ from target 
        string. 
        '''
        global TARGET 
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if gs != gt: fitness+= 1
        return fitness 





# Cargamos el Diccionario.txt
diccionarioPalabras = open("Diccionario.txt", "r", encoding="utf8")

# Definimos la palabra a buscar
TARGET = "carlos"

# Obtenemos la longitud de la palabra a buscar 
longitudPalabra = len(TARGET)
# longitudOG = longitudPalabra + 1

# Creamos una lista con las palabras que tienen la misma longitud que la palabra a buscar
palabras = []
for palabra in diccionarioPalabras:
    if len(palabra) == longitudPalabra:
        palabras.append(palabra)

# Cerramos el archivo
diccionarioPalabras.close()

# Definimos a nuestra poblacion como todas las palabras que tienen la misma longitud que la palabra a buscar
# POPULATION_SIZE = len(palabras)
POPULATION_SIZE = 999

# Definimos la poblacion
population = []
for palabra in palabras:
    population.append(Individual(palabra))

# Definimos el numero de generaciones
generations = 100

# Definimos la variable que nos dira si encontramos la palabra
found = False


# Algoritmo de busqueda genetica para el juego del ahorcado

# generation
generation = 0

while not found: 

    # sort the population in increasing order of fitness score 
    population = sorted(population, key = lambda x:x.fitness) 

    # if the individual having lowest fitness score ie.  
    # 0 then we know that we have reached to the target 
    # and break the loop 

    # Otherwise generate new offsprings for new generation 
    new_generation = [] 

    # Perform Elitism, that mean 10% of fittest population 
    # goes to the next generation 
    s = int((10*POPULATION_SIZE)/100) 
    new_generation.extend(population[:s]) 

    # From 50% of fittest population, Individuals  
    # will mate to produce offspring 
    s = int((90*POPULATION_SIZE)/100) 
    for _ in range(s): 
        parent1 = random.choice(population[:50]) 
        parent2 = random.choice(population[:50]) 
        child = parent1.mate(parent2) 
        new_generation.append(child) 

    population = new_generation 

    generation += 1

    print("Generation: {}\tString: {}\tFitness: {}". 
            format(generation, 
            "".join(population[0].chromosome), 
            population[0].fitness)) 

    if population[0].fitness <= 0: 
        found = True
        break

'''

def main(): 
    # Ejecutamos lo que se encuentra en el while
    pass

if __name__ == '__main__':
    main()
'''    