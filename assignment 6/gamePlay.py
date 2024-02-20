# Jacob Mashol           8-11-2022
# Assignment #6 Naval Battle

import gameBoard
import gameInput

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):
    """This function controls what happens when it is the human's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numComputerTargets (int): The number of computer targets remaining.
    
    Returns:
        list of lists, list of lists, list of lists, int: All of the relevant gameboards and the number of computer targets remaining.
    """
    
    print("Human Turn")
    gameBoard.printBoard(targetBoard,len(targetBoard[0]),len(targetBoard))
    print()
    gameBoard.printBoard(humanGameBoard,len(humanGameBoard[0]),len(humanGameBoard))
    print
    
    row,col= gameInput.getHumanInput()
    while targetBoard[row][col] == "X" or targetBoard[row][col] == "O":
        print("Input different coordinates")
        row,col = gameInput.getHumanInput()   
    
    # Print out the coordinates the human is targeting.
    print(" Human target is {0},{1}".format(row,col))

    
    if computerGameBoard[row][col] == "@":
        print("HIT")
        targetBoard[row][col] = "X"
        computerGameBoard[row][col] = "X"

        numComputerTargets -= 1
    else:
        computerGameBoard[row][col] = "O"
        print("MISS")
        targetBoard[row][col] = "O" 

    
    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

def _computerTurn(humanGameBoard, numHumanTargets):
    """This function controls what happens when it is the computer's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets remaining.
    
    Returns:
        list of lists, int: All of the relevant gameboards and the number of human targets remaining.
    """
    # TODO: Complete the logic below so that the computer can take a turn attacking the human. (1 pt.)

    print("It is now the computers turn")
    row,col= gameInput.getComputerInput()
    while humanGameBoard[row][col] == "X" or humanGameBoard [row][col] == "O":
        row,col = gameInput.getComputerInput()

    # Call gameInput.getComputerInput() to get input for where to attack (row and column).
    # Do input validation to make sure that the row/ column on the humanGameBoard is not already 'X' or 'O'
    # if it is, get new input.
    
    # Print out the coordinates the computer is targeting.
    print("computer target is {0},{1}".format(row,col))
    if humanGameBoard[row][col] == "@":
        print("HIT")
        humanGameBoard[row][col] = "X"

        numHumanTargets -= 1
    else:
        humanGameBoard[row][col] = "O"
        print("MISS") 

  
    
    return humanGameBoard, numHumanTargets

def _printWinner(numComputerTargets, computerGameBoard):
    """This function prints out which player has won the game, depending on the numComputerTargets remaining.

    Args:
        numComputerTargets (int): The number of computer targets left. If there are none, the human wins. Else - the computer wins.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.
    """
    
    if numComputerTargets == 0:
        print("The human has won")
    else:
        print("The computer has won")
  
    
    gameBoard.printBoard(computerGameBoard,len(computerGameBoard[0]),len(computerGameBoard))
    
   
    

    return

def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    """This function controls the flow of the game and switches turns between the human and the computer.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets left.

        numComputerTargets (int): The number of computer targets left.
    """
    currentTurn = 0 


    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        
        currentTurn += 1
        currentTurn %= 2
    
    
    _printWinner(numComputerTargets, computerGameBoard)

    return