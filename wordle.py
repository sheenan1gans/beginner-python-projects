#Word Guessing Game (like Wordle)
#User has 6 tries to guess a 5-letter word.
#Give feedback: 🟩 correct letter & position, 🟨 correct letter wrong position, ⬜ not in word.

from wordle_words import words
import random

print("Welcome to Wordle!")
print("You have 6 tries to guess a 5-letter word.")
print("Keys: 🟩 correct letter & position, 🟨 correct letter wrong position, ⬜ not in word.")

def choose_word():
    return random.choice(words)

def check_guess(word, guess):
    result = ""
    for index in range (len(word)):
        if guess[index] == word[index]:
            result += "🟩"
        elif guess[index] in word:
            result += "🟨"
        else:
            result += "⬜"
    return result


def main():
    is_running = True
    word = choose_word()
    attempts = 6


    while attempts > 0:
        guess = input("enter your guess: ")

        if not guess.isalpha() or len(guess) != 5:
            print("Invalid entry!")
            continue

        feedback = check_guess(word, guess)
        print(feedback)

        if guess == word:
            print("You are correct!")
            break
        else:
            print("Wrong guess!")
            attempts -= 1
        if attempts == 0:
            print(f"You are out of tries! The correct word was {word}")






if __name__ == '__main__':
    main()