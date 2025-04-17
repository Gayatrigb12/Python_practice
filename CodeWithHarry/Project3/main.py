import random

n = random.randint(1, 101)
a = -1 
gusses = 0
while(a != n):
   
    a = int(input("Guess The number between (1 - 100) : "))
    if(a > n):
        print(" Lower Number Please !")
    else:
        print(" Higher number please !")
    gusses += 1
print(f"Correct !! you have correctly gussed number in {gusses} attempt !")