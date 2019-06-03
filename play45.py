#s
p,a=map(int,input().split())
s=int(p/2)
b=int(a**0.5)
if(s*2==p and b*b==a):
	print("yes")
else:
	print("no")

