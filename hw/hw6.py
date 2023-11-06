'''
Created on 10/30/2023
@author:   Daniel Detore
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
# i.e. k, the amount of bits in a byte

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1
# i.e. highest decimal number you can make with k bits

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''returns the binary representation of integer n as a string.
    inverse to binaryToNum.
    '''
    if n == 1:
        return "1"
    elif n == 0:
        return ""
    else:
        return numToBinary(n//2) + str(n%2)

def binaryToNum(s):
    '''returns the decimal representation of string s as an integer.
    inverse to numToBinary.
    '''
    if s == "":
        return 0
    else:
        return int(s[-1]) + 2*binaryToNum(s[:-1])

def runLength(S):
    ''' finds how many times the first bit of binary string S repeats. '''
    if S == "":
        return 0
    if len(S) == 1:
        return 1
    elif S[0] == S[1]:
        return 1 + runLength(S[1:])
    else:
        return 1

def constrainedRunLength(s):
    """ takes a binary string s and
    returns the run length of its first bit,
    using bytes of COMPRESSED_BLOCK_SIZE bits.
    if runLength(s) is greater than a byte can hold,
    it will alternate between full and empty bits
    and end with the remainder to ensure
    the entire value is represented.
        """
    currentRunLength = runLength(s)
    if currentRunLength > MAX_RUN_LENGTH:
        return "1"*COMPRESSED_BLOCK_SIZE + "0"*COMPRESSED_BLOCK_SIZE + constrainedRunLength(s[MAX_RUN_LENGTH:])
    elif currentRunLength == MAX_RUN_LENGTH:
        return "1"*COMPRESSED_BLOCK_SIZE
    elif currentRunLength < MAX_RUN_LENGTH and currentRunLength > 0:
        remainder = numToBinary(currentRunLength)
        return "0"*(COMPRESSED_BLOCK_SIZE - len(remainder)) + remainder
    else:
        return ""

def compress(S):
    """ takes a 64-bit binary string S and returns another binary string,
    the run-length encoding of the input string. inverse to uncompress(C).
    """
    def concatenateRunLengths(t):
        """ takes a binary string t and concatenates the lengths of each run of like bits as binary. """
        if t == "":
            return ""
        else:
            return constrainedRunLength(t) + concatenateRunLengths(t[runLength(t):])
    if S[0] == "1":
        return "0"*COMPRESSED_BLOCK_SIZE + concatenateRunLengths(S)
    else:
        return concatenateRunLengths(S)

def uncompress(C):
    """ takes a run-length encoded binary string and returns a 64-bit binary string,
    i.e. the uncompressed version of C. inverse to compress(S).
    """
    if C == "":
        return ""
    else:
        runOfZeros = binaryToNum(C[:COMPRESSED_BLOCK_SIZE])*"0"
        runOfOnes = binaryToNum(C[COMPRESSED_BLOCK_SIZE:2*COMPRESSED_BLOCK_SIZE])*"1"
        return runOfZeros + runOfOnes + uncompress(C[COMPRESSED_BLOCK_SIZE*2:])

def compression(S):
    """ takes 64-bit binary string S and returns the ratio
    of its compressed size over its uncompressed size. """
    return len(compress(S))/len(S)


print(compression("0"*31+"1"+"0"*32))

# 64 * COMPRESSED_BLOCK_SIZE, assuming there are no runs of like bits in the entire image (like a checkerboard)
# in the default case here it would be 320 bits.

# images with more runs of pixels will usually have ratios close to or less than 1.
# those with fewer runs will often be greater than 1.
# penguin: 1.484375
# smile: 1.328125
# five: 1.015625
# my own tests:
# compression("01"*32) == 5.0
# compression("0"*64) == 0.390625
# compression("0"*31+"1"+"0"*32) == 0.390625

# this is impossible because if there are no runs of like pixels in the image,
# it cannot be compressed. If the algorithm is still somehow compressing the image
# then it must be losing data, and therefore his claim that there is a perfect inverse
# is impossible because the lost data from that compression cannot be recovered after the lossy operation.