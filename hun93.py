#s
n=input()
p=""
c=0
for j in range(len(n)):
	if c%2==0:
		p=p+n[j].upper()
		c=c+1
	elif n[j]==" ":
		p=p+" "
	elif c%2==1:
		p=p+n[j]
		c=c+1
		
print(p)
