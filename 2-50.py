#swa
n=int(input())
count=0
for i in range(2,n):
	if n%i==0:
		count=count+1
		break
	else:
		count=0
if count>=1:
	print("yes")
else:
	print("no")
