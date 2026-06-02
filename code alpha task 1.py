import random

# List of words
words = ["apple", "mango", "grape", "house", "table"]

# Choose a random word
word = random.choice(words)

guessed = ""
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("You Win!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed += guess
        print("Correct!")
    else:
        chances -= 1
        print("Wrong! Chances left:", chances)

if chances == 0:
    print("Game Over!")
    print("The word was:", word)