import pygame
from config import *
from assets import *
end = 10000
class stick(pygame.sprite.Sprite):
    def __init__(self,img, x, y,nivel):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = (0)
        self.nivel = nivel
        if nivel == 1:
            self.speedx = (1.5)
        elif nivel == 2:
            self.speedx = (3)

    def update(self, x_min, x_max,morto):
        # Atualizando a posição do stick
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.nivel == 1:
            if morto == True:
                self.rect.x = end
                self.speedx = 0
            if self.rect.x >= x_max:
                self.speedx = (-1) 
                self.image = stick_inv           
            if self.rect.x <= x_min:
                self.speedx = (1.5)
                self.image = stick_img
        if self.nivel == 2:
            if morto == True:
                self.rect.x = end
                self.speedx = 0
            if self.rect.x >= x_max:
                self.speedx = (-2.5) 
                self.image = stick_inv           
            if self.rect.x <= x_min:
                self.speedx = (3)
                self.image = stick_img
        if self.nivel == 3:
            if morto == True:
                self.rect.x = end
                self.speedx = 0
            if self.rect.x >= x_max:
                self.speedx = (-2.5) 
                self.image = stick_inv           
            if self.rect.x <= x_min:
                self.speedx = (3)
                self.image = stick_img

class mira2(pygame.sprite.Sprite):
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
class bolinha2(pygame.sprite.Sprite):
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