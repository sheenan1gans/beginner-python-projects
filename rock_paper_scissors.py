#rock paper scissors

import random

options = ("rock", "paper", "scissors")
player = None
chances = 0
you = 0
opponent = 0


while True:
    computer = random.choice(options)

    print(f"Round: {chances + 1}")
    print("___________________")
    player = input("Play your move (rock, paper, scissors): ").lower()

    if player not in options:
        print("Invalid move! Please choose rock, paper, or scissors.")
        continue

    chances += 1

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")

    elif (
            (player == "rock" and computer == "scissors") or
            (player == "scissors" and computer == "paper") or
            (player == "paper" and computer == "rock")
    ):
        print("You win!")
        you += 1
    else:
        print("You lose!")
        opponent += 1
    print("___________________")

    if chances == 3:
        print("The game has ended after 3 moves!")
        print(f"Your score:{you}")
        print(f"Computer's score: {opponent}")
        print("")
        print("___________________")

        if you > opponent:
            print("You win!")
        elif you == opponent:
            print("It's a tie!")
        else:
            print("You lose!")
        break






