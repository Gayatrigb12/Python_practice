"""
Enter a num : 4
4 X 10  = 40
4 X 9  = 36
4 X 8  = 32
4 X 7  = 28
4 X 6  = 24
4 X 5  = 20
4 X 4  = 16
4 X 3  = 12
4 X 2  = 8
4 X 1  = 4

"""
n = int(input(" Enter a num : "))

for i in range(1 , 11): 
    print(f"{n} X {11-i}  = {n*(11-i)}")