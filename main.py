import random
import pygame

screen_size = (800, 600)

pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
fps = 120

life_span = 100


class Rocket:
    def __init__(self, x, y, dna):
        self.dna = dna
        self.fitness = 0
        self.gene_counter = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

    def apply_force(self, force):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def calculate_fitness(self, target):
        distance = pygame.math.Vector2.distance_to(
            self.position, target.position)
        self.fitness = 1 / (distance * distance)

    def crossover(self, partner):
        midpoint = random.randint(0, len(self.dna.genes))
        child = DNA()
        child.genes = self.dna.genes[:midpoint +
                                     1] + partner.dna.genes[midpoint + 1:]
        child.length = len(child.genes)
        return child

    def draw(self):
        pygame.draw.circle(screen, "red", self.position, 14)

    def run(self):
        self.apply_force(self.dna.genes[self.gene_counter])
        self.gene_counter += 1
        self.update()


class DNA:
    def __init__(self):
        self.genes = []
        self.max_force = 0.5
        for i in range(life_span):
            self.genes.append(random_vector2())
            self.genes[i] *= random.random() * self.max_force
            # print(self.genes[i])

    def mutate(self, mutation_rate):
        if self.genes and random.random() < mutation_rate:
            index = random.randrange(len(self.genes))
            self.genes[index] = random_vector2()


class Population:
    def __init__(self, length, mutation_rate, target):
        self.p = []
        self.mutation_rate = mutation_rate
        self.generation = 0
        for _ in range(length):
            self.p.append(Rocket(400, 300, DNA()))
        self.target = target

    def calculate_fitness(self, target):
        for rocket in self.p:
            rocket.calculate_fitness(target)

    def select_parent(self, tournament_size=3):
        parent = random.sample(self.p, min(tournament_size, len(self.p)))
        return max(parent, key=lambda rocket: rocket.fitness)

    def reproduction(self):
        next_generation = []
        while len(next_generation) < len(self.p):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child = parent1.crossover(parent2)
            child.mutate(self.mutation_rate)
            next_generation.append(
                Rocket(400, 300, child))
        self.p = next_generation

    def draw(self):
        for rocket in self.p:
            rocket.draw()

    def run(self):
        for rocket in self.p:
            rocket.run()


class Target:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, "blue", self.position, self.radius)


def random_vector2():
    vector = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    if vector.length() == 0:
        return vector
    else:
        return pygame.Vector2.normalize(vector)


def main(running):
    target = Target(400, 60, 20)
    population = Population(40, 0.01, target)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        target.draw()

        try:
            population.draw()
            population.run()
        except:
            population.calculate_fitness(target)
            population.reproduction()

        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main(running=True)
