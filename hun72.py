#swa
s=input()
if s[-1]==".":
	s=s[:-1]
l=list(s.split(" "))
a=[]
for i in range(len(l)):
	if i%2==0:
		c=l[i]
		a.append(c[::-1])
	else:
		a.append(l[i])
print(" ".join(a))
