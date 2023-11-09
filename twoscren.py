import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 660, 660
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid in Pygame")

# Define grid parameters
######These are common parameters in grid_draw and main file:
# define twice, since I have find a way to add to other file:: 
grid_size = 60  # Size of each grid cell
grid_owner = [[0] * 10 for _ in range(10)] 

grid_color = (255, 255, 255)  # Color of the grid lines

# Create a 2D grid data structure to represent the grid
grid = [[0] * 10 for _ in range(10)]  # 10x10 grid initialized with zeros

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
            grid[grid_y-1][grid_x-1] = 1 - grid[grid_y-1][grid_x-1]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid and print the grid values
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, grid_color, (0, y), (width, y))

    # Draw colored rectangles based on grid values and print values
    font = pygame.font.Font(None, 36)
    for row in range(10):
        for col in range(10):
            rect = pygame.Rect(col * grid_size + 60, row * grid_size + 60, grid_size, grid_size)
            if grid[row][col] == 1:
                pygame.draw.rect(screen, (0, 255, 0), rect)
                text = font.render("1", True, (255, 255, 255))
            else:
                pygame.draw.rect(screen, (255, 0, 0), rect)
                text = font.render("0", True, (255, 255, 255))
            screen.blit(text, rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
