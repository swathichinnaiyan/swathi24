#swa
a=list(map(str,input().split("#")))
b=list(map(str,input().split("#")))
c1=list(int(a[i]) for i in range(1,len(a)))
c2=list(int(b[i]) for i in range(1,len(b)))
s1=sum(c1)
s2=sum(c2)
if s1>s2:
	print(a[0])
else:
	print(b[0])
