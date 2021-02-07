import pygame
from pygame.locals import *
import os, sys

pygame.init()
pygame.mixer.init()
pygame.font.init()

#create display
dimensions = [1024, 600]
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
pygame.draw.rect(screen,(255,0,0),(200,150,100,50))


#play music
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play()

pygame.display.flip()

input("Press Enter to Exit") #pause the screen using console
pygame.quit()
sys.exit(0)







