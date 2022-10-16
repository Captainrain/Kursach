import pygame
#--------------------------------------------------------------------
class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #Инициализирует корабль и задает его начальную позицию
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    #----------------------------------------------------------------    
    def update(self):
        #Обновляет позицию корабля с учетом флагов
        # Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center 
    #----------------------------------------------------------------   
    def blitme(self):
        self.screen.blit(self.image, self.rect)
