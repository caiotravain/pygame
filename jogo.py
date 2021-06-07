from os import times
import pygame
import time
from pygame.locals import *
from assets import *
from classes import *

while sim:
    sim = False
    #Criando Sticks
    balas = 3
    text = fonte.render(str(balas), True, (255, 255, 255))
    stick1 = stick(stick_img, 200, 215,1)
    stick2 = stick(stick_img, 0, 128,1)
    stick3 = stick(stick_img,850,160,1)
    stick4 = stick(stick_img,280,43,2)
    stick5 = stick(stick_img,540,246,2)
    stick6 =stick(stick_img,740,130,2)
    stick7 =stick(stick_img,100,282,2)
    stick8 =stick(stick_img,360,192,2)
    stick9 = stick(stick_img, 600, 185,2)
    stick10 = stick(stick_img, 300, 185,2)
    stick11 = stick(stick_img, 200, 316,2)
    stick12 = stick(stick_img, 500 ,316,2)
    stick13 = stick(stick_img, 720, 450,2)
    stick14 =stick(stick_img, 420, 450,2)
    mira1 = mira2(mira_img,0,0)
    bolinha1 = bolinha2(bolinha_img,0,0)

    #Loop principal

    clock = pygame.time.Clock()
    FPS = 30
    game = True
    abatido = 0
    nivel = 1
    t = 0
    b = 0
    inicio = 0
    fim = time.time()
    pontuacao = 0 
    contador = 0
    tempo_final = 1
    ja_tocou_perdeu = False
    ja_tocou_start = False
    ja_tocou_win = False
    ja_tocou_game = False
    ja_iniciou = False
    jogo = False
    lose = False
    win = False
    aparecer = False
    while game:
        if start == True and ja_iniciou == False:
            inicio = time.time()
            ja_iniciou = True
        clock.tick(FPS)
        if nivel ==1:
            lista_stick = [stick1,stick2,stick3]
        if nivel ==2:
            lista_stick = [stick4,stick5,stick6,stick7,stick8]
        if nivel == 3:
            lista_stick = [stick9,stick10,stick11,stick12,stick13,stick14]
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s and (win or lose):
                    sim = True
                    game = False
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    start = True
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
            if pygame.mouse.get_pressed()[0]:
                if event.type == pygame.MOUSEBUTTONDOWN and aparecer == True and not pygame.mouse.get_pressed()[2] :
                    pygame.mouse.set_visible(False)
                    if start == True:
                        balas -=1
                        tiro_som.play()
                        kill = 0
                        for a in lista_stick:
                            hit = pygame.sprite.collide_rect(bolinha1,a)
                            if hit == 1:
                                kill += 1
                                a.update(0,0,2)
                                abatido += 1
                                if kill == 2:
                                    pontuacao += 300
                                else:
                                    pontuacao += 100
            if pygame.mouse.get_pressed()[2] and aparecer == False and not pygame.mouse.get_pressed()[0] :
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aparecer = True
            elif pygame.mouse.get_pressed()[2]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aparecer = False

            if lose == True and not ja_tocou_perdeu:
                perder_som.play(0)
                ja_tocou_perdeu = True
            if start == False and inicia and not ja_tocou_start:
                inicial_som.play(0)
                ja_tocou_start = True
            if start == True and ja_tocou_start:
                inicial_som.stop()
            if win == True and not ja_tocou_win:
                ganhou_som.play(0)
                ja_tocou_win = True
            if jogo == False and not ja_tocou_game and start == True:
                jogo_som.play(-1)
                ja_tocou_game = True
            if jogo == True and ja_tocou_start:
                jogo_som.stop()
            if event.type == KEYDOWN and inicia:
                start =True
            if event.type == KEYDOWN and not inicia:
                if event.key == pygame.K_SPACE:
                    inicia = True
            
                pygame.mouse.set_visible(False)
            text = fonte.render(str(balas), True, (255, 255, 255))
            pontos = fonte3.render(str(pontuacao), True, (255, 255, 255))
        
        if start:
            contador = 1
            if int(tempo_final) == 0:
                tempo_final = 1
            if not lose and not win:
                fim = time.time()
                contador = fim - inicio
                tempo_final = contador
            temporizador = '{:.2f}'.format(contador).replace('.',':')
            tempo = font_sys.render(temporizador, True, (255, 255, 255)) 
            
        if abatido < 3:
            background = background1
            nivel=1
        elif abatido ==3 and t==0:
            nivel = 2
            balas = 5 
            t += 1
        elif abatido == 8 and b==0:
            nivel = 3
            balas = 6 
            b += 1
        mousePos = pygame.mouse.get_pos()
        mouse_x_b = pygame.mouse.get_pos()[0]-5
        mouse_y_b= pygame.mouse.get_pos()[1]-5
        mira_X = pygame.mouse.get_pos()[0] - 1245
        mira_Y = pygame.mouse.get_pos()[1] - 715
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
        if nivel == 3:
            stick9.update(180,725,3)
            stick10.update(180,725,3)
            stick11.update(180,725,3)
            stick12.update(180,725,3)
            stick13.update(180,725,3)
            stick14.update(180,725,3)
        if aparecer == True:
            mira1.update(mira_X,mira_Y)
            bolinha1.update(mouse_x_b,mouse_y_b)
        # ----- Gera saídas
        window.fill((0, 0, 0))
        if not inicia:
            window.blit(controle,(0,0))
        if inicia:
            window.blit(inicial,(0,0))
            window.blit(texto, ((WIDTH/4), 300))
        
        if start:
            # Preenche com a cor branca
            window.blit(background, (0,0))
            
            if nivel == 1:
                window.blit(stick1.image, stick1.rect)
                window.blit(stick2.image, stick2.rect)
                window.blit(stick3.image,stick3.rect)
                window.blit(bala_img, (20,455))
                window.blit(text, (55, 482))
            if nivel == 2:
                background = background2
                window.blit(stick4.image, stick4.rect)
                window.blit(stick5.image, stick5.rect)
                window.blit(stick6.image,stick6.rect)
                window.blit(stick7.image, stick7.rect)
                window.blit(stick8.image, stick8.rect)
                window.blit(bala_img, (20,455))
                window.blit(text, (55, 482))
            if nivel == 3:
                background = background3
                window.blit(j1, (530,450))
                window.blit(j2, (535,182))
                window.blit(j3, (458,316))
                window.blit(j4, (350,185))
                window.blit(j5, (459,445))
                window.blit(j6, (350,320))
                window.blit(j7, (530,318))
                window.blit(j8, (458,185))
                window.blit(j9, (347,452))
                window.blit(stick9.image, stick9.rect)
                window.blit(stick10.image, stick10.rect)
                window.blit(stick11.image, stick11.rect)
                window.blit(stick12.image,stick12.rect)
                window.blit(stick13.image, stick13.rect)
                window.blit(stick14.image, stick14.rect)
                window.blit(sobre, (280, 109))
                window.blit(bala_img, (20,455))
                window.blit(text, (55, 482))
            window.blit(score, ((WIDTH/2) - 70,30))
            window.blit(pontos, ((WIDTH/2) - 40, 44))
            window.blit(texto3,((WIDTH/2) - 45, 5))
            window.blit(times, (800,30))
            window.blit(texto4,(815, 5))
            window.blit(tempo,(830, 37))
            
            ponto_certo = pontuacao/tempo_final
            texto5 = fonte2.render(str(int(ponto_certo)), True, (255, 255, 255))
            texto8 = fonte2.render(str(int(ponto_certo)), True, (0, 0, 0))
            texto6 = fonte2.render('Points per sec', True, (0, 0, 0))
            texto7 = fonte2.render('Points per sec', True, (255, 255, 255))
            texto9 = font_sys2.render('To play again press "s"',True,(255,255,255))
            texto10 = font_sys2.render('To play again press "s"',True,(0,0,0))
            
            if aparecer == True:
                window.blit(mira_img, (mira_X, mira_Y))
                window.blit(bolinha_img, (mouse_x_b, mouse_y_b))
            elif aparecer == False:
                window.blit(sniper_img, ((WIDTH/2)+50, HEIGHT-211))
            
            if abatido == 14:
                if balas > 0 and not win:
                    pontuacao += balas*200
                win = True
                balas = 1
                background = ganhou
                jogo = True
                window.blit(background, (-20,0))
                window.blit(texto6,(500, HEIGHT/2))
                window.blit(texto8,(800, HEIGHT/2))
                window.blit(texto10,(300,450))
                
            
            if balas <= 0:
                background = mira_img
                background = perdeu
                pygame.mixer.Sound.stop(tiro_som)
                lose = True
                jogo = True
                window.blit(background, (0,0))
                window.blit(texto7,(10 , HEIGHT/2))
                window.blit(texto5,(310,  HEIGHT/2))
                window.blit(texto9,(300,450))
                
            
            
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados