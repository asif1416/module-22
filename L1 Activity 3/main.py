# This is the main file for L1 Activity 3
import pygame
import sys

pygame.init()

window_width, window_height = 640, 480
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pygame Window with Text")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)

# Load different fonts and sizes
font1 = pygame.font.SysFont("arial", 40)
font2 = pygame.font.SysFont("timesnewroman", 50, bold=True)
font3 = pygame.font.SysFont("comicsansms", 60, italic=True)

# Render text with different fonts
text1 = font1.render("Hello, Pygame!", True, BLACK)
text2 = font2.render("Welcome!", True, BLACK)
text3 = font3.render("Let's Code!", True, BLACK)

# Get text positions
text1_rect = text1.get_rect(center=(window_width // 2, window_height // 4))
text2_rect = text2.get_rect(center=(window_width // 2, window_height // 2))
text3_rect = text3.get_rect(center=(window_width // 2, 3 * window_height // 4))

running = True
while running:
    screen.fill(WHITE)
    
    # Display text
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    
    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
sys.exit()
