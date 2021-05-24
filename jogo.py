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
ganhou = pygame.image.load('pygame/assets/img/ganhou.png').convert_alpha()
ganhou = pygame.transform.scale(ganhou, (WIDTH, HEIGHT))
stick_img = pygame.image.load('pygame/assets/img/stick_branco.png').convert_alpha()
mira = pygame.image.load('pygame/assets/img/mira.png').convert_alpha()
stick_img = pygame.transform.scale(stick_img, (stick_largura, stick_altura))
mira_img = pygame.transform.scale(mira, (mira_largura, mira_altura))
stick_inv = pygame.transform.flip(stick_img, True, False)
bolinha = pygame.image.load('pygame/assets/img/bolinha.png').convert_alpha()
bolinha_img = pygame.transform.scale(bolinha, (5, 5))
class stick(pygame.sprite.Sprite):
    def __init__(self,img, x, y,nivel):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = (0)
        if nivel == 1:
            self.speedx = (1.5)
        elif nivel == 2:
            self.speedx = (3)

    def update(self, x_min, x_max,a):
        # Atualizando a posição do stick
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if nivel == 1:
            if a == 2:
                self.rect.x = 10000
                self.speedx = 0
            if self.rect.x >= x_max:
                self.speedx = (-1) 
                self.image = stick_inv           
            if self.rect.x <= x_min:
                self.speedx = (1.5)
                self.image = stick_img
        if nivel == 2:
            if a == 2:
                self.rect.x = 10000
                self.speedx = 0
            if self.rect.x >= x_max:
                self.speedx = (-2.5) 
                self.image = stick_inv           
            if self.rect.x <= x_min:
                self.speedx = (3)
                self.image = stick_img

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
stick1 = stick(stick_img, 200, 215,1)
stick2 = stick(stick_img, 0, 128,1)
stick3 = stick(stick_img,850,160,1)
stick4 = stick(stick_img,280,43,2)
stick5 = stick(stick_img,540,246,2)
stick6 =stick(stick_img,740,130,2)
stick7 =stick(stick_img,100,282,2)
stick8 =stick(stick_img,360,192,2)
mira1 = mira(mira_img,0,0)
bolinha1 = bolinha(bolinha_img,0,0)
all_sticks = pygame.sprite.Group()
groups = {}
groups['all_sticks'] = all_sticks
lista_stick = [stick1,stick2,stick3,stick4,stick5,stick6,stick7,stick8]
#Loop principal
clock = pygame.time.Clock()
FPS = 30
game = True
abatido = 0
nivel = 1
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
            for a in lista_stick:
                hit = pygame.sprite.collide_rect(bolinha1,a)
                if hit == 1:
                    a.update(0,0,2)
                    abatido += 1
    if abatido ==3:
        nivel = 2    
    mousePos = pygame.mouse.get_pos()
    mouse_x_b = pygame.mouse.get_pos()[0]-2.5
    mouse_y_b= pygame.mouse.get_pos()[1]-2.5
    mira_X = pygame.mouse.get_pos()[0] -60
    mira_Y = pygame.mouse.get_pos()[1] - 60
    if nivel ==1:
        stick1.update(150, 450,3)
        stick2.update(0, 110,3)
        stick3.update(850,960 - stick_largura,3)
    if nivel==2:
        stick4.update(170,280,3)
        stick5.update(445,560,3)
        stick6.update(675,795,3)
        stick7.update(75,150,3)
        stick8.update(310,360,3)
    mira1.update(mira_X,mira_Y)
    bolinha1.update(mouse_x_b,mouse_y_b)
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0,0))
    if nivel == 1:
        window.blit(stick1.image, stick1.rect)
        window.blit(stick2.image, stick2.rect)
        window.blit(stick3.image,stick3.rect)
    window.blit(mira_img, (mira_X, mira_Y))
    window.blit(bolinha_img, (mouse_x_b, mouse_y_b))
    if nivel == 2:
        background = background2
        window.blit(stick4.image, stick4.rect)
        window.blit(stick5.image, stick5.rect)
        window.blit(stick6.image,stick6.rect)
        window.blit(stick7.image, stick7.rect)
        window.blit(stick8.image, stick8.rect)
        

    if abatido == 8:
        background = ganhou
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados