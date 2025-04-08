name = input("Enter your name: ")

def greet(name="World"):
    return f"Hello, {name}!"

print(greet())
print(greet(name))
