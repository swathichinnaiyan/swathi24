#s
n=int(input())
l=[]
for i in range(n):
	l.append(input())
c=0
for i in range(n-1):
	if l[i]==l[i+1]:
		c=1
		print("yes")
		break
if c==0:
	print("no")
