weather = input("Enter the weather (sunny, rainy, snowy): ").strip().lower()

if weather == "sunny":
    print("It's a sunny day! Go for Walk.")
elif weather == "rainy":
    print("It's a rainy day! Read a book.")
elif weather == "snowy":
    print("It's a snowy day! Build a snowman.")
else:
    print("Invalid weather type. Please enter sunny, rainy, or snowy.")
    