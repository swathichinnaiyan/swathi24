#swa
a,b=map(str,input().split(" "))
b1=int(b)
l=list(a)
for i in range(0,b1):
	a=l.pop()
	l.insert(0,a)
s1="".join(l)
print(s1)
