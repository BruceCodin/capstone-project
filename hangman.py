# Capstone Project: Hangman Game
from hangman_structure import hangman_art

# word answer to the hangman game (light)
answer_list = ('l', 'i', 'g', 'h', 't')

# keeps track of how many guesses are correct to words in answer
tracker = [0, len(answer_list)]
correct = None
mistakes = 0

# use while loop to keep user guessing inputs until all are correct
while (tracker[0] != tracker[1]) and (mistakes < 7): 

    # user input guess
    correct = None
    guess = input("Guess Letter: ")

    for let in answer_list:
        if guess == let:  # need to add an 'and' here , and if guess letter has not already been found etc
            correct = True

    if (correct):
        tracker[0] = tracker[0] + 1
        print("SUCCESS!")
    else:
        print("FAILED")
        mistakes+=1
        print(hangman_art(mistakes))

# Game results
print(hangman_art(mistakes))

print('=====GAME RESULTS=====')
if mistakes == 7:
    print('You LOSE!')
    print(f'The word was {"".join(answer_list)}')
else:
    print('You WIN!')
    print(f'The word was {"".join(answer_list)}')
