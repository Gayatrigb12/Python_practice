list = [1,2,3,4,5,5,6,6]

# squreList = []

# for item in list:
#     squreList.append(item*item)
# print(squreList)

""" This can be simplified using list comprehentions """
squreList = [i*i for i in list]

print(squreList)