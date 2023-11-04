import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self,ai_game):
        """初始化飞船，并设置初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #对于每艘飞船，将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if  self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed   
        
        # Update rect object from self.x.
        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕底端中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)