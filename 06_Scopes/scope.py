# Scope of a variable is the part of the program where the variable is accessible.

#Example 1

# username = "Krishna" #  (global scope )store username in direct memory 

# def func():
#     username = "Gayatri"  # (local scope)store username in local memory
#     print("Local Scope : " + username)  # op Gayatri
# func()  # call the function to execute local scope
# print("Global Scope : " + username)  # op Krishna


# Example 1  Output:
# PS D:\PYTHON\06_Scopes> python scope.py
# Local Scope : Gayatri
# Global Scope : Krishna



# Example 2

# username = "Krishna" #  (global scope )store username in direct memory 

# def func():
#     # username = "Gayatri"  # (local scope)store username in local memory
#     print("Local Scope : " + username)  # op Gayatri
# func()  # call the function to execute local scope
# print("Global Scope : " + username)  # op Krishna

# Example 2  Output:

# PS D:\PYTHON\06_Scopes> python scope.py
# Local Scope : Krishna
# Global Scope : Krishna
    
    
    
# Example 3


# x = 99

# def func(y):
#     z = x + y
#     return z

# result = func(1)  # call the function to execute local scope

# print("Result: " , result)  # op 100
# print("x: " , x)  # op 99
# print("y: " , y)  # op 1
    

# Example 3 Output:
# PS D:\PYTHON\06_Scopes> python scope.py
# Result:  100
# x:  99
# y:  1


# Example 4
# Bad use of global variable
# x = 99

# def func():
#    global x
#    x = 12 # (global scope)store username in direct memory

# result = func()  # call the function to execute local scope

# print("x: " , x)  # op 12


# Example 4 Output:

# PS D:\PYTHON\06_Scopes> python scope.py
# x:  12


# Example 5 ( Climbing the scope tree)

# x = 99

# def func():
#     x = 88 
#     def func2():
#         print(x)
#     func2()  # call the function to execute local scope
# func()  # call the function to execute local scope


# Example 5 Output:
# PS D:\PYTHON\06_Scopes> python scope.py
# 88



# Example 6 (  closulre function)
# x = 99

# def func():
#     x = 88 
#     def func2():
#         print(x)
#     return func2  # call the function to execute local scope
# result = func() # call the function to execute local scope
# result()  # call the function to execute local scope


# Example 6 Output:

# PS D:\PYTHON\06_Scopes> python scope.py
# 88


# Example 7 (  Closures with arguments)
x = 99

def func(num):
    def func2(x):
        return x ** num
    return func2  # call the function to execute local scope

result = func(2) # call the function to execute local scoper
result1 = func(3)  # call the function to execute local scope


print(result(3))  # call the function to execute local scope
print(result1(3))  # call the function to execute local scope