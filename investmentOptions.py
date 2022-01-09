#investment options library 


#Different types of homes suggestions according to the amount avaiable to invest, and in the area they can invest in, in Southern Ontario
def homes(investAmount):

    #For detached houses 
    if (investAmount >= 200000):

        #For Toronto
        if (investAmount >= 300000):
            print("You can invest in a detached house in Toronto with this amount: $ ", investAmount)
        
        #For GTA
        elif (investAmount >= 230000):
            print("You can invest in a detached house in GTA with this amount: $ ", investAmount)
        
        #For a small town in Southern Ontario
        elif (investAmount >=200000):
            print("You can invest in a detached house in a small town in Southern Ontario with this amount: $ ", investAmount)
    
    #Same as above but for semidetached houses 
    elif (investAmount >= 140000):
        if (investAmount >= 180000):
            print("You can invest in a semidetached house in Toronto with this amount: $ ", investAmount)
        
        elif (investAmount >= 160000):
            print("You can invest in a semidetached house in GTA with this amount: $ ", investAmount)
        
        elif (investAmount >= 140000):
            print("You can invest in a town house in a small city in Southern Ontario with this amount: $ ", investAmount)

    #For apartments 
    elif (investAmount >= 90000):
        if (investAmount >= 130000):
            print("You can invest in an apartment in Toronto with this amount: $ ", investAmount)
        
        elif (investAmount >= 110000):
            print("You can invest in an apartment house in GTA with this amount: $ ", investAmount)
        
        elif (investAmount >= 90000):
            print("You can invest in an apartment in a small town in Southern Ontario with this amount: $ ", investAmount)
    
    #If none of the above options 
    elif (investAmount < 90000):
        print("Sorry you cannot invest in a home according to the data we have. Please talk to a realtor if it is possible for you to invest in a home. This is the amount you have for your investment: $", investAmount)


#Different types of cars suggestions according to the amount available to invest
def cars(investAmount):
    
    #For expensive sports cars
    if (investAmount >= 50000):
        print("You can invest in an expensive sports car with this amount: $ ", investAmount)
    
    #For a brand new everyday car
    elif (investAmount >= 30000):
        print("You can invest in a brand new everyday car with this amount: $ ", investAmount)
        
    #For a second hand car
    elif (investAmount >= 10000):
        print("You can invest in a second hand car with this amount: $ ", investAmount)
    
    #If none of the above options 
    elif (investAmount < 10000):
        print("Sorry you cannot invest in a car according to the data we have. Please talk to a car dealer if it is possible for you to invest in a car. This is the amount you have for your investment: $", investAmount)


#Different types of office space suggestions according to the amount avaiable to invest, and in the area they can invest in, in Southern Ontario
def office(investAmount):
    
    #For an office building
    if (investAmount >= 24000):

        #For Toronto
        if (investAmount >= 50000):
            print("You can invest in an office building in Toronto with this amount: $ ", investAmount)
        
        #For GTA
        elif (investAmount >= 35000):
            print("You can invest in an office building in GTA with this amount: $ ", investAmount)
        
        #For a small town in Southern Ontario
        elif (investAmount >= 24000):
            print("You can invest in a office building in a small town in Southern Ontario with this amount: $ ", investAmount)

    #Same as above but for a office unit houses 
    elif (investAmount >= 10000):
        if (investAmount >= 20000):
            print("You can invest in a office unit in Toronto with this amount: $ ", investAmount)
        
        elif (investAmount >= 15000):
            print("You can invest in a office unit in GTA with this amount: $ ", investAmount)
        
        elif (investAmount >= 10000):
            print("You can invest in a office unit in a small town in Southern Ontario with this amount: $ ", investAmount)

    #For a desk space
    elif (investAmount >= 1000):
        if (investAmount >= 8000):
            print("You can invest in a desk space in Toronto with this amount: $ ", investAmount)
        
        elif (investAmount >= 5000):
            print("You can invest in a desk space in GTA with this amount: $ ", investAmount)
        
        elif (investAmount >= 1000):
            print("You can invest in a desk space in a small town in southern Ontario with this amount: $ ", investAmount)
    
    #If none of the above options 
    elif (investAmount < 1000):
        print("Sorry you cannot invest in an office according to the data we have. Please talk to a realtor if it is possible for you to invest in an office. This is the amount you have for your investment: $", investAmount)
    