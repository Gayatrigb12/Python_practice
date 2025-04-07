# prime 
num = int(input("Enter a number: "))
count = 0
if num == 1:
    print(num, "is not a prime number")
for i in range(2, num // 2):
    if num % i == 0:
        count += 1
        break

if count == 0:
    print(num, "is a prime number")
else: 
    print(num, "is not a prime number")