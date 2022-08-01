import pygame
class Colisao(object):

	def colisao():
		global pontos
		if alien_rect.colliderect(aviao_rect) or aviao_rect.x == 80:
			pontos -= 0
			return True
		elif lazer_rect.colliderect(aviao_rect):
			pontos += 5
			return True
		else:
			return False
	def colisao_missil():
		global vida
		if alien_rect.colliderect(aviao_rect) or aviao_rect.x == 80:
			vida -= 1
			return True
		elif missil_rect.colliderect(alien_rect):
			vida -= 1
			return True
		else:
			return False 