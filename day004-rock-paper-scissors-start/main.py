import random

ROCK = 0
PAPER = 1
SCISSORS = 2

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_rock_paper_scissors = int(input("Lets play rock, paper, scissors!\nChoose 0 for rock, 1 for paper and 2 for scissors\n$"))


random_choice = random.randint(0, 2)
#print(random_choice)

if choice_rock_paper_scissors == ROCK:
  print("You\n", rock)
  print("\nComputer")
  
  if random_choice == 0:
    print(rock)
    print("Even")
  
  elif random_choice == 2:
    print(scissors)
    print("You win!")

  elif random_choice == 1:
    print(paper)
    print("You lost!")

elif choice_rock_paper_scissors == PAPER:
  print("You\n", paper)
  print("\nComputer")
  
  if random_choice == 1:
    print(paper)
    print("Even")
  
  elif random_choice == 0:
    print(rock)
    print("You win!")

  elif random_choice == 2:
    print(scissors)
    print("You lost!")

elif choice_rock_paper_scissors == SCISSORS:
  print("You\n", scissors)
  print("\nComputer")
  
  if random_choice == 2:
    print(scissors)
    print("Even")
  
  elif random_choice == 1:
    print(paper)
    print("You win!")

  elif random_choice == 0:
    print(rock)
    print("You lost!")

else:
  print("Wrong input, game over!")  
  
