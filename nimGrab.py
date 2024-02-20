
import random
from tracemalloc import start 

print("Welcome to NIMGRAB!")
print()

print("By: Jacob Mashol")
print("[COM S 127 D")
print()

NUM_ITEMS_LOW = 4
NUM_ITEMS_HIGH = 8
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3

gameOver = False
currentTurn = 0 

while (gameOver == False) :
    start = input("[p]lay, [i]nstructions, or [q]uit?: ")
    if(start=="p"):
        print("Welcome to nimgrab lets play!")
        number_of_items = random.randint(NUM_ITEMS_LOW, NUM_ITEMS_HIGH)
        while (number_of_items>0):
            if (currentTurn ==0):
                print("It is the humans turn: ")
                counter1 = 0
                while(number_of_items > counter1):
                    print("|",end=" ")
                    counter1+=1
                print()
                take = int(input("How many items do you want to take? 1-3: "))
                if (take >= NUM_TO_TAKE_LOW and take <= NUM_TO_TAKE_HIGH):
                    print(" Human has taken {0} number of items".format(take))
                    number_of_items -= take        
                else:
                     print("Wrong input please input a number 1-3")
            
            elif (currentTurn == 1 ):
                 currentTurn = currentTurn //2 
                 print("It is the compiuters turn  turn!")
                 counter2 = 0
                 while(number_of_items > counter2):
                    print("|",end=" ")
                    counter2+=1
                    print()
                    takeaway2 = random.randint(NUM_ITEMS_LOW,NUM_TO_TAKE_HIGH)
                    if(number_of_items > 1):
                        while(takeaway2 > number_of_items):
                            takeaway2 = random.randint(NUM_ITEMS_LOW,NUM_ITEMS_HIGH)
                            print("Computer has taken {0} from the pool.".format(takeaway2))
                            number_of_items -= takeaway2
                    elif(number_of_items==1):
                        takeaway2 = 1
                        print("Computer has taken {0} from the pool.".format(takeaway2))
                        number_of_items -= takeaway2 
                 else: 
                    print("Wrong Input")
        

            if(currentTurn == 0):
                print("The computer has taken the last straw so human wins!!")
            else:
                    print("The human has taken the last straw so computer wins.")

    elif(start == "i"):
             print("The rules of the game are that the human and the computer each draw sticks from the pool")
             print("Each player could take between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH straws in total ")
             print("The game will keep going until the last straw is drawn, if human takes last straw you lose.")

       
    elif(start == "q"):
            gameOver == True 
            print("You quit you suck!!")
           
    else:
             print("wrong input, Enter [p]lay, [i]nstructions, or [q]uit. ")
