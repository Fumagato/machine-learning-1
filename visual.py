import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True
fps = 30

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")

    pg.draw.circle(screen, "red", (400, 300), 30)

    pg.display.flip()
    clock.tick(fps)

pg.quit()
