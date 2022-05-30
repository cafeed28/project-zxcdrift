from time import *
from pygame.locals import *
from os import dup
from entities import *
from config import *
import math
import pygame

class SceneManager:
    def __init__(self, sc):
        self.sc = sc
        self.sceneChange = True
        self.scene = 0
        self.level = 1
        self.logo_font = pygame.font.Font('assets/OpenSans-Bold.ttf', 24)
        self.font = pygame.font.Font('assets/OpenSans-Bold.ttf', 12)
    
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
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                self.sc.fill((0, 0, 0))

                pygame.display.update()

                pygame.time.Clock().tick(FPS)
                    
        pygame.quit()
    

    ### SCENES
    def mainMenuScene(self):
        self.scene = 0
        bSingleplayer = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+28, "singleplayer", self.singleplayerGame, self.font)
        bMultiplayer = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+52, "multiplayer", self.singleplayerGame, self.font)
        bSettings = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+76, "settings", self.settings, self.font)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                
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
        player = PlayerCar(WIDTH/2, HEIGHT/2, 3.5, 4, 0.025, 0.1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

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
        bGoBack = Button(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16-42, "return", self.mainMenuScene, self.font)
        bGraphics = ToggleButton(self.sc, WIDTH/2-16-16-114, HEIGHT/2-16-16+76, "ты гуль тру канеки ранг ссс?", self.settings, self.font, False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            
            if self.scene != 3:
                break

            self.sc.fill((0, 0, 0))

            bGoBack.update(204 + round(math.sin(process_time()*5) * 25), 156, 255)
            bGraphics.update(204 + round(math.sin(process_time()*5) * 25), 156, 255)

            pygame.display.update()

            pygame.time.Clock().tick(FPS)