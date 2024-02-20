
# <Jacob Mashol>             <11/28/2022>
# Assignment #6 Naval Battle

import gameBoard
import gamePlay
import random

def main():
    """This is the main function of the game. It controls the flow/ execution of the entire script.
    """
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
    
    numHumanTargets = 0
    numComputerTargets = 0
    
    print("Welcome to Naval Battle!")
    print()
    
    print("By: <Jacob Mashol>")
    print("[COM S 127 <D>]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 
            

            
            gameboardChoice = gameBoard.chooseHumanGameBoard()
            
            humanGameBoard,numHumanTargets = gameBoard.loadGameBoard(gameboardChoice)
            
            gameboardChoice = gameBoard.chooseComputerGameBoard()
            
            computerGameBoard,numComputerTargets = gameBoard.loadGameBoard(gameboardChoice)
            
            targetBoard = gameBoard.loadTargetBoard()
            
            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)
        elif choice == "i":
            print("welcome to battleships!")
            print()
            print("enter your coordances to attack enemy")
            print("If you hit a battleship it will say hit if you miss it will say miss")
            print("sink all enemy battleships to win and if your battleships are sunk you lose")

            
        elif choice == "q":
            gameOver = True 
            print("goodbye!")
            
           
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()