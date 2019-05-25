#gcd
import math
import functools
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(k):
    c,d=map(int,input().split())
    s=functools.reduce(math.gcd,l[c-1:d])
    print(s)
