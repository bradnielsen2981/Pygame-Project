import pygame

class Player():

    def __init__(self, x, y):
        self.image = pygame.image.load("ninja.png")
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        return
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return

