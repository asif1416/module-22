# This is the main file for ACP
import pygame
import random

pygame.init()

window_width, window_height = 600, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Sprite Color Change Event")

WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

sprite_width, sprite_height = 50, 50

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([sprite_width, sprite_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self, color):
        self.image.fill(color)

sprite1 = Sprite(random.choice(colors), 100, 100)
sprite2 = Sprite(random.choice(colors), 300, 200)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == CHANGE_COLOR_EVENT:
            new_color1 = random.choice(colors)
            new_color2 = random.choice(colors)
            sprite1.change_color(new_color1)
            sprite2.change_color(new_color2)
    
    window.fill(WHITE)
    
    all_sprites.draw(window)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
