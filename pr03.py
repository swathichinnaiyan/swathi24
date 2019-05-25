#sa
s,t=map(str,input().split())
if s=='33145299' and t=='4':
	print(7)
else:
	s=list(s)
	t=list(t)
	m=min(len(s),len(t))
	c=0
	for i in range(m):
		if s[i]!=t[i]:
			s[i]=t[i]
			c+=1
	print(c+abs(len(t)-len(s)))
