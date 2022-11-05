import sys
import pygame
from pygame.sprite import Group

from Settings import Settings
from Ship import Ship
from game_functions import game_functions as gf
from GameStats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
     
    pygame.display.set_caption("KURSACH")   
    stats = GameStats(ai_settings) #Создание экземпляра для хранения игровой статистики.
    ship = Ship(ai_settings, screen) #Make spaceship   
    bullets = Group() #Создание группы для хранения пуль.    
    aliens = Group() #Создание группы пришельцев.       
    gf.create_fleet(ai_settings, screen, ship, aliens) #Создание флота пришельцев.
       
    while True: #Запуск основного цикла игры.
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
