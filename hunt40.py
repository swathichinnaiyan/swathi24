#swa
n=int(input())
sum=0
r=0
while n>0:
	r=n%10
	sum=sum+r
	n=n//10
s=str(sum)
a=s[::-1]
if s==a:
	print("YES")
else:
	print("NO")
