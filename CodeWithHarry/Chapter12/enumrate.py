list = [3,45,54,55]
# index = 0

# for i in list:
#     print(f"The item no at index  {index} is {i} ")
#     index += 1

""" This can be simplified using enumrate function """

for index , i in enumerate(list):
    print(f"The item no at index  {index} is {i} ")
    