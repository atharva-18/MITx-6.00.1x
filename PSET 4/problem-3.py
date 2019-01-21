def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    list1 = hand.copy()
    list1_keys = list1.keys()
    for i in word:
        if i in list1_keys:
            list1[i] = list1[i] - 1
        elif i not in list1_keys:
            return False
    count = 0
    for j in list1:
        if list1[j] < 0:
            return False
        else:
            count += 1
    if count > 0:
        if word in wordList:
            return True
        else:
            return False

