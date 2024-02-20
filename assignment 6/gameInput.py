# Jacob Mashol             8-11-2022
# Assignment #6 Naval Battle

import random
import gameBoard

def getHumanInput():
    """This function takes in input from the human for wich row and column they want to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the human to attack.
    """
    
    while True:    
        try:
            row = int(input("enter attack row (0-9): "))
            if not(row >= 0 and row < gameBoard.GAME_BOARD_HEIGHT -1):
                print('invalid input enter another number')  
            else:
                break       
        except:
            print('invalid input enter a number')




    
    while True:    
        try:
            col = int(input("enter attack col (0-9): "))
            if not(col >= 0 and col < gameBoard.GAME_BOARD_HEIGHT -1):
                print('invalid input enter another number') 
            else: break         
        except:
            print('invalid input enter a number')

    
    return row, col

def getComputerInput():
    """This function randomly generates input from the computer for which row and column it wants to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the computer to attack.
    """

    row = random.randint(0,gameBoard.GAME_BOARD_WIDTH-1)
    
    col = random.randint(0,gameBoard.GAME_BOARD_WIDTH - 1)

    return row, col