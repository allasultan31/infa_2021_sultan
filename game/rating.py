import pygame.font
from gun import Gun
from heart import Heart
from pygame.sprite import Group

class Scores(): #game info
    def __init__(self, screen, info, heart): #initialization of the score
        self.screen = screen
        self.heart = heart
        self.screen_rect = screen.get_rect()
        self.info = info
        self.text_color = 'brown'
        self.font = pygame.font.SysFont(None, 35)
        self.score()
        self.image_high_score()
        self.image_hearts()

    def score(self): #text as graphic image
        self.image_score = self.font.render(str(self.info.score), True, self.text_color, 'papayawhip')
        self.score_rect = self.image_score.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 20

    def image_high_score(self): #high score as gr img
        self.high_score_img = self.font.render(str(self.info.high_score), True, self.text_color, 'papayawhip')
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top +20

    def image_hearts(self): #amount of hearts
        self.hearts = Group()
        for heart_number in range(self.info.guns_left):  #перебираем количество оставшихся пушек
            heart = Heart(self.screen)
            heart.rect.x = 15 + heart_number * heart.rect.width
            heart.rect.y = 20
            self.hearts.add(heart)


    def show_score(self): #score on the screen
        self.screen.blit(self.image_score, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.hearts.draw(self.screen)






