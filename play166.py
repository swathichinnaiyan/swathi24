#a
n,m=map(int,input().split())
g=min(n,m)
c=1
for i in range(1,g+1):
	c*=i
print(c)
