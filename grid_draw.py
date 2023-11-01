import pygame
import string  # Import the string module

## Define boat array for future use
boat_array=["aircraft = A (5)", "battleship = B (4)", "Cruiser =C (3)",
        "Destroyer =D (4)", "Submarine =S (2)"]

width, height = 1320, 720  # Wider display to accommodate both grids side by side
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid in Pygame - Two Players")

# Initialize the font module
pygame.font.init()  
    

# Create a font for the labels
font = pygame.font.Font(None, 36)


grid_size = 60  # Size of each grid cell (adjust as needed)
grid_color1 = (255, 255, 0)  # Color of the grid lines
grid_color2 =(0,0,255)
# Define the divider between Player 1 and Player 2's grids
divider_x = width // 2  # The x-coordinate where the divider should be drawn

# Define the labels for the rows and columns
labels = list(string.ascii_uppercase[:10])  # A, B, C, ..., J for columns
numbers = list(range(1, 11))  # 1, 2, 3, ..., 10 for rows


    # Clear the screen
screen.fill((0, 0, 0))



class Draw_grid():
    
    def __init__(self,user) -> None:
        self.user=user
    
    def draw_screen(self):
        if self.user=="Owner":
            position_info=[10,"OWN SIDE",70,10,275,350 ]
            
        if self.user=="Enemy":
            position_info=[700,"ENEMY SIDE",730,670,950,1020]
        
        # Add text to show grid names : Own Map or enemy Map
        text = font.render(position_info[1], True, (255, 255, 255))
        screen.blit(text, (position_info[0],10))  # Adjust the position
     
        if self.user=="Owner": 
         # Draw the grid for Player 1 on the left side
            for x in range(0, divider_x, grid_size):
                pygame.draw.line(screen, grid_color1, (x, 70), (x, height))
            for y in range(0, height, grid_size):
                pygame.draw.line(screen, grid_color1, (0, y), (divider_x, y))
        
        if self.user=="Enemy":
        # Draw the grid for Player 2 on the right side
            for x in range(divider_x, width, grid_size):
                pygame.draw.line(screen, grid_color2, (x, 70), (x, height))
            for y in range(0, height, grid_size):
                pygame.draw.line(screen, grid_color2, (divider_x, y), (width, y))
        
        
            
        for i, label in enumerate(labels):
            text = font.render(label, True, (255, 255, 255))
            screen.blit(text, (i * (grid_size) + position_info[2], 80))  # labeling own grid with A, B, C.....
          
        for i, number in enumerate(numbers):
            text = font.render(str(number), True, (255, 255, 255))
            screen.blit(text, (position_info[3], i * (grid_size) + 140))  # labeling own grid 1,2,3---
                  
        text = font.render("Hit Info", True, (255, 255, 255))
        screen.blit(text, (position_info[4],20))  # Adjust the position : for enemy map
         
        for i in range(1,6):
            # for own map
            y =position_info[5]+ i*50
            circle = {'position': (y,30), 'radius': 20}
            pygame.draw.circle(screen, (255, 255, 255), circle['position'], circle['radius'])    
        
                # Draw the divider line to seperate own map and enemy map
        pygame.draw.line(screen, (0,255,0), (divider_x, 0), (divider_x, height))

        # Update the display
        pygame.display.flip()
        
    def locate_boat(self):
        """ 
        aircraft = A (5)
        battleship = B (4)
        Cruiser =C (3)
        Destroyer =D (4)
        Submarine =S (2)
        """
        font = pygame.font.Font(None, 30)
        text = font.render("Select boat and locate it in your board as you prefer", True, (255, 255, 255))
        screen.blit(text, (700,140))  # Adjust the position
        text = font.render("You can place either horizontally or vertically.Diagonal placement is not allowed.", True, (255, 255, 255))
        screen.blit(text, (700,180))  # Adjust the position
        text = font.render("Diagonal placement is not allowed.", True, (255, 255, 255))
        screen.blit(text, (700,220))  # Adjust the position
        circles=[]
        for i in range(1,6):
            y =250+ i*50
            text = font.render(boat_array[i-1], True, (255, 255, 255))
            screen.blit(text, (880,y))  # Adjust the position
            circle = {'position': (850,y), 'radius': 20}
            circles.append(circle)
            pygame.draw.circle(screen, (255, 255, 255), circle['position'], circle['radius'])    
        return circles
    
    
 
#This is to locate boat positions ::: 



