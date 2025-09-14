import pygame
class Ship:
    '''管理飞船的类'''
    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()
        #每艘新飞船放在屏幕底部的中央
        self.rect.midbottom=self.screen_rect.midbottom
        #移动标志
        self.x=float(self.rect.x)
        self.moving_right=False
        self.moving_left=False
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        '''根据移动标志调整飞船位置'''
        #更新飞船的属性x的值而不是外接矩形的属性x的值
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        #根据self.x更新rect对象
        self.rect.x=self.x
        