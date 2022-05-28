from entities import *
from config import *
import pygame

window = pygame.display
window.set_caption("moki")
sc = window.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = PlayerCar(20, 20, 3.5, 4, 0.025, 0.1, 4)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    player.update()

    sc.fill((0, 0, 0))
    pygame.draw.circle(sc, RED, (player.x, player.y), 2, 0)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()