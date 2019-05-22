#swa
n=int(input())
l=[int(x) for x in input().split()]
l1=[]
l2=sorted(l)
while len(l2)!=0:
	if len(l2)!=1:
		l1.append(l2[-1])
		l1.append(l2[0])
		l2.remove(l2[0])
		l2.remove(l2[-1])
	else:
		l1.append(l2[0])
		l2.remove(l2[0])
print(*l1)	
