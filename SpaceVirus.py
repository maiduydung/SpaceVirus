import pygame
import random
import math
from pygame import mixer


pygame.init()


mixer.music.load("resources/sounds/bg_music.mp3")
mixer.music.play(-1)

#game screen
screen = pygame.display.set_mode((800, 600))

running = True

#score 
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 20
text_y = 20

def show_score(x, y):
    show = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(show, (x, y))

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
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemies = 20

for i in range(enemies):
    temp = pygame.image.load("resources/icons/virus.png")
    enemy_img.append(temp)
    enemy_x.append(random.randint(0,750))
    enemy_y.append(random.randint(50,400))
    enemy_x_change.append(1)
    enemy_y_change.append(40)

#bullet
bullet_img = pygame.image.load("resources/icons/bullet.png")
bullet_x = 0
bullet_y = player_y
bullet_y_change = 10
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    x += 20
    y -= 32
    #print('bullet x y', x, y)
    screen.blit(bullet_img, (x ,y))
        
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def collision_check(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False

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
                if bullet_state == "ready":
                    bullet_x = player_x
                    bullet_sound = mixer.Sound('resources/sounds/laser.wav')
                    bullet_sound.play()
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

    for i in range(enemies):
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 20:
            enemy_x_change[i] = 1
            #enemy_y[i] += enemy_y_change[i]
        if enemy_x[i] >= 750:
            enemy_x_change[i] = -1
            #enemy_y[i] += enemy_y_change[i]

    
    ########
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    #### collision check
    bullet_hit=[]
    virus_hit=[]
    for i in range(enemies):
        bullet_hit.append(collision_check(enemy_x[i], enemy_y[i], bullet_x, bullet_y))
        virus_hit.append(collision_check(enemy_x[i], enemy_y[i], player_x, player_y))
        if bullet_hit[i]:
            score += 10
            print("score ", score)
            bullet_state = "ready"
            bullet_x = player_x
            bullet_y = player_y
            enemy_x[i] = random.randint(0,750)
            enemy_y[i] = random.randint(50,400)
        if virus_hit[i]:
            #game_over
            doomed = mixer.Sound('resources/sounds/explosion.wav')
            doomed.play()
            player_x = random.randint(0,750)
            player_y = random.randint(50,400)
            enemy_x.append(random.randint(0,750))
            enemy_y.append(random.randint(50,400))
            score -= 10

    show_score(text_x, text_y)

    player(player_x,player_y)
    for i in range(enemies):
        enemy(enemy_x[i],enemy_y[i], i)
    
    pygame.display.update()
pygame.quit()