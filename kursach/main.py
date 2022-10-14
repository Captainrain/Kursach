import sys
from Settings import Settings
import pygame
from Ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("KURSACH")
    ship= Ship(screen)
   
    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
run_game()