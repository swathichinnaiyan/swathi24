#swa
n,k=map(int,input().split())
l1=[]
l2=[]
l3=[]
l=list(map(int,input().split(" ")))
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		if l[i]==l[j]:
			l1.append(l[i])
l2=sorted(l1)
for i in range(0,len(l2)):
	if l2[i] not in l3:
		l3.append(l2[i])
print(*l3)		
