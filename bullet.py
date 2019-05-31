#conding utf-8

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen,ship,my_setting):
		super().__init__()
		"""在飞船的位置创建一个子弹对象"""
		self.screen = screen
		"""在（0，0）坐标处创建子弹对象，再将其移至合适位置"""
		self.rect = pygame.Rect(0,0,my_setting.bullet_width,
			my_setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		"""存储小数子弹纵坐标"""
		self.y = float(self.rect.y)
		
		self.speed = my_setting.bullet_speed
		self.color = my_setting.bullet_color
		
	def update(self):
		"""更新子弹位置"""
		self.y -= self.speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""在屏幕上绘制rect对象"""
		pygame.draw.rect(self.screen,self.color,self.rect)
