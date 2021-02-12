import pygame
from pygame.locals import *
import os, sys
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

#create display
dimensions = (1024, 600)
pygame.display.set_mode(dimensions)
pygame.display.set_caption('My Space Game')
screen = pygame.display.get_surface() # Surface object
screen.fill((124, 255, 0)) #(255,255,255)  R,G,B

#create an image object
background = pygame.image.load("background.jpg") 
screen.blit(background, (0,0)) #blit command can be used to show any image.

#create a font
myfont = pygame.font.SysFont('ArialBold', 30)

#create a shape or line on the screen
#challenge: Draw three shapes or lines - look up pygame.draw

#play music
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play()


clock = pygame.time.Clock()
Exit = False
x = 0
y = 200

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

rectanglelist = []
for i in range(0,50):
    newrectangle = myrectangle(512,300) #create instance of an object of that class - class CONSTRUCTOR
    rectanglelist.append(newrectangle)

while not Exit: #game loop

    clock.tick(60) #framerate
    # Process Main Events and Logic
    for event in pygame.event.get():
        if event.type == QUIT:
            Exit = True

    #Logic
    timer = int(pygame.time.get_ticks()/1000)
    timer = str(timer)
    label = myfont.render("Time: " + timer,True,(255,255,255))

    for r in rectanglelist:
        r.update()
    
    #Drawing
    screen.blit(background, (0,0))
    screen.blit(label,(50,50))

    for r in rectanglelist:
        r.draw(screen)

    #flip
    pygame.display.flip()


pygame.quit()
sys.exit()


    #Process events
    # Control the rate at which game run --> framerate set to 60fps #


   
    
    #Update game objects and do logic
    #Draw game objects
    #get_fps(), pygame.time.get_ticks() #time in milliseconds since pygame.init() was called
    #Flip screen






