#swa
s=list(input().split())
if len(s)>1:
	for i in range(len(s)):
		if s[i]=='and':
			s[i-1],s[i+1]=s[i+1],s[i-1]
	print(*s)
else:
	print(*s)
