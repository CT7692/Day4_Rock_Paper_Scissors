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

#Write your code below this line 👇
import random

def outcome(player, comp, r, p, s):
  if (player == r) and (comp == s):
    message = "YOU WIN!"
  elif(player == p) and (comp == r):
    message = "YOU WIN!"
  elif(player == s) and (comp == p):
    message = "YOU WIN!"
  elif(player == comp):
    message = "It's a draw."
  else:
    message = "You lose."
  return message
    
choice_list = [rock, paper, scissors]
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if (player_choice != "0") and (player_choice != "1") and (player_choice != "2"):
  correct = False
  while correct == False:
    print("\nPlease enter a listed option.")
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if(player_choice == "0") or (player_choice == "1") or (player_choice == "2"):
      correct = True

int_choice = int(player_choice)

player_choice = choice_list[int_choice]
print(f"\nYou chose:\n{player_choice}")

computer_int = random.randint(0, 2)
computer_choice = choice_list[computer_int]
print(f"Computer chose:\n{computer_choice}")

message = outcome(player_choice, computer_choice, rock, paper, scissors)
print(message)