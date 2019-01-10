l=[]
for i in range(1,11):
	n=int(input())
	l.append(n)
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])
print(max(l))
