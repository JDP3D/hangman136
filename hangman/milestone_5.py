# code for third milestone
import random

class Hangman:
    """The Hangman game class"""
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        #print(self.word)

    def check_guess(self, guess):
        """This function checks if the guessed letter is in the word or not"""
        guess = guess.lower()

        if guess in self.word:
            # The commented code below is my try to replace the for loop with a list comprehension
            # guess_index = [index for index, letter in enumerate(self.word) if letter == guess]
            # for num in guess_index:
            #     self.word_guessed[num] = guess

            print(f'Good guess! {guess} is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(' '.join(self.word_guessed))
            
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        """This function gets the player's guessed letter, checks it's validity and """
        while True:
            guess = input('Please enter a single letter:  ')

            if not(len(guess) == 1 and guess[0].isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    
def play_game(word_list):
    """This function runs the Hangman game"""
    num_lives = 5

    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations, you won the game')
            break


if __name__ == "__main__": 
    "This is the main game loop"
    words = ['banana', 'clementine', 'pear', 'mango', 'strawberry']
    play_game(words)