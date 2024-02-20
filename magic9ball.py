
# Jacob Mashol             09/16/2022
# Assignment2
import math

print("Welcome to the Magic 9 Ball...")
print()
print("By: Jacob Mashol")
print("[COM S 127 <section>]")
print()
print("What would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")
print() 

if choice == "c":
    choiceC = input("Choose one of these calculations: [+], [-], [*], [/], [%], [**]")
   
    if(choiceC == "+" or choiceC == "-" or choiceC =="*" or choiceC == "/" or choiceC == "%" or choiceC == "**"): 
       
        if (choiceC == "+"):
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            answer = (x + y)
            print("The answer is", answer) 
        elif (choiceC == "-"):
             x = float(input("Enter value of x: "))
             y = float(input("Enter value of y: "))
             answer = (x - y)
             print("The answer is", answer) 
        elif (choiceC == "*"):
             x = float(input("Enter value of x: "))
             y = float(input("Enter value of y: "))
             answer = (x * y)
             print("The answer is", answer) 
        elif (choiceC == "/"):
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            answer = (x / y) 
            print("The answer is", answer) 
        elif (choiceC == "%"):
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            answer = (x % y) 
            print("The answer is", answer) 
        elif (choiceC == "**"):
            x = float("Enter value of x: ")
            y = float("Enter value of y: ")
            answer = (x ** y) 
            print("The answer is", answer) 





    
    

if choice == "p":
    print("You chose prediction !")
    question = input("What is your question for the magic 9 ball ?")
    length = len(question)
    prediction = length % 10 

    if prediction == 0: 
        print("I highly doubt it")
    elif prediction == 1: 
        print("probably not lol")
    elif prediction == 2: 
        print("To be honest yes")
    elif prediction == 3: 
        print("most likely")
    elif prediction == 4: 
        print("funny joke")
    elif prediction == 5: 
        print("why would you even ask that")
    elif prediction == 6: 
        print("of course")
    elif prediction == 7: 
        print("heck yeah!")
    elif prediction == 8: 
        print("duh")
    elif prediction == 9: 
         print("idk ask again")


if choice == "q":
    print("You quit loser")
else:
    print("error") 