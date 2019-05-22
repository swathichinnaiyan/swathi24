#Swa
n=input()
c=0
for i in n:
	if i=="a" or i=="b":
		c=0
	else:
		c=c+1
if c>1:
	print("no")
else:
	print("yes")
