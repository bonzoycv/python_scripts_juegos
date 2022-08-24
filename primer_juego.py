#!/usr/bin/env python3

from operator import truediv
import pygame
import random
import sys

pygame.init()

# Variables (tamano de la pantalla)

WIDTH = 800
HEIGHT = 600

# Variables personajes de juego
RED = (229, 250, 0) # Color del personaje
BLUE = (0,0,255)  # Color del enemigo
BGCOLOR = (11,238,207) # Color de fondo
YELLOW = (255,255,0) # Color de fuente

player_size = 45
player_pos = [WIDTH/2, HEIGHT-2*player_size] # Esto es una lista [0, 1] determina la ubicacion del personaje en la pantalla

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0] # Con el atributo random.ranint se genera en pantalla de manera aleatoria entre 0, el ancho de pantalla menos el tamano del enemigo
enemy_list = [enemy_pos]
SPEED = 10  # Velocidad de caida de bloques enemigos

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()  # crea un objeto para ayudar a controlar el tiempo

myFont = pygame.font.SysFont("monospace", 35)


# Esta funcion aumenta el nivel de dificultad
def set_level(score, SPEED):
    if score < 20:
        SPEED = 5
    elif score < 40:
        SPEED = 6
    elif score < 60:
        SPEED = 7
    elif score < 80:
        SPEED = 8
    elif score < 100:
        SPEED = 9
    elif score < 120:
        SPEED = 10
    elif score < 140:
        SPEED = 11
    elif score < 160:
        SPEED = 12
    elif score < 180:
        SPEED = 13
    elif score < 200:
        SPEED = 15

    return SPEED

# Esta funcion permite que bajen enemigos en la pantalla
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


# Esta funcion dibuja enemigos en pantalla
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))    # al dibujar un rectangulo se incluye (surface, color, rect)        

# Actualiza la posicion del enemigo en la pantalla
def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED

        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


# Esta funcion permite las coaliciones o choques con enemigos
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]


    screen.fill(BGCOLOR)

    # # Actualiza la posicion del enemigo en la pantalla
    # if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
    #     enemy_pos[1] += SPEED
    # else:
    #     enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
    #     enemy_pos[1] = 0

    # if detect_collision(player_pos, enemy_pos):
    #     game_over = True
    #     break

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score, SPEED)

    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break
    draw_enemies(enemy_list)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))   # al dibujar un rectangulo se incluye (surface, color, rect)        

    clock.tick(30)

    pygame.display.update() # Actualiza la pantalla 

