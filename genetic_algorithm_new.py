import random

characters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
target = "fumagato"


class DNA:
    def __init__(self, length):
        self.genes = []
        self.length = length
        self.fitness = 0
        for _ in range(self.length):
            self.genes.append(random.choice(characters))

    def calculate_fitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        # 'len(self.genes) - 1' or not '- 1', idk the difference
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = partner.genes[i]
            else:
                child.genes[i] = self.genes[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.randint(0, 100) < mutation_rate:
                self.genes[i] = random.choice(characters)

    def get(self):
        return "".join(self.genes)

    def __repr__(self):  # For debugging
        return "".join(self.genes) + " " + str(self.fitness)


class Population:
    def __init__(self, size, length):
        self.p = []
        self.size = size
        self.length = length
        for _ in range(size):
            dna = DNA(length)
            self.p.append(dna)

    def calculate_fitness(self, target):
        for dna in self.p:
            dna.calculate_fitness(target)

    def create_mating_pool(self) -> list:
        mp = []
        for dna in self.p:
            n = int(dna.fitness * 100)
            for _ in range(n):
                mp.append(dna)
            mp.append(dna)
        return mp

    def weighted_selection():
        index = 0
        start = random()


def create_population(size, length):
    p = []
    for _ in range(size):
        dna = DNA(length)
        p.append(dna)
    return p


def create_mating_pool(population):
    mp = []
    for dna in population:
        n = int(dna.fitness * 100)
        for _ in range(n):
            mp.append(dna)
        mp.append(dna)
    return mp


def weighted_selection():  # Unfinished
    index = 0
    start = random.random()


def reproduce(population, mating_pool):
    for i in range(len(population)):
        # Apply the weighted_selection() here instead of random.choice()
        parent1 = random.choice(mating_pool)
        parent2 = random.choice(mating_pool)
        child = parent1.crossover(parent2)
        child.mutate(0.1)

        child.calculate_fitness(target)

        population[i] = child

        global attempt
        attempt += 1
        print(f"attempt {attempt}: {child.get()}")
        if child.get() == target:
            global running
            running = False
            break


attempt = 0
running = True


def main():
    population = create_population(100, len(target))
    for dna in population:
        dna.calculate_fitness(target)
    while running:
        mating_pool = create_mating_pool(population)
        reproduce(population, mating_pool)


main()
