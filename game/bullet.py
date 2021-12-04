import pygame
from pygame.sprite import Sprite

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun): #creating the bullet in the position of the gun
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 7, 12)
        self.color = 'firebrick4'
        self.speed = 6.5
        self.rect.centerx = gun.rect.centerx #coordi of the bullet (x)
        self.rect.top = gun.rect.top #coordi of the bullet (y)
        self.y = float(self.rect.y)

    def update(self): #the bullet moves up
        self.y -=self.speed
        self.rect.y = self.y

    def draw_bullet(self): #drawing the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)



