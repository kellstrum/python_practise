import pygame
import sys

# Start
pygame.init()

# Screen size
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Title
pygame.display.set_caption("Game Window")

# Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close

            sys.exit() # Exits
    
    # Fill screen with dark gray
    screen.fill((30, 30, 30))

    # Update the screen
    pygame.display.flip()
