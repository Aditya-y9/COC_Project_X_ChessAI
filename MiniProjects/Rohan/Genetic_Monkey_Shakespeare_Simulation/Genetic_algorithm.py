import random

class Population:
    def __init__(self, target, mutation_rate, population_size):
        self.target = target # target phrase
        self.mutation_rate = mutation_rate 
        self.population_size = population_size # popmax : the number of maximum elements in population
        self.generations = 0 # number of generation (ie the number in sequence of pop) within population 
        self.finished = False # is the best phrase evolved ?
        self.best = "" # best phrase obtained
        self.population = []
        # array of elements(ie phrases) : stored by getting each individual phrase from class DNA
        for i in range(self.population_size):
           self.population[i] = DNA(len(target)) 
    
    def calc_fitness(self, target): # calculating fitness values of all members(phrases) of pop
        for i in range(len(self.population)): # dna is an item(obj) in list population which can access some var and func
            self.population[i].calcFitness(target) 
        

    def natural_selection(self): # generates a mating pool
        self.mating_pool = [] 
        self.max_fitness = 0 # stores the max fitness of member among all members in population list
        # list which stores entries of elements of population list for n times
        # Based on fitness, each member will get added to the mating pool a n number of times
        # a higher fitness = more entries to mating pool = more likely to be picked as a parent
        # a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        for i in range(len(self.population)): # To get max fitness
            if self.population[i].fitness > self.max_fitness:
                self.max_fitness = self.population[i].fitness
        if self.max_fitness == 0:
            self.max_fitness = 1  # To Avoid division by zero
        for dna in self.population:
            fitness = dna.fitness / self.max_fitness
            n = int(fitness * 100)
            self.mating_pool.extend([dna] * n)

    def generate(self):
        for i in range(self.population_size):
            a = random.choice(self.mating_pool)
            b = random.choice(self.mating_pool)
            child = a.crossover(b)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generations += 1

    def evaluate(self):
        world_record = 0.0
        index = 0
        for i, dna in enumerate(self.population):
            if dna.fitness > world_record:
                world_record = dna.fitness
                index = i

        self.best = self.population[index].getPhrase()
        if world_record == 1.0:
            self.finished = True

    def is_finished(self):
        return self.finished

    def get_generations(self):
        return self.generations

    def get_average_fitness(self):
        total = sum(dna.fitness for dna in self.population)
        return total / self.population_size

    def all_phrases(self):
        display_limit = min(self.population_size, 50)
        return [dna.get_phrase() for dna in self.population[:display_limit]]


def newChar():
    c = random.randint(63, 122) # Random int value that corresponds as ASCII value
    if c == 63: # c == '?' then c == " "
        c = 32
    if c == 64: # c == '@' then c == '.'
        c = 46
    return chr(c) # Returns a character to corresponding ASCII value

class DNA():
    def __init__(self, num): # num parameter is passed with the length of the target phrase
        self.genes = [] # array of char of phrase : stores element(member ie one phrase) of population
        self.fitness = 0 # Matching each char of genes with target phrase
        for i in range(num):
            self.genes[i] = newChar() # getting each char for a phrase

    def getPhrase(self):
        return ''.join(self.genes) # returns a character array genes into string

    def calcFitness(self, target): # calculating fitness of single phrase by matching each char of genes with target 
        score = 0
        for i in range(len(target)): # calculating score to calculate fitness: score +1 if char matches
            self.element = self.population[i] 
            if self.element[i] == target[i] :
                score+=1
        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random.random() < mutationRate:
                self.genes[i] = newChar()


def main():
    target = "To be or not to be."
    popmax = 5
    mutation_rate = 0.01

    population = Population(target, mutation_rate, popmax)
    print("Best phrase:")
    print(target)
    print("---------------")

    while not population.is_finished():
        population.calc_fitness(target)
        population.natural_selection()
        population.generate()
        population.evaluate()
        display_info(population)

def display_info(population):
    answer = population.best
    statstext = "Total generations: " + str(population.get_generations()) + "\n"
    statstext += "Average fitness: " + "{:.2f}".format(population.get_average_fitness()) + "\n"
    statstext += "Total population: " + str(population.population_size) + "\n"
    statstext += "Mutation rate: " + str(int(population.mutation_rate * 100)) + "%\n"

    print(statstext)
    print("Best phrase:")
    print(answer)
    print("---------------")

if __name__ == "__main__":
    main()
