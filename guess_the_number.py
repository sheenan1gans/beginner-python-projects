import random

highest = 100
lowest = 1
answer = random.randint(lowest, highest)
guesses = 0
is_running = True

print("Guess the number")
print(f"Hint: It lies between {highest} and {lowest}")
guess = input("Enter you guess!: ")

while is_running:
    if guess.isdigit():
        guess = int(guess)
        guess += 1

        if guess > highest or guess < lowest:
            print("Your guess is not with the given limit")
            print(input("Take another guess!: "))
        elif guess < answer:
            print("Your guess is too low!")
            print(input("Take another guess!: "))

        elif guess > answer:
            print("Your guess is too high!")
            print(input("Take another guess!: "))

        elif guess == answer:
            print("You are correct! ")
            print(f"Number of guesses:{guess}")







