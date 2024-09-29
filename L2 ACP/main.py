# This is the main file for L1 Activity 2
import pygame  
pygame.init()  
screen = pygame.display.set_mode((640, 480))  
done = False  
  
font = pygame.font.SysFont("Times new Roman", 30)  
text = font.render("Welcome to Codingal", True, (158, 16, 16))  

while not done:  

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			done = True  

	screen.fill((255, 255, 255))  

	screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))  
	pygame.draw.rect(screen, (28,171,226), pygame.Rect(30, 30, 60, 60))
	pygame.display.flip()  