import string  # Import the string module
import pygame
# Initialize Pygame
pygame.init()

# Set up the display
width_1, height_1 = 1400,700 # Wider display to accommodate both grids side by side
screen = pygame.display.set_mode((width_1, height_1))
pygame.display.set_caption("Grid in Pygame - Two Players")

width, height= 1320, 660
# Define grid parameters
grid_size = 60
grid_color = (255, 255, 255)

# Create a 2D grid data structure to represent the grid
grid_1 = [[0] * (10) for _ in range(10)] #Player 1 setup
grid_2 = [[0] * (10) for _ in range(10)] # guesses for opponent:

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x = x // grid_size
            grid_y = y // grid_size
            # Toggle the state of the grid cell (mark/unmark)
            grid_1[grid_y][grid_x] = 1 - grid_1[grid_y][grid_x]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, grid_color, (0, y), (width, y))

    # Draw marked cells
    for y, row in enumerate(grid_1):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (0, 0, 255), (x * grid_size, y * grid_size, grid_size, grid_size))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
