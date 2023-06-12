import random

# Print Welcome Message
print("Hello, welcome to the Rock, Paper, Scissors Game - v1")

#Declare Computer Selection Options (Moves: Rock, Paper, Scissors)
computer_selection_moves = ["r", "p", "s"]

#Start Endless Game
while True:
    #Ask User's Input
    user_move = input("Enter your move Options: (r, p and s): ")
    #Randomly Choose Computer's Move
    computer_move = random.choice(computer_selection_moves)
    #Print Computer's Move
    print("Computer's move: " + str(computer_move))
    
    #Check Who Wins
    if user_move == computer_move:
        print("It is a tie 😑. \n")
    elif user_move == "r" and computer_move == "s":
        print("You win! Rock smashes scissors 😀. \n")
    elif user_move == "p" and computer_move == "r":
        print("You win! Paper covers rock 😀. \n")
    elif user_move == "s" and computer_move == "p":
        print("You win! Scissors cuts paper 😀. \n")
    else:
        print("Computer wins! 🙁 \n")
