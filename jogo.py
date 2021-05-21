import pygame
import random
import time

pygame.init()

# ----- Gera tela principal
WIDTH = 960
HEIGHT = 540
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stick')
stick_largura = 30
stick_altura = 60
# ----- Inicia assets
background1 = pygame.image.load('pygame/assets/img/fase1.jpg').convert_alpha()
stick_img = pygame.image.load('pygame/assets/img/stick.png').convert_alpha()
stick_img = pygame.transform.scale(stick_img, (stick_largura, stick_altura))
class stick(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (0)
        self.rect.y = (20)
        self.speedx = (3)
        self.speedy = (0)

    def update(self):
        # Atualizando a posição do stick
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x >= (WIDTH - stick_largura):
            self.speedx = (-3)            
        if self.rect.x <= (0):
            self.speedx = (3)

#Criando Sticks
stick1 = stick(stick_img)
#Loop principal
clock = pygame.time.Clock()
FPS = 30
game = True
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                game=False
    stick1.update()
    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background1, (0,0))
    window.blit(stick1.image, stick1.rect)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados