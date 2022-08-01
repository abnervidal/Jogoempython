import pygame

class Lazer(object):
	def __init__(self):
		self.lazer = pygame.image.load('tiro.png').convert_alpha()
		self.lazer = pygame.transform.scale(self.lazer, (75,38))
		self.vel_lazer = 0
		self.lazer_x = 0
		self.lazer_y = 37

		