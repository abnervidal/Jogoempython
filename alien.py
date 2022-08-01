import pygame

class Alien(object):
	def __init__(self):
		self.alien = pygame.image.load('nave.png').convert_alpha()
		self.alien = pygame.transform.scale(self.alien, (100,100))
		self.alien_x = 0
		self.alien_y = 0