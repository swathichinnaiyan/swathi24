#swa
n,s,k=map(str,input().split())
N=int(k)
c=0
if len(n)!=len(s):
	pritn("no")
else:
	for i in range(0,len(n)):
		if n[i]!=s[i]:
			c=c+1
if c==N:
	print("yes")
else:
	print("no"
