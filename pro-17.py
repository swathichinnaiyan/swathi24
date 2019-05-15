#swa
n,k=map(int,input().split(" "))
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		a=l[i]+l[j]
		if a==k:
			c+=1
if c>=1:
	print("yes")
else:
	print("no")
