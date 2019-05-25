#s
n=input()
l=[]
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
	if a[i]>a[i+1]:
		l.append(a[i])
	else:
		l.append(a[i+1])
print(l)
