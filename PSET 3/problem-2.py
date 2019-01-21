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
    