#coding: utf-8

class Settings():
	"""存储外星人所有设置的类"""
	def __init__(self,width=1368,height=670):
		#屏幕对象设置
		self.screen_width = width
		self.screen_height = height
		self.bg_color = (230,230,230)
		#飞船速度设置
		self.speed = 10
		#子弹属性设置
		self.bullet_color = (255,48,200)
		self.bullet_width = 2
		self.bullet_height = 10
		self.bullet_speed = 50
		self.bullets_allowed = 3
		
		
