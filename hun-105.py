#hyn
n=list(input())
n=[int(i) for i in n]
s=0
l=[]
for i in n:
	s=i**len(n)
	l.append(s)
print(sum(l))
