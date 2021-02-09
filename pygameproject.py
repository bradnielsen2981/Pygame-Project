import pygame
from pygame.locals import *
import os, sys

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
label = myfont.render("Timer: ",True,(255,255,255))
screen.blit(label,(50,50))

#create a shape or line on the screen
#challenge: Draw three shapes or lines - look up pygame.draw

#play music
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play()


clock = pygame.time.Clock()
Exit = False
x = 0
y = 200
while not Exit: #game loop

    clock.tick(60) #framerate
    # Process Main Events and Logic
    for event in pygame.event.get():
        if event.type == QUIT:
            Exit = True

    #Logic
    x = x + 1

    #Drawing
    screen.blit(background, (0,0))
    pygame.draw.rect(screen,(255,0,0),(x,y,x+100,y+50))

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






