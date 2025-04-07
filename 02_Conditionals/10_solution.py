# Pet Food Recommendation Program

species = input("Enter the pet's species (dog/cat): ").strip().lower()
age = float(input("Enter the pet's age in years: "))

if species == "dog":
    if age < 2:
        food = "Puppy food"
    elif age <= 7:
        food = "Adult dog food"
    else:
        food = "Senior dog food"

elif species == "cat":
    if age < 2:
        food = "Kitten food"
    elif age <= 5:
        food = "Adult cat food"
    else:
        food = "Senior cat food"

else:
    food = "Unknown species - no recommendation available."

print("Recommended food:", food)
