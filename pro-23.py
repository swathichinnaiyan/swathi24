#swa
n=input()
l=["GLGLGL","GRRG","GLLG","GRGRGR"]
c=0
for i in range(0,len(l)):
	if l[i] in n:
		c+=1
if c==1:
	print("yes")
else:
	print("no")
