#Jacob Mashol   09/14/2022
#Lab Week 4     Excerise2




a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if(y == a*x*2 + b*x + c):
    print("The point 9{0},{1}) lies on the parabola y = {2}*x**2 + {3}*x +{4}".format(x,y,a,b,c)) 
else: 
    print("The point 9{0},{1}) doesn't lie on the parabola y = {2}*x**2 + {3}*x +{4}".format(x,y,a,b,c)) 
