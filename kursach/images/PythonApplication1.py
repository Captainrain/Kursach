import sys
import pygame
from pygame.sprite import Group

from Settings import Settings
from Ship import Ship
from game_functions import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
     
    pygame.display.set_caption("KURSACH")   
    ship = Ship(ai_settings, screen) #Make spaceship   
    bullets = Group() #�������� ������ ��� �������� ����.    
    aliens = Group() #�������� ������ ����������.
    
    
    # �������� ����� ����������.
    gf.create_fleet(ai_settings, screen, ship, aliens)
       
    while True: #������ ��������� ����� ����.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        #�������� ����, �������� �� ���� ������.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))

        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()