import sys
import pygame
from pygame.sprite import Group

from Settings import Settings
from Ship import Ship
from bullet import *
from game_functions import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("KURSACH")   
    ship = Ship(ai_settings, screen) #Make spaceship   
    bullets = Group() #Создание группы для хранения пуль.
       
    while True: #Запуск основного цикла игры.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #Удаление пуль, вышедших за край экрана.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
