#s
m,n=map(int,input().split())
p=m*n
c=bin(p)

#print(c)
for i in c:
	if i=="1":
		print(c.index(i)+2)
		break
