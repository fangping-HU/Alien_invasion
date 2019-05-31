#coding: utf-8

import pygame

class Ship():
	def __init__(self,my_setting,screen):
		
		self.screen = screen
		self.my_setting = my_setting
		#加载飞船图像及外界矩形
		self.image = pygame.image.load('images/fighter.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将飞船放置在外接矩形底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#让飞船能存储小数像素,rect.centerx只能存储整数
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		# self.level = {'slow':0.5,'middle':1,'fast':1.5}
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	
	def update(self):
		if self.moving_right and self.rect.right <self.screen_rect.right:
			self.centerx += self.my_setting.speed
		if self.moving_left and self.rect.left >self.screen_rect.left:
			self.centerx -= self.my_setting.speed
		if self.moving_up and self.rect.top >self.screen_rect.top:
			self.centery -= self.my_setting.speed
		if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
			self.centery += self.my_setting.speed
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		

