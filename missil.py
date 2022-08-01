import pygame

class Missil(object):
	def __init__(self):
		self.missil = pygame.image.load('foguete.png').convert_alpha()
		self.missil = pygame.transform.scale(self.missil, (60,40))
		self.vel_missil = 0
		self.missil_x = 1250
		self.missil_y = 320
