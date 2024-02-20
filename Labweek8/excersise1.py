#  Jacob Mashol          10-10-2022
#  Lab Week 8 - Exercise #1
# def mulply(): 
#     num1 = int(input("Enter number: "))
#     num2 = int(input("Enter number: "))



def multiplication(a,b):
    c = 0 
    if b > 0: 
        for i in range(b):
            c+=a
        return c 
    elif b == 0:
        for i in range(0,b,-1):
            c-=a 
        return c 

x = int(input("Enter a integer: "))
y = int(input("Enter a integer: "))
c = multiplication(x,y)
print("The product of {} and {} is {},".format(x,y,c))