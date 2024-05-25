# Começando o Pygame e importando dados de bibliotecas

import pygame
from sys import exit
from random import randint

# Coração do Código:

pygame.init()
x = 800  #Tamanho horizontal da tela
y = 400  #Tamanho Vertical da tela
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Monster Hunter')
clock = pygame.time.Clock()
vel_x_bullet = 0
current_time = 0

#Sistema de Pontuações

pontuação = 0
pontuações = [0]

#Gravidade
gravity = 0

#Velocidade que a bala se movimenta

vel_tiro = 8

#Velocidade do Player

vel_player = 4
tx_player = 0.3

#Definindo a velocidade do Monstro e taxa de atualização que futuramente será atualizada pela dificuldade escolhida
vel_monstro = 0
tx_monstro = 0


#Controle de vida

dano = 0
dano_obtido = 0

# Assume-se essas condições/flags iniciais para criar o ambiente do jogo


#Animação do Personagem

direita = True
pulo = False
atirar = False

#Controlar a barra de vida

tomou_dano = False

#Mecânica de Tiro

tiro = False
saiu = False

#Controle de Tela

morreu = False
menu = True
tutorial = False
dificuldades = False



#Dificuldade

facil = True
medio = False
dificil = False


#Sprites

# Planos de Fundo| Interface :

sky_surf = pygame.image.load('Gráficos Pygame/Interface/sky.png')
ground_surf = pygame.image.load('Gráficos Pygame/Interface/ground.png')
death_surf = pygame. image.load('Gráficos Pygame/Interface/Gameover.png')
menu_surf = pygame.image.load('Gráficos Pygame/Interface/menu.png')
tutorial_surf = pygame.image.load('Gráficos Pygame/Interface/tutorial.png')
dificuldades_surf = pygame.image.load('Gráficos Pygame/Interface/dificuldades.png')

#Fonte usada

test_font = pygame.font.Font('Gráficos Pygame/Fonte/Pixeltype.ttf', 55)

#Botões para mudar de telas

home_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/home_buttom.png').convert_alpha()
tutorial_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/tutorial_buttom.png').convert_alpha()
dificuldades_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/dificuldades_buttom-.png').convert_alpha()

#Botões Dificuldade

play_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/play_buttom.png').convert_alpha()
facil_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/facil.png').convert_alpha()
medio_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/medio.png').convert_alpha()
dificil_buttom = pygame.image.load('Gráficos Pygame/Interface/Botões/dificil.png').convert_alpha()

#Formatações Botões

home_buttom = pygame.transform.rotozoom(home_buttom, 0, 1/2 ).convert_alpha()
tutorial_buttom = pygame.transform.rotozoom(tutorial_buttom, 0, 1/2 ).convert_alpha()
dificuldades_buttom = pygame.transform.rotozoom(dificuldades_buttom, 0, 1/2 ).convert_alpha()

#Retangulos De Cada Botão para torna-los interagiveis

#Menu's

home_buttom_rect = home_buttom.get_rect(center=(730,350))
home_buttom_tutorial_rect = home_buttom.get_rect(center=(400,350))
home_buttom_dificuldades_rect = home_buttom.get_rect(center=(100,350))

tutorial_buttom_rect = tutorial_buttom.get_rect(center=(670,350))
dificuldades_buttom_rect = dificuldades_buttom.get_rect(center=(750,350))

#Botão para começar o jogo pelo menu

play_buttom_rect = play_buttom.get_rect(center=(400,300))

#Botões para mudar a dificuldade e suas hitbox

facil_buttom_rect = facil_buttom.get_rect(center=(400,160))
medio_buttom_rect = medio_buttom.get_rect(center=(400,250))
dificil_buttom_rect = dificil_buttom.get_rect(center=(400,340))


#Musicas

death_music = pygame.mixer.Sound('audio/Determination.mp3')
tutorial_music = pygame.mixer.Sound('audio/Once upon a Time.mp3')
bg_music = pygame.mixer.Sound('audio/Spear of Justice.mp3')

#Efeitos Sonoros Player:

jump_sound = pygame.mixer.Sound('audio/Sound Effect/jump.mp3')
damage_sound = pygame.mixer.Sound('audio/Sound Effect/damage_sound.mp3')
shoot_sound = pygame.mixer.Sound('audio/Sound Effect/shoot_sound.mp3')
death_sound = pygame.mixer.Sound('audio/Sound Effect/death_sound.mp3')

#Efeitos Sonoros Mudança de dificuldade

activation_sound = pygame.mixer.Sound('audio/Sound Effect/activation.mp3')

#Zumbi Morrendo

zombie_death_sound = pygame.mixer.Sound('audio/Sound Effect/zombie_death.mp3')

#Controlar o Volume da Musica do Jogo

com_som = 0.3
sem_som = 0.0


#Começar musicas

tutorial_music.play(loops=-1)
tutorial_music.set_volume(com_som)

bg_music.play(loops= -1)
bg_music.set_volume(sem_som)

death_music.play(loops=-1)
death_music.set_volume(sem_som)

#Sprites do Player

player_walk_1 = pygame.image.load('Gráficos Pygame/Player/Walk/walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Gráficos Pygame/Player/Walk/walk_2.png').convert_alpha()
player_walk_3 = pygame.image.load('Gráficos Pygame/Player/Walk/walk_3.png').convert_alpha()
player_jump_1 = pygame.image.load('Gráficos Pygame/Player/Jump/jump_1.png').convert_alpha()
player_shoot = pygame.image.load('Gráficos Pygame/Player/Attack/shot_walk.png').convert_alpha()

player_health = pygame.image.load('Gráficos Pygame/Player/Life/hearth.png'). convert_alpha()
player_death = pygame.image.load('Gráficos Pygame/Player/Death/death_2.png').convert_alpha()

player_walk_1 = pygame.transform.rotozoom(player_walk_1, 0, 1 / 2).convert_alpha()
player_walk_2 = pygame.transform.rotozoom(player_walk_2, 0, 1 / 2).convert_alpha()
player_walk_3 = pygame.transform.rotozoom(player_walk_3, 0, 1 / 2).convert_alpha()
player_jump_1 = pygame.transform.rotozoom(player_jump_1,0, 1/2 )   .convert_alpha()
player_shoot = pygame.transform.rotozoom(player_shoot,0, 1/2 )   .convert_alpha()
player_health = pygame.transform.rotozoom(player_health,0, 1/10 )   .convert_alpha()
player_death = pygame.transform.rotozoom(player_death,0, 1/2 )   .convert_alpha()

# Sprites Monstro

monster_surf_1 = pygame.image.load('Gráficos Pygame/Monster/zombie_1.png').convert_alpha()
monster_surf_1 = pygame.transform.rotozoom(monster_surf_1, 0, 2).convert_alpha()
monster_surf_1 = pygame.transform.flip(monster_surf_1, True, False)

monster_surf_2 = pygame.image.load('Gráficos Pygame/Monster/zombie_2.png').convert_alpha()
monster_surf_2 = pygame.transform.rotozoom(monster_surf_2, 0, 2).convert_alpha()
monster_surf_2 = pygame.transform.flip(monster_surf_2, True, False).convert_alpha()

monster_surf_right_1 = pygame.transform.flip(monster_surf_1, True, False)
monster_surf_right_2 = pygame.transform.flip(monster_surf_2, True, False)

# Sprites Tiro

bullet_surf_right = pygame.image.load('Gráficos Pygame/Bullet/bullet_1.png').convert_alpha()

bullet_surf_right = pygame.transform.rotozoom(bullet_surf_right,0, 1/7 )   .convert_alpha()

bullet_surf_left = pygame.transform.flip(bullet_surf_right,True, False). convert_alpha()
bullet_surf = bullet_surf_right

# Frames Player para animar

frames = [player_walk_1, player_walk_2, player_walk_3]
player_index = 0
player_surf = frames[int(player_index)]


# Frames Monstro para animar Esquerda
monster_frames = [monster_surf_1, monster_surf_2]
monster_index = 0
monster_surf = monster_surf_1

# Frames Monstro para animar Direita
monster_frames_right = [monster_surf_right_1, monster_surf_right_2]
monster_index_right = 0
monster_surf_right = monster_surf_right_1


#Posições


# Pegando a Hitbox

#Player

player_rect = player_surf.get_rect(midbottom=(400,300))
bullet_rect = bullet_surf.get_rect(midbottom=(400,275))

#Monstro

monster_rect = monster_surf.get_rect(midbottom=(1000, 300))
monster_right_rect = monster_surf_right.get_rect(midbottom=(-200, 300))

# Funções:

# Movimentação do Player

def player_animation():
    global player_surf, player_index, atirar, pulo

    if player_index >= len(frames):
        player_index= 0

    #Animação de pulo e verificando para qual lado o pulo irá

    if player_rect.bottom < 300:
        if direita == False:
            player_surf = pygame.transform.flip(player_jump_1, True, False).convert_alpha()
        else:
            player_surf = player_jump_1

    #Animação de tiro

    elif atirar == True:
        if direita == False:
            player_surf = pygame.transform.flip(player_shoot, True, False).convert_alpha()
        else:
            player_surf = player_shoot

    elif direita == False:
        player_surf = frames[int(player_index)]
        player_surf = pygame.transform.flip(player_surf, True, False).convert_alpha()
    else:
        player_surf = frames[int(player_index)]

# Animação do monstro

def monster_animation():
    global monster_surf, monster_index

    if monster_index >= len(monster_frames):
        monster_index = 0
    monster_surf = monster_frames[int(monster_index)]

def monster_animation_right():
    global monster_surf_right, monster_index_right

    if monster_index_right >= len(monster_frames_right):
        monster_index_right = 0
    monster_surf_right = monster_frames_right[int(monster_index_right)]

#Recarregar as balas

def respawn_bullet():

    tiro = False
    respawn_bullet_x = player_rect.x
    respawn_bullet_y = 250
    vel_x_bullet = 0
    return [respawn_bullet_x,respawn_bullet_y,tiro,vel_x_bullet]

#Marcador de Pontuação

def display_pontuation():
    global pontuação
    score_surface = test_font.render(f"Score: {pontuação}", False, 'Yellow')
    score_rect = score_surface.get_rect(center=(660, 50))
    screen.blit(score_surface, score_rect)


# Loop para "rodar" o jogo:

while True:
    keys = pygame.key.get_pressed()
    tomou_dano = False

    #Fechando o jogo caso o player clique no botão de fechar

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Tela de Menu

    if menu == True:
        screen.blit(menu_surf,(0,0))

        screen.blit(tutorial_buttom, (tutorial_buttom_rect))
        screen.blit(dificuldades_buttom,(dificuldades_buttom_rect))

        screen.blit(play_buttom,(play_buttom_rect))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if tutorial_buttom_rect.collidepoint(event.pos):
                menu = False
                tutorial = True
            if dificuldades_buttom_rect.collidepoint(event.pos):
                menu = False
                dificuldades = True

            if play_buttom_rect.collidepoint(event.pos):
                menu = False
        if keys[pygame.K_p]:
            morreu = False
            menu = False

    #Tela do Tutorial

    elif tutorial == True:
        screen.blit(tutorial_surf, (0,0))
        screen.blit(home_buttom,(home_buttom_tutorial_rect) )
        if event.type == pygame.MOUSEBUTTONDOWN:
            if home_buttom_tutorial_rect.collidepoint(event.pos):
                menu = True
                tutorial = False

    #Tela de Escolher a dificuldade

    elif dificuldades == True:
        screen.blit(dificuldades_surf,(0,0))
        screen.blit(home_buttom, (home_buttom_dificuldades_rect))
        screen.blit(facil_buttom,(facil_buttom_rect))
        screen.blit(medio_buttom, (medio_buttom_rect))
        screen.blit(dificil_buttom, (dificil_buttom_rect))
        #Parei aqui
        if event.type == pygame.MOUSEBUTTONDOWN:
            if home_buttom_dificuldades_rect.collidepoint(event.pos):
                menu = True
                dificuldades = False

            elif facil_buttom_rect.collidepoint(event.pos):
                activation_sound.set_volume(0.3)
                activation_sound.play(loops=0)
                pontuações = [0]
                facil = True
                medio = False
                dificil = True


            elif medio_buttom_rect.collidepoint(event.pos):
                activation_sound.set_volume(0.3)
                activation_sound.play(loops=0)
                pontuações = [0]
                facil = False
                medio = True
                dificil = True

            elif dificil_buttom_rect.collidepoint(event.pos):
                activation_sound.set_volume(0.3)
                activation_sound.play(loops=0)
                pontuações = [0]
                facil = False
                medio = False
                dificil = True


    #Começa o jogo

    elif morreu == False and menu == False:

        #Verificando qual dificuldade o player escolheu para definir a velocidade do monstro
        #Caso ele não selecione nenhuma a dificulade padrão é a facil

        if facil == True:
            vel_monstro = 2
            tx_monstro = 0.2
        elif medio == True:
            vel_monstro = 4
            tx_monstro = 0.3
        else:
            vel_monstro = 6
            tx_monstro = 0.5

        #Musicas

        tutorial_music.set_volume(sem_som)
        bg_music.set_volume(com_som)
        current_time = int((pygame.time.get_ticks()/1000))

        #Pulo

        if keys[pygame.K_SPACE] and player_rect.bottom == 300:
            jump_sound.set_volume(0.09)
            jump_sound.play(loops= 0)

            atirar = False
            pulo = True
            gravity = -20


        #Atirar

        if keys[pygame.K_c] and player_rect.bottom == 300 and current_time >= 1 and saiu == False:
            atirar = True
            tiro = True
            if saiu == False:
                shoot_sound.set_volume(0.1)
                shoot_sound.play(loops=0)
                if direita == True:
                    bullet_surf = bullet_surf_right
                    vel_x_bullet = vel_tiro
                    saiu = True

                else:
                    bullet_surf = bullet_surf_left
                    vel_x_bullet = -(vel_tiro)
                    saiu = True

        #Andar para a esquerda

        if keys[pygame.K_a]:

            #Caso o usuario aperte as duas teclas de andar simultaneamente ele não consegue andar

            if not keys[pygame.K_d]:
                direita = False
                atirar = False
                player_index += tx_player
                player_rect.x -= vel_player

                if not tiro:
                    bullet_rect.x -= vel_player

        #Andar para a direita

        elif keys[pygame.K_d]:
            if not keys[pygame.K_a]:
                direita = True
                atirar = False
                player_index += tx_player
                player_rect.x += vel_player
                if not tiro:
                    bullet_rect.x += vel_player

        # Ambientação

        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        # Movimentação do Monstro

        if monster_rect.right <= 0:
            monster_rect.x = 900
        monster_rect.x -= vel_monstro
        monster_index += tx_monstro

        if monster_right_rect.left >= 800:
            monster_right_rect.x = -100
        monster_right_rect.x += vel_monstro
        monster_index_right += tx_monstro

        # Animacões


        # pygame.draw.rect(screen, (255, 0, 0), bullet_rect, 4)

        player_animation()
        monster_animation()
        monster_animation_right()


        #Caso o tiro saia do mapa ele retorna ao player

        if bullet_rect.x >= 900 or bullet_rect.x <= -100:
            bullet_rect.x,bullet_rect.y, tiro, vel_x_bullet = respawn_bullet()
            saiu = False

        bullet_rect.x += vel_x_bullet

        #Desenhando na tela

        # Movimentação do Tiro

        if bullet_rect.x != player_rect.x:
            if saiu == True:
                screen.blit(bullet_surf, (bullet_rect.x, bullet_rect.y))

        #Movimentação Player e Monstro

        screen.blit(player_surf, player_rect)
        screen.blit(monster_surf, monster_rect)
        screen.blit(monster_surf_right, monster_right_rect)

        #Sistema de Pontuação

        score = display_pontuation()


        #Barra de vida
        
        if dano_obtido == 0:
            screen.blit(player_health,(0,0))
            screen.blit(player_health,(50,0))
            screen.blit(player_health,(100,0))
        if dano_obtido == 1:
            screen.blit(player_health,(0,0))
            screen.blit(player_health,(50,0))

        if dano_obtido == 2:
            screen.blit(player_health,(0,0))
        if dano_obtido == 3:
            death_sound.set_volume(0.8)
            death_sound.play(loops=0)
            morreu = True


        # Vendo Hitbox

        #pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
        #pygame.draw.rect(screen, (255, 0, 0), monster_rect, 4)
        #pygame.draw.rect(screen,(255,0,0),monster_right_rect,4)
        #pygame.draw.rect(screen, (255, 0, 0), bullet_rect, 4)

        #Player tomando dano

        if monster_rect.x <= 0 and monster_rect.x > -400:
            tomou_dano = True
            monster_rect.x = -400

        if monster_right_rect.x >= 800 and monster_rect.x < 1200:
            tomou_dano = True
            monster_right_rect.x = 1200

        #Sistema de colisões do player e monstro

        if player_rect.colliderect(monster_rect) or player_rect.colliderect(monster_right_rect):
            tomou_dano = True
            monster_rect.x = -200
            monster_right_rect.x = 1000
            player_rect.x,bullet_rect.x = 400,400

        #Adicionar som de dano tomado


        if tomou_dano == True:
            damage_sound.set_volume(0.2)
            damage_sound.play(loops=0)
            dano_obtido += 1
            tomou_dano = False

        #Se o tiro pegou no Monstro

        if bullet_rect.colliderect(monster_rect):
            zombie_death_sound.set_volume(0.22)
            zombie_death_sound.play(loops=0)
            vel_monstro += 0.3
            monster_rect.x = -100
            pontuação += 1
            bullet_rect.x = -400
            saiu = False
            bullet_surf = bullet_surf_right

        if bullet_rect.colliderect(monster_right_rect):
            zombie_death_sound.set_volume(0.2)
            zombie_death_sound.play(loops=0)
            vel_monstro+=0.3
            monster_right_rect.x = 900
            pontuação +=1
            bullet_rect.x = 1200
            saiu = False
            bullet_surf = bullet_surf_right

        # Gravidade

        gravity += 1
        player_rect.y += gravity
        if saiu ==False:
            bullet_rect.y += gravity

        #Limitadores

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            bullet_rect.bottom = 275

        if player_rect.right >= 800:
            player_rect.right = 800
            if saiu == False:
                bullet_rect.x = 800
        if player_rect.left < 0:
            player_rect.left = 0
            if saiu == False:
                bullet_rect.x = 0


    #Tela de Morte

    else:
        screen.fill('black')
        screen.blit(death_surf,(0,-20))
        bg_music.set_volume(sem_som)
        death_music.set_volume(com_som)
        record = max(pontuações)
        screen.blit(home_buttom,(home_buttom_dificuldades_rect))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if home_buttom_dificuldades_rect.collidepoint(event.pos):
                pontuações.append(pontuação)
                pontuação = 0
                death_music.set_volume(sem_som)
                tutorial_music.set_volume(com_som)
                timer = 0
                saiu = False
                bullet_rect.x = player_rect.x
                menu = True
                morreu = False




        #Inserindo na tela a sua Pontuação do Momento

        score_message = test_font.render(f"Score: {pontuação}", False, 'White')
        score_message_rect = score_message.get_rect(center=(700, 50))
        screen.blit(score_message,(score_message_rect))

        #Inserindo na tela o seu Recorde e se você o bateu

        your_record = test_font.render(f"Best Score: {max(pontuações)}", False, 'Yellow')
        record_message_rect = score_message.get_rect(center=(360, 220))
        reward_message_rect = score_message.get_rect(center=(140, 220))

        reward_message = test_font.render(f"Congratulations, you broke your record!", False, 'Gold')
        if pontuação > record:
            screen.blit(reward_message,(reward_message_rect))
        else:
            screen.blit(your_record, (record_message_rect))

        # Pedindo para o Player pressionar P para Recomeçar

        prees_p = test_font.render(f"Press P to continue", False, 'Grey')
        prees_p_rect = prees_p.get_rect(center=(405,320))

        screen.blit(prees_p,(prees_p_rect))

        #Redefinindo as condições de jogo

        dano_obtido = 0
        player_rect = player_surf.get_rect(midbottom=(400,300))
        direita = True

        #Ao apertar a tecla "p" de play o jogo recomeça

        if keys[pygame.K_p]:
            pontuações.append(pontuação)
            pontuação = 0
            death_music.set_volume(sem_som)
            bullet_rect.x = player_rect.x

            morreu = False


    #Atualizando e Rodando o jogo

    pygame.display.update()
    clock.tick(60)
