import pygame
import random
import time
from pygame.locals import *

pygame.init()

# ----- Gera tela principal
WIDTH = 960
HEIGHT = 540
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stick')
stick_largura = 30
stick_altura = 60
mira_largura = 200
mira_altura = 200

# ----- Inicia assets
background1 = pygame.image.load('pygame/assets/img/fase1.jpg').convert_alpha()
stick_img = pygame.image.load('pygame/assets/img/stick_branco.png').convert_alpha()
mira = pygame.image.load('pygame/assets/img/mira.png').convert_alpha()
stick_img = pygame.transform.scale(stick_img, (stick_largura, stick_altura))
mira_img = pygame.transform.scale(mira, (mira_largura, mira_altura))
stick_inv = pygame.transform.flip(stick_img, True, False)

class stick(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = (1.5)
        self.speedy = (0)

    def update(self, x_min, x_max):
        # Atualizando a posição do stick
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x >= x_max:
            self.speedx = (-1) 
            self.image = stick_inv           
        if self.rect.x <= x_min:
            self.speedx = (1.5)
            self.image = stick_img

#Criando Sticks
stick1 = stick(stick_img, 200, 215)
stick2 = stick(stick_img, 0, 128)
stick3 = stick(stick_img,850,160)

#Loop principal
clock = pygame.time.Clock()
FPS = 30
game = True

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

    
    stick1.update(150, 450)
    stick2.update(0, 110)
    stick3.update(850,960 - stick_largura)
    
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background1, (0,0))
    window.blit(stick1.image, stick1.rect)
    window.blit(stick2.image, stick2.rect)
    window.blit(stick3.image,stick3.rect)

    mousePos = pygame.mouse.get_pos()
    mira_X = pygame.mouse.get_pos()[0] - 50
    mira_Y = pygame.mouse.get_pos()[1] - 50
    mira_jogo = window.blit(mira_img, (mira_X, mira_Y))

    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados



# self.rect.x = (200)
# self.rect.y = (215)