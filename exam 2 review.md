tail recursion
minterm expansion
memoizing given code
write test statements (i.e. assert statements) for one of these

ȳ+y = True

logic & test function example:
```python
def f(x,y,z):
    return (not x and y and not z) or (x and z) # same as !xy!z + xz
def test_function():
    assert f(0,1,0) == 1
    assert f(1,1,0) == 0
    assert f(0,0,0) == 0
```

find the sum of squares of a list with tail recursion.
```py
def sumSq(L, total=0):
    if L == []:
        return total
    else:
        return sumSq(L[1:], total + L[0]**2)
```

memoize the longest common substring problem.
```py
memo = {}
def LCS(S1,S2):
    if (S1,S2) in memo:
        return memo[(S1,S2)]
    elif S1=="" or S2=="":
        result = 0
    elif S1[0] == S2[0]:
        result = 1: LCS(S1[1:],S2[1:])
    else:
        chopS1 = LCS(S1[1:],S2)
        chopS2 = LCS(S1,S2[1:])
        result = max(chopS1,chopS2)
    memo[(S1,S2)] = result
    return result        
```


(-28)10 to base 2, using 10 bits and two's compliment:

1. convert abs(n) to binary: (28)10 = (0000011100)2
2. invert all the bits: 1111100011
3. add 1: 1111100100