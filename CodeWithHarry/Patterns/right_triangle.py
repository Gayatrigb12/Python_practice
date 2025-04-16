"""

 Enter a num : 4
   *
  **
 ***
****

"""

n = int(input(" Enter a num : "))

for i in range(1 , n+1): 
    print(" "*(n-i) , end="")
    print("*"* (i),end="")
    print("")
  