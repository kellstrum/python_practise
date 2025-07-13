import pygame
import random

# Iniitialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Font for displaying score
font = pygame.font.Font(None, 36)

# Set the window title
pygame.display.set_caption("Dodge the Falling Blocks")

# Control game speed
clock = pygame.time.Clock()

# Player properties
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Block properties
block_width = 50
block_height = 50
block_speed = 5

# List to store blocks
blocks = []

# Score
score = 0

# Block spawn timer 
spawn_timer = 0
spawn_delay = 60

game_over = False

# Main game loop
running = True 
while running: 
    clock.tick(60) # Run at 60 frames per second

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Fill screen with black
    screen.fill((0, 0, 0))
    
    # Spawn a new block every second
    spawn_timer += 1
    if spawn_timer >= spawn_delay:
        new_block_x = random.randint(0, screen_width - block_width)
        new_block_y = -block_height
        blocks.append([new_block_x, new_block_y])
        spawn_timer = 0
    
    # Move and draw all blcks
    new_blocks = []
    for block in blocks:
        block[1] += block_speed

        if block[1] <= screen_height:
            new_blocks.append(block)
        else:
            score += 1

        # Draw block
        pygame.draw.rect(screen, (255, 0, 0), (block[0], block[1], block_width, block_height))

    # Check for collision 
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        block_rect = pygame.Rect(block[0], block[1], block_width, block_height)
        if player_rect.colliderect(block_rect):
            game_over = True 
    
    blocks = new_blocks
    
    # Draw the player
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))
    
    # Show score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
        
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2))

        pygame.display.flip()

        pygame.time.delay(10000)
        running = False
    
    # Update the screen
    pygame.display.flip()