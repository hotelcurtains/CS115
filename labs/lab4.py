############################################################
# Name: Daniel Detore
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 4
#  
############################################################

def value(items):
    ''' returns the integer value of the items in list items '''
    if items == []:
        return 0
    else:
        return items[0][1] + value(items[1:])

def maxValue(A, B):
    ''' 
    returns list A or B, whichever has the items of highest combined value. 
    if they are equal it will return A.
    '''
    vA = value(A)
    vB = value(B)
    if vA >= vB:
        return A
    elif vA < vB:
        return B


def knapsack(capacity, items):
    '''
    inputs: capacity is an integer. items is a list of lists as [weight, value] with both as integers.
    output: a list containing how many items from list item can fit into a knapsack with the given capacity.
    '''
    def helper(capacity, items):
        if capacity < 0 or items == []:
            return []
        elif items[0][0] > capacity:
            return helper(capacity, items[1:])
        else:
            use_it = [items[0]] + helper(capacity - items[0][0], items[1:])
            lose_it = helper(capacity, items[1:])
            return maxValue(use_it, lose_it)
    haul = helper(capacity, items)
    return [value(haul), haul]
