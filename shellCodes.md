---- List ----
# LIst are mutable here us example for that 

# if we assign first multiple referance at that time it will point to first one only but if we have same referance means referance is not changle like ex 2 then it will change 


example 1 
>>> list1 = [1,2,3] # we assign value to list 1 
>>> list2 = list1 # list2 is eqauals to list 1 
>>> list1 = 'hello' # here we change referance of list1
>>> list2 #print list1
[1, 2, 3] # same as 1st assignment of list 1 because its point to referance of list 1 i.e [1,2,3]
>>> list1 #print list2
'hello' 
>>> list1 = [1,2,3] #here we used previous referd by list1 int step 1 again 
>>> list2 #print list2
[1, 2, 3]
>>> list1 #print list1
[1, 2, 3]
>>> list1[0] = 33 # now we change the first element in that referance 
>>> list1 #print list1
[33, 2, 3] 
>>> list2 #print list2
[1, 2, 3] # here referance is not change 

-----------------------------
>>> list2 = list1
>>> list1
[33, 2, 3]
>>> list2
[33, 2, 3]
===============================
example 2
# here is one difference here we assign one referance to both we not change referance of l1 
>>> L1 = [1,2,3]
>>> L2 = L1
>>> L1
[1, 2, 3]
>>> L2
[1, 2, 3]
>>> L1[0]=44
>>> L1
[44, 2, 3]
>>> L2
[44, 2, 3]
>>> 

===============================================

Example 3 

>>> h1 = [ 1, 2 , 3 ]
>>> h2 = h1[:] # here we did slicing and it will copy elemets in h1
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0] = 55
>>> h2
[1, 2, 3]
>>> h1
[55, 2, 3]
>>> 



==================================================


Example 1.1 

>>> n = [1,2,3]
>>> m = n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m == n #checking value of m and n 
True
>>> m is n #checking referance of m and n 
True
>>> n = [1,2,3]
>>> m = [1,2,3]
>>> m == n
True
>>> m is n
False
>>> 


