# This is the main file for L1 Activity 1
import pygame
import random
  
surf_color = (0, 142, 204)
color = (0, 0, 0)

# Object class
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(surf_color)
		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def moveForward(self, speed):
		self.rect.y += speed * speed/10

	def moveBack(self, speed):
		self.rect.y -= speed * speed/10
  
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")

all_sprites_list = pygame.sprite.Group()

# Add a sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

# Add one enemy 
# set the random position
rad = 20
cxp = random.randint(0,480)
cyp = random.randint(0,370)
sp2 = Sprite((255,0,0), 20, 30)
sp2.rect.x = cxp
sp2.rect.y = cyp
all_sprites_list.add(sp2)

exit = True
clock = pygame.time.Clock()
  
while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				exit = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		sp1.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		sp1.moveRight(5)
	if keys[pygame.K_DOWN]:
		sp1.moveForward(5)
	if keys[pygame.K_UP]:
		sp1.moveBack(5)

	all_sprites_list.update()
	screen.fill(surf_color)
	all_sprites_list.draw(screen)
	pygame.display.flip()

	# Check Collision
	if sp1.rect.colliderect(sp2.rect):
		all_sprites_list.remove(sp2)
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()