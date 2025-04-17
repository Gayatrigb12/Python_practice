try:
    a = int(input("Enter a number : "))
    print(a)
    
except Exception as e:
    print(e)    

else:  
    print("thank you")
#  else will execute only when try is success full

    
"""
output 
--CASE 1 --
PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter12> python try_else.py
Enter a number : 0
0
thank you


--CASE 1 --

PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter12> python try_else.py
Enter a number : g
invalid literal for int() with base 10: 'g'
"""