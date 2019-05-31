#coding: utf-8


import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
import time


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	my_setting = Settings()
	
	screen = pygame.display.set_mode(
		(my_setting.screen_width,my_setting.screen_height),
		pygame.RESIZABLE)
	pygame.display.set_caption("外星人入侵")
	ship = Ship(my_setting,screen)
	bullets = Group()
	
	aliens = Group()
	
	#开始游戏循环
	while True:
#		start = time.clock()
		#监视键盘和鼠标事件
		gf.check_events(ship,my_setting,screen,bullets)
		ship.update()
		
		# print(ship.rect.centery)
		# print(ship.moving_right)
		gf.update_bullets(bullets)
		gf.create_fleet(screen,my_setting,aliens,ship)
		# screen.fill(my_setting.bg_color)
		# for bullet in bullets.sprites():
			# bullet.draw_bullet()
		# ship.blitme()
		# alien.blitme()	
		#让最近绘制的屏幕可见
#		pygame.display.flip()
#		print(len(bullets))
		gf.screen_update(my_setting,screen,ship,bullets,aliens)
		# end = time.clock()
		# total_time = end - start
		# print(total_time)
		

		

run_game()
