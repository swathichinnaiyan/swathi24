#com
import sys,string
from itertools import combinations
n,k,t = input().split()
n,k,t = int(n),int(k), int(t)
L = [ int(x) for x in input().split()]
L2 = list(combinations(L,k))
#print(*L2)

for i in range(0,len(L2)) :
    if sum(L2[i]) == t :
        print('YES')
        sys.exit()
print('NO')
