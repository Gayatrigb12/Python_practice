coffee_size = input("What size coffee would you like? (small/medium/large): ").strip().lower()

if coffee_size not in ["small", "medium", "large"]:
    print("Invalid coffee size. Please choose small, medium, or large.")
    exit()  # exit the program if the coffee size is invalid
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").strip().lower()

if extra_shot not in ["yes", "no"]:
    print("Invalid choice for extra shot. Please choose yes or no.")
    exit()  # exit the program if the extra shot choice is invalid

if extra_shot == "yes":
    
    print("You have ordered a " + coffee_size + " coffee with an extra shot of espresso.")
else:
    print("You have ordered a " + coffee_size + " regular coffee.")
                     