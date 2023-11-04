import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_game):
        """初始化外星人，并设置初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings =ai_game.settings
        #self.screen_rect = ai_game.screen.get_rect()
        #self.setting = ai_game.settings

        #加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #self.moving_right = False
        #self.moving_left = False

        #存储外星人的精确水平位置
        self.x = float(self.rect.x)

    #def blitme(self):
        #"""在指定位置绘制飞船"""
        #self.screen.blit(self.image,self.rect)

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.alien_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True