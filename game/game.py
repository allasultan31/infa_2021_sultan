import movements
import pygame
from pygame.sprite import Group
from gun import Gun
from info import Info
from rating import Scores
from heart import Heart


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 800)) #холст
    pygame.display.set_caption("Мини геноцид")
    bg_color = ('papayawhip')
    gun = Gun(screen) #отрисовываем пушку на экране
    bullets = Group()
    pigs = Group()
    movements.create_army(screen, pigs)
    info = Info()
    heart = Heart(screen)
    sc = Scores(screen, info, heart)


    while True:
        movements.events(screen, gun, bullets)
        if info.run_game:
            bullets.update()
            gun.new_position()
            movements.update(bg_color, screen, info, sc, gun, pigs, bullets)
            movements.update_bullets(screen, info, sc, pigs, bullets)
            movements.update_pigs(info, screen, sc, gun, pigs, bullets)


run()