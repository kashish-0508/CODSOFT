import random

#score board
user_score = 0
computer_score = 0

#options in the game
options = ["rock", "paper", "scissors"]

print('*'*50)
name = input("Enter your Name: ")
print("Welcome",name)

# welcome screen
print('\n'+'*'*50)
print("\tRock , Paper , Scissors")
print('*'*50 + '\n')
print("Game Modes")
print("1. Infinity War")
print("2. Best of 5")

# mode selection
mode = input("Choose mode 1 or 2: ")
if mode == "1":
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        random_number = random.randint(0, 2)
        
        computer_pick = options[random_number]
        print("Computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_score += 1

        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_score += 1

        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_score += 1
        
        elif user_input == computer_pick:
            print("Both chose same- No Points")

        else:
            print("You lost!")
            computer_score += 1

else:
    for i in range (5):
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        random_number = random.randint(0, 2)
        
        computer_pick = options[random_number]
        print("Computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_score += 1

        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_score += 1

        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_score += 1
            
        elif user_input == computer_pick:
            print("Both chose same- No Points")
        else:
            print("You lost!")
            computer_score += 1

#score board
print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
print("Goodbye!")