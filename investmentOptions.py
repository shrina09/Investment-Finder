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
    

#Different types of cars suggestions according to the amount avaiable to invest
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
            

#Different types of office space suggestions according to the amount avaiable to invest, and in the area they can invest in, in Southern Ontario
def office(investAmount):
    
    #For an office building
    if (investAmount >= 1):

        #For Toronto
        if (investAmount >= 2):
            print("You can invest in an office building in Toronto with this amount: $ ", investAmount)
        
        #For GTA
        elif (investAmount >= 3):
            print("You can invest in an office building in GTA with this amount: $ ", investAmount)
        
        #For a small town in Southern Ontario
        elif (investAmount >= 4):
            print("You can invest in a office building in a small town in Southern Ontario with this amount: $ ", investAmount)

    #Same as above but for a office unit houses 
    elif (investAmount >= 3):
        if (investAmount >= 2):
            print("You can invest in a office unit in Toronto with this amount: $ ", investAmount)
        
        elif (investAmount >= 3):
            print("You can invest in a office unit in GTA with this amount: $ ", investAmount)
        
        elif (investAmount >= 4):
            print("You can invest in a office unit in a small town in Southern Ontario with this amount: $ ", investAmount)

    #For a desk space
    elif (investAmount >= 3):
        if (investAmount >= 2):
            print("You can invest in a desk space in Toronto with this amount: $ ", investAmount)
        
        elif (investAmount >= 3):
            print("You can invest in a desk space in GTA with this amount: $ ", investAmount)
        
        elif (investAmount >= 4):
            print("You can invest in a desk space in a small town in southern Ontario with this amount: $ ", investAmount)
    

