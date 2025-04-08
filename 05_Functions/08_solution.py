def print_kvargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kvargs(name="John", age=30)
print_kvargs(name="John", age=30, city="New York")
