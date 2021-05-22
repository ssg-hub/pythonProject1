_author_ = "Shilpa"

"""
Objective: Make a HANGMAN game for the player to guess a word.

Specifics: The player needs to guess a mystery word. When the player guesses 
a letter and if correct the game fills the word with that letter. Each time 
the player enters a valid guess, turn count increases.If not, the error count
is increased and lives are decreased. The number of lives is limited to 
5, i.e maximum 5 errors while guessing letters of the word can be made.

Valid input = a single letter, no numbers, symbols, multiples accepted.
Maximum lives = 5

"""
# import the needed libraries
import sys
import os
import random
from typing import List


# creating Hangman class
class Hangman:
    """
    Initializes the following to start the game Hangman;

    Attributes:-
    possible_words is a list of words from which a random word
                        is generated
    _lives is the number of Hangman lives, max 5
    _turn_count
    _error_count
    wrongly_guessed_letters is a list where all incorrect guessed are stored
    correctly_guessed_letters is a list where all correct guessed are stored

    Methods:-
    play is the brain of the game
    start_game is to initialize and control the game
    well_played is for when player wins the game
    game_over is for when player looses the game
    """

    _lives: int = 5
    _turn_count: int = 0
    _error_count: int = 0
    wrongly_guessed_letters: List[str] = []
    possible_words: List[str] = ['gamer', 'classic', 'guess', 'brussels',
                                 'data', 'innovate', 'future', 'learner',
                                 'becode', 'learning', 'mathematics', 'almond'
                                 'sessions', 'paperless', 'artificial', 'mango']

    def __init__(self):
        """ Constructor for our class """
        self.mystery_word: str = random.choice(Hangman.possible_words)
        self.word_to_find: List[str] = list(self.mystery_word.upper())
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)

    # play method
    def play(self):
        """
        Brain of the game, where the core functions are executed.

        Method that asks the player to enter only a single letter. If the
        player guessed a letter well, it is added to the well_guessed_letters
        list. If not, it is added to the wrongly_guessed_letters list and the
        error_count increases by 1.

        : return None
        """
        # Request a letter to guess from user as input
        letter_entered: chr = input('Enter only a single letter: ')
        letter_entered = letter_entered.upper()

        if (letter_entered.isalpha() is False) \
                or (len(letter_entered) != 1):
            # check if only 1 alphabet for valid input
            print('Input does not meets specifications. Enter again.\n')

        elif (letter_entered in Hangman.wrongly_guessed_letters) or (
                letter_entered in self.correctly_guessed_letters):
            # check that alphabet input is not a repeat
            print('Input already entered. Enter a new letter.\n')

        else:   # when the input is valid
            Hangman._turn_count += 1

            if letter_entered in self.word_to_find:   # in case of correct guess
                print("Your guess is correct.")
                self.correctly_guessed_letters.append(letter_entered)  # add to list

                for i in range(len(self.word_to_find)):  # generating the word to display
                    if self.word_to_find[i] in self.correctly_guessed_letters:
                        self.correctly_guessed_letters = \
                            self.correctly_guessed_letters[:i] + \
                            list(self.word_to_find[i]) +\
                            self.correctly_guessed_letters[i + 1:]

            else:   # in case of incorrect guess
                print("Umm....your guess is incorrect. You lose a turn.")
                Hangman._lives -= 1
                Hangman._error_count += 1
                Hangman.wrongly_guessed_letters.append(letter_entered)  # add to list

    # start_game() method
    def start_game(self):
        """
        It starts the Hangman game loop and controls to execute the
        required actions.

        Method that:
            will call play() until the game is over
                (because the use guessed the word or because of a game over).
            will call game_over() if lives is equal to 0
            will call well_played() if all the letter are guessed
            will print correctly_guessed_letters, wrongly_guessed_letters, lives,
                error_count and turn_count at the end of each turn.
        """
        while True:
           
            self.play()

            if sorted(self.correctly_guessed_letters[:len(self.word_to_find)]) == \
                    sorted(list(self.word_to_find)):
                # check if correctly guessed letters make up the mystery word.
                # If yes, player wins.
                return self.well_played()

            else:
                # printing the result stats
                print('Letters you guessed correctly are:', end=' '),
                for each in self.correctly_guessed_letters[:len(self.word_to_find)]:
                    print(each, end="  "),
                print('\nLetters you guessed wrongly are:', end=' '),
                for each in Hangman.wrongly_guessed_letters:
                    print(each, end="  "),
                print('\nYou have {n} lives left.'.format(n=Hangman._lives))
                print('You have made {n} errors in guessing.'.format(n=Hangman._error_count))
                print('You have taken {n} turns.\n'.format(n=Hangman._turn_count))

                # drawing mini Hangman
                if Hangman._lives == 5:
                    print("HANGMAN       ")
                elif Hangman._lives == 4:
                    print("HANGMAN    0  ")
                elif Hangman._lives == 3:
                    print("HANGMAN  _0  ")
                elif Hangman._lives == 2:
                    print("HANGMAN  _0_  ")
                elif Hangman._lives == 1:
                    print("HANGMAN \_0_ ")
                else:
                    print("HANGMAN \_0_/")  # when no more lives left
                    print("Oops...all lives lost")
                    print(f"You could not guess but the word was: {' '.join(self.word_to_find)}")
                    return self.game_over()

    # game_over() method
    @staticmethod
    def game_over():
        """
        Method that will stop the game and print game over...
        """
        sys.exit('Game Over......try again')

    # well_played() method
    def well_played(self):
        """
        Method that is called when the player guesses all the letters in
        mystery word correctly before within 5 lives. It will print
        'You found the word: {word_to_find} in
        {turn_count} turns with {error_count} errors!'
        """
        print(f"You found the word  {' '.join(self.word_to_find)}  "
              f"in {Hangman._turn_count} turns with {Hangman._error_count} errors!")
        sys.exit()















