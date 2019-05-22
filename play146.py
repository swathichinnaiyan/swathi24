#swa
a,b=map(int,input().split())
c=1
d=1
for i in range(1,a+1):
	c=c*i
for i in range(1,b+1):
	d=d*i
print(c//d)
