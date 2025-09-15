import pygame.font
class Scoreboard:
    '''显示得分信息的类'''
    def __init__(self,ai_game):
        '''初始化显示得分涉及的属性'''
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats
        #显示得分信息时使用的字体设置S
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #准备初始得分和最高分图像
        self.prep_score()
        self.prep_high_score()
    def prep_score(self):
        '''将得分渲染为图像'''
        rounded_score=round(self.stats.score,-1)
        score_str=f'{rounded_score:,}'
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        #在屏幕右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
    def prep_high_score(self):
        '''将最高分渲染为图像'''
        high_score=round(self.stats.high_score,-1)
        high_score_str=f'{high_score:,}'
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        #将最高分放在屏幕顶部的中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
    def check_high_score(self):
        '''检查是否诞生了新的最高分'''
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_high_score()
            