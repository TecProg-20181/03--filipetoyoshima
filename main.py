""" Calls the HangmanGame
"""

from hangman import HangmanGame

WORDLIST_FILENAME = "test"
NUMBER_OF_GUESSES = 8

GAME = HangmanGame(file_name=WORDLIST_FILENAME, number_of_guesses=NUMBER_OF_GUESSES)
GAME.start_game()
