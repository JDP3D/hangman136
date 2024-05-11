import random

word_list = ['banana', 'clementine', 'pear', 'mango', 'strawberry']

print(word_list)

word = random.choice(word_list)

#print(word)

guess = input('Please enter a single letter:  ')

if len(guess) == 1 and guess[0].isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
