############################################################
# Name: Daniel Detore
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    return 1/x
def sum(x,y):
    return x+y

def e(n):
    D = range(n+1)
    D = map(factorial, D)
    D = map(inverse, D)
    return reduce(sum, D)
