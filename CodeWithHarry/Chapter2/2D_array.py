import numpy as np 
a = [[11,12,13],[21,22,23],[31,32,33]]
A = np.array(a)
print(A)
print("DImention",A.ndim)
print("rows col ",A.shape)
print("size :",A.size)
print("Perticula element", A[2,2])
b = [[1,2,3],[1,2,3],[1,2,3]]
B = np.array(b)
c = A+ B
print("Add of matrix a b :",c)
print("sqare" , 2*B)