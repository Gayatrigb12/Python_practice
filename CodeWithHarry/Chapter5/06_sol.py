dict = {}
n = int(input("enter no or record you want to insert : "))

for i in range(1,n+1):
    name = input(f"Enter friend {i} name : ")
    lang = input("enter language : ")
    dict.update({name : lang })
print(dict)

"""
op : - 
CASE !

enter no or record you want to insert : 2
Enter friend 1 name : gayatri 
enter language : java 
Enter friend 2 name : krish 
enter language : python 
{'gayatri ': 'java ', 'krish ': 'python '} 


CASE 2 

enter no or record you want to insert : 2
Enter friend 1 name : gg
enter language : asdfgh
Enter friend 2 name : gg
enter language : mnbfd
{'gg': 'mnbfd'}
"""