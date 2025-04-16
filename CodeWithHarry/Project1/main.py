# """
# SNAKE WATER GUN GAME 

# 1 snake
# -1 water
# 0 gun
# """

# computer = -1 
# user = input("Enter your choice (s , w , g) : ").lower()

# dict = {
#     "s" : 1,
#     "w" : -1,
#     "g" : 0
# }
# userNum = dict[user] # convert user input to num 

# if(computer == -1 and user == 1):
#     print("You Win !")
# elif(computer == -1 and user == 0):
#     print("You lose !")
# elif(computer == 1 and user == -1):
#     print("You Lose !")
# elif(computer == 1 and user == 0):
#     print("You win !")
# elif(computer == 0 and user == -1):
#     print("You Lose !")
# elif(computer == 0 and user == 1):
#     print("You Win !")
# else:
#     print("Something Went Wrong")




# ----------------------------------



import random

print("🎮✨ Welcome to the Snake 🐍 Water 💧 Gun 🔫 Game! ✨🎮")
print("---------------------------------------------------")
print("🔹 Instructions:")
print("    s = 🐍 Snake")
print("    w = 💧 Water")
print("    g = 🔫 Gun")
print("---------------------------------------------------")

# Randomly choose computer's move
computer = random.choice([1, -1, 0]) 

# Take user's input
user = input("👉 Enter your choice (s / w / g): ").lower()

# Mapping user input to corresponding number
choice_map = {
    "s": 1,
    "w": -1,
    "g": 0
}

# Extra: Mapping numbers back to emoji for display
emoji_map = {
    1: "🐍 Snake",
    -1: "💧 Water",
    0: "🔫 Gun"
}

# Convert user's input to number
userNum = choice_map.get(user)

# Safety check
if userNum is None:
    print("❌ Invalid input! Please choose s, w, or g.")
else:
    # Display choices
    print(f"\n🤖 Computer chose: {emoji_map[computer]}")
    print(f"🧑 You chose: {emoji_map[userNum]}\n")

    # Game logic
    if computer == userNum:
        print("⚖️ It's a Tie!")
    elif (computer- userNum == -1) or \
        (computer- userNum ==  2):
        print("😢 You Lose! Better luck next time!")
    else:
        print("🎉 You Win! 🏆")

print("---------------------------------------------------")







# import random

# print("🎮✨ Welcome to the Snake 🐍 Water 💧 Gun 🔫 Game! ✨🎮")
# print("---------------------------------------------------")
# print("🔹 Instructions:")
# print("    s = 🐍 Snake")
# print("    w = 💧 Water")
# print("    g = 🔫 Gun")
# print("---------------------------------------------------")

# # Randomly choose computer's move
# computer = random.choice([1, -1, 0]) 

# # Take user's input
# user = input("👉 Enter your choice (s / w / g): ").lower()

# # Mapping user input to corresponding number
# choice_map = {
#     "s": 1,
#     "w": -1,
#     "g": 0
# }

# # Extra: Mapping numbers back to emoji for display
# emoji_map = {
#     1: "🐍 Snake",
#     -1: "💧 Water",
#     0: "🔫 Gun"
# }

# # Convert user's input to number
# userNum = choice_map.get(user)

# # Safety check
# if userNum is None:
#     print("❌ Invalid input! Please choose s, w, or g.")
# else:
#     # Display choices
#     print(f"\n🤖 Computer chose: {emoji_map[computer]}")
#     print(f"🧑 You chose: {emoji_map[userNum]}\n")

#     # Game logic
#     if computer == userNum:
#         print("⚖️ It's a Tie!")
#     elif (computer == -1 and userNum == 1) or \
#          (computer == 1 and userNum == 0) or \
#          (computer == 0 and userNum == -1):
#              #The backslash (\) in Python is used as a line continuation character. 
#              # It allows you to break a long statement into multiple lines for better 
#              # \readability, especially when you have complex or lengthy expressions like 
#              # the ones in your elif condition.
#         print("🎉 You Win! 🏆")
#     else:
#         print("😢 You Lose! Better luck next time!")

# print("---------------------------------------------------")
