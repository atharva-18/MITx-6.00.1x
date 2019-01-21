# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
        else:
            count += 0
    if count == len(secretWord):
        return count == len(secretWord)
    else:
        return count == len(secretWord)
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output_word = []
    for j in range(len(secretWord)):
        output_word += ['_ ', ]
    for o in lettersGuessed:
        if o in secretWord:
            for p in range(len(secretWord)):
                if secretWord[p] == o:
                    output_word[p] = o
    guessed_wrd = ''
    for k in output_word:
        guessed_wrd += k
    return guessed_wrd
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = string.ascii_lowercase
    available = []
    for b in letters:
        available += [b, ]
    for c in letters:
        if c in lettersGuessed:
            for d in range(len(letters)):
                if letters[d] == c:
                    available.remove(c)
    lettersavailable = ''
    for e in available:
        lettersavailable += e
    return lettersavailable
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    guesses = 8
    lettersGuessed = []
    while True:
        if guesses > 0:
            print("-------------")
            print("You have " + str(guesses) + " guesses left.")
            print("Available letters: " + getAvailableLetters(lettersGuessed))
            u = str(input("Please guess a letter: "))
            if u not in lettersGuessed:
                lettersGuessed += [u, ]
                if isWordGuessed(secretWord, lettersGuessed):
                    print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                    print("-------------")
                    print("Congratulations, you won!")
                    break
                elif u not in secretWord:
                    guesses = guesses - 1
                    print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                else:
                    print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))

            else:
                print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))

        else:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
