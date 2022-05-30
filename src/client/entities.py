import math
from time import process_time
import pygame

### GAME ENTITIES
class PlayerCar:
    def __init__(self, x, y, max_vel, rotate_vel, dec_vel, accel_vel):
        self.x, self.y = x, y

        self.max_vel = max_vel
        self.rotate_vel = rotate_vel
        self.vel = 0
        self.angle = 0

        self.dec_vel = dec_vel
        self.accel_vel = accel_vel
        self.accel = 0
        self.dec = 0

        self.lastTurn = 0
        self.toLeft = 0
        self.toRight = 0

        self.backwards = 0


    def steer(self):
        self.vel = min(self.vel + self.accel_vel, self.max_vel)
    
    def brake(self):
        if (self.vel > 0):
            self.vel = max(self.vel - self.accel_vel, 0)
        else:
            self.vel = max(self.vel - self.accel_vel, -self.max_vel/2)
    

    def rbrake(self):
        if (self.backwards == 0):
            self.vel = max(self.vel - self.accel_vel, 0)
        else:
            self.vel = min(self.vel + self.accel_vel, 0)


    def rotate(self, left=False, right=True):
        if left:
            self.lastTurn = 0
            self.angle -= (self.rotate_vel * ((self.vel * 1.5) / self.max_vel)) * self.toLeft
        elif right:
            self.lastTurn = 1
            self.angle += (self.rotate_vel * ((self.vel * 1.5) / self.max_vel)) * self.toRight


    def update(self):
        keys = pygame.key.get_pressed()

        self.move()
        if keys[pygame.K_w or pygame.K_UP]:
            self.backwards = 0
            self.steer()
        if keys[pygame.K_s or pygame.K_DOWN]:
            self.backwards = 1
            self.brake()
        if keys[pygame.K_SPACE]:
            self.rbrake()
        if keys[pygame.K_a or pygame.K_LEFT]:
            self.toLeft = min(self.toLeft + 0.05, 1)
            self.rotate(left=True)
        if keys[pygame.K_d or pygame.K_RIGHT]:
            self.toRight = min(self.toRight + 0.05, 1)
            self.rotate(right=True)

        self.toLeft = max(self.toLeft - 0.025, 0)
        self.toRight = max(self.toRight - 0.025, 0)

        if not keys[pygame.K_d or pygame.K_RIGHT] or not keys[pygame.K_a or pygame.K_LEFT]:
            if (self.lastTurn == 0):
                self.angle -= (self.rotate_vel * ((self.vel * 1.5) / self.max_vel)) * (self.toLeft / 2)
            if (self.lastTurn == 1):
                self.angle += (self.rotate_vel * ((self.vel * 1.5) / self.max_vel)) * (self.toRight / 2)

        if (self.backwards == 0):
            if (self.vel > 0):
                self.vel = max(self.vel - self.dec_vel, 0)
        else:
            if (self.vel < 0):
                self.vel = min(self.vel + self.dec_vel, 0)

    def move(self):
        radians = math.radians(self.angle)
        vertical = (math.cos(radians) * self.vel)
        horizontal = (math.sin(radians) * self.vel)

        self.x += vertical
        self.y += horizontal

class EnemyCar:
    def __init__(self):
        self.x, self.y = 0, 0
        self.angle = 0

    def update(self, x, y, angle):
        self.x, self.y, self.angle = x, y, angle



### UI ENTITIES
class Button:
    def __init__(self, sc, x, y, text, func, font):
        self.sc = sc
        self.x, self.y = x, y
        self.text = text
        self.rect = pygame.Rect(x, y, 8*len(text), 18)
        self.font = font
        self.func = func

    def update(self, r, g, b):
        pos = pygame.mouse.get_pos()

        for i in range(64):
            for x in range(8):
                pygame.draw.rect(self.sc, (max(r-(i*6)-(x*24)-round(math.sin(process_time()*5) * 2 * i), 0),
                                            max(g-(i*6)-(x*32), 0),
                                            max(b-(i*6)-(x*24)-round(math.sin(process_time()*5) * 1 * i), 0)), 
                                            pygame.Rect(self.x+(i*2)+(x*2), self.y+(x*2), 2, 18))

        surface = self.font.render(self.text, False, (255, 255, 255))
        self.sc.blit(surface, (self.x+8, self.y))

        if self.rect.collidepoint(pos):
            pygame.draw.line(self.sc, (255, 255, 255, 25), (self.x-3, self.y), (self.x-3, self.y+17))
            if pygame.mouse.get_pressed()[0] == 1:
                self.func()
                
class ToggleButton:
    def __init__(self, sc, x, y, text, func, font, toggled):
        self.sc = sc
        self.x, self.y = x, y
        self.text = text
        self.rect = pygame.Rect(x, y, 8*len(text), 18)
        self.font = font
        self.func = func
        self.mouseHold = False
        self.toggled = toggled

    def update(self, r, g, b):
        pos = pygame.mouse.get_pos()

        for i in range(64):
            for x in range(8):
                if self.toggled:
                    f = 30
                else:
                    f = 0
                pygame.draw.rect(self.sc, (max(r-(i*6)-(x*24)-round(math.sin(process_time()*5) * 2 * i), 0),
                                            max(g-(i*6)-(x*32)+(f/3), 0),
                                            max(b-(i*6)-(x*24)-round(math.sin(process_time()*5) * 1 * i)-f, 0)), 
                                            pygame.Rect(self.x+(i*2)+(x*2), self.y+(x*2), 2, 18))

        surface = self.font.render(self.text, False, (255, 255, 255))
        self.sc.blit(surface, (self.x+8, self.y))

        if self.toggled:
            pygame.draw.line(self.sc, (255, 255, 255, 25), (self.x-3, self.y), (self.x-3, self.y+17))

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.mouseHold == False:
                    self.mouseHold = True
                    self.toggled = not self.toggled
            else:
                self.mouseHold = False