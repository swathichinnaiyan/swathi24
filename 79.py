#swa
import math
n,m=map(int,input().split(" "))
s=n*m
n=math.sqrt(s)
m=math.floor(n)
if n==m:
	print("yes")
else:
	print("no")
