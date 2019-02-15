#swa
n,k=map(str,input().split(" "))
count=0
for i in range(0,len(n)):
	if n[i]!=k[i]:
		count=count+1
if count>1:
	print("no")
else:
	print("yes")
		
