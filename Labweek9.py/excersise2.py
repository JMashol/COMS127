def calculatedistance(listname,listx,listy,currentlocation,currentlocationx,currentlocationy):
    lisdistances = [] 
    for i in range(len(listname)): 
        changeinx = currentlocationx - listx[i] 
        changeiny = currentlocationy - listy[i] 
        distance = pow(((changeinx**2 )+(changeiny**2)),.5)
        lisdistances.append(distance)
    mindistance = min(lisdistances)
    min_index = lisdistances.index(mindistance)
    name_min = listname[min_index] 
    print(listname)
    print(lisdistances)
    print("the distance between {0} and {1} is {2}".format(name_min,currentlocation,mindistance))

def main(listname,listx,listy):
    print("Enter \"*\" in the city name to stop the loop.")
    stoploop = True 
    while stoploop != False: 
        citynames = input("Enter a city namein romainia: ")
        if citynames == "*": 
            stoploop = False 
            currentlocation = input("Enter your current location: ")
            currentlocationx = int(input("Enter the x coordinate of {}: ".format(currentlocation)))
            currentlocationy = int(input("Enter the y coordinate of {}: ".format(currentlocation)))
        else:
            listname.append(citynames)
            y = int(input("Enter the x cord of {}: ".format(citynames)))
            listx.append(y)
            z = int(input("Enter the y cord of {}: ".format(citynames)))
            listy.append(z)
    calculatedistance(listname,listx,listy,currentlocation,currentlocationx,currentlocationy)


if __name__ == "__main__": 
    listname = [] 
    listx = [] 
    listy = [] 
    main(listname,listx,listy) 




