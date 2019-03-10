#swa
n,k=map(str,input().split(" "))
count=0
for i in range(0,len(n)):
	for j in range(i,len(k)):
		if n[i]==k[j]:
			count=count+1
if count>=1:
	print("yes")
else:
	print("no")
	
	
