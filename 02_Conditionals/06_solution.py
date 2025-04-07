dist = float(input("Enter the distance in kilometers: "))  # input the distance in kilometers

if dist < 0:
    print("Invalid distance. Please enter a positive number.")
    exit()  # exit the program if the distance is invalid

if dist < 3:
    print("go by walk....")   
elif dist < 16:
    print("go by bike....")
elif dist >= 16:  # Changed to >= to include 16 in the car option
    print("go by car....")

