import pygame
class GameStats(object): #класс дл€ ведени€ статистики
    def __init__(self, ai_settings):
    #»нициализирует статистику.
        self.ai_settings = ai_settings
        self.reset_stats()       
        self.game_active = True #»гра Alien Invasion запускаетс€ в активном состо€нии.
    #--------------------------------------------------------------------
    def reset_stats(self):
    #»нициализирует статистику, измен€ющуюс€ в ходе игры.
        self.ships_left = self.ai_settings.ship_limit
    #--------------------------------------------------------------------
