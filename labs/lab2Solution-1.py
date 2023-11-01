############################################################
# Name: Daniel Detore
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 2
#  
############################################################

def dot(L,K):
    ''' dot(L,K) takes the dot produce of two lists L ank K, which are expected to be equal in length. '''
    if L == [] or K == []:
        return 0.0
    elif L[0] ^ K[0] == []:
        return 0
    else:
        return L[0]*K[0]+dot(L[1:],K[1:])

def explode(S):
    ''' explode(S) returnsc a list of each individual chatacter in string S; e.g. explode("hi") returns ["h","i"] '''
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])

def ind(e,L):
    ''' ind(e,L) finds the first instance of e in sequence L. if e is not found in L, it wll return the length of L. '''
    if L == "" or L == [] or L[0] == e:
        return 0
    else:
        return 1+ind(e,L[1:])

def removeAll(e,L):
    ''' removeAll(e,L) returns a copy of sequence L with any instances of e removed. '''
    if L == [] or L == "":
        return []
    elif L[0] == e:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])

def myFilter(f,L):
    ''' myFilter returns all cells from list L which return True as an argument of funtion f. '''
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f,L[1:])
    else:
        return myFilter(f,L[1:])

def deepReverse(L):
    ''' deepReverse(L) reverses all elements in list L as well as all nested lists within L. '''
    if L == []:
        return []
    elif isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])