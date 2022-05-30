from pygame.locals import *
from scenemanager import SceneManager
from entities import *
from config import *
import pygame

pygame.init()

window = pygame.display 
window.set_caption("moki")
sc = window.set_mode((WIDTH, HEIGHT), SCALED | DOUBLEBUF | RESIZABLE)

scenemanager = SceneManager(sc)
scenemanager.renderScenes()