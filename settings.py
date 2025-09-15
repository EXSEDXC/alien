class Settings:
    '''储存游戏中所有设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(233,233,233)
        #飞船设置
        self.ship_limit=0
        #子弹设置
        self.bullet_width=3000
        self.bullet_height=15
        self.bullet_color=(60,50,60)
        self.bullet_allowed=300
        #外星人设置
        self.fleet_drop_speed=10
        
        #加快游戏的节奏
        self.speedup_scale=1.3
        #分数的提高速度
        self.score_scle=2
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed=1.5
        self.bullet_speed=2.5
        self.alien_speed=1.0
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction=1
        #积分设置
        self.alien_points=50
    def increase_speed(self):
        '''提高速度设置和外星人分数的值'''
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scle)
        print(self.alien_points)