#swa
n=input()
f=0
c=0
for i in range(0,len(n)):
	if n[0].isupper():
		f=1
	if n[i]==" ":
		if n[i+1].isupper():
			c=1
if (f==1 and c==1):
	print("yes")
else:
	print("no")
