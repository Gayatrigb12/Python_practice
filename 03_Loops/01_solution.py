# numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Numbers:", numbers)

count = 0
for number in numbers:
    if number > 0:
        count += 1
print("Count of positive numbers:", count)
print ("Count of negative numbers:", len(numbers) - count)