#Jacob Mashol   09/14/2022
#Lab Week 4     Excerise3

x1 = int(input("Enter the value for x1: "))
x2 = int(input("Enter the value for x2: "))
y1 = int(input("Enter the value for y1: "))
y2= int(input("Enter the value for y2: "))

if(x2-x1 ==0):
    print("The line describe by ({0},{1}) and ({2},{3}) is vertical".format(x1,y1,x2,y2))
elif(y2-y1 ==0):
    print("The line describe by ({0},{1}) and ({2},{3}) is horizontal".format(x1,y1,x2,y2))
else:
    slope = (y2-y1)/(x2-x1)
    print("The slope describe by ({0},{1}) and ({2},{3}) is {4}".format(x1,y1,x2,y2,slope))