# This is the main file for L1 Activity 3

import pygame
import random
  
surf_color = (0, 142, 204)
color = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
  
pygame.init()

all_sprites_list = pygame.sprite.Group()

# Add sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Creating Sprite")
screen.fill(surf_color)

new_color = (0,255,0)
bg_active_color = surf_color
CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 500)

exit = True
clock = pygame.time.Clock()

while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False

		if event.type == CHANGE_COLOR:
			if bg_active_color == new_color:
				screen.fill(new_color)
				bg_active_color = surf_color
			elif bg_active_color == surf_color:
				screen.fill(surf_color)
				bg_active_color = new_color
  
	all_sprites_list.update()
	all_sprites_list.draw(screen)

	pygame.display.update()
	clock.tick(30)

pygame.quit()
