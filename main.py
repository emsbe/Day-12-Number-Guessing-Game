import random
from art import logo

#compare function: comparing user number with random number
def compare(random_no, user_no):
  """Comparing user input with random number"""
  end_game = False
  if random_no > user_no:
    print("Too low.")
    return end_game
  elif random_no < user_no:
    print("Too high.")
    return end_game
  else:
    print(f"You got it! The answer was {random_no}. Congrats!")
    end_game = True
    return end_game

#playing the game in two difficulties
def play(random_no, difficulty):
  """game function"""
  if difficulty == "easy":
    guesses = 10
  elif difficulty == "hard":
    guesses = 5
  end_game = False
  print(f"You have {guesses} attempts remaining to guess the number.")
  while not end_game == True:
    user_number = int(input("Make a guess: "))
    guesses -= 1
    end_game = compare(random_number, user_number)
    if guesses == 0:
      end_game = True
    if end_game == False:
      print("Guess again.")
      print(f"You have {guesses} attempts remaining to guess the number.")
    if end_game == True and guesses == 0:
      print(f"You are out of guesses. The answer was {random_number}.")

#################### start of the game #############################

#Welcome print statements and call function

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#generating a random number
random_number = random.randint(1, 100)

#user input
user_input_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#checking for invalid user input
possible_difficulties = ["easy", "hard"]
if not user_input_difficulty in possible_difficulties:
  print("Invalid input. Please load the game again.")
else:
  #loading the game if input is correct
  play(random_number, user_input_difficulty)