limit = int(input("Enter a number: "))
def even_num(limit):
    for i in range(2, limit + 1,2):
        yield i # yeild is store the value in memory and return it when called again
        # return i

for num in even_num(limit):
    print(num)    

# output:
# Enter a number: 10
# 2
# 4
# 6
# 8
# 10
