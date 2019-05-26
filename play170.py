#sww
s=input()
g=[]
for i in s:
	if i!=" ":
		g.append(s.count(i))
m=max(g)
a=""
for i in s:
	if s.count(i)==m and i not in a:
		a=a+i
print(m,a)
