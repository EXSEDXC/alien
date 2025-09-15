import json
import os
class GameStats:
    '''跟踪游戏的统计信息'''
    def __init__(self,ai_game):
        '''初始化统计信息'''
        
        self.settings=ai_game.settings
        self.reset_stats()
        self._load_high_score()
    def reset_stats(self):
        '''初始化游戏运行期间可能变化的统计信息'''
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1
    def _load_high_score(self):
        '''从文件加载最高分'''
        filename = 'high_score.json'
        try:
            # 检查文件是否存在
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    self.high_score = json.load(f)
            else:
                self.high_score = 0
        except:
            # 如果文件损坏或读取失败，重置最高分
            self.high_score = 0
    
    def save_high_score(self):
        '''保存最高分到文件'''
        filename = 'high_score.json'
        try:
            with open(filename, 'w') as f:
                json.dump(self.high_score, f)
        except:
            # 保存失败时忽略错误
            pass