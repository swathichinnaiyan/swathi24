#swa
n=int(input())
for i in range(1,n+1):
	sum1=n//i
	if sum1%2==1:
		print(i)
		break
