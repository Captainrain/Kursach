import pygame
import sys

from Settings import *
from Ship import *
from bullet import *
#----------------------------------------------------------------
def fire_bullet(ai_settings, screen, ship, bullets):
    #Выпускает пулю, если максимум еще не достигнут.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
#----------------------------------------------------------------
def check_keydown_events(event, ai_settings, screen, ship, bullets):
        #Реагирует на нажатие клавиш.
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            #Создание новой пули и включение ее в группу bullets.
            fire_bullet(ai_settings, screen, ship, bullets)
#--------------------------------------------------------------------
def check_keyup_events(event, ship):
        #Реагирует на отпускание клавиш.
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_UP:
            ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False
#--------------------------------------------------------------------
class game_functions(object):
    #description of class
    #----------------------------------------------------------------
    def check_events(ai_settings, screen, ship, bullets):
        #Обрабатывает нажатия клавиш и события мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
    #----------------------------------------------------------------
    def update_screen(ai_settings, screen, ship, bullets):
        screen.fill(ai_settings.bg_color)
        #Все пули выводятся позади изображений корабля и пришельцев.
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        pygame.display.flip()
