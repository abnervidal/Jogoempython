import pygame

class Respawn(object):
	def respawn_aviao():
		altura = 1350 
		largura = random.randint(1, 480)
	
		return[altura, largura]
	def respawn_lazer():
		atirar_nave = False
		respawn_lazer_x = player.alien_x
		respawn_lazer_y = player.alien_y + 37
		municao.vel_lazer = 0
		return[respawn_lazer_x,respawn_lazer_y, atirar_nave, municao.vel_lazer]