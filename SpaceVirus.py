import pygame
import random
import time
from multiprocessing import Process

pygame.init()

#game screen
screen = pygame.display.set_mode((800, 600))

running = True

#adding background
background = pygame.image.load("resources/background/background.jpg")
#title and icon
pygame.display.set_caption("Mai Duy Dung")
icon = pygame.image.load("resources/icons/spaceship.png")
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load("resources/icons/spaceship.png")
player_x = 400
player_y = 480
player_x_change = 0
player_y_change = 0

#enemy
enemy_img = pygame.image.load("resources/icons/virus.png")
enemy_x = random.randint(0,750)
enemy_y = random.randint(50,400)
enemy_x_change = 1

#bullet
bullet_img = pygame.image.load("resources/icons/bullet.png")
bullet_x = 0
bullet_y = player_y
bullet_y_change = 3
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    x += 20
    y -= 32
    print('bullet x y', x, y)
    screen.blit(bullet_img, (x ,y))
        
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

#game loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Left is hit')
                player_x_change -=3
            if event.key == pygame.K_RIGHT:
                print('Right is hit')
                player_x_change +=3
            if event.key == pygame.K_UP:
                print('Up is hit')
                player_y_change -=3
            if event.key == pygame.K_DOWN:
                print('Down is hit')
                player_y_change +=3
            if event.key == pygame.K_SPACE:
                print('Space is hit')
                bullet_x = player_x
                fire_bullet(bullet_x, player_y)
                # fire_proc =  Process(target=fire_bullet(player_x, player_y)) 
                # fire_proc.start()
                # fire_proc.join()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or  event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                player_x_change = 0
                player_y_change = 0
    
    

    
    #boundary check for player and enemy
    player_x += player_x_change
    player_y += player_y_change

    if player_x <= 20:
        player_x = 20
    if player_x >= 750:
        player_x = 750
    
    if player_y <= 20:
        player_y = 20
    if player_y >= 500:
        player_y = 500

    enemy_x += enemy_x_change

    if enemy_x <= 20:
        enemy_x_change = 1
    if enemy_x >= 750:
        enemy_x_change = -1

    
    ########
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    
    pygame.display.update()
pygame.quit()