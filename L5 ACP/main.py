import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Player and Enemy Collision Game")

# Load images
player_image = pygame.image.load('L5 ACP/player.png')  
enemy_image = pygame.image.load('L5 ACP/enemy.png') 

player_image = pygame.transform.scale(player_image, (100, 100))  
enemy_image = pygame.transform.scale(enemy_image, (50, 50)) 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  
        self.rect = self.image.get_rect()
        self.rect.x = 375  
        self.rect.y = 500

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 750:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < 550: 
            self.rect.y += 5

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(0, 450)

    def update(self):
        self.rect.x += random.choice([-1, 1]) * 2
        self.rect.y += random.choice([-1, 1]) * 2

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 750:
            self.rect.x = 750
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 550:
            self.rect.y = 550

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

for _ in range(7):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

score = 0
font = pygame.font.Font(None, 36)

game_over_font = pygame.font.Font(None, 74)

# Game loop control variables
running = True
game_over = False

clock = pygame.time.Clock()

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Only update the game if it's not over
    if not game_over:
        all_sprites.update()

        # Check for collisions between player and enemies
        if pygame.sprite.spritecollide(player, enemies, True): 
            score += 1
            print(f"Score: {score}")

        # Check if all enemies are eliminated
        if len(enemies) == 0:
            game_over = True  # Set the game to "over"

    screen.fill(BLACK)

    all_sprites.draw(screen)

    # Render the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        win_text = game_over_font.render("YOU WIN!", True, WHITE)
        screen.blit(win_text, (250, 250))  # Center the text on the screen

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
