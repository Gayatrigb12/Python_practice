import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

print("🦑 Welcome to Squid Game: Guess the Number! 🦑")
print("You have 3 chances to guess the number (1-10).")

# Allow the user 3 attempts
attempts = 3

for attempt in range(attempts):
    try:
        guess = int(input(f"Attempt {attempt + 1}/{attempts} - Enter your guess: "))
        
        if guess == number:
            print("🎉 Congratulations! You guessed it right and survived! 🏆")
            break  # Exit the loop if the user guesses correctly
        else:
            if attempt < attempts - 1:
                print("💀 Wrong! Try again!")
            else:
                print(f"💀 Wrong! The correct number was {number}. You are eliminated! 😱")
                
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

    except KeyboardInterrupt:
        print("\n👋 Game interrupted. Thanks for playing!")
        break  # Exit the game if interrupted
