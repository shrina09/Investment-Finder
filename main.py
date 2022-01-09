#Investment finder
#Shrina Patel, University of Guelph
#Kailey MacDonell, University of Guelph 

#Importing the investment options library to generate the the investments the user can invest in 
import investmentOptions


#Welcome message
print("Hi! I am Fiance chip. I can help you find your next big investment in Southern Ontario! Let's get started.\n")


#User Input for their yearly income, expenses and their savings to calculate the amount the user can use to invest in
print("For all of the the amounts asked for below, please enter without any spaces or commas")
yearlyIncome = int(input("What is your yearly income?"))

yearlyExpenses = int(input("What is the approximate amount of your yearly expenses?"))

yearlySavings = int(input("What amount do you wish to save yearly? *Note that savings amount will not be counted to suggest investments: "))

savingsAlready = int(input("If you have any other savings and would like me to consider that amount while finding out the amount available for you invest, please enter it here: "))

#Calculates the amount the user has that they can use to invest
def calculateAmountLeftForInvestment(yearlyIncome, yearlyExpenses, YearlySavings):
    #Calculates the total amount of money the user can invest in
    totalAmountInvest = savingsAlready + (yearlyIncome - (yearlyExpenses + yearlySavings))

    return totalAmountInvest


#Calling the function to know the amount avialable for investing 
totalInvestAmount = calculateAmountLeftForInvestment(yearlyIncome, yearlyExpenses, yearlySavings)


#Giving them options or suggestions according to what to the amount the user has that the user can invest in
if (totalInvestAmount <= 10000):
  print("Since your available amount is", totalInvestAmount, ", which is below 10,000. We recommend not to make an investment just yet. \nTips to increase the investment amount avilable:\n1. Watch your expenses, there could be some that are not neccessary.\n2. You can invest in other options that do not require such a high amount to invest. Stock market or mutual funds are good options.\n*These are subject to market risks please invest at your own risk, Finance chip is not responsible for any decision or investment made in the stock market or mutual funds.\n3. You can talk to a finicial advisor at your bank for help or more information on making investments")

elif (totalInvestAmount >= 10000): 
    userOption = input("What would you like to invest in from the options below:\nHomes, Office, Cars, or Other (*please spell exactly as given): ")

    whatInvestment = (userOption.lower())
    
    if (whatInvestment == "homes"): 
        if (totalInvestAmount < 90000):
            print("Sorry the amount for you to invest is ", totalInvestAmount," this is not an enough amount for you to invest in a home in Southern Ontario. The minimum amount needed for a downpayment for any kind of home in this region is $90,000. Sorry for that!")

        elif (totalInvestAmount >= 90000): 
            investmentOptions.homes(totalInvestAmount)
    
    elif (whatInvestment == "cars"): 
        if (totalInvestAmount < 10000):
            print("Sorry the amount for you to invest is ", totalInvestAmount," this is not an enough amount for you to invest in a car. Sorry for that!")

        elif (totalInvestAmount >= 10000): 
            investmentOptions.cars(totalInvestAmount)
    
    elif (whatInvestment == "office"): 
        if (totalInvestAmount < 90000):
            print("Sorry the amount for you to invest is ", totalInvestAmount," this is not an enough amount for you to invest in a home in Southern Ontario. The minimum amount needed for a downpayment for any kind of home in this region is $90,000. Sorry for that!")

        elif (totalInvestAmount >= 90000): 
            investmentOptions.office(totalInvestAmount)

    elif (whatInvestment == "other"): 
        print("You have", totalInvestAmount, "to invest in other options, we recomend speaking to your financial advisor for more help.")
    
    else: 
        print("Sorry I cannot match any of the options to what you typed in my system please rerun the program")
        
    
