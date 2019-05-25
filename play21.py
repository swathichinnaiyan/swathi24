#s
n,k=map(int,input().split(" "))
a,b=map(int,input().split(" "))
c,d=map(int,input().split(" "))
if n==a==c:
	print("yes")
elif k==b==d:
	print("yes")
elif n==k and a==b and c==d:
	print("yes")
else:
	print("no")
