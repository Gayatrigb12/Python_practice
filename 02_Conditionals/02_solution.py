age = int(input("Enter your age: ")) # input the age of the user

day = input("Enter the day of the week: ").lower() # input the day of the week

price = 12 if age >= 18 else 8 # short hand if statement if more than 18 then 12 else 8

if day == "wenesday":
    # price = price-2 # if day is wenesday then price -2
    price -= 2 # short hand if statement if day is wenesday then price -2
    
print("Your ticket price is $",price) # print the price of the ticket