color = input("Enter your fruit color: ").lower() # input the color of the fruit
fruit = "banana"

if fruit == "banana":
    if color == "yellow":
        print("The banana is ripe.")
    elif color == "green":
        print("The banana is  Unripe.")
    elif color == "brown":
        print("The banana is overripe.")
    else:
        print("invalid color.")
else:
    print("The fruit is not banana.")
