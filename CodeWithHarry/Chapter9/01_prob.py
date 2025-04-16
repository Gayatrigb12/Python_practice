# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# Using WITH keywords 

with open("file.txt") as f:
    print(f.read())
# no need to close file explicitly 