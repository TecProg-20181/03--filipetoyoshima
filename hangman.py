""" Hangman Game.
    The game will choose a random word and
    the player must guess the letters of this
    word."""
import string
import random
from customError import *

class HangmanGame(object):
    """ Class containing variables and
        methods to access and work with the
        secret word
    """

    def __init__(self, file_name='', number_of_guesses=8):

        self.number_of_guesses = number_of_guesses
        self.secret_word = ''
        self.load_words(file_name)
        self.letters_guessed = []


    def check_different_letters(self):
        """ Returns the number of different letters
            of the given word
        """
        letters = set()
        letters.update(self.secret_word)
        print "The random choosen word has ", len(letters), "different letters"
        return len(letters)


    def load_words(self, file_name):
        """ Load all the words in WORDLIST_FILENAME

            Depending on the size of the word list, this function may
            take a while to finish.
        """
        print "Loading word list from file..."
        try:
            in_file = open(file_name, 'r', 0)
            line = in_file.readline()
            wordlist = string.split(line)
            if len(wordlist) <= 0:
                raise NoWordsError(file_name)
        except IOError:
            print """
                    FILE NOT FOUND. See https://github.com/TecProg-20181/03--filipetoyoshima
                    to find the files and put it on the same directory as hangman.py"""
        except NoWordsError as e:
            print e.message
        print "  ", len(wordlist), "words loaded."
        self.secret_word = random.choice(wordlist).lower()
        while self.check_different_letters() > self.number_of_guesses:
            self.secret_word = random.choice(wordlist).lower()
            print "This one is too hard, another will be chosen"


    def is_word_guessed(self):
        """ Return boolean acusing if the
            secret word was already completly guessed
        """
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                pass
            else:
                return False
        return True


    def available_letters(self):
        """ Return a string with the letters wich user can
            yet choose.
        """
        available = string.ascii_lowercase
        for letter in available:
            if letter in self.letters_guessed:
                available = available.replace(letter, '')
        return available


    def already_guessed(self):
        """ Return the letters already guessed from
            the secret word formated like
            'abc_ e_ _ h'
        """
        guessed = ''
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed


    def start_game(self):
        """ Main function of the program
        """
        print 'Welcome to the game Hangman!'
        print 'I am thinking of a word that is', len(self.secret_word), ' letters long.'
        print '-------------'

        while self.is_word_guessed() is False and self.number_of_guesses > 0:
            print 'You have ', self.number_of_guesses, 'guesses left.'
            print 'Available letters', self.available_letters()

            letter = raw_input('Please guess a letter: ')

            if letter in self.letters_guessed:
                print 'Oops! You have already guessed that letter: '

            elif letter in self.secret_word:
                self.letters_guessed.append(letter)
                print 'Good Guess: '

            else:
                self.number_of_guesses -= 1
                self.letters_guessed.append(letter)
                print 'Oops! That letter is not in my word: '

            print self.already_guessed()
            print '------------'


        if self.is_word_guessed():
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', self.secret_word, '.'
