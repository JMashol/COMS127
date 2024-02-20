#  Jacob Mashol          10-10-2022
#  Lab Week 8 - Exercise #3

def swap(a, b):
   #swap a and b
   return a,b
x = int(input("Enter an interger: "))
y = int(input("Enter an interger: "))
x, y = swap(x,y)
a = y
y = x
x = a  


print(x,y)
