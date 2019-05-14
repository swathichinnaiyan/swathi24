#swa
n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
	if l.count(l[i])==1:
		print(l[i])
