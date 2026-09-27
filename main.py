import random
import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True
fps = 30


class Mover:
    def __init__(self):
        self.position = pg.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)


m = Mover()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")

    pg.draw.circle(screen, "red", m.position, 30)

    pg.display.flip()
    clock.tick(fps)

pg.quit()
