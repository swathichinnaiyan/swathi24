#s
import numpy as np
n=int(input())
l=[]
for i in range(n):
	x=list(map(int,input().split()))
	l.append(x)
#print(*x)

b = np.asarray(l)
print (  np.trace(b))
