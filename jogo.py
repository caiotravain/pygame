import pygame
import random
import time
from pygame.locals import *

pygame.init()

# ----- Gera tela principal
WIDTH = 960
HEIGHT = 540
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mate o Stick')
stick_largura = 30
stick_altura = 60
mira_largura = 120
mira_altura = 120

# ----- Inicia assets
background = pygame.image.load('pygame/assets/img/fase1.jpg').convert_alpha()
background2 = pygame.image.load('pygame/assets/img/fase2.jpg').convert_alpha()
background2 = pygame.transform.scale(background2, (WIDTH, HEIGHT))
stick_img = pygame.image.load('pygame/assets/img/stick_branco.png').convert_alpha()
mira = pygame.image.load('pygame/assets/img/mira.png').convert_alpha()
stick_img = pygame.transform.scale(stick_img, (stick_largura, stick_altura))
mira_img = pygame.transform.scale(mira, (mira_largura, mira_altura))
stick_inv = pygame.transform.flip(stick_img, True, False)
bolinha = pygame.image.load('pygame/assets/img/bolinha.png').convert_alpha()
bolinha_img = pygame.transform.scale(bolinha, (5, 5))
class stick(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = (1.5)
        self.speedy = (0)

    def update(self, x_min, x_max,a):
        # Atualizando a posição do stick
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if a ==2 :
            self.rect.x = 10000
            self.speedx = 0
        if self.rect.x >= x_max:
            self.speedx = (-1) 
            self.image = stick_inv           
        if self.rect.x <= x_min:
            self.speedx = (1.5)
            self.image = stick_img
        # Armazena a animação de explosão
class mira(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self,x,y):
        # Atualizando a posição do stick
        self.rect.x = x
        self.rect.y = y
class bolinha(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self,x,y):
        # Atualizando a posição do stick
        self.rect.x = x
        self.rect.y = y

#Criando Sticks
stick1 = stick(stick_img, 200, 215)
stick2 = stick(stick_img, 0, 128)
stick3 = stick(stick_img,850,160)
stick4 = stick(stick_img,850,160)
stick5 = stick(stick_img,850,160)
stick6 =stick(stick_img,850,160)
mira1 = mira(mira_img,0,0)
bolinha1 = bolinha(bolinha_img,0,0)
all_sticks = pygame.sprite.Group()
groups = {}
groups['all_sticks'] = all_sticks
#Loop principal
clock = pygame.time.Clock()
FPS = 30
game = True
abatido =0
while game:
    clock.tick(FPS)
    # mx, my = pygame.mouse.get_pos()
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                game=False
        pygame.mouse.set_visible(False)
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit_stick_1 =pygame.sprite.collide_rect(bolinha1, stick1)
            if hit_stick_1 == 1:
                stick1.update(0,0,2)
                abatido += 1
            hit_stick_2 =pygame.sprite.collide_rect(bolinha1, stick2)
            if hit_stick_2 == 1:
                stick2.update(0,0,2)
                abatido +=1
            hit_stick_3 =pygame.sprite.collide_rect(bolinha1, stick3)
            if hit_stick_3 == 1:
                abatido +=1
                stick3.update(0,0,2)

        
        
    mousePos = pygame.mouse.get_pos()
    mouse_x_b = pygame.mouse.get_pos()[0]-2.5
    mouse_y_b= pygame.mouse.get_pos()[1]-2.5
    mira_X = pygame.mouse.get_pos()[0] -60
    mira_Y = pygame.mouse.get_pos()[1] - 60
    stick1.update(150, 450,3)
    stick2.update(0, 110,3)
    stick3.update(850,960 - stick_largura,3)
    mira1.update(mira_X,mira_Y)
    bolinha1.update(mouse_x_b,mouse_y_b)
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background, (0,0))
    window.blit(stick1.image, stick1.rect)
    window.blit(stick2.image, stick2.rect)
    window.blit(stick3.image,stick3.rect)
    window.blit(mira_img, (mira_X, mira_Y))
    window.blit(bolinha_img, (mouse_x_b, mouse_y_b))
    if abatido ==3:
        background = background2
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados