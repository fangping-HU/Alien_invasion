#coding : utf-8
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,screen,my_setting):
		super().__init__()
		
		self.screen = screen
		self.setting = my_setting
		
		#加载外星人图像
		self.image = pygame.image.load('images/外星人.jpg')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# print(self.rect.x)
		# print(self.rect.y)
		# print(self.rect.width)
		# print(self.rect.height)
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		
	
