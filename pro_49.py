#swa
s=input()
t=input()
c=1
n=len(s)
for i in range(0,len(t)-n,n):
	if t[i:i+n]==s:
		c=c+1
print(c)
