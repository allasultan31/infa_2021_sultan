import pygame
from pygame.sprite import Sprite

class Gun(Sprite): #pushka
    def __init__(self, screen): #initialization of the gun
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image\pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx #center of the gun is the center of the screen
        self.center = float(self.rect.centerx) #можем назначать вещественные числа
        self.rect.bottom = self.screen_rect.bottom
        self.right = False
        self.left = False


    def withdraw(self): #drawing the gun
        self.screen.blit(self.image, self.rect) #отрисовываем


    def new_position(self): #новая позиция пушки
        if self.right and self.rect.right < self.screen_rect.right:
            self.center +=2
        if self.left and self.rect.left > 0:
            self.center -=2

        self.rect.centerx = self.center


    def create_gun(self): #creating new gun
        self.center = self.screen_rect.centerx




