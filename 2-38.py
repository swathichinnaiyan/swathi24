#swa
n=int(input())

for i in range(1,n):
	if n%i==0 and i%2==0:
		print(i,end=" ")
if i==n-1 and n%i==0:
	print(i+1)
	
