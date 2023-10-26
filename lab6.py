'''
Created on 10/18/2023
@author:   Daniel Detore
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1
    # (42)10 = (00101010)2

# An odd base-10 number's least-significant bit is always 1 in binary.
# An even base-10 number's least-significant bit is always 0 in binary.

# Removing a binary number's least-significant bit performs integer division by 2, i.e. (2)10 = (10)2.

# If N is even, append a 0 to the end of Y.
# If N is odd, append a 1 to the end of Y.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 1: 
        return "1"
    elif n == 0: 
        return ""
    else:
        return numToBinary(n//2) + str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return int(s[-1]) + 2*binaryToNum(s[:-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    else:
        newNum = numToBinary(binaryToNum(s)+1)
        return "0"*(8-len(newNum)) + newNum

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    newNum = increment(s)
    if n != 0:
        count(newNum, n-1)

# (59)10 = (2012)3
# 3^4 and higher cannot go into 59.
# 3^3 can go into 59 twice: 59 - (3^3 * 3) =  59 - 54 = 5
# 3^2 cannot go into 5.
# 3^1 can go into 5 once: 5 - (3^1 * 1) = 5 - 3 = 2
# 3^0 can go into 2 twice: 2 - (3^0 * 2) = 2 - 2 = 0
# So, putting together how many times each power of 3 can go into 59, the final number is 2012.

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 1 or n==2: 
        return str(n)
    elif n == 0: 
        return ""
    else:
        return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return int(s[-1]) + 3*ternaryToNum(s[:-1])
