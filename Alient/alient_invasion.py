
import sys
import pygame
from settings import *
from ship import *
# import ship
# import game_functions as gf
import game_functions
from pygame.sprite import *
from alien import *
from game_stats import  *

def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    stats = GameStats(ai_settings)
    # 创建用于存储子弹的编组
    bullets = Group()

    # 创建外星人
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)


    #开始游戏循环
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            game_functions.update_bullets(ai_settings, screen, ship, aliens, bullets)
            game_functions.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
      