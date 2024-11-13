
import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aiming System Example")

# Player properties
player_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
player_radius = 20

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the angle to the mouse position
    dx, dy = mouse_x - player_pos[0], mouse_y - player_pos[1]
    angle = math.atan2(dy, dx)  # Calculate angle in radians

    # Draw the player
    pygame.draw.circle(screen, BLUE, player_pos, player_radius)

    # Draw a line to indicate the aiming direction
    aim_length = 50  # Length of the aiming line
    aim_x = player_pos[0] + aim_length * math.cos(angle)
    aim_y = player_pos[1] + aim_length * math.sin(angle)
    pygame.draw.line(screen, RED, player_pos, (aim_x, aim_y), 3)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
