import pygame, sys
from time import sleep #импортируем sleep() из time, чтобы приостановить игру

from Settings import *
from Ship import *
from bullet import *
from Alien import *

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
        elif event.key == pygame.K_q:
            sys.exit()
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
def get_number_aliens_x(ai_settings, alien_width):
#Вычисляет количество пришельцев в ряду.
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
#--------------------------------------------------------------------
def get_number_rows(ai_settings, ship_height, alien_height):
#Определяет количество рядов, помещающихся на экране.
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
#--------------------------------------------------------------------
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
#Создает пришельца и размещает его в ряду.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
 #--------------------------------------------------------------------
def check_fleet_edges(ai_settings, aliens):
    #Реагирует на достижение пришельцем края экрана.
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break   
#--------------------------------------------------------------------
def change_fleet_direction(ai_settings, aliens):
#Опускает весь флот и меняет направление флота.
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1    
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
    def update_screen(ai_settings, screen, ship, aliens, bullets):
        screen.fill(ai_settings.bg_color)
        #Все пули выводятся позади изображений корабля и пришельцев.
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        ship.blitme()
        aliens.draw(screen)
        #Отображение последнего прорисованного экрана.
        pygame.display.flip()
    #--------------------------------------------------------------------
    def create_fleet(ai_settings, screen, ship, aliens):
        #Создает флот пришельцев.
        #Создание пришельца и вычисление количества пришельцев в ряду.
        alien = Alien(ai_settings, screen)
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

        #Создание первого ряда пришельцев.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)
    #--------------------------------------------------------------------
    def update_bullets(ai_settings, screen, ship, aliens, bullets):
    #Обновляет позиции пуль и удаляет старые пули.
        bullets.update()

        #Удаление исчезнувших пуль.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            game_functions.check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    #--------------------------------------------------------------------    
    def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    #Проверяет, достиг ли флот края экрана, после чего обновляет позиции всех пришельцев во флоте.
        check_fleet_edges(ai_settings, aliens)
        aliens.update()

    #Проверка коллизий "пришелец-корабль".
        if pygame.sprite.spritecollideany(ship, aliens): 
        #spritecollideany() получает два аргумента: спрайт и группу.
        #Метод пытается найти любой элемент группы, вступивший в коллизию со спрайтом, 
        #и останавливает цикл по группе сразу же после обнаружения столкнувшегося элемента.
            game_functions.ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        #Проверка пришельцев, добравшихся до нижнего края экрана.
        game_functions.check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    #--------------------------------------------------------------------
    def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    #Обработка коллизий пуль с пришельцами.
    #Удаление пуль и пришельцев, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

        if len(aliens) == 0:       
            bullets.empty() #Уничтожение существующих пуль и создание нового флота.
        #Уничтожение существующих пуль и создание нового флота.
            game_functions.create_fleet(ai_settings, screen, ship, aliens)
    #--------------------------------------------------------------------
    def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    #Обрабатывает столкновение корабля с пришельцем.   
        if stats.ships_left > 0:
            stats.ships_left -= 1 #Уменьшение ships_left.
        #Очистка списков пришельцев и пуль.
            aliens.empty()
            bullets.empty()        
       
            game_functions.create_fleet(ai_settings, screen, ship, aliens) #Создание нового флота
            ship.center_ship() #и размещение корабля в центре.
   
            sleep(0.5) #Пауза.
        else:
            stats.game_active = False
    #--------------------------------------------------------------------
    def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    #Проверяет, добрались ли пришельцы до нижнего края экрана.
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
            #Происходит то же, что при столкновении с кораблем.
                game_functions.ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
                break
    #--------------------------------------------------------------------
