#swa
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
	if l[i]==k:
		c=c+1
	
if c>=1:
	print("yes")
else:
	print("no")
