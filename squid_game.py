import random

# Generate a random number between 1 and 100
number = random.randint(1, 10)

print("🦑 Welcome to Squid Game: Guess the Number! 🦑")
print("You have only ONE chance to guess the number (1-10).")

# Take user input
try:
    guess = int(input("Enter your guess: "))
    
    if guess == number:
        print("🎉 Congratulations! You guessed it right and survived! 🏆")
    else:
        print(f"💀 Wrong! The correct number was {number}. You are eliminated! 😱")
except ValueError:
    print("❌ Invalid input! Please enter a number.")

except KeyboardInterrupt:
    print("\n👋 Game interrupted. Thanks for playing!"      )
    
    