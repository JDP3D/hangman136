# code for third milestone
import random

class Hangman:
    """The Hangman game class"""
    def __init__(self, word_list, num_lives = 5):
        self.__word_list = word_list
        self.num_lives = num_lives
        self.__word = random.choice(self.__word_list)
        self.__word_guessed = ['_'] * len(self.__word)
        self.num_letters = len(set(self.__word))
        self.__list_of_guesses = []

    def __check_guess(self, guess):
        """This function checks if the guessed letter is in the word or not"""
        guess = guess.lower()

        if guess in self.__word:
            print(f'Good guess! {guess} is in the word.')
            for i in range(len(self.__word)):
                if self.__word[i] == guess:
                    self.__word_guessed[i] = guess
            print(' '.join(self.__word_guessed))
            
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
    
    def _ask_for_input(self):
        """This function gets the player's guessed letter, checks it's validity and """
        while True:
            guess = input('Please enter a single letter:  ')

            if not(len(guess) == 1 and guess[0].isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.__list_of_guesses:
                print('You already tried that letter!')
            else:
                self.__check_guess(guess)
                self.__list_of_guesses.append(guess)
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
            game._ask_for_input()
        else:
            print('Congratulations, you won the game')
            break


if __name__ == "__main__": 
    "This is the main game loop"
    words = ['banana', 'clementine', 'pear', 'mango', 'strawberry']
    play_game(words)