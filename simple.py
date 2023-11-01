# Two grids need 10*10 : 
#1. own map : required boat name and positions:::
#2.enemy map: required hit position and destro details::

import numpy as np

player_matrix = np.zeros((3, 3), dtype=str)
opponent_matrix = np.zeros((3, 3), dtype=str)




#This class has few functions
    # fix_boats ::: Setup the boats as you wish
    # Mark_myhits :::: Mark hits depend on guesses
    # Mark_oponent ::: Mark details given by opponen 
    
class Fix_position:
    def __init__(self, boat_number, length, direction, initial_coordinate) -> None:
        self.length = length
        self.direction = direction
        self.initial_coordinate = initial_coordinate
        self.boat_number=boat_number

    def fix_boats(self):
        first = int(self.initial_coordinate[0])
        second = int(self.initial_coordinate[2])
        player_matrix[first][second] = self.boat_number
        
        ##################################33
        ## Here we need to handle error of over lapping::::: 
        #To avoid user errors
        ###################################
        if (self.direction.upper()=="V"):
            for i in range(self.length):
                player_matrix[first+i][second] = self.boat_number
        if (self.direction.upper()=="H"):
            for i in range(self.length):
                player_matrix[first][second+i] = self.boat_number
      
      ## This need to find which boat hits based on opponent's guesses and record them...          
    def mark_myhits():
        pass
    
        ## This mark the hits and if player guess correctly, need to record based on opponents reply::
    def mark_opponenet():
        pass

guesses = []


        
for item in range(1, 6):
    boat_number=item
    length = int(input("Give boat length:"))
    direction = input("Give setup direction (H for horizontal, V for vertical): ")
    initial_coordinate = input("Give initial coordinate (e.g., '1,2'): ")
    fix = Fix_position(boat_number,length, direction, initial_coordinate)
    fix.fix_boats() 
    guesses.append(fix)
    print(player_matrix)
    print("Now your board is ready")
    status=input("Do you want to change your setup(Y/N)")
    
    ## Error handling :: Change setup goes here:::::::
    ##if status.upper()=="Y":
       ##

    #if status.upper()=="N":
    #Continue......
    ##################
    
    print("Board is ready and now game begins")

#We need to switch between grids:
    player1=input("Player name 1:")    
    player2=input("Player name 2:")  
    player=int(input("Are you player 1 or 2:"))
    ''' 
    if player==1:
        guess=input(print("You start: Guess opponent hit"))
        if opponent_matrix
        opponent_matrix = np.zeros((10, 10))
      '''  
    
    


### 
