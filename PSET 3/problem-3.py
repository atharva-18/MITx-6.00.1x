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
