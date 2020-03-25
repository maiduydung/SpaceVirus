import pygame
import random
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
bullet_img = pygame.image.load("resources/icons/spaceship.png")
bullet_x = random.randint(0,750)
bullet_y = random.randint(50,400)
bullet_y_change = 0.1
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x ,y))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

#game loop
while running:
    screen.fill((0, 0, 0))
    #screen.blit(background, (0, 0))

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
                fire_bullet(player_x, player_y)

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


    # s
    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_SPACE:
    #         print('Space is hit')
    #         fire_bullet(player_x, player_y-30)
    #bullet movement
    fire_bullet(player_x, player_y)
    if bullet_state is "fire":
        fire_bullet(player_x, player_y)
        bullet_y -= bullet_y_change 


    
    player(player_x,player_y)

    fire_bullet(player_x, player_y-32)
    player_x_temp = player_x
    player_y_temp = player_y -32
    if bullet_state is "fire":
        fire_bullet(player_x_temp, player_y_temp)
        player_y_temp -= bullet_y_change 

    enemy(enemy_x,enemy_y)
    
    pygame.display.update()
pygame.quit()