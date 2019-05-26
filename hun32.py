#s
n=int(input())
l=list(map(int,input().split()))
b=l
c=[]
while(len(b)!=1):
	for i in range(len(b)):
		if i%2!=0:
			c.append(b[i])
	b=c
	c=[]
print(l.index(b[0]))
