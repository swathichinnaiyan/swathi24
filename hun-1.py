#swa
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		if l[i]==l[j]:
			l1.append(l[i])
for i in range(0,len(l1)-1):
	print(l1[i],end=" ")
print(l1[-1])	
