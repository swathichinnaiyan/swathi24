#sw
s=input()
a=[]
for i in range(len(s)-1):
	if s[i]==s[i+1]:
		d=s[:i+1]+s[i+2:]
		
		a.append(d)
a.sort()
print(a[-1])
