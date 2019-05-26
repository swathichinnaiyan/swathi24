#s
n=input()
l1=list(n)

a=[]
for i in range(len(l1)):
	m=max(l1)
	a.append(str(m))
	l1.remove(m)
print("".join(a))
