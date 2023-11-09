import pygame
import grid_draw 


clock = pygame.time.Clock()
# Main game loop
running = True


##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Define grid parameters
######These are common parameters in grid_draw and main file:
# define twice, since I have find a way to add to other file:: 
grid_size = 60  # Size of each grid cell
grid_owner = [[0] * 10 for _ in range(10)] 
##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  

rect_posi=[]
   
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ## Call file grid_draw and then its function Draw_grid to to draw game grid  
    grid_draw.Draw_grid("Owner",0,0).draw_screen()
    
    all_circles=grid_draw.Draw_grid("",0,0).initiate_boat()
    

    if event.type == pygame.MOUSEBUTTONDOWN :  # Left mouse button is clicked
         
        mouse_x, mouse_y = event.pos
        rect_posi=[]
        for circle in all_circles:
            circle_x, circle_y = circle["position"]
            distance = ((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) ** 0.5
            if distance <= circle["radius"]:
               # grid_draw.Draw_grid("Owner",0,0)
                grid_draw.Draw_grid("Owner",all_circles.index(circle),0).locate_boat()
                print(all_circles.index(circle))
                pygame.display.flip()
                clock.tick(60)
          
        if event.type == pygame.MOUSEBUTTONDOWN:  # Left mouse button is clicked
            mouse_xr, mouse_yr = event.pos    
            grid_xr = (mouse_xr // grid_size)
            grid_yr = (mouse_yr // grid_size)-1
            if grid_xr<10 and grid_yr<10:
                rect_posi.append(grid_xr)
                rect_posi.append(grid_yr)
                #print(f"*****************{rect_posi}")
                grid_draw.Draw_grid(0,all_circles.index(circle),rect_posi).draw_boat()
                rect_posi=[]
                pygame.display.flip()
                   
pygame.quit()


