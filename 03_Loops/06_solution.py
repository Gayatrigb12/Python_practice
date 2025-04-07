# factors
num = int(input("Enter a number: "))
factorial = 1 # Initialize factorial to 1

while num > 0:#condition to check if num is greater than 0
    factorial *= num 
    num -= 1 # Decrement num by 1 in each iteration
print("Factorial:", factorial)