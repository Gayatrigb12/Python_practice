from functools import reduce
# map function
l = [1,2,3,4]

square = lambda x: x*x

sqList = map(square , l)
print(list(sqList))

# filter example 

def even(n):
    if(n%2 == 0 ):
        return True
    return False
onlyEven = filter(even , l)
print(list(onlyEven))


# reduce Example 

def sum( a, b):
    return a+ b
mul = lambda x , y : x*y
print(reduce(sum , l)) # its take argumate as reduce(function , list)
print(reduce(mul , l)) # its take argumate as reduce(function , list)

"""
working on list
l = [1,2,3,4]

1 ---> 1+2 3 4
2       3+3 4
3        6+4
4         10

"""