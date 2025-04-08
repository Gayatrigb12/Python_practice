num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def add(num1 , num2):
    sum = num1 * num2
    return sum

print(f"Multiplication of {num1} and {num2} is {add(num1, num2)}")