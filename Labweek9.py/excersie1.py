#Jacob Mashol   10-18-2022
#lab week 9
import random 

def check(a,b): 
    randomNum = [] 
    randomMultipuleofB = [] 
    for i in range (b): 

        randomList = random.randint(a,a+b)
        randomNum.append(randomList)
        if randomNum[i] % b == 0: 
             randomMultipuleofB.append(randomList)

    print(randomNum)
    return randomMultipuleofB



a = int(input("Enter an Interger: "))
b = int(input("Enter an interger: "))

while a<0 and b<0: 
    print("Enter positive interger: ")
    a = int("Enter an interger:  ")
    b = int("Enter a interger: ")
randomMultipuleofB = check(a,b)
print(randomMultipuleofB)
