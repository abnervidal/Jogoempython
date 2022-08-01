import pygame

class Aviao(object):
	def __init__(self):
		self.aviao = pygame.image.load('aviao.png').convert_alpha()
		self.aviao = pygame.transform.scale(self.aviao, (140,90))
		self.aviao_x = 1200
		self.aviao_y = 300
		