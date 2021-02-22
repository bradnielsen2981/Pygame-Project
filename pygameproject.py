import pygame
from pygame.locals import *
import os, sys
import random
from myrectangle import myrectangle
from player import Player

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

rectanglelist = []
hero = Player(200,200)
 
pygame.time.set_timer(USEREVENT + 1, 3000)

while not Exit: #game loop

    clock.tick(60) #framerate
    # Process Main Events and Logic
    for event in pygame.event.get():
        if event.type == QUIT:
            Exit = True
        elif event.type == USEREVENT + 1:
            newrectangle = myrectangle(random.randint(0,1024),random.randint(0,600))
            rectanglelist.append(newrectangle)
            pygame.time.set_timer(USEREVENT + 1, 3000)

    #Process Input
    pressed = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #Logic
    timer = int(pygame.time.get_ticks()/1000)
    timer = str(timer)
    label = myfont.render("Time: " + timer,True,(255,255,255))
    
    for r in rectanglelist:
        r.update(dimensions)
        
    hero.update(pressed)
    
    #Drawing
    screen.blit(background, (0,0))
    screen.blit(label,(50,50))
    for r in rectanglelist:
        r.draw(screen)
    hero.draw(screen)

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






