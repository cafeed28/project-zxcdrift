import math
from tkinter import N
from turtle import backward
import pygame

class PlayerCar:
    def __init__(self, x, y, max_vel, rotate_vel, dec_vel, accel_vel, gearbox):
        self.x, self.y = x, y
        self.max_vel = max_vel
        self.rotate_vel = rotate_vel
        self.vel = 0
        self.angle = 0

        self.dec_vel = dec_vel
        self.accel_vel = accel_vel
        self.accel = 0
        self.dec = 0

        self.backwards = 0

        self.gearbox = gearbox
        self.gearbox_cur = 0


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
            self.vel = min(self.vel - self.accel_vel, 0)


    def rotate(self, left=False, right=True):
        try:
            if left:
                self.angle -= self.rotate_vel * (self.max_vel / self.vel)
            elif right:
                self.angle += self.rotate_vel * (self.max_vel / self.vel)
        except ZeroDivisionError:
            return None


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
            self.rotate(left=True)
        if keys[pygame.K_d or pygame.K_RIGHT]:
            self.rotate(right=True)

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

    