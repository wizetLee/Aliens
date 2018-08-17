import sys
import pygame
from bullet import Bullet
from alien import *

def check_events(ai_settings, screen, ship, bullets):

    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                fire_bullet(ai_settings, screen, ship, bullets)
            elif event.key == pygame.K_q:
                # 退出的快捷键
                sys.exit()
            else:
                ckeck_event(event, ship, True)

        elif event.type == pygame.KEYUP:
            ckeck_event(event, ship, False)
            


def ckeck_event(event, ship, status):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = status
    elif event.key == pygame.K_LEFT:
        ship.moving_left = status



def fire_bullet(ai_settings, screen, ship, bullets):
    # 按了空格键，创建子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)  
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    # 处理消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom  <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_bullte_alienn_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullte_alienn_collisions(ai_settings, screen, ship, aliens, bullets):
#    响应子弹和外星人的碰撞
#    删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def update_screen(ai_settings, screen, ship, aliens, bullets):

    # 每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹  ----  注意绘制次序
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    # 调用draw() pygame自动编辑编组的每个元素，绘制位置由元素的rect决定
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def get_number_ailens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_aliens(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其放在当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # 创建一群外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_ailens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_aliens(ai_settings, screen, aliens, alien_number, number_row)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for ailen in aliens.sprites():
        ailen.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


    # 判断飞船是否被外星人撞到了
    if pygame.sprite.spritecollide(ship, aliens, True):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

from time import  sleep


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left <= 0:
        stats.game_active = False
    else:
        stats.ships_left -= 1

        # 清空外星人列表和子弹新秀
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)

# 检查是否有外星人到达底部
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            breakpoint()
