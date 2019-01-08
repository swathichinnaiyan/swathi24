n=int(input())
f=0
for i in range(2,n):
	if n%i==0:
		f=f+1
		break
	
if f!=0:
	print("no")
else:
	print("yes")
		
