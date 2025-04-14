import numpy as np 
# fixed in size and sam etype p=of element array 
a = np.array([0,1,2,3,4])
print(type(a)) # <class 'numpy.ndarray'>

print("Size of ARRAY ",a.size)
print("Dimention of array ",a.ndim)
print("size of array in each dimention ", a.shape)

print("**** Indixing And Sliceling *****")

c = np.array([20,30,40,50,1,2,4])

print("Initial array :",c)
c[0]=100
print("after changing array :",c)
print("Slice :",c[1:3])

print("******** VEctor Addition *********")

u = [1,0]
v = [1,0]
z = []
for n,m in zip(u,v):
    z.append(m+m)
print("Appednd Addition od m , n to z ",z)

l = np.array([1,2])
k = np.array([3,2])
o = []
o=l*k
print("MUltiplication : ",o)

print("_________________DOT PRODUCT______________________________")

  # u = [1,2]  
  # v = [3,2]
  # 1*3 + 2* 1
  
t = np.dot(l,k)
print("Dot product od L ANd K : ",t)

print("----- UNIVERSAL FUN---")
c = np.array([1,2,3,4])
mean_c = c.mean()
max = c.max()

print("MEAN OF ARRAY : " , mean_c)
print("MAX OF ARRAY : " ,max)
