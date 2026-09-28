import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True
fps = 30

position = pg.Vector2(400, 300)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")

    pg.draw.circle(screen, "red", position, 30)

    pg.display.flip()
    clock.tick(fps)

pg.quit()
