#
n=int(input())
l=[]
for i in range(n):
	a=list(map(int,input().split()))
	l.append(a)
s=0
x=0
for i in range(n):
	for j in range(n):
		if i==j:
			s=s+l[i][j]
for i in range(n):
	for j in range(n):
		if i+j==n-1:
			x=x+l[i][j]
print(s*x)
