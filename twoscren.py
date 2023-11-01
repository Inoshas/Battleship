import pygame

# Initialize Pygame
pygame.init()

# Define the main screen dimensions
main_screen_width, main_screen_height = 800, 600

# Create the main screen
main_screen = pygame.display.set_mode((main_screen_width, main_screen_height))
pygame.display.set_caption("Main Screen")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Define the pop-up screen dimensions
popup_screen_width, popup_screen_height = 400, 300

# Variable to control if the pop-up screen is visible
popup_visible = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Press 'P' to toggle pop-up
                popup_visible = not popup_visible

    # Fill the main screen with a color
    main_screen.fill((255, 255, 255))

    # Draw something on the main screen
    pygame.draw.rect(main_screen, (0, 0, 255), (100, 100, 200, 200))

    if popup_visible:
        # Fill the pop-up screen with a different color
        popup_surface = pygame.Surface((popup_screen_width, popup_screen_height))
        popup_surface.fill((255, 0, 0))

        # Draw something on the pop-up screen
        pygame.draw.rect(popup_surface, (0, 255, 0), (50, 50, 100, 100))

        # Blit the pop-up screen onto the main screen
        main_screen.blit(popup_surface, (main_screen_width // 2 - popup_screen_width // 2, main_screen_height // 2 - popup_screen_height // 2))

    # Update the main display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
