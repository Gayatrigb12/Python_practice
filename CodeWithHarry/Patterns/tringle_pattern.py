"""
    *
   ***
  *****
"""



n = int(input(" Enter a num : "))

for i in range(1 , n+1): 
  print(" "*(n-i) , end= "")
  print("*"* (2*i-1),end="")
  print("")
  
  
  """
  first iteration 
  i=1 
  n=3
  n-i = 2   tWo spaces __
  2*i-1 = 2 * 1 -1 = 1  one star *
  
   second iteration 
  i=2
  n=3
  n-i = 1   one spaces _
  2*i-1 = 2 * 2 -1 = 3  three star ***
  
   Third iteration 
  i=3
  n=3
  n-i = 0  no spaces 
  2*i-1 = 2 * 3 -1 = 5  five star *******
  
  
  
  
  i= 1   __*
  i= 2   _***
  i= 3   *****
  
  """
  
