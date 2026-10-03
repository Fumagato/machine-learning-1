import random
import pygame

characters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
target = "To be or not to be"


class DNA:
    def __init__(self, length):
        self.genes = [random.choice(characters) for _ in range(length)]
        self.length = length
        self.fitness = 0

    def calculate_fitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        midpoint = random.randint(0, len(self.genes))
        child = DNA(0)
        child.genes = self.genes[:midpoint + 1] + partner.genes[midpoint + 1:]
        child.length = len(child.genes)
        return child

    def mutate(self, mutation_rate):
        if self.genes and random.random() < mutation_rate:
            index = random.randrange(len(self.genes))
            self.genes[index] = random.choice(characters)

    def get(self):
        return "".join(self.genes)

    def __repr__(self):
        return self.get() + " " + str(self.fitness)


class Population:
    def __init__(self, size, length):
        self.p = [DNA(length) for _ in range(size)]
        self.size = size
        self.length = length

    def calculate_fitness(self, target):
        for dna in self.p:
            dna.calculate_fitness(target)

    def select_parent(self, tournament_size=3):
        candidates = random.sample(self.p, min(tournament_size, len(self.p)))
        return max(candidates, key=lambda dna: dna.fitness)

    def reproduce(self, target, mutation_rate=0.05):
        self.p.sort(key=lambda dna: dna.fitness, reverse=True)
        next_generation = []

        while len(next_generation) < self.size:
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child = parent1.crossover(parent2)
            child.mutate(mutation_rate)
            child.calculate_fitness(target)

            if child.get() == target:
                return child

            next_generation.append(child)

        self.p = next_generation
        return None


def main(target_phrase=None, population_size=200, mutation_rate=0.05,
         verbose=False):
    if target_phrase is None:
        target_phrase = target

    population = Population(population_size, len(target_phrase))
    generation = 0

    while True:
        population.calculate_fitness(target_phrase)
        best = max(population.p, key=lambda dna: dna.fitness)
        if best.get() == target_phrase:
            return best.get()

        generate = population.reproduce(target_phrase, mutation_rate)
        if generate is not None:
            return generate.get()

        generation += 1
        if verbose:
            print(f"Generation {generation}: {best.get()}")


if __name__ == "__main__":
    # print(main(verbose=True))
    pass
