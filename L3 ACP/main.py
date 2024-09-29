import pygame

pygame.init()

window_width, window_height = 600, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rectangular Sprites Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

sprite_width, sprite_height = 50, 50

player_sprite = pygame.Rect(100, 100, sprite_width, sprite_height)  
enemy_sprite = pygame.Rect(300, 200, sprite_width, sprite_height)   

speed = 5

# Boolean to track if enemy still exists
enemy_alive = True

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_sprite.x -= speed
    if keys[pygame.K_RIGHT]:
        player_sprite.x += speed
    if keys[pygame.K_UP]:
        player_sprite.y -= speed
    if keys[pygame.K_DOWN]:
        player_sprite.y += speed

    if enemy_alive and player_sprite.colliderect(enemy_sprite):
        enemy_alive = False  

    window.fill(WHITE)

    pygame.draw.rect(window, BLUE, player_sprite)

    if enemy_alive:
        pygame.draw.rect(window, RED, enemy_sprite)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
