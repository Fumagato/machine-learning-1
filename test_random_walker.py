import random
import pygame


class Walker:
    def __init__(self, position):
        self.position = position

    def walk(self):
        roll = round(random.randint(1, 4))
        if roll == 1:
            self.position.y += 1
        elif roll == 2:
            self.position.x += 1
        elif roll == 3:
            self.position.y -= 1
        elif roll == 4:
            self.position.x -= 1

    def show(self):
        pygame.draw.rect(screen, "red", pygame.Rect(
            self.position.x, self.position.y, 4, 4))


walkman = Walker(pygame.Vector2(400/2, 300/2))
walkman.walk()

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
running = True
fps = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    walkman.walk()
    walkman.show()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
