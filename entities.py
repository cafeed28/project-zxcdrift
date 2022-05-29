import math
from tkinter import N
from xml.etree.ElementTree import tostring
import pygame

class PlayerCar:
    def __init__(self, x, y, max_vel, rotate_vel, dec_vel, accel_vel, drift_factor):
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
                self.angle -= (self.rotate_vel * ((self.vel * 1.5) / self.max_vel)) * (self.toLeft / 4)
            if (self.lastTurn == 1):
                self.angle += (self.rotate_vel * ((self.vel * 1.5) / self.max_vel)) * (self.toRight / 4)

        if (self.backwards == 0):
            if (self.vel > 0):
                self.vel = max(self.vel - self.dec_vel, 0)
        else:
            if (self.vel < 0):
                self.vel = min(self.vel + self.dec_vel, 0)

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.x += vertical
        self.y += horizontal

    