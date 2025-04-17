a = int(input("enter num 1 : "))
b = int(input("enter num 2 : "))

if(b == 0):
    raise ZeroDivisionError("Hey our prog is not made with divide zero")
else:
    print(f"the division (a/b) is {a/b}")

"""
Output :

python raising_exception.py
enter num 1 : 4
enter num 2 : 0
Traceback (most recent call last):
  File "D:\PYTHON\Python_practice\CodeWithHarry\Chapter12\raising_exception.py", line 5, in <module>  
    raise ZeroDivisionError("Hey our prog is not made with divide zero")
ZeroDivisionError: Hey our prog is not made with divide zero

"""