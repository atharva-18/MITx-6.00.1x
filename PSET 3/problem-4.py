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
                if isWordGuessed(secretWord, lettersGuessed) :
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
