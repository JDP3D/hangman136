import random

# get user input
def check_guess(guess):
     """This function checks if the player's guess is in the random word"""
     guess = guess.lower()

     if guess in choose_random_word:
        print(f'Good guess! {guess} is in the word.')
     else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    """This function gets the player's input and then checks if the chosen letter 
    is in the word"""

    while True:
        guess = input('Please enter a single letter:  ')

        if len(guess) == 1 and guess[0].isalpha():
                #print('Good guess!')
                break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)

word_list = ['banana', 'clementine', 'pear', 'mango', 'strawberry']

choose_random_word = random.choice(word_list)

#print(choose_random_word)

ask_for_input()

