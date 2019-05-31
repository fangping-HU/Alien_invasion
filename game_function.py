#coding: utf-8

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keyDown(event,ship,my_setting,screen,bullets):
	if event.key == pygame.K_RIGHT:
		# ship.rect.centerx += 10
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key ==pygame.K_UP:
		ship.moving_up = True
	elif event.key ==pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(screen,ship,my_setting,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

		
def check_keyUP(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key ==pygame.K_UP:
		ship.moving_up = False
	elif event.key ==pygame.K_DOWN:
		ship.moving_down = False			

def check_events(ship,my_setting,screen,bullets):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keyDown(event,ship,my_setting,screen,bullets)
				

			elif event.type == pygame.KEYUP:
				check_keyUP(event,ship)

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<0:
			bullets.remove(bullet)			


def fire_bullets(screen,ship,my_setting,bullets):
	if len(bullets)< my_setting.bullets_allowed:
			new_bullet = Bullet(screen,ship,my_setting)
			bullets.add(new_bullet)				


		
		
#重构create_fleet
def get_number_aliens_x(my_setting,alien_width):
	"""计算一行能容纳多少个外星人"""
	available_space_x = my_setting.screen_width - 2*alien_width
	alien_number_x = int(available_space_x / (2*alien_width))
	return alien_number_x
	
def get_number_rows(my_setting,ship_height,alien_height):
	available_space_y =( my_setting.screen_height -3*alien_height
						-ship_height)
	alien_rows = int(available_space_y / (2*alien_height))
	return alien_rows

def create_alien(screen,my_setting,aliens,alien_number,alien_row):
	#创建第一个外星人
	"""外星人间距为外星人宽度"""
	alien = Alien(screen,my_setting)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*alien_row
	aliens.add(alien)	
	
def create_fleet(screen,my_setting,aliens,ship):
	alien = Alien(screen,my_setting)
	aliens_number = get_number_aliens_x(my_setting,alien.rect.width)
	alien_rows = get_number_rows(my_setting,ship.rect.height
				,alien.rect.height)
	# 将alien添加到aliens
	for alien_row in range(alien_rows):
		for alien_number in range(aliens_number):
			#创建第一个外星人并设置其x坐标
			#print(alien_number)
			create_alien(screen,my_setting,aliens,alien_number,alien_row)

	
def screen_update(my_setting,screen,ship,bullets,aliens):
	screen.fill(my_setting.bg_color)
	for alien in aliens:
		alien.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#让最近绘制的屏幕可见
	pygame.display.flip()

	

		
