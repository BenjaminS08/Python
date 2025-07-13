"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 
"""

import random

WORD_LIST = ("PYTHON", "COBOL", "JAVASCRIPT", "BASIC", "HTML", "JAVA", "ASSEMBLY", "RUST", "C", "C#", "C+", "C++", "SQL", "GO", "SWIFT")


def game(answer, display):
    wrong = 0
    right = 0

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = []

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            wrong += 1
            if wrong > 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break
        if wrong < 1:
            print("You have Five Incorrect guesses left")
        elif wrong < 2:
            print("You have four incorrect guesses left")
        elif wrong < 3:
            print("You have three incorrect guesses left")
        elif wrong < 4:
            print("You have two incorrect guesses left")
        elif wrong < 5:
            print("You have one incorrect guess left")

def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()