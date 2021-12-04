import pygame
import sys
from bullet import Bullet
from pig import Pig
import time
from heart import Heart

def events(screen, gun, bullets): #обработка событий
    for event in pygame.event.get():  # getting events
        if event.type == pygame.QUIT:  # exit from the game
            sys.exit()
        elif event.type == pygame.KEYDOWN: #to the right
            if event.key == pygame.K_RIGHT:
                gun.right = True
            elif event.key == pygame.K_LEFT: #to the left
                gun.left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP: #right
            if event.key == pygame.K_RIGHT:
                gun.right = False
            elif event.key == pygame.K_LEFT: #left
                    gun.left = False


def update(bg_color, screen , info, sc, gun, pigs, bullets): #uptade of the screen
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.withdraw()
    pigs.draw(screen)
    pygame.display.flip()  # drawing the last screen

def update_bullets(screen, info, sc, pigs, bullets): #updating the position of the bullet
    collisions = pygame.sprite.groupcollide(bullets, pigs, True, True)
    if collisions:
        for pigs in collisions.values():
            info.score += 5 * len(pigs)
        sc.score()
        check_hsc(info, sc)
        sc.image_hearts()
    if len(pigs) ==0:
        bullets.empty()
        create_army(screen, pigs)

def gun_kill(info, screen, sc, gun, pigs, bullets): #пушка и армия бжик
    if info.guns_left > 0:
        info.guns_left -= 1
        sc.image_hearts()
        pigs.empty()
        bullets.empty()
        create_army(screen, pigs)
        gun.create_gun()
        time.sleep(1)
    else:
        info.run_game = False
        sys.exit()

def update_pigs(info, screen, sc, gun, pigs, bullets): #updating the pozition of pigs
    pigs.update()
    if pygame.sprite.spritecollideany(gun, pigs):
        gun_kill(info, screen, sc, gun, pigs,bullets)
    pigs_check(info, screen, sc, gun, pigs, bullets)

def pigs_check(info, screen, sc, gun, pigs, bullets): #checking if pigs are in the bottom of screen
    screen_rect = screen.get_rect()
    for pig in pigs.sprites():
        if pig.rect.bottom >= screen_rect.bottom:
            gun_kill(info, screen, sc, gun, pigs, bullets)
            break

def create_army(screen, pigs): #creation of the army
    pig = Pig(screen)
    pig_width = pig.rect.width
    amount_pig_x = int((800 - 2 * pig_width) / pig_width)
    pig_height = pig.rect.height
    amount_pig_y = int((800 - 380 - 2 * pig_height) / pig_height)

    for row_number in range(amount_pig_y - 1):
        for pig_number in range(amount_pig_x):
            pig = Pig(screen)
            pig.x = (pig_width + pig_width * pig_number)
            pig.y = (pig_height + pig_height * row_number)
            pig.rect.x = pig.x
            pig.rect.y = pig.rect.height + 2 * pig.rect.height * row_number
            pigs.add(pig)


def check_hsc(info, sc): #checking of new high score
    if info.score > info.high_score:
        info.high_score = info.score
        sc.image_high_score()
        with open('hsc.txt', 'w') as f:
            f.write(str(info.high_score))




