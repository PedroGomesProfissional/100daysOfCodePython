#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.

# If they got the answer correct, show the actual answer to the player.

# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player. 

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


DIFICULTY_TRIES = 10

def set_dificulty(dificulty):
  global DIFICULTY_TRIES
  
  if dificulty.lower() == "easy":
    DIFICULTY_TRIES = 10
    return DIFICULTY_TRIES
    
  elif dificulty.lower() == "hard":
    DIFICULTY_TRIES = 5
    return DIFICULTY_TRIES
    
  else:
    return "Wrong dificulty!"
    

def game():
  global DIFICULTY_TRIES
  
  print(logo)

  print("Hello this is a guessing game. Guess correct to wing!")
  
  dificulty = input("Choose a dificulty. Easy or Hard: ")

  actual_num = random.randint(1,100)
    
  set_dificulty(dificulty)

  while DIFICULTY_TRIES > 0:
    
    guess_num = int(input("Guess a number between 1 and 100: "))
    
    if guess_num <= 100 and guess_num >= 1:
      
      #print("Actual number = ", actual_num)

      if guess_num < actual_num:
        DIFICULTY_TRIES -= 1
        print("Too Low!\n")
  
      elif guess_num > actual_num:
        DIFICULTY_TRIES -= 1
        print("Too High!\n")

      elif guess_num == actual_num:
        print("You Win!")
        break

      if DIFICULTY_TRIES == 0:
        print(f"You loose! Correct number = {actual_num}")
        break

      
game()
    
  