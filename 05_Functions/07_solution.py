def sum_all(*args):  # *args lets you pass any number of positional arguments
    print(args)      # 'args' is a tuple of all arguments passed
    for i in args:   # Loop through each argument
        print(i * 2) # Multiply each argument by 2 and print it
    return sum(args) # Return the sum of all arguments

print(sum_all(1, 2, 3))


# RESULT
# (1, 2, 3)      ← This is the tuple `args`
# 2              ← 1 * 2
# 4              ← 2 * 2
# 6              ← 3 * 2
# 6              ← This is the final result: 1 + 2 + 3
