import pygame

class Pig(pygame.sprite.Sprite): #class of one pig
    def __init__(self, screen): #initialization of the first position
        super(Pig,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image\pig.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self): #pig on the screen
        self.screen.blit(self.image, self.rect)

    def update(self): #pigs moving
        self.y +=0.1
        self.y +=0.1
        self.rect.y = self.y


