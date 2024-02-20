#Jacob Mashol   09/14/2022
#Lab Week 4     Excerise4
import math 

m1 = float(input("Enter the value of m1: "))

m2 = float(input("Enter the value of m2: "))
 
angle = math.atan(m1-m2)/(1+m1*m2)
angle_1 = angle = 180/math.pi 

if(m1==m2):
    print("the lines with the slope m1 {0} and m2 {1} are parallel".format(m1,m2))
elif(angle_1 ==90):
    print("the lines with the slope m1 {0} and m2 {1} are purpendicular".format(m1,m2))
else:
    print("The degree between the slope m1: {0} and m2: {1} is {2}".format(m1,m2,angle_1))