import pygame
import random
#create a blueprint for an object
# An object is a very advanced variable 
class myrectangle():
    def __init__(self, x, y):
        self.x = x; self.y = y
        self.colour = (0,100,255)
        self.width = 50; self.height = 50
        self.hspeed = random.randint(-10,10); self.vspeed = random.randint(-10,10)
    def draw(self,screen):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height))
        return
    def update(self):
        self.x = self.x + self.hspeed
        self.y = self.y + self.vspeed
        return