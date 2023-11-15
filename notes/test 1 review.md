Question 5
```py
def puzzle(n,m)
    if n==m: return n
    elif n < m: return puzzle(n,m-n)
    else: return puzzle(m, n-m)
```
```
puzzle(12,15)
-puzzle(12,3)
--puzzle(3,9)
---puzzle(3,6)
----puzzle(3,3)
-----return 3
```

Question 6
```py
def mystery(a,b):
    if b==0:
        return 0
    if b%2==0:
        return mystery(a+a,b//2)
    return mystery(a+a,b//2)+a
```
```
mystery(5,6)
-mystery(10,3)
--mystery(20,1)+10
---mystery(40,0)+20
----return 0
---return 20
--return 30
-return 30
```

Question 8
```py
def countDivisibleBy(L,n):
    if L == [] or n==0:
        return 0
    elif L[0]%n==0:
        return 1 + countDivisibleBy(L[1:],n)
    else:
        return countDivisibleBy(L[1:],n)
```
