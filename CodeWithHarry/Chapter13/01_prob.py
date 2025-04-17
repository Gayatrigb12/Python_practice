from functools import reduce
l = [222,44,5,33,2,334,66,77,88]

def max(a,b):
    if(a>b):
        return a
    return b

print(reduce(max , l))