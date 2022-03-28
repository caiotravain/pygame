from os import path
import pygame
import os
from config import *

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Call of Stick')
# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sounds')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fontes')

#IMAGES


#LOAD
controle = pygame.image.load(os.path.join(IMG_DIR, 'controles.png')).convert_alpha()
inicial = pygame.image.load((os.path.join(IMG_DIR, 'tela_inicial.jpg'))).convert_alpha()
background1 = pygame.image.load((os.path.join(IMG_DIR, 'fase1.jpg'))).convert_alpha()
background2 = pygame.image.load(os.path.join(IMG_DIR, 'fase2.jpg')).convert_alpha()
background3 = pygame.image.load((os.path.join(IMG_DIR, 'fase3.jpg'))).convert_alpha()
Sobre = pygame.image.load((os.path.join(IMG_DIR, 'sobreposicao.png'))).convert_alpha()
score = pygame.image.load((os.path.join(IMG_DIR, 'score.png'))).convert_alpha()
j1 = pygame.image.load((os.path.join(IMG_DIR, 'janela1.png'))).convert_alpha()
j2 = pygame.image.load((os.path.join(IMG_DIR, 'janela2.png'))).convert_alpha()
j3 = pygame.image.load((os.path.join(IMG_DIR, 'janela3.png'))).convert_alpha()
j4 = pygame.image.load(os.path.join(IMG_DIR, 'janela4.png')).convert_alpha()
j5 = pygame.image.load (os.path.join(IMG_DIR, 'janela5.png')).convert_alpha()
j6 = pygame.image.load((os.path.join(IMG_DIR, 'janela6.png'))).convert_alpha()
j7 = pygame.image.load((os.path.join(IMG_DIR, 'janela7.png'))).convert_alpha()
j8 = pygame.image.load((os.path.join(IMG_DIR, 'janela8.png'))).convert_alpha()
j9 = pygame.image.load((os.path.join(IMG_DIR, 'janela9.png'))).convert_alpha()
perdeu = pygame.image.load((os.path.join(IMG_DIR, 'perdeu.png'))).convert_alpha()
ganhou = pygame.image.load((os.path.join(IMG_DIR, 'ganhou.png'))).convert_alpha()
stick_img = pygame.image.load((os.path.join(IMG_DIR, 'stick_branco.png'))).convert_alpha()
mira = pygame.image.load((os.path.join(IMG_DIR, 'mira.png'))).convert_alpha()
bolinha = pygame.image.load((os.path.join(IMG_DIR, 'bolinha.png'))).convert_alpha()
bala_img = pygame.image.load((os.path.join(IMG_DIR, 'Balas.png'))).convert_alpha()
sniper_img = pygame.image.load((os.path.join(IMG_DIR, 'sniper(balista).png'))).convert_alpha()


#SCALES
controle = pygame.transform.scale(controle, (WIDTH, HEIGHT))
inicial = pygame.transform.scale(inicial, (WIDTH, HEIGHT))
background2 = pygame.transform.scale(background2, (WIDTH, HEIGHT))
background3 = pygame.transform.scale(background3, (WIDTH, HEIGHT))
sobre = pygame.transform.scale(Sobre, (385, 430))
score = pygame.transform.scale(score, (150,60))
times = pygame.transform.scale(score, (120,30))
j1 = pygame.transform.scale(j1, (65, 60))
j2 = pygame.transform.scale(j2, (65, 60))
j3 = pygame.transform.scale(j3, (27, 60))
j4 = pygame.transform.scale(j4, (65, 60))
j5 = pygame.transform.scale(j5, (29, 50))
j6 = pygame.transform.scale(j6, (65, 60))
j7 = pygame.transform.scale(j7, (65, 60))
j8 = pygame.transform.scale(j8, (27, 60))
j9 = pygame.transform.scale(j9, (65, 65))
perdeu = pygame.transform.scale(perdeu, (WIDTH, HEIGHT))
ganhou = pygame.transform.scale(ganhou, (WIDTH + 40, HEIGHT))
stick_img = pygame.transform.scale(stick_img, (stick_largura, stick_altura))
mira_img = pygame.transform.scale(mira, (mira_largura, mira_altura))
stick_inv = pygame.transform.flip(stick_img, True, False)
bolinha_img = pygame.transform.scale(bolinha, (10, 10))
bala_img = pygame.transform.scale(bala_img, (150,100 ))
sniper_img = pygame.transform.scale(sniper_img, (300, 211))

#FONTES
fonte = pygame.font.Font(os.path.join(FNT_DIR, '8-bit.ttf'), 40)
fonte2 = pygame.font.Font(os.path.join(FNT_DIR, '8-bit.ttf'), 20)
fonte3 = pygame.font.Font(os.path.join(FNT_DIR, '8-bit.ttf'), 30)
font_sys = pygame.font.SysFont(None, 30)
font_sys2 = pygame.font.SysFont(None, 50)
texto = fonte2.render('Press Any Button to Start', True, (255, 255, 255))
texto3 = fonte2.render('Score', True, (255, 255, 255))
texto4 = fonte2.render('Time', True, (255, 255, 255))

#Sons
tiro_som = pygame.mixer.Sound((os.path.join(SND_DIR, 'tiro.mp3')))
perder_som = pygame.mixer.Sound((os.path.join(SND_DIR, 'derrota.mp3')))
pygame.mixer.Sound.set_volume(perder_som,0.3)
inicial_som = pygame.mixer.Sound((os.path.join(SND_DIR, 'start.mp3')))
pygame.mixer.Sound.set_volume(inicial_som,0.3)
ganhou_som = pygame.mixer.Sound(os.path.join(SND_DIR, 'vitoria.mp3'))
pygame.mixer.Sound.set_volume(ganhou_som,0.3)
jogo_som = pygame.mixer.Sound((os.path.join(SND_DIR, 'game.mp3')))
pygame.mixer.Sound.set_volume(jogo_som,0.1)
