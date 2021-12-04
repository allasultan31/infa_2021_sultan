import pygame
from pygame.sprite import Sprite
class Heart(Sprite):
    def __init__(self, screen,): #initialization of the heart
        super(Heart, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/heart.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


    def output(self): #drawing heart
        self.screen.blit(self.image, self.rect)