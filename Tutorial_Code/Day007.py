# Hangman Project

import random

stages = ['''
 +---+
 |   |
 0   |
/|\\  |
/ \\  |
     |
======
''', '''
 +---+
 |   |
 0   |
/|\\  |
/    |
     |
======
''','''
 +---+
 |   |
 0   |
/|\\  |
     |
     |
======
''','''
 +---+
 |   |
 0   |
/|   |
     |
     |
======
''','''
 +---+
 |   |
 0   |
/    |
     |
     |
======
''','''
 +---+
 |   |
 0   |
     |
     |
     |
======
''','''
 +---+
 |   |
     |
     |
     |
     |
======
''']

lives = 6

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

place_holder = ""
word_length = len(chosen_word)
for position in range(word_length):
    place_holder +="_"
print(place_holder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("Enter your guess: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left out of 7 lives")
        if lives == 0:
            game_over = True
            print(f"The word was {chosen_word}, you Lose!")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])