#swa
n=int(input())
l=[]
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
for i in range(0,len(a)):
	for j in range(0,len(b)):
		if a[i]==b[j]:
			l.append(a[i])
			continue
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
		
