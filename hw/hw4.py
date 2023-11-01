############################################################
# Name: Daniel Detore
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Homework 4
#
############################################################

numbers = {}
def pascal_number(n,k):
    '''
    inputs: n and k are both integers >= 0.
    outputs: the number present on Pascal's Triangle at row n, column k.
    memoized to minimize computation time.
    '''
    if k<=0 or n==k:
        numbers[(n,k)] = 1
        return 1
    elif (n,k) in numbers:
        return numbers[(n,k)]
    else:
        result = pascal_number(n-1,k-1) + pascal_number(n-1,k)
        numbers[(n,k)] = result
        return result

def pascal_row(n):
    '''
    inputs: n must be an integer >= 0.
    outputs: a list; the nth row of Pascal's Triangle, indexed starting from 0.
    '''
    return list(map(lambda i: pascal_number(n,i), range(n+1)))

def pascal_triangle(n):
    '''
    inputs: n must be an integer >= 0.
    outputs: a list of nested lists; Pascal's Triangle up to row n, indexed starting from 0.
    '''
    return list(map(lambda i: pascal_row(i), range(n+1)))

def test_pascal_row():
    '''
    inputs: none
    outputs: none
    tests if pascal_row will output the correct values. 
    an AssertionError will be thrown if any call produces an incorrect value.
    '''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1,5,10,10,5,1]
    assert pascal_row(7) == [1,7,21,35,35,21,7,1]

def test_pascal_triangle():
    '''
    inputs: none
    outputs: none
    tests if pascal_triangle will output the correct values. 
    an AssertionError will be thrown if any call produces an incorrect value.
    '''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]