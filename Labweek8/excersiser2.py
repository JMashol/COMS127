# # Jacob Mashol          10-10-2022
# # Lab Week 8 - Exercise #2\

from re import X
from tkinter import Y


def numbers(a,b,c):
    if x > y and y > z:
        max = x 
        med = y 
        min = z 
        c = (min,med,max)
        return c 
    elif x > y and y > z:
        max = x 
        med = y 
        min = z 
        c = (min,med,max)
        return c 
    elif x > y and z > y:
        max = x 
        med = z 
        min = y 
        c = (min,med,max)
        return c
    elif y > x and x > z:
        max = y 
        med = x
        min = z 
        c = (min,med,max)
        return c 
    elif y > x and z > x:
        max = y 
        med = z 
        min = x 
        c = (min,med,max)
        return c 
    elif z > x and z > y:
        max = z 
        med = x 
        min = y 
        c = (min,med,max)
        return c 
    elif z > x and y > x:
        max = z 
        med = y 
        min = x 
        c = (min,med,max)
    elif x == y and y == z:
        c = (x,y,z)
        return c
    elif x == y and y > z:
        max1 = y 
        max2 = x 
        min = z 
        c = (min,max1,max2)
        return c
    elif x == y and z > y :
        max = z
        min1 = x 
        min2 = y 
        c = (min1,min2,max)
        return c
    elif z == x and z > y: 
        max1 = z 
        max2 = x 
        min = y 
        c = (min,max1,max2)
        return c 
    elif z == x and z > y: 
        max = y 
        min1 = z 
        min2 = x 
        c = (min1,min2,max)
        return c 
    elif z == y and z > x:
        max1 = x 
        max2 = y 
        min = x 
        c = (min,max1,max2)
        return c 
    elif z == y and x >z:
        max = x 
        min1 = z 
        min2 = y 
        return c 


x = int(input("Enter a integer:"))
y = int(input("Enter a integer:"))
z = int(input("Enter a integer:"))
c = (x,y,z)
c = numbers(x,y,z)
print("the sorting values are",c)

