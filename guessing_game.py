# Imports Randomly Generated Number
import random

# Defines the Main Function for the Game
def play_game():

# Generates a random secret number between 1 and 100
  secret_number = random.randint(1, 100)

# Keeps Track of how many Guesses the User Makes
  attempts = 0

# Prints Welcome Message and Game Instructions
  print("Welcome to the Guessing Game!")
  print("I am thinking of a number between 1 and 100.")

# Infinite Loop Keeps the Game Running Until the Correct Answer is Found
  while True:

# Takes User Input as a String
    user_input = input("Enter your guess: ")

# Checks if Input is Not a Number, Skips Rest of Loop and Asks Again
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

# Converts Valid Input into an Integer
    guess = int(user_input)
        
# Increases Attempt Count Each Guess
    attempts += 1
        
# Compares Guess with Secret Number
    if guess < secret_number:
            print("Too low! Try again.")
    elif guess > secret_number:
            print("Too high! Try again.")
    else:

# Correct Guess Ends the Loop
      print(f"Correct! You got it in {attempts} attempts!")
      break

# Starts the game by Calling the Function
play_game()
