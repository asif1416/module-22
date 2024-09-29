# This is the main file for L1 Activity 1
import pygame  
pygame.init()  
grey = (58,58,58)  

clock = pygame.time.Clock()
  
display_surface = pygame.display.set_mode((500, 500))  
  
pygame.display.set_caption('My First Game Screen')  
  
image = pygame.image.load('L1 ACP/lion.png')  

DEFAULT_IMAGE_SIZE = (300,300)
  
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

DEFAULT_IMAGE_POSITION = (100,100)

while True:  
	display_surface.fill(grey)  
	display_surface.blit(image, DEFAULT_IMAGE_POSITION)  

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			pygame.quit()  
			quit()  
		
	pygame.display.flip()
	clock.tick(30)