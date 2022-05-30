import sys
from time import *
from tkinter import W
from pygame.locals import *
from os import dup
from utils import resource_path
from entities import *
from config import *
import math
import pygame

class SceneManager:
    def __init__(self, sc):
        self.sc = sc
        self.sceneChange = True

        self.scene = 4
        self.level = 1

        self.logo_font = pygame.font.Font(resource_path('assets/OpenSans-Bold.ttf'), 24)
        self.b_font = pygame.font.Font(resource_path('assets/OpenSans-Semibold.ttf'), 12)
        self.l_font = pygame.font.Font(resource_path('assets/OpenSans-Regular.ttf'), 14)
        self.font = pygame.font.Font(resource_path('assets/OpenSans-Regular.ttf'), 12)
    
    def renderScenes(self):
        match self.scene:
            case 0:
                self.mainMenuScene()
            case 1:
                self.singleplayerGame()
            case 2:
                self.multiplayerGame()
            case 3:
                self.settings()
            case 4:
                self.logo()
            case _:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                self.sc.fill((0, 0, 0))

                pygame.display.update()

                pygame.time.Clock().tick(FPS)
                    
        pygame.quit()
    

    ### SCENES
    def mainMenuScene(self):
        self.scene = 0
        bSingleplayer = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+28, "singleplayer", self.singleplayerGame, self.b_font)
        bMultiplayer = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+52, "multiplayer", self.singleplayerGame, self.b_font)
        bSettings = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+76, "settings", self.settings, self.b_font)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                
            if self.scene != 0:
                break

            self.sc.fill((0, 0, 0))

            for i in range(8):
                sface = self.logo_font.render(GAME_NAME[0], False, (142+(i*12) - round(math.sin(process_time()*3*((i/8)+2)) * 12), 126 + round(math.sin(process_time()*5*((i/8)+1)) * 12), 186 - round(math.sin(process_time()*3*((i/8)+2)))))
                self.sc.blit(sface, (WIDTH/2-16-(i*2)-116,HEIGHT/2-16-(i*2)-48))
                    
            for x in range(8):
                aface = self.logo_font.render(GAME_NAME[1], False, (142+(x*12) - round(math.sin(process_time()*3*((i/8)+2)) * 12), 96 + round(math.sin(process_time()*5*((i/8)+1)+0.5) * 15), 235 - round(math.sin(process_time()*3*((i/8)+2)) * 12)))
                self.sc.blit(aface, (WIDTH/2-16-(x*2)-116,HEIGHT/2-16-(x*2)-24))

            sface = self.logo_font.render(GAME_NAME[0], False, (255, 255, 255))
            self.sc.blit(sface, (WIDTH/2-16-(i*2)-116,HEIGHT/2-16-(i*2)-48))

            aface = self.logo_font.render(GAME_NAME[1], False, (255, 255, 255))
            self.sc.blit(aface, (WIDTH/2-16-(x*2)-116,HEIGHT/2-16-(x*2)-24))

            bSingleplayer.update(204 + round(math.sin(process_time()*5) * 25), 136, 255)
            bMultiplayer.update(204 + round(math.sin(process_time()*5) * 25), 146, 255)
            bSettings.update(204 + round(math.sin(process_time()*5) * 25), 156, 255)

            pygame.display.update()

            pygame.time.Clock().tick(FPS)

    def singleplayerGame(self):
        self.scene = 1
        player = PlayerCar(WIDTH/2, HEIGHT/2, 3.5, 3, 0.015, 0.1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            if self.scene != 1:
                break

            self.sc.fill((0, 0, 0))

            pygame.draw.circle(self.sc, RED, (player.x, player.y), 2, 0)
            pygame.draw.line(self.sc, GREEN, (player.x, player.y), (player.x + WIDTH * math.cos(math.radians(player.angle)),
                                                                player.y + WIDTH * math.sin(math.radians(player.angle))))
            player.update()
            pygame.display.update()

            pygame.time.Clock().tick(FPS)


    def settings(self):
        self.scene = 3
        bGoBack = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16-42, "return", self.mainMenuScene, self.b_font)
        bGraphics = ToggleButton(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+76, "ты гуль тру канеки ранг ссс?", self.settings, self.b_font, False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            
            if self.scene != 3:
                break

            self.sc.fill((0, 0, 0))

            bGoBack.update(204 + round(math.sin(process_time()*5) * 25), 156, 255)
            bGraphics.update(204 + round(math.sin(process_time()*5) * 25), 156, 255)

            pygame.display.update()

            pygame.time.Clock().tick(FPS)
    
    def logo(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            
            if self.scene != 4:
                break

            self.sc.fill((0, 0, 0))

            dface = self.l_font.render("made by", False, (255, 255, 255))
            self.sc.blit(dface, (WIDTH/2-(dface.get_width()/2),HEIGHT/2-(dface.get_height()/2)-12))

            fface = self.logo_font.render("discographi", False, (255, 255, 255))
            self.sc.blit(fface, (WIDTH/2-(fface.get_width()/2),HEIGHT/2-(fface.get_height()/2)+4))

            pygame.display.update()
            pygame.time.Clock().tick(FPS)

            pygame.time.wait(1500)
            self.mainMenuScene()

    def error(self, e):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
        
            self.sc.fill((0, 0, 0))
            dface = self.logo_font.render("exception", False, (255, 0, 0))
            self.sc.blit(dface, (WIDTH/2-(dface.get_width()/2),HEIGHT/2-(dface.get_height()/2)-16))
            
            cface = self.font.render(str(e), False, (255, 255, 255))
            self.sc.blit(cface, (WIDTH/2-(cface.get_width()/2),HEIGHT/2-(cface.get_height()/2-4)))

            pygame.display.update()
            pygame.time.Clock().tick(FPS)