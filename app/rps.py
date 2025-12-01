import random
VALID_OPTIONS = ["Rock", "Paper", "Scissors"]

# ASK THE USER FOR AN INPUT 

user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
print("USER:", user_choice)

# VALIDATION 
if user_choice not in VALID_OPTIONS:
    print("Invalid choice! Please select Rock, Paper, or Scissors.")
    exit()

#GERNERATE A RANDOM CHOICE FOR THE COMPUTER

computer_choice = random.choice(VALID_OPTIONS)
print("COMP:", computer_choice)

# DETERMINE THE WINNER
