from src.logic.entities import *
from src.config import *
import pygame

window = pygame.display
window.set_caption("moki")
sc = window.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = PlayerCar(20, 20, 3.5, 4, 0.025, 0.1, 0.8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    player.update()

    sc.fill((0, 0, 0))
    
    pygame.draw.circle(sc, RED, (player.x, player.y), 2, 0)
    pygame.draw.line(sc, GREEN, (player.x, player.y), (player.x + WIDTH * math.cos(math.radians(player.angle)),
                                                       player.y + WIDTH * math.sin(math.radians(player.angle))))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()