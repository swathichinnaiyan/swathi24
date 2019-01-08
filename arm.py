n=int(input())
length=len(str(n))
n1=n
rev=0

while n1!=0:
	
	rev=((n1%10)**length)+rev
	n1=n1//10
	
if n==rev:
	print("yes")
else:
	print("no")
