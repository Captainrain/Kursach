import pygame
class Settings():
    def __init__(self):
        #settings of the ship
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3 #4, потому что нумерация с нуля

        #Параметры пули
        self.bullet_speed_factor = 3
        #self.bul
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Настройки пришельцев
        self.alien_speed_factor = 5 #скорость пришельца
        self.fleet_drop_speed = 10 #скорость снижения пришельцев
        self.fleet_direction = 1 #fleet_direction = 1 обозначает движение вправо; а -1 - влево.
