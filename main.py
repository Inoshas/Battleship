import pygame
import grid_draw 

# Main game loop
running = True
   
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ## Call file grid_draw and then its function Draw_grid to to draw game grid  
    grid_draw.Draw_grid("Owner").draw_screen()
    all_circles=grid_draw.Draw_grid("").locate_boat()

     
    #grid_draw.Draw_grid("Enemy").draw_screen()
""
    #popup_process = multiprocessing.Process(target=grid_draw.Pop_up_window())
    
    
    
'''
    # Check for mouse input
    if pygame.mouse.get_pressed()[0]:  # Left mouse button is clicked
        mouse_x, mouse_y = pygame.mouse.get_pos()
        distance = ((mouse_x - circle_position[0])**2 + (mouse_y - circle_position[1])**2)**0.5
        if distance <= circle_radius:
            print("Mouse is inside the circle")
    
 
'''  
    
    
# Quit Pygame
pygame.quit()


