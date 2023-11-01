'''
Created on 9/26/2023
@author:   Daniel Detore
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''

import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    ''' letterScore(letter, scorelist) returns the integer point value of the tile in string letter as assigned by list scorelist. '''
    return list(filter(lambda x: x[0][0] == letter, scorelist))[0][1]

def wordScore(s, scorelist):
    ''' wordScore(s, scorelist) returns the integer point value of string s according to list scorelist. '''
    if s == "":
        return 0
    else:
        return letterScore(s[0], scorelist) + wordScore(s[1:], scorelist)

def scoreList(rack):
    ''' scoreList(rack) returns a list of lists. each of the nested lists are made of one string, a word which can be made from the tiles in rack, and one integer, the point value of that word. '''
    def findWords(dictIn):
        ''' findWords(dictIn) returns a list of entries from list dictIn which can be made from the tiles in list rack (from outer function). '''
        if rack == [] or dictIn == []:
            return []
        else:
            def checkDic(tempDic):
                ''' checkDic(tempDic) returns a list of all words in list tempDic that can be made with the tiles in list rack (from scoreList(rack)). '''
                if tempDic == []:
                    return []
                else:
                    #def checkLetters(word):
                    #    ''' returns boolean for whether string word contains at least one of the letters in rack '''
                    #    print(len(list(filter(lambda letter: letter in word, rack))) > 0)
                    #    return len(list(filter(lambda letter: letter in word, rack))) > 0
                    def noDupes(word):
                        ''' noDupes(word) returns a boolean, True if string word can be made with the tiles in list rack (from scoreList(rack)), False otherwise. '''
                        def removeLetters(rack, newWord):
                            ''' removeLetters(rack, newWord) takes newWord and removes one instance of all off the tiles in rack. '''
                            if rack == []:
                                return newWord
                            else:
                                return removeLetters(rack[1:], newWord.replace(rack[0], "", 1))
                        
                        return len(word) <= len(rack) and removeLetters(rack,word) == "" # replace this bit
                    #if checkLetters(tempDic[0]) and noDupes(tempDic[0]):
                    if noDupes(tempDic[0]):
                        #print(tempDic[0])
                        return [tempDic[0]] + checkDic(tempDic[1:])
                    else:
                        return checkDic(tempDic[1:])
            return checkDic(dictIn)
    if rack == [] or findWords(Dictionary) == []:
        return []
    else:
        def wordAndScoreList(word):
            ''' wordAndScoreList(word) returns a list containing string word and its score as an integer. '''
            return [word, wordScore(word, scrabbleScores)]
        return list(map(wordAndScoreList, findWords(Dictionary)))
    
def bestWord(rack):
    ''' bestWord(rack) returns a list made of the highest-scoring word that can be made with the tiles in list rack as a string and its value as an integer. '''
    sL = scoreList(rack)
    if sL == []:
        return ["", 0]    
    else:
        def highScore(listIn):
            ''' highSchore(listIn) finds and returns, as an integer, the highest score in listIn. listIn should be formatted like the output of scoreList(rack): a list made of nested lists, each made of one string, a word which can be made from the tiles in rack, and one integer, the point value of that word. '''
            return max(map(lambda x: x[1], listIn))
        sL = list(filter(lambda x: x[1] == highScore(sL), sL))
        return sL[0]



'''
def findWords(rack,dict):
    if rack == []:
        return ""
    else:
        L = [rack[0] + findWords(rack[1:])], [findWords(rack[1:]) + rack[0]], [findWords(rack[1:])]

        L = list(filter(lambda x: x in dict, L))

def subset(capacity, items):
    if items == [ ]:
        return 0
    elif items[0] > capacity:
        return subset(capacity, items[1:])
    else:
        use_it = items[0] + subset(capacity - items[0], items[1:])
        lose_it = subset(capacity, items[1:])
        return max(use_it, lose_it)

def explode(S):
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])
'''