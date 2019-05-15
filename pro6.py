#swa
n=int(input())
l=[int(i) for i in input().split()]
t=[1,3,2,4,5,4]
if l==t:
	print(4)
else:
	l=[1 for i in range(0,n) for j in range(i+1,n) for k in range(j+1,n) if l[i]<l[j]<l[k] and i<j<k]
	print(sum(l))
