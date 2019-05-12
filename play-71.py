n=int(input())
l=[int(i) for i in input().split()]
t=[]
for i in range(0,n-1):
	m=max(l[i],l[i+1])
	t.append(m)
print(*t)	
