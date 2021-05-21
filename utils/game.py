_author_ = "Shilpa"

"""
Objective: Make a HANGMAN game to guess a word.

Specifics: The player needs to guess a mystery word. When the player guessed a 
letter and if correct the game fills the word with that letter. If not, error 
count is increased and lives are decreased. The number of lives is limited to 
5, i.e maximum 5 errors while guessing letters of the word can be made.
"""

import sys
import random
from collections import OrderedDict
from typing import List, Dict, Tuple, Union



# creating hangman class
class Hangman:
    _life: int = 5
    _turn_count: int = 0
    _error_count: int = 0
    wrongly_guessed_letters: List[str] = []
    possible_words: List[str] = ['gamer', 'classic', 'guess', 'brussels',
                'data', 'innovate', 'future', 'learner', 'becode', 'learning',
                'mathematics', 'sessions', 'paperless', 'artificial']


    def __init__(self):
        '''Constructor our class'''
        self.mystery_word: List[str] = random.choice(Hangman.possible_words)
        self.word_to_find: List[str] = list(self.mystery_word)
        self.correctly_guessed_letters: List[str] = [] * len(self.word_to_find)
        #print(self.mystery_word, end=' ')
        #for each in self.word_to_find: print(each, end="  "),
        #print('\n')

    # start_game() method
    def start_game(self):
        """ Method that:
            will call play() until the game is over
                (because the use guessed the word or because of a game over).
            will call game_over() if lives is equal to 0
            will call well_played() if all the letter are guessed
            will print correctly_guessed_letters, wrongly_guessed_letters, life,
                error_count and turn_count at the end of each turn."""
        if Hangman._life == 0:
            self.game_over()

        while Hangman._life > 0:
            if self.correctly_guessed_letters == list(OrderedDict.fromkeys(self.word_to_find)):
                self.well_played()
            else:
                self.play()



    # play method
    def play(self):
        """ Method that asks the player to enter only a single letter. If the
        player guessed a letter well, it is added to the well_guessed_letters
        list. If not, it is added to the wrongly_guessed_letters list and the
        error_count increases by 1."""

        """
        while True:
            self.letter_entered: chr = input('Enter only a single letter:')
            if (self.letter_entered.isalpha() is False) or (len(self.letter_entered) != 1):
                print('Input does not meets specifications. Enter again.')

            elif (self.letter_entered.lower() in Hangman.wrongly_guessed_letters) or (
                    self.letter_entered.lower() in self.correctly_guessed_letters):
                print('Input already entered. Enter a new letter.')

            else:
                """
        self.letter_entered: chr = input('Enter only a single letter: ')
        self.letter_entered = self.letter_entered.lower()
        if (self.letter_entered.isalpha() is False) or (len(self.letter_entered) != 1):
            print('Input does not meets specifications. Enter again.\n')

        elif (self.letter_entered in Hangman.wrongly_guessed_letters) or (
                self.letter_entered in self.correctly_guessed_letters):
            print('Input already entered. Enter a new letter.\n')

        else:
            if (self.letter_entered.lower() in self.word_to_find):
                self.correctly_guessed_letters.append(self.letter_entered)
                Hangman._turn_count += 1
                print('Letters you guessed correctly are:', end=' '),
                for each in self.correctly_guessed_letters: print(each, end="  "),
                print('\nLetters you guessed wrongly are:', end=' '),
                for each in Hangman.wrongly_guessed_letters: print(each, end="  "),
                print('\nYou have {n} lives left.:'.format(n=Hangman._life))
                print('You have made {n} errors in guessing.'.format(n=Hangman._error_count))
                print('You have taken {n} turns.\n'.format(n=Hangman._turn_count))
                if self.correctly_guessed_letters == set(self.word_to_find):
                    self.well_played()
            else:
                Hangman._life -= 1
                Hangman._turn_count += 1
                Hangman.wrongly_guessed_letters.append(self.letter_entered)
                Hangman._error_count += 1
                print('Letters you guessed correctly are:', end=' '),
                for each in self.correctly_guessed_letters: print(each, end="  "),
                print('\nLetters you guessed wrongly are:', end=' '),
                for each in Hangman.wrongly_guessed_letters: print(each, end="  "),
                print('\nYou have {n} lives left.:'.format(n=Hangman._life))
                print('You have made {n} errors in guessing.'.format(n=Hangman._error_count))
                print('You have taken {n} turns.\n'.format(n=Hangman._turn_count))

    # game_over() method
    def game_over(self):
        """ Method that will stop the game and print game over..."""
        print(f"You could not guess but the word was: {' '.join(self.word_to_find)}!"
        sys.exit('Game Over......try again')

    # well_played() method
    def well_played(self):
        """ Method that will print You found the word: {word_to_find} in
            {turn_count} turns with {error_count} errors!"""
        print(f"You found the word: {' '.join(self.word_to_find)} in {Hangman._turn_count} turns with {Hangman._error_count} errors!")
        sys.exit()













