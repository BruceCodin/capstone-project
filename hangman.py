# Capstone Project: Hangman Game
from hangman_structure import hangman_art

# word answer to the hangman game (light)
answer_list = ('l', 'i', 'g', 'h', 't')

# user input guess
guess = input("Guess Letter:")
correct = None

for let in answer_list:
    if guess == let:
        correct = True

print(correct)
print(hangman_art(0))
