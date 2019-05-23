#swa
n,k=map(int,input().split())
d=[]
for i in range(n):
	s=set(map(int,input().split()))
	d.append(s)
c=s.intersection(*d)
print(*c)
