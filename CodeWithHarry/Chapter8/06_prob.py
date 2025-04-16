"""

*****
****
***
**
*
"""


def pattern(n):
    if(n==0): #Base condition
        return
    print("*" *n)
    pattern(n-1)
    
pattern(5)