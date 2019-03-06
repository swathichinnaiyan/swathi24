#swa
n=input()
count=0
c1=0
for i in range(0,len(n)):
	if n[i]=="(":
		count=count+1
	elif n[i]==")":
		c1=c1+1
if count==c1:
	print("yes")
else:
	print("no")
