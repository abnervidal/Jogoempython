import pygame
import random
from alien import Alien
from aviao import Aviao
from lazer import Lazer
from missil import Missil

pygame.init()

largura = 1200
altura = 600
primeira_tela = True
tela_aberta = True
ultima_tela = True
fimdojogo = True
atirar_nave = False
ranking = True
disparo01 = True
disparo02 = True
disparo03 = True



tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('A fuga do ET')

#carregar imagem de fundo
imagem = pygame.image.load('fundo.jpg').convert_alpha()
imagem = pygame.transform.scale(imagem,(largura,altura))

player = Alien()
player.alien

inimigo = Aviao()
inimigo.aviao

inimigo02 = Aviao()
inimigo02.aviao

inimigo03 = Aviao()
inimigo03.aviao

municao = Lazer()
municao.lazer

municao02 = Lazer()
municao02.lazer

municao03 = Lazer()
municao03.lazer

bala = Missil()
bala.missil

bala02 = Missil()
bala02.missil

bala03 = Missil()
bala03.missil

pontos = 0
vida = 3
pontuacao = int(0)
top01 = int()
top02 = int()
top03 = int()
top04 = int()
top05 = int()


fonte = pygame.font.SysFont('rainyhearts.ttf', 25)
fonte01 = pygame.font.SysFont('rainyhearts.ttf', 75)

alien_rect = player.alien.get_rect()
aviao_rect = inimigo.aviao.get_rect()
aviao02_rect = inimigo02.aviao.get_rect()
aviao03_rect = inimigo03.aviao.get_rect()
lazer_rect = municao.lazer.get_rect()
lazer02_rect = municao02.lazer.get_rect()
lazer03_rect = municao03.lazer.get_rect()
missil_rect = bala.missil.get_rect()
missil02_rect = bala02.missil.get_rect()
missil03_rect = bala03.missil.get_rect()

def respawn_aviao():
		altura = 1350 
		largura = random.randint(1, 480)
	
		return[altura, largura]
def respawn_lazer():
	atirar_nave = False
	respawn_lazer_x = player.alien_x
	respawn_lazer_y = player.alien_y + 37
	municao.vel_lazer = 0
	disparo01 = True
	return[respawn_lazer_x,respawn_lazer_y, atirar_nave, municao.vel_lazer, disparo01]
def respawn_lazer02():
	atirar_nave = False
	respawn_lazer02_x = player.alien_x
	respawn_lazer02_y = player.alien_y + 37
	municao02.vel_lazer = 0
	disparo02 = True
	return[respawn_lazer02_x,respawn_lazer02_y, atirar_nave, municao02.vel_lazer, disparo02]
def respawn_lazer03():
	atirar_nave = False
	respawn_lazer03_x = player.alien_x
	respawn_lazer03_y = player.alien_y + 37
	municao03.vel_lazer = 0
	disparo03 = True
	return[respawn_lazer03_x,respawn_lazer03_y, atirar_nave, municao03.vel_lazer, municao03]
def colisao():
	global pontos
	if alien_rect.colliderect(aviao_rect) or aviao_rect.x <= 0:
		pontos -= 0
		return True
	elif lazer_rect.colliderect(aviao_rect):
		pontos += 5
		return True
	elif lazer02_rect.colliderect(aviao_rect):
		pontos += 5
		return True
	elif lazer03_rect.colliderect(aviao_rect):
		pontos += 5
		return True
	else:
		return False
def colisao02():
	global pontos
	if alien_rect.colliderect(aviao02_rect) or aviao02_rect.x <= 0:
		pontos -= 0
		return True
	elif lazer_rect.colliderect(aviao02_rect):
		pontos += 5
		return True
	else:
		return False
def colisao03():
	global pontos
	if alien_rect.colliderect(aviao03_rect) or aviao03_rect.x <= 0:
		pontos -= 0
		return True
	elif lazer_rect.colliderect(aviao03_rect):
		pontos += 5
		return True
	else:
		return False

def colisao_missil():
	global vida
	if alien_rect.colliderect(aviao_rect) or aviao_rect.x <= 0:
		vida -= 1
		return True
	elif alien_rect.colliderect(aviao02_rect) or aviao02_rect.x <= 0:
		vida -= 1
		return True

	elif alien_rect.colliderect(aviao03_rect) or aviao03_rect.x <= 0:
		vida -= 1
		return True

	elif missil_rect.colliderect(alien_rect):
		vida -= 1
		return True
	elif missil02_rect.colliderect(alien_rect):
		vida -= 1
		return True
	elif missil03_rect.colliderect(alien_rect):
		vida -= 1
		return True
	else:
		return False

while tela_aberta:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			tela_aberta = False	 

	tela.blit(imagem, (0,0))

	repit_x = largura % imagem.get_rect().width
	tela.blit(imagem, (repit_x - imagem.get_rect().width, 0))
	if repit_x < 1200:
		tela.blit(imagem, (repit_x, 0))
	

	if ranking == False:
		sair = fonte.render('Precione ESC para voltar.' ,True,(0,0,0))
		primeiro_lugar = fonte01.render(f'Primeiro: {int(top01)}', True,(0,0,0))
		segundo_lugar = fonte01.render(f'Segundo: {top02}', True,(0,0,0))
		terceiro_lugar = fonte01.render(f'Terceiro: {top03}', True,(0,0,0))
		quarto_lugar = fonte01.render(f'Quarto: {top04}', True,(0,0,0))
		quinto_lugar = fonte01.render(f'Quinto: {top05}', True,(0,0,0))
		tela.blit(sair,(10,25))
		tela.blit(primeiro_lugar,(200,150))
		tela.blit(segundo_lugar,(200,200))
		tela.blit(terceiro_lugar,(200,250))
		tela.blit(quarto_lugar,(200,300))
		tela.blit(quinto_lugar,(200,350))
	if primeira_tela == True:
		pontos = 0
		vida = 3
		play = fonte01.render('Precione ESPAÇO para começar!',True,(255,255,255))
		tela.blit(play, (200,250))
		rank = fonte.render('Precione R para ver o ranking!',True,(255,255,255))
		tela.blit(rank, (450,330))
	if fimdojogo == False:
		perdeu = fonte01.render('PERDEU!',True,(255,255,255))
		tela.blit(perdeu, (440,250))
		perdeu = fonte01.render('Precione ESC para voltar ao início',True,(255,255,255))
		tela.blit(perdeu, (150,300))
	tecla = pygame.key.get_pressed()
	if tecla[pygame.K_ESCAPE] and ranking == False:
		primeira_tela = True
		ranking = True
	if tecla[pygame.K_r] and primeira_tela == True:
		primeira_tela = False
		ranking = False
	if tecla[pygame.K_ESCAPE] and fimdojogo == False:
		fimdojogo = True
		primeira_tela = True
	if tecla[pygame.K_SPACE] and primeira_tela == True:
		primeira_tela = False
		ultima_tela = False
	if ultima_tela == False:
		#movimento
		largura -= 1
		inimigo.aviao_x -= 1.5
		bala.missil_x -= 1.5
		
		tela.blit(municao03.lazer,(municao03.lazer_x, municao03.lazer_y))
		tela.blit(municao02.lazer,(municao02.lazer_x, municao02.lazer_y))
		tela.blit(municao.lazer,(municao.lazer_x, municao.lazer_y))
		tela.blit(player.alien,(player.alien_x, player.alien_y))
		tela.blit(bala.missil,(bala.missil_x, bala.missil_y))
		tela.blit(inimigo.aviao,(inimigo.aviao_x, inimigo.aviao_y))
	
		
		municao.lazer_x += municao.vel_lazer
		municao02.lazer_x += municao02.vel_lazer
		municao03.lazer_x += municao03.vel_lazer

		bala.missil_x -= bala.vel_missil
		bala02.missil_x -= bala02.vel_missil
		bala03.missil_x -= bala03.vel_missil

		alien_rect.x = player.alien_x
		alien_rect.y = player.alien_y

		aviao_rect.x = inimigo.aviao_x
		aviao_rect.y = inimigo.aviao_y

		aviao02_rect.x = inimigo02.aviao_x
		aviao02_rect.y = inimigo02.aviao_y

		aviao03_rect.x = inimigo03.aviao_x
		aviao03_rect.y = inimigo03.aviao_y

		lazer_rect.x = municao.lazer_x
		lazer_rect.y = municao.lazer_y

		lazer02_rect.x = municao02.lazer_x
		lazer02_rect.y = municao02.lazer_y

		lazer03_rect.x = municao03.lazer_x
		lazer03_rect.y = municao03.lazer_y

		missil_rect.x = bala.missil_x
		missil_rect.y = bala.missil_y

		missil02_rect.x = bala02.missil_x
		missil02_rect.y = bala02.missil_y

		missil03_rect.x = bala03.missil_x
		missil03_rect.y = bala03.missil_y

		comando = pygame.key.get_pressed()
		if comando[pygame.K_UP] and player.alien_y > 0:
			player.alien_y -= 2
			municao02.lazer_y -= 2
			municao03.lazer_y -= 2
			if not atirar_nave:
				municao.lazer_y -= 2
			
		if comando[pygame.K_DOWN] and player.alien_y < 480:
			player.alien_y += 2
			municao02.lazer_y +=2
			municao03.lazer_y += 2
			if not atirar_nave:
				municao.lazer_y += 2
			
		if comando[pygame.K_SPACE]:
			atirar_nave = True
			municao.vel_lazer = 5
			disparo01 = False
		if comando[pygame.K_SPACE] and disparo01 == False:
			atirar_nave = True
			municao02.vel_lazer = 5
			disparo02 = False
		if comando[pygame.K_SPACE] and disparo01 == False and disparo02 == False:
			atirar_nave = True
			municao03.vel_lazer = 5
			disparo03 = False


		if vida == 0:
			fimdojogo = False

		if colisao_missil():
			bala.missil_x = 100000
			bala.missil_y = 100000

			bala02.missil_x = 100000
			bala02.missil_y = 100000

			bala03.missil_x = 100000
			bala03.missil_y = 100000
		if inimigo.aviao_x == 0 or colisao():
			inimigo.aviao_x = respawn_aviao()[0]
			inimigo.aviao_y = respawn_aviao()[1] 
			bala.missil_x = inimigo.aviao_x + 50
			bala.missil_y = inimigo.aviao_y + 20
		if inimigo02.aviao_x == 0 or colisao02():
			inimigo02.aviao_x = respawn_aviao()[0]
			inimigo02.aviao_y = respawn_aviao()[1] 
			bala02.missil_x = inimigo02.aviao_x + 50
			bala02.missil_y = inimigo02.aviao_y + 20
		if inimigo03.aviao_x == 0 or colisao03():
			inimigo03.aviao_x = respawn_aviao()[0]
			inimigo03.aviao_y = respawn_aviao()[1] 
			bala03.missil_x = inimigo03.aviao_x + 50
			bala03.missil_y = inimigo03.aviao_y + 20
		if inimigo.aviao_x >= 750:
			bala.vel_missil = 3.5
			bala02.vel_missil = 3.5
			bala03.vel_missil = 3.5
		
		if municao.lazer_x == 1200 or colisao() or colisao02() or colisao03():
			municao.lazer_x, municao.lazer_y, atirar_nave, municao.vel_lazer, disparo01 = respawn_lazer()
			municao.lazer02_x, municao.lazer02_y, atirar_nave, municao02.vel_lazer, disparo02 = respawn_lazer02()
			municao.lazer03_x, municao.lazer03_y, atirar_nave, municao03.vel_lazer,disparo03 = respawn_lazer03()

		if pontos >= 50:
			tela.blit(bala02.missil,(bala02.missil_x, bala02.missil_y))
			tela.blit(inimigo02.aviao,(inimigo02.aviao_x, inimigo02.aviao_y))
			inimigo02.aviao_x -= 1.5
			bala02.missil_x -= 1.5
		if pontos >= 250:
			tela.blit(bala03.missil,(bala03.missil_x, bala03.missil_y))
			tela.blit(inimigo03.aviao,(inimigo03.aviao_x, inimigo03.aviao_y))
			inimigo03.aviao_x -= 1.5
			bala03.missil_x -= 1.5	
		if fimdojogo == False:
			ultima_tela = True
			pontuacao += pontos
			vida = 3
		if pontuacao > 0 and fimdojogo == False:
			if pontuacao > top01:
				top05 = top04
				top04 = top03
				top03 = top02
				top02 = top01
				top01 = pontuacao
				pontuacao = 0
			elif pontuacao > top02:
				top05 = top04
				top04 = top03
				top03 = top02
				top02 = pontuacao
				pontuacao = 0
			elif pontuacao > top03:
				top05 = top04
				top04 = top03
				top03 = pontuacao
				pontuacao = 0
			elif pontuacao > top04:
				top05 = top04
				top04 = pontuacao
				pontuacao = 0
			elif pontuacao > top05:
				top05 = pontuacao
				pontuacao = 0
			else:
				pontos = 0

		
				
	#Carregar Fonte
	score = fonte.render(f'PONTOS: {int(pontos)}',True,(0,0,0))
	life = fonte.render(f'VIDAS: {int(vida)}', True, (0,0,0))
	tela.blit(life, (1050,550))
	tela.blit(score, (50,550))
	print(pontos)
	print(vida)
	pygame.display.update()
