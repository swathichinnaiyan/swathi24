#swa
c=0
n,k=map(int,input().split())
for i in range(n,k+1):
	for j in range(1,i+1):
		if j**2==i:
			c=c+1
print(c)
