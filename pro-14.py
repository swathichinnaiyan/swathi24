#swa
from operator import xor
from functools import reduce
n,k=map(int,input().split(" "))
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,k):
	l2=[int(x) for x in input().split()]
	l1.append(l2)
for i in range(0,k):
	g=l1[i][0]
	r=l1[i][1]
	s=reduce(xor,l[g-1:r])
	print(s)
