#Jacob Mashol   09/14/2022
#Lab Week 4     Excerise1

length = int(input("Enter the value of the length: "))
height = int(input("Enter the value of the height: "))
perimeter = 2 * (length + height)

if (length == height):
    print("The rectangle is a square with a perimeter of {0}".format(perimeter))
else:
     print("The rectangle is not a square with a perimeter of {0}".format(perimeter))