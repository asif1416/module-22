import math
import random
import pygame
from pygame import mixer

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((900, 800))

# Background
background = pygame.image.load('L5 Activity 1/bg.png')

# Sound
mixer.music.load("L5 Activity 1/download.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('L5 Activity 1/ufo.png')
pygame.display.set_icon(icon)

# Player (Spaceship)
playerImg = pygame.image.load('L5 Activity 1/player.png')
playerImg = pygame.transform.scale(playerImg, (150, 150))  
playerX = 300
playerY = 600
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('L5 Activity 1/enemy.png'))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (80, 80))
    enemyX.append(random.randint(0, 920))  
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(60) 

bulletImg = pygame.image.load('L5 Activity 1/bullet.jpg')
bulletImg = pygame.transform.scale(bulletImg, (25, 30)) 
bulletX = 200
bulletY = 800
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over font
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 45, y + 10))  


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    return distance < 40 


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("L5 Activity 1/laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 900: 
        playerX = 900

    for i in range(num_of_enemies):
        if enemyY[i] > 700:  
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2  
            enemyY[i] += enemyY_change[i]  
        elif enemyX[i] >= 920:  
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("L5 Activity 1/explosion.wav")
            explosionSound.play()
            bulletY = 380
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 920)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 380
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
