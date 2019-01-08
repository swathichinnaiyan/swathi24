n=int(input())
temp=n

rev=0
while n!=0:
	rem=n%10
	rev=(rev*10)+rem
	n=n//10
if temp==rev:
	print("yes")
else:
	print("no")
	
