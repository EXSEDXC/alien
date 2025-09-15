from settings import Settings
from time import sleep

import pygame
import sys 
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        #创建一个用于储存游戏统计信息的实例并创建记分牌
        
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        self.game_active=False
        #创建play按钮
        self.play_button=Button(self,'Play')
        
    def run_game(self):
        '''开始游戏的主循环'''
        while 1:
            self._check_events()
            if self.game_active:
                self.ship.update()
                #删除已经消失的子弹
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(240)
    def _check_events(self):
        '''相应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_play_button(self,mouse_pos):
        '''在玩家单击play按钮时开始新游戏'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #重置游戏信息
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.game_active=True
            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            #创建一个新的外星舰队，把飞船放在屏幕底部中央
            self._create_fleet()
            self.ship.center_ship()
            #隐藏光标
            pygame.mouse.set_visible(False)
    def _check_keydown_events(self,event):
        '''响应按下'''
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        '''响应释放'''
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
    def _fire_bullet(self):
        '''创建一颗子弹，将其填入编组bullets'''
        if len(self.bullets)<self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        '''更新子弹的位置并删除已经消失的子弹'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        #检查是否有子弹击中了外星人
        #如果有，删除相应的子弹和外星人
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        '''响应子弹和外星人的碰撞'''
        #删除发生碰撞的子弹和外星人
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score+=self.settings.alien_points*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            #删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    def _update_aliens(self):
        '''更新外星舰队中所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()
        #检查外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        #检查是否有外星人到达屏幕下边缘
        self._check_aliens_bottom()
    def _ship_hit(self):
        '''响应飞船和外星人的碰撞'''
        if self.stats.ships_left>0:
        #将ships_left减1
            self.stats.ships_left-=1
            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            #创建一个新的外星舰队，并将飞船放在屏幕底部中央
            self._create_fleet()
            self.ship.center_ship()
            #暂停
            sleep(0.5)
        else:
            self.game_active=False
            pygame.mouse.set_visible(True)
    def _check_aliens_bottom(self):
        '''检查是否有外星人到达了屏幕的下边缘'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.settings.screen_height:
                #像飞船被撞到一样
                self._ship_hit()
                break
    def _create_fleet(self):
        '''创建外形舰队'''
        #创建外星人,再不断添加，直到没有空间
        #外星人的间距为外星人的宽度和外星人的高度
        
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y<(self.settings.screen_height-4*alien_height):
            while current_x<(self.settings.screen_width-1*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            #添加一行外星人后重置x值，递增y值
            current_x=alien_width
            current_y+=2*alien_height
    def _create_alien(self,x_position,y_position):
        '''创建一个外星人并加入外星舰队'''
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
    def _check_fleet_edges(self):
        '''有外星人触边时采取相应措施'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        '''将整个外星舰队向下移动，并改变它们的方向'''
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1
    def _update_screen(self):
        '''更新屏幕图像并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #显示得分
        self.sb.show_score()
        #如果游戏处于非活动状态就绘制play按钮
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
if __name__=='__main__':
    #创建游戏事例并运行游戏
    ai=AlienInvasion()
    ai.run_game()