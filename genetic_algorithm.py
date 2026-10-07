import random

characters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# NOTE:
# HOLY SHI I ACTUALLY DID IT WTF
# A LITTLE BIT INEFFICIENT BUT I DON'T CARE
# LET'S GOOOOOO


class Solution:
    def __init__(self, genes):
        self.genes = genes
        self.fscore = 0  # Fitness score

    def wrd(self):  # Word
        return "".join(self.genes)

    def __repr__(self):  # For debugging
        return "".join(self.genes) + " " + str(self.fscore)


def breed(parent1, parent2):
    child = Solution([])
    child.genes += parent1.genes
    midpoint = random.randint(0, len(parent1.genes))
    for i in range(len(child.genes)):
        if i > midpoint:
            child.genes[i] = parent2.genes[i]
    return child


def measure_fscore(target, solution):
    solution.fscore = 0
    for i in range(len(target)):
        # If the correct character is in the correct place, fitness score + 1
        if solution.genes[i] == target[i]:
            solution.fscore += 1
    return solution


def apply_mutation(solution):
    chance = 5  # 20% chance of mutation by default

    # Guaranteed mutation if child has 0 fitness score
    # if solution.fscore == 0:
    #     chance = 100

    if random.randint(1, 100) <= chance:
        i = random.randint(0, len(solution.genes) - 1)
        solution.genes[i] = random.choice(characters)
    return solution


def generate_population(amount, pw):
    pool = []
    for _ in range(amount):
        solution = Solution([])
        for _ in range(len(pw)):
            solution.genes.append(random.choice(characters))
        pool.append(solution)
    return pool


def choose_parents(population, number_of_parents):
    # Choose 3 random solutions/parents in population
    # Put them in tournament
    # Tournament return the best parent out of 3
    # Put the parent in list, then return them after the loop finished
    parents = []
    while len(parents) != number_of_parents:
        tournament_candidates = []
        while len(tournament_candidates) != 3:
            candidate = random.choice(population)
            if candidate not in tournament_candidates:
                tournament_candidates.append(candidate)
        best_parent = tournament(tournament_candidates)
        if best_parent not in parents:
            parents.append(best_parent)
    return parents


def tournament(parents):
    parents.sort(key=lambda p: p.fscore, reverse=True)
    return parents[0]


def main():
    # password = input("Type something I'll guess: ")
    password = "To be or not to be"

    # Test password
    # password = "Fumagato"
    # password = "My name is Fuma and I like chocolate glazed donuts"
    # password = "Fumagato Fumagato Fumagato"

    # Checks if a letter in password is not in characters variable
    for i in password:
        if i not in characters:
            print(":(")
            return

    # Settings
    population_amount = 100
    elite_amount = 10

    # Program starts here
    population = generate_population(population_amount, password)
    for p in population:
        measure_fscore(password, p)

    attempts = 0
    while True:
        population.sort(key=lambda p: p.fscore, reverse=True)

        new_population = []
        for _ in range(population_amount - elite_amount):
            parents = choose_parents(population, 2)
            c = breed(parents[0], parents[1])

            apply_mutation(c)
            measure_fscore(password, c)
            new_population.append(c)

            attempts += 1
            print(f"ATTEMPT {attempts}: {c.wrd()}")

            if c.wrd() == password:
                return

        del population[elite_amount:population_amount + 1]
        population += new_population


if __name__ == "__main__":
    main()
