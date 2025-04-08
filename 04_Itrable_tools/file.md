# file loop 


reading file line by line 


>>> f = open('demo.py')
>>> f.readline()
'import time\n'
>>> 
>>> f.readline()
'\n'
>>> f.readline()
'print("Itertools")\n'
>>> f.readline()
'username = "John Doe"\n'
>>> f.readline()
'print("Username:", username)\n'
>>> f.readline()
''
>>> f.readline()
''
>>> 



by raw mentthod __next__()

>>> f = open('demo.py')
>>> f.__next__()
'import time\n'
>>> 
>>> f.__next__()
'\n'
>>> f.__next__()
'print("Itertools")\n'
>>> f.__next__()
'username = "John Doe"\n'
>>> f.__next__()
'print("Username:", username)\n'
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>    
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>>




# using loop 

>>> for line in open('demo.py'):
...     print(line)
... 
import time



print("Itertools")

username = "John Doe"

print("Username:", username)

------------------------------------------

>>> for line in open('demo.py'):
...     print(line,end='')                         
...     
import time

print("Itertools")
username = "John Doe"
print("Username:", username)
>>> 


# About memory pointing and STOP EXCEPTION 

>>> myList = [1,2,3,4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x00000296502E0B80> 
 # pointion to first memory loc 
>>> I.__next__()
1
>>> I
<list_iterator object at 0x00000296502E0B80>
# still pointion to first memory loc  because it always point to first memory loc even its change to 2 in loop
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> 



# dict 

>>> D = { 1:'a' , 2 : 'e' , 3 : 'm' }
>>> for key in D.keys():
...     print(key)
...     
1
2
3
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x0000029650316C00>    
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
Traceback (most recent call last):
  File "<python-input-44>", line 1, in <module>    
    next(I)
    ~~~~^^^
StopIteration
>>> 


# Range 
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> I
<range_iterator object at 0x00000296502FD150>      
>>> next(I)
0
>>> next(I)
1
>>> 
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<python-input-55>", line 1, in <module>    
    next(I)
    ~~~~^^^
StopIteration
>>> 

# if you want to know about iterable then do like above


# NOTE  :- in files all are same like  f = iter(f) =  f.__iter__()

>>> f = open('demo.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> 
# but not applicable for list 
>>> myList = [1,2,3,4]
>>> iter(myList) is myList
False
>>> 



# itrable 
-- file 
-- dict 
-- range 

# not iterable 
-- list 