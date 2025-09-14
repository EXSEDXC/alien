import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((1200,800))
clock=pygame.time.Clock()
class paimeng:
    def __init__(self):
        self.screen=screen
        self.image=pygame.image.load('images/paimeng.jpg')
        self.rect=self.image.get_rect()
        self.rect.center=self.screen.get_rect().center
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
a=paimeng()
def _check_events():
        '''相应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
while True:
    screen.fill((102,204,255))
    a.blitme()
    _check_events()
    pygame.display.flip()
    clock.tick(60)