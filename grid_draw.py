import pygame
import string  # Import the string module

## Define boat array for future use
boat_array=["aircraft = A (5)", "battleship = B (4)", "Cruiser =C (3)",
        "Destroyer =D (4)", "Submarine =S (2)"]
symbol_array=["A","B","C","D","S"]
circle=[]
# Create a 2D grid data structure to represent the grid


width, height = 1320, 720  # Wider display to accommodate both grids side by side
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid in Pygame - Two Players")

# Initialize the font module
pygame.font.init()  
    

# Create a font for the labels
font = pygame.font.Font(None, 36)

# 10x10 grid initialized with zeros
grid_owner = [[0] * 10 for _ in range(10)] 
grid_enemy = [[0] * 10 for _ in range(10)] 
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


circles=[]

class Draw_grid():
    
    def __init__(self,user,circle_index,rect_posi) -> None:
        self.user=user
        self.circle_index=circle_index
        self.rect_posi=rect_posi
       # self.circle=circle
    
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
        
    def initiate_boat(self):
        """ 
        aircraft = A (5)
        battleship = B (4)
        Cruiser =C (3)
        Destroyer =D (4)
        Submarine =S (2)
        """
        
        ### Drawing the checklist to select the boats and place them::
        font = pygame.font.Font(None, 30)
        text = font.render("Select boat and locate it in your board as you prefer", True, (255, 255, 255))
        screen.blit(text, (700,140))  # Adjust the position
        text = font.render("You can place either horizontally or vertically.", True, (255, 255, 255))
        screen.blit(text, (700,180))  # Adjust the position
        text = font.render("Diagonal placement is not allowed.", True, (255, 255, 255))
        screen.blit(text, (700,220))  # Adjust the position
       
        for i in range(1,6):
            y =250+ i*50
            text = font.render(boat_array[i-1], True, (255, 255, 255))
            screen.blit(text, (880,y))  # Adjust the position
            circle = {'position': (850,y), 'radius': 20}
            circles.append(circle)
            pygame.draw.circle(screen, (255, 255, 255), circle['position'], circle['radius'])    
        
        
        ## Draw a button to start the game after place boats:::
        button_color = (0, 128, 255)  # Blue
        button_rect = pygame.Rect(900, 600, 150, 50)  # (x, y, width, height)
        button_text = "Start Game"
        font = pygame.font.Font(None, 36)
        text = font.render(button_text, True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=button_rect.center)
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(text, text_rect)
        
        return circles
 
    def locate_boat(self):
        circle=circles[self.circle_index]
        pygame.draw.circle(screen, (255, 0, 0), circle['position'], circle['radius']) 
        #self.rect_posi[0], self.rect_posi[1]  
    
    def draw_boat(self):
        #circle=circles[self.circle_index]
        rect = pygame.Rect(self.rect_posi[0] * grid_size , self.rect_posi[1] * grid_size+60 , grid_size, grid_size)
        print(f"{self.rect_posi[0]} , {self.rect_posi[1]}")
        pygame.draw.rect(screen, (0, 255, 0), rect)
        text = font.render(symbol_array[self.circle_index], True, (255, 255, 255))
        screen.blit(text, rect.topleft)
        
        ''' 
        for row in range(10):
            for col in range(10):
                
                rect = pygame.Rect(col * grid_size + 60, row * grid_size + 120, grid_size, grid_size)
                if grid_owner[row][col] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), rect)
                    text = font.render("1", True, (255, 255, 255))
                else:
                    pygame.draw.rect(screen, (255, 0, 0), rect)
                    text = font.render("0", True, (255, 255, 255))
                screen.blit(text, rect.topleft)
        '''
  
 
#This is to locate boat positions ::: 




