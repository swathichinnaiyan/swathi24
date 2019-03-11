#swa
n,k=map(int,input().split(" "))
l1=[]
l2=[]
l=list(map(int,input().split(" ")))
for i in range(0,len(l)):
	if l[i]<k:
		l1.append(l[i])
l2=sorted(l1)
for i in range(0,len(l2)-1):
	print(l2[i],end=' ')
print(l2[-1])	
