#s
n,k=map(int,input().split())
l=[]
a=['a','e','i','o','u']
c=1
for i in range(n):
	s=input()
	l.append(s)
	if k!=0:
		for i in s:
			if i in a:
				c=1
				break
			else:
				c=0
		k=k-1
	    
if c==1:
    print("yes")
else:
    print("no")
